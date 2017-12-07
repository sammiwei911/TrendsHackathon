To run the server, do the following:
1. Install virtualenv (`pip install virtualenv`. If you don't have pip, `brew install pip` first)
2. Once you've set up a virtualenv in the backend directory, run `source bin/activate`
3. Install the requirements by running `pip install -r requirements.txt` from the backend dir.
4. Run `python server.py` from inside backend/src. You can find the available routes in server.py.

Example json required to increment clicks:
```
{
	'entity': 'Napa, CA', 
	'viz_type': 'single_entity_spend_pc_py', 
	'y': 'administrative', 
	'z': 'income_per_capita'
}
```

Example json for setting click totals:
```
{
	'entity': ['Napa, CA', 100], 
	'viz_type': ['single_entity_spend_pc_py', 100], 
	'y': ['administrative', 100], 
	'z': ['income_per_capita',100]
}
```

No json is required to reset clicks.
