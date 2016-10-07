import MySQLdb
from flask import json
class gopark(object):
  rdscnx= {'host': 'jgross-hack-db-cluster-1.cluster-culomlubyiwb.us-west-2.rds.amazonaws.com',
  'username': 'jgross',
  'password': '14gVe#yg7!',
  'db': 'gopark'}

  def apiSensor(self, sensorid):
    db = MySQLdb.connect(self.rdscnx['host'],self.rdscnx['username'],self.rdscnx['password'],self.rdscnx['db'])
    cursor = db.cursor()
    cursor.execute("""INSERT INTO sensor_input (sensor_id)VALUES (%s)""",(sensorid))
    db.commit()
    return "\nOK\n"

  def loginUser(self, email, fname, lname, avatar):
    db = MySQLdb.connect(self.rdscnx['host'],self.rdscnx['username'],self.rdscnx['password'],self.rdscnx['db'])
    cursor = db.cursor()
    thesql = """select id from users where email_address = '%s' limit 1""" % (email)
    cursor.execute(thesql)
    row_count = cursor.rowcount
    if row_count == 0:
      thesql = """INSERT INTO users (email_address, firstname, lastname, avatar )VALUES ('%s','%s','%s','%s')""" % (email, fname, lname, avatar)
      cursor.execute(thesql)
      db.commit()
    else:
      return "ok"     

  def apiPoints(self, user, thetype):
    if thetype == 'bike':
      pointval = 3
      typetext = 'bicycle'
    elif thetype == 'train':
      pointval = 3
      typetext = 'train'
    elif thetype == 'car':
      pointval = 2
      typetext = 'carpool'
    elif thetype == 'carself':
      pointval = 1
      typetext = 'car'
    else:
      pointval = 0

    if pointval == 0:
      return "ok"
    
    t
    db = MySQLdb.connect(self.rdscnx['host'],self.rdscnx['username'],self.rdscnx['password'],self.rdscnx['db'])
    cursor = db.cursor()
    thesql = """select id from users where email_address = '%s' limit 1""" % (user)
    print(thesql)
    cursor.execute(thesql)
    row = cursor.fetchone()
    userid = row[0]
    thesql = """INSERT INTO points (type, points, user_id )VALUES ('%s','%s','%s')""" % (typetext, pointval, userid)
    print(thesql)
    cursor.execute(thesql)
    db.commit()
    return "\nOK\n"

  def checkin(self, email):
    db = MySQLdb.connect(self.rdscnx['host'],self.rdscnx['username'],self.rdscnx['password'],self.rdscnx['db'])
    cursor = db.cursor()
    thesql = """select points.type, users.id, points.id from users left join points on users.id=points.user_id where points.point_time > DATE_SUB(now(), INTERVAL 24 HOUR) and users.email_address = '%s' order by points.point_time desc limit 1 """ % (email)
    cursor.execute(thesql)
    row_count = cursor.rowcount
    if row_count == 0:
      return 1
    else:
      row = cursor.fetchone()
      return str(row[0])

  def apiZone(self):
    db = MySQLdb.connect(self.rdscnx['host'],self.rdscnx['username'],self.rdscnx['password'],self.rdscnx['db'])
    cursor = db.cursor()
    cursor.execute("""SELECT name, cur_cars, capacity FROM zones""")
    return_data = {}
    for row in cursor.fetchall():
      name = row[0]
      cur_cars = row[1]
      capacity = row[2]
      diff = capacity- cur_cars
      return_data[name] = diff
    return json.dumps(return_data)

  def getLeaders(self):
    db = MySQLdb.connect(self.rdscnx['host'],self.rdscnx['username'],self.rdscnx['password'],self.rdscnx['db'])
    cursor = db.cursor() 
    cursor.execute("""select firstname, lastname, avatar as avatar, (SELECT SUM(points) from points where users.id=points.user_id) as points from users order by points desc limit 10""")
    lrows = cursor.fetchall()
    html = ''
    for row in lrows:
      if str(row[3]) == 'None':
        pointnum = '0'
      else:
        pointnum = str(row[3]) 
      html = html + '<div class="row"><div class="col-xs-12 col-md-2">' + '<img src="' + str(row[2]) + '" width="50px" height="50px alt=\"some_text\" >'
      html = html + '<div class="names">' + str(row[0]) + '</div></div><div class="col-xs-12 col-md-4"><h4>' + pointnum + ' points</h4></div></div>'

    return html

  def getHistory(self):
    db = MySQLdb.connect(self.rdscnx['host'],self.rdscnx['username'],self.rdscnx['password'],self.rdscnx['db'])
    cursor = db.cursor() 
    cursor.execute("""select year(DATE_SUB(historytime, INTERVAL 7 HOUR)) as year, month(DATE_SUB(historytime, INTERVAL 7 HOUR)) as month, day(DATE_SUB(historytime, INTERVAL 7 HOUR)) as day, hour(DATE_SUB(historytime, INTERVAL 7 HOUR)) as hour, minute(DATE_SUB(historytime, INTERVAL 7 HOUR)) as minute, cars from zone_history where historytime > DATE_SUB(now(), INTERVAL 24 HOUR) order by historytime desc""")
    hrows = cursor.fetchall()
    theseries = ""
    for row in hrows:
      theseries = theseries +  "[Date.UTC(" + str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]) + "," + str(row[4]) + "), " + str(row[5]) + "],"
    return theseries

