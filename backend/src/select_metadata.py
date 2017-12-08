import pickle as pkl
import random as rand
import numpy as np

entities = pkl.load(open('../db/ent.pkl'))
viz_types = pkl.load(open('../db/viz_types.pkl'))
y_axis = pkl.load(open('../db/y.pkl'))
z_axis = pkl.load(open('../db/z.pkl'))

unit_lookup = {
  'population': 'people',
  'robberies_per_100k': 'people_per_100k',
  'college_grads': 'percent',
  'income_per_capita': 'dollars'
}

def compute_probs(tup_list):
  return [(choice, float(weight)/sum(dict(tup_list).values())) for choice, weight in tup_list]

def weighted_random(tup_list, num_samples):
  prob_tups = compute_probs(tup_list)
  choices, probs = map(lambda x: x[0], prob_tups), map(lambda x: x[1], prob_tups)
  return list(np.random.choice(choices, num_samples, p=probs, replace=False))

def get_ents_by_viz_type(viz_type):
  ents = map(lambda x: x[0], entities) # by default we take all entities (this covers the sized by charts)
  if viz_type == 'single_entity_spend_pc_py':
    ents = weighted_random(entities, 1)
  elif viz_type == 'single_entity_v_others_pc_py':
    num_ents = rand.randint(1, len(entities))
    ents = weighted_random(entities, num_ents)
  return ents

def generate_chart_metadata():
  viz_type = weighted_random(viz_types, 1)[0]
  ents = get_ents_by_viz_type(viz_type)
  y = weighted_random(y_axis, 2)
  y_units = 'dollars'
  out = {'entities': ents, 'viz_type': viz_type, 'y': y[0], 'y_units': y_units}
  if 'all' in viz_type:
    z = weighted_random(z_axis, 1)[0]
    out['z'] = z
    out['z_units'] = unit_lookup[z]
    if viz_type == 'all_entity_spend_v_spend_sized_by_z':
      out['y1'] = y[1] 
      out['y1_units'] = y_units
  return out

