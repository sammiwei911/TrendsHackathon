import pickle as pkl

entities = dict(pkl.load(open('../db/ent.pkl')))
viz_types = dict(pkl.load(open('../db/viz_types.pkl')))
y_axis = dict(pkl.load(open('../db/y.pkl')))
z_axis = dict(pkl.load(open('../db/z.pkl')))

def increment_clicks(json):
  for entity in json['entities']:
    entities[entity] += 1
  viz_types[json['viz_type']] += 4
  y_axis[json['y']] += 3
  if 'z' in json:
    z_axis[json['z']] += 1.5
  if 'y1' in json:
    y_axis[json['y1']] += 2
  dump_all()
  return (entities, viz_types, y_axis, z_axis)

def reset_scores(d, val):
  for k in d:
    d[k] = val
  return d

def reset_clicks():
  reset_scores(entities, 1)
  reset_scores(viz_types, 1)
  reset_scores(y_axis, 1)
  reset_scores(z_axis, 1)
  dump_all()
  return (entities, viz_types, y_axis, z_axis)

def set_scores(f, t):
  for k in t:
    f[k] = t[k]
  return f

def set_click_totals(json):
  entities_updates = json['entities']
  viz_types_updates = json['viz_types']
  y_axis_updates = json['y']
  z_axis_updates = json['z']
  global entities
  entities = set_scores(entities, entities_updates)
  global viz_types
  viz_types = set_scores(viz_types, viz_types_updates)
  global y_axis
  y_axis = set_scores(y_axis, y_axis_updates)
  global z_axis
  z_axis = set_scores(z_axis, z_axis_updates)
  dump_all()
  return (entities, viz_types, y_axis, z_axis)

  
def dump_all():
  pkl.dump(entities.items(), open('../db/ent.pkl', 'w'))
  pkl.dump(viz_types.items(), open('../db/viz_types.pkl', 'w'))
  pkl.dump(y_axis.items(), open('../db/y.pkl', 'w'))
  pkl.dump(z_axis.items(), open('../db/z.pkl', 'w'))

def reload_and_print():
  entities = dict(pkl.load(open('../db/ent.pkl')))
  viz_types = dict(pkl.load(open('../db/viz_types.pkl')))
  y_axis = dict(pkl.load(open('../db/y.pkl')))
  z_axis = dict(pkl.load(open('../db/z.pkl'))) 
  print entities
  print
  print viz_types
  print
  print y_axis
  print
  print z_axis
  print
  print

# See below for the type of json i'm expecting
#
# increment_clicks({'entity': 'Napa, CA', 'viz_type': 'single_entity_spend_pc_py', 'y': 'administrative', 'z': 'income_per_capita'})
# reload_and_print()
# set_click_totals({'entities': {'Napa, CA': 100, 'Alameda, CA': 72}, 'viz_types': {'single_entity_spend_pc_py': 100}, 'y': {'administrative': 100, 'police': 59}, 'z': {'income_per_capita': 100, 'population': 46}})
# reload_and_print()
# reset_clicks()
# reload_and_print()
