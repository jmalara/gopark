from flask import Flask, render_template, request, redirect, json
from modules import gopark
from modules.gopark import gopark

application = Flask(__name__)
# Main redirect
@application.route('/api', methods = ['POST'])
def api():
  gpy = gopark()
  jsondata = request.json
  sensorid =jsondata.get("sensor") 
  print("\n" + json.dumps(request.json) + "\n")
  print("\n" + jsondata.get("sensor") + "\n")
  gpy.apiSensor(sensorid)
  return "1"

  #retVal = lh.sensorAPI(

@application.route('/')
def splasht():
  return render_template("splash.html")
  
@application.route('/3')
def direct3():
  return render_template("3.html")

@application.route("/dashboard")
def dashboard():
  return render_template("dashboard.html")

@application.route("/cost")
def cost():
  lh = lighthouse()
  therows = lh.getServers('all')
  envChart = lh.genCostChart('env', therows)
  dcChart = lh.genCostChart('dc', therows)
  appChart = lh.genCostChart('app', therows)
  return render_template("cost.html",title="title", lh=lh, therows = therows, envChart=envChart, appChart=appChart, dcChart=dcChart,)

@application.route("/servermgmt")
def serverMgmt():
  lh = lighthouse()
  therows = lh.getServers('all')
  envChart = lh.genCostChart('env', therows)
  dcChart = lh.genCostChart('dc', therows)
  appChart = lh.genCostChart('app', therows)
  return render_template("servermgmt.html",title="title", lh=lh, therows = therows, envChart=envChart, appChart=appChart, dcChart=dcChart,)

# Foreman API Function
@application.route("/api/foreman")
def forman_return():
   ForemanAPI.getHosts()

if __name__ == "__main__":
  application.run(host='0.0.0.0', port=5000, debug=True)
