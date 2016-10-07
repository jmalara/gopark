from flask import Flask, render_template, request, redirect, json, session
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

@application.route('/apizone')
def apizone():
  gpy = gopark()
  return gpy.apiZone()

@application.route('/login', methods = ['POST'])
def loginuser():
  gpy = gopark()
  email = request.form['email']
  fname = request.form['fname']
  lname = request.form['lname']
  avatar = request.form['avatar'] 
  gpy.loginUser(email, fname, lname, avatar)
  session['email'] = email
  #gpy.apiSensor(sensorid)
  return "ok"

@application.route('/apiuser', methods = ['POST'])
def apiuser():
  gpy = gopark()
  jsondata = request.json
  sensorid =jsondata.get("sensor") 
  print("\n" + json.dumps(request.json) + "\n")
  print("\n" + jsondata.get("sensor") + "\n")
  #gpy.apiSensor(sensorid)
  return "1"

@application.route('/apipoints', methods = ['POST'])
def apipoint():
  gpy = gopark()
  user = session['email']
  thetype = request.form['type']
  gpy.apiPoints(user, thetype)
  return gpy.getLeaders()

  #retVal = lh.sensorAPI(

@application.route('/')
def splash():
  return render_template("splash.html")

@application.route('/signin')
def sign():
  return render_template("signin.html")

@application.route('/zito')
def zito():
  return render_template("zito.html")

@application.route('/signup')
def signup():
  return render_template("signup.html")

@application.route('/3')
def direct3():
  return render_template("3.html")

@application.route("/dashboard")
def dashboard():
  print(session['email'])
  gpy = gopark()
  leaderhtml = gpy.getLeaders()
  history = gpy.getHistory()
  return render_template("dashboard.html", leaderhtml=leaderhtml  , history=history)

if __name__ == "__main__":
  application.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWXs,?Ra'
  application.run(host='0.0.0.0', port=80, debug=True)
