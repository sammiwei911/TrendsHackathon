import pickle as pkl
import random as rand

entities = pkl.load(open('../db/ent.pkl'))
viz_types = pkl.load(open('../db/viz_types.pkl'))
y_axis = pkl.load(open('../db/y.pkl'))
z_axis = pkl.load(open('../db/z.pkl'))

def weighted_random(tup_list):
  to_flatten = map(lambda x: [x[0]] * x[1], tup_list)
  to_choose_from = [item for sublist in to_flatten for item in sublist]
  return rand.choice(to_choose_from)

def generate_chart_metadata():
  viz_type = weighted_random(viz_types)
  ents = map(lambda x: x[0], entities) if viz_type == 'all_entity_spend_py_sized_by_z' else [weighted_random(entities)]
  y = weighted_random(y_axis)
  z = weighted_random(z_axis)
  return {'entities': ents, 'viz_type': viz_type, 'y': y, 'z': z}
