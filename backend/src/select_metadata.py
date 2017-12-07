import pickle as pkl
import random as rand

entities = pkl.load(open('../db/ent.pkl'))
viz_types = pkl.load(open('../db/viz_types.pkl'))
y_axis = pkl.load(open('../db/y.pkl'))
z_axis = pkl.load(open('../db/z.pkl'))

unit_lookup = {
  'population': 'people',
  'robberies_per_100k': 'people',
  'college_grads': 'percent',
  'income_per_capita': 'dollars'
}

def weighted_random(tup_list):
  to_flatten = map(lambda x: [x[0]] * x[1], tup_list)
  to_choose_from = [item for sublist in to_flatten for item in sublist]
  return rand.choice(to_choose_from)

def generate_chart_metadata():
  viz_type = weighted_random(viz_types)
  ents = map(lambda x: x[0], entities) # by default we take all entities
  if viz_type == 'single_entity_spend_pc_py':
    ents = [weighted_random(entities)]
  elif viz_type == 'single_entity_v_others_pc_py':
    num_ents = rand.randint(1, len(entities))
    ents = rand.sample(ents, num_ents)
  y = weighted_random(y_axis)
  out = {'entities': ents, 'viz_type': viz_type, 'y': y, 'y_units': 'dollars'}
  if viz_type == 'all_entity_spend_py_sized_by_z':
    z = weighted_random(z_axis)
    out['z'] = z
    out['z_units'] = unit_lookup[z]
  return out

