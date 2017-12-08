import pandas as pd

ydf = pd.read_csv('../db/entityy.csv')
zdf = pd.read_csv('../db/entityz.csv')

col_name_lookup = {
  'population': 'Population',
  'income_per_capita': 'Income per capita',
  'college_grads': 'College graduates',
  'robberies_per_100k': 'Robberies/100K people',
  'entity': 'Entity',
  'administrative': 'Administrative',
  'public_works': 'Public Works',
  'community_services': 'Community Services',
  'fire': 'Fire',
  'police': 'Police'
}

def format_tuple(tup):
  if len(tup) == 3:
    return {'x': tup[0], 'y': tup[1], 'size': tup[2]}
  else:
    return {'x': tup[0], 'y': tup[1]}


def chart_format(d):
  out = dict()
  for entity in d:
    entity_tuples = d[entity]
    formatted_entity_tuples = map(format_tuple , entity_tuples)
    out[entity] = formatted_entity_tuples
  return out

def augment(xy_pairs, z_vals_by_entity):
  out = dict()
  for entity in xy_pairs:
    entity_pairs = xy_pairs[entity]
    entity_triples = map(lambda x: (x[0], x[1], z_vals_by_entity[entity]), entity_pairs)
    out[entity] = entity_triples
  return out

def clean(s):
  return s.replace(',', '').replace('%', '')

def get_entity_public_metric(entity, metric):
  return float(clean(str(zdf.loc[zdf['Entity'] == entity][col_name_lookup[metric]].iloc[0])))

def get_row_by_entity_and_dept(entity, dept):
  return ydf.loc[ydf['Entity'] == entity].loc[ydf['Department'] == col_name_lookup[dept]].drop('Department', 1)

def collect_data(metadata):
  entities = metadata['entities']
  viz_type = metadata['viz_type']
  dept = metadata['y']
  y_row_dfs = [get_row_by_entity_and_dept(entity, dept) for entity in entities] 
  xy_pairs = {}
  for df in y_row_dfs:
    headers = list(df.columns.values)
    entity = ""
    entity_pairs = []
    for _, row in df.iterrows():
      entity = list(row)[0]
      entity_population = get_entity_public_metric(entity, 'population')
      # years should be the x values unless we are looking at spend v spend viz type
      xvals = headers[1:] if viz_type != 'all_entity_spend_v_spend_sized_by_z' else map(lambda x: float(clean(x)), get_row_by_entity_and_dept(entity, metadata['y1']).iloc[0][1:])
      yvals = map(lambda val: float(clean(val)) / entity_population, row[1:])
      entity_pairs = zip(xvals, yvals)
      xy_pairs[entity] = entity_pairs
  if 'all' in viz_type:
    public_metric_name = metadata['z']
    public_metrics = [get_entity_public_metric(entity, public_metric_name) for entity in entities]
    return chart_format(augment(xy_pairs, dict(zip(entities, public_metrics))))
  return chart_format(xy_pairs)
