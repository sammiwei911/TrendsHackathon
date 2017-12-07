#!/usr/bin/python3

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import json

from select_metadata import generate_chart_metadata
from collect_data import collect_data
import change_clicks as cc

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


class GenerateChartRoute(Resource):
  def get(self):
    metadata = generate_chart_metadata()
    data = collect_data(metadata)
    return jsonify({'metadata' : metadata, 'data': data})
    
class ReportClickRoute(Resource):
  def post(self):
    click_json = json.loads(request.data)
    entities, viz_types, y, z = cc.add_click(click_json)
    return jsonify({'entity_counts' : entities, 'viz_type_counts': viz_types, 'y_counts': y, 'z_counts': z})

class SetClicksRoute(Resource):
  def post(self):
    click_json = json.loads(request.data)
    entities, viz_types, y, z = cc.set_click_totals(click_json)
    return jsonify({'entity_counts' : entities, 'viz_type_counts': viz_types, 'y_counts': y, 'z_counts': z})

class ResetClicksRoute(Resource):
  def post(self):
    entities, viz_types, y, z = cc.reset_clicks()
    return jsonify({'entity_counts' : entities, 'viz_type_counts': viz_types, 'y_counts': y, 'z_counts': z})

api.add_resource(ReportClickRoute, '/increment_clicks')
api.add_resource(GenerateChartRoute, '/generate_chart')
api.add_resource(SetClicksRoute, '/set_clicks')
api.add_resource(ResetClicksRoute, '/reset_clicks')


if __name__ == '__main__':
   app.run()
