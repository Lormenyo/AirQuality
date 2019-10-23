from flask import Flask, render_template
from flask import request
import requests
import  mongoengine
from models import AQvalues

mongoengine.connect("AirQuality")
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  url = "http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID=ce52a38dd86d624e2ac8e06eb512dda5"

  r = requests.get(url.format()).json()
  weather = {
    'city': r['name'],
    'temperature': r['main']['temp'],
    'description': r['weather'][0]['description'],
    'icon': r['weather'][0]['icon']
  }
  return render_template("web.html")


@app.route('/postdata', methods=['POST', 'GET'])
def postdata():
    pmvalues = AQvalues()
    content = request.data      
    pmvalues.pm25 = content[0:4]
    pmvalues.pm10 = content[5:9]
    pmvalues.save()
    print(pmvalues.to_json(indent=4))
    # return "<h1>" + str(pmvalues.pm25) + "</h1><h1>" + str(pmvalues.pm10 ) + "</h1>"
    return render_template("web.html", pmvalues=pmvalues)

if __name__ == "__main__":
        app.run(debug=True)




#TODO: <---------IMPORTANT ----------------------------------->
# when you use the host='0.0.0.0' it wont work in the browser
#  but would work in the arduino ide(gives output in serial)
# I am sure it will work when I deploy it 

# with open('aq.csv', 'a') as csvFile:
#     fields = ['Date', 'Aq']
#     writer = csv.DictWriter(csvFile, fieldnames=fields)
#     # writer.writeheader()
#     writer.writerows(content)
#     return 'JSON posted' + str(content['temp'][0])