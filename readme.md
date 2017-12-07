To run the server, do the following:
1. Install virtualenv (`pip install virtualenv`. If you don't have pip, `brew install pip` first)
2. Once you've set up a virtualenv (run `virtualenv .`)  in the backend directory, run `source bin/activate`.
3. Install the requirements by running `pip install -r requirements.txt` from the backend dir.
4. Run `python server.py` from inside backend/src. You can find the available routes in server.py.

Example json required to increment clicks:
```
{
  "entity": "Napa, CA", 
  "viz_type": "single_entity_spend_pc_py", 
  "y": "administrative", 
  "z": "income_per_capita"
}
```
Route is `/increment_clicks` (POST).

Example json for setting click totals:
```
{
 "entities": {"Napa, CA": 100, "Alameda, CA": 72}, 
 "viz_types": {"single_entity_spend_pc_py": 100}, 
 "y": {"administrative": 100, "police": 59}, 
 "z": {"income_per_capita": 105, "population": 46}
}
```
Route is `/set_clicks` (POST).

No json is required to reset clicks. Route is `/reset_clicks` (POST).

The route to generate a chart is `/generate_chart` (GET).
