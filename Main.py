from flask import Flask
from flask_restful import Resource, Api
import json, xmltodict
import csv
app = Flask(__name__)
api = Api(app)

class Valencia(Resource):
    def get(self):
        data = []
        with open("directorio-de-bibliotecas-valencianas_2020.csv", encoding="utf8") as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=';')
            for rows in csvReader:
                data.append(rows)
            return {'data': data}, 200

class EuskadiJson(Resource):
    def get(self):
        with open('bibliotecas.json', encoding="utf8") as json_file:
            data = json.load(json_file)
        
            return {'data': data}, 200  # return data and 200 OK code


class CatJson(Resource):
    def get(self):
        with open('biblioteques.xml', 'r', encoding="utf8") as myfile:
            #data = []
            #obj = xmltodict.parse(myfile.read())

            #return {'data': obj["response"]["row"]}, 200
            return {'data': myfile.read()}, 200

api.add_resource(Valencia, '/valencia')  # '/valencia' is our entry point for Valencia
api.add_resource(EuskadiJson, '/euskadiJson')  # '/euskadiJson' is our entry point for EuskadiJson
api.add_resource(CatJson, '/catJson')  # '/catJson' is our entry point for CatJson

if __name__ == '__main__':
    app.run()  # run our Flask app