#!/usr/bin/python3

from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_cors import CORS
import json

from select_metadata import generate_chart_metadata
from collect_data import collect_data
import change_clicks as cc

app = Flask(__name__)
api = Api(app)
CORS(app)

# access_control_response_headers = {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept', 'Access-Control-Allow-Methods': 'GET, POST'}

class GenerateChartRoute(Resource):
  def get(self):
    metadata = generate_chart_metadata()
    data = collect_data(metadata)
    return make_response(jsonify({'metadata' : metadata, 'data': data}), 200)
    
class ReportClickRoute(Resource):
  def post(self):
    click_json = json.loads(request.data)
    entities, viz_types, y, z = cc.increment_clicks(click_json)
    return make_response(jsonify({'entity_counts' : entities, 'viz_type_counts': viz_types, 'y_counts': y, 'z_counts': z}), 200)

class SetClicksRoute(Resource):
  def post(self):
    click_json = json.loads(request.data)
    entities, viz_types, y, z = cc.set_click_totals(click_json)
    return make_response(jsonify({'entity_counts' : entities, 'viz_type_counts': viz_types, 'y_counts': y, 'z_counts': z}), 200)

class ResetClicksRoute(Resource):
  def post(self):
    entities, viz_types, y, z = cc.reset_clicks()
    return make_response(jsonify({'entity_counts' : entities, 'viz_type_counts': viz_types, 'y_counts': y, 'z_counts': z}), 200)

api.add_resource(ReportClickRoute, '/increment_clicks')
api.add_resource(GenerateChartRoute, '/generate_chart')
api.add_resource(SetClicksRoute, '/set_clicks')
api.add_resource(ResetClicksRoute, '/reset_clicks')


if __name__ == '__main__':
   app.run()
