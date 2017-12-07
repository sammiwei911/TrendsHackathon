#!/usr/bin/python3

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json

from select_metadata import generate_chart_metadata
from collect_data import collect_data
import change_clicks as cc

app = Flask(__name__)
api = Api(app)

access_control_response_headers = {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept'}

class GenerateChartRoute(Resource):
  def get(self):
    metadata = generate_chart_metadata()
    data = collect_data(metadata)
    return jsonify({'metadata' : metadata, 'data': data}), 200, access_control_response_headers
    
class ReportClickRoute(Resource):
  def post(self):
    click_json = json.loads(request.data)
    entities, viz_types, y, z = cc.add_click(click_json)
    return jsonify({'entity_counts' : entities, 'viz_type_counts': viz_types, 'y_counts': y, 'z_counts': z}), 200, access_control_response_headers

class SetClicksRoute(Resource):
  def post(self):
    click_json = json.loads(request.data)
    entities, viz_types, y, z = cc.set_click_totals(click_json)
    return jsonify({'entity_counts' : entities, 'viz_type_counts': viz_types, 'y_counts': y, 'z_counts': z}), 200, access_control_response_headers

class ResetClicksRoute(Resource):
  def post(self):
    entities, viz_types, y, z = cc.reset_clicks()
    return jsonify({'entity_counts' : entities, 'viz_type_counts': viz_types, 'y_counts': y, 'z_counts': z}), 200, access_control_response_headers

api.add_resource(ReportClickRoute, '/increment_clicks')
api.add_resource(GenerateChartRoute, '/generate_chart')
api.add_resource(SetClicksRoute, '/set_clicks')
api.add_resource(ResetClicksRoute, '/reset_clicks')


if __name__ == '__main__':
   app.run()
