import pickle as pkl

entities = dict(pkl.load(open('../db/ent.pkl')))
viz_types = dict(pkl.load(open('../db/viz_types.pkl')))
y_axis = dict(pkl.load(open('../db/y.pkl')))
z_axis = dict(pkl.load(open('../db/z.pkl')))

def add_clicks(json):
  entities[json['entity']] += 1
  viz_types[json['viz_type']] += 1
  y_axis[json['y']] += 1
  z_axis[json['z']] += 1
  dump_all()
  return (entities, viz_types, y_axis, z_axis)

def reset_vals(d, val):
  for k in d:
    d[k] = val
  return d

def reset_clicks():
  reset_vals(entities, 1)
  reset_vals(viz_types, 1)
  reset_vals(y_axis, 1)
  reset_vals(z_axis, 1)
  dump_all()
  return (entities, viz_types, y_axis, z_axis)

def set_click_totals(json):
  entities[json['entity'][0]] = json['entity'][1]
  viz_types[json['viz_type'][0]] = json['viz_type'][1]
  y_axis[json['y'][0]] = json['y'][1]
  z_axis[json['z'][0]] = json['z'][1]
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
# add_clicks({'entity': 'Napa, CA', 'viz_type': 'single_entity_spend_pc_py', 'y': 'administrative', 'z': 'income_per_capita'})
# reload_and_print()
# set_click_totals({'entity': ['Napa, CA', 100], 'viz_type': ['single_entity_spend_pc_py', 100], 'y': ['administrative', 100], 'z': ['income_per_capita',100]})
# reload_and_print()
# reset_clicks()
# reload_and_print()
