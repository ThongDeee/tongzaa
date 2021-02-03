
# Server Side
from flask import Flask
from flask_restful import Api,Resource,abort,reqparse,marshal_with,fields
import os
import json
import time
import requests



app=Flask(__name__)
api=Api(app)

##data  

def getbotnoi(self,name):
    return name



#design
class WeatherCity(Resource):
    def get(self,name):
        return {"ภาษา":"Hi"+ getbotnoi(self,name)}
   


#call
api.add_resource(WeatherCity,"/w/<string:name>")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
