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
    #cursor.execute(thesql)
    #if cursor.fetchone()[0]:
    return "ok"

  def apiPoints(self, user, thetype):
    if thetype == 'bike':
      pointval = 3
    elif thetype == 'train':
      pointval = 3
    else:
      pointval = 2
    db = MySQLdb.connect(self.rdscnx['host'],self.rdscnx['username'],self.rdscnx['password'],self.rdscnx['db'])
    cursor = db.cursor()
    thesql = """select id from users where email_address = '%s' limit 1""" % (user)
    cursor.execute(thesql)
    row = cursor.fetchone()
    userid = row[0]
    thesql = """INSERT INTO points (type, points, user_id )VALUES ('%s','%s','%s')""" % (thetype, pointval, userid)
    cursor.execute(thesql)
    db.commit()
    return "\nOK\n"

  def apiZone(self):
    db = MySQLdb.connect(self.rdscnx['host'],self.rdscnx['username'],self.rdscnx['password'],self.rdscnx['db'])
    cursor = db.cursor()
    cursor.execute("""SELECT name, cur_cars FROM zones""")
    return_data = {}
    for row in cursor.fetchall():
      name = row[0]
      cur_cars = row[1]
      return_data[name] = cur_cars
    return json.dumps(return_data)

  def getLeaders(self):
    db = MySQLdb.connect(self.rdscnx['host'],self.rdscnx['username'],self.rdscnx['password'],self.rdscnx['db'])
    cursor = db.cursor() 
    cursor.execute("""select firstname, lastname, lcase(firstname) as avatar, (SELECT SUM(points) from points where users.id=points.user_id) as points from users order by points desc limit 5""")
    lrows = cursor.fetchall()
    html = ''
    for row in lrows:
      html = html + '<div class="row"><div class="col-xs-12 col-md-2">' + '<img src="static/img/' + str(row[2]) + '.png" width="50px" height="50px alt=\"some_text\" >'
      html = html + '<div class="names">' + str(row[0]) + '</div></div><div class="col-xs-12 col-md-4"><h4>' + str(row[3]) + '</h4></div></div>'

    return html

  def getHistory(self):
    db = MySQLdb.connect(self.rdscnx['host'],self.rdscnx['username'],self.rdscnx['password'],self.rdscnx['db'])
    cursor = db.cursor() 
    cursor.execute("""select year(DATE_SUB(historytime, INTERVAL 7 HOUR)) as year, month(DATE_SUB(historytime, INTERVAL 7 HOUR)) as month, day(DATE_SUB(historytime, INTERVAL 7 HOUR)) as day, hour(DATE_SUB(historytime, INTERVAL 7 HOUR)) as hour, minute(DATE_SUB(historytime, INTERVAL 7 HOUR)) as minute, cars from zone_history order by historytime""")
    hrows = cursor.fetchall()
    theseries = ""
    for row in hrows:
      theseries = theseries +  "[Date.UTC(" + str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]) + "," + str(row[4]) + "), " + str(row[5]) + "],"
    return theseries

      #hours, minutes = map(int, "00:00".split(':'))
      #theseries = theseries + "Date.UTC(2016, 8, 5" +  str(row[0]) + ","
    #print(theseries)

    #2016-10-07 03:00:00

   # [Date.UTC(2013, 3, 22, 1, 15), 12.7], 
      #      [Date.UTC(2012, 3, 24, 3, 20), 13.5], 
      #      [Date.UTC(2012, 2, 22, 2, 25), 18.8]
    #return theseries
    #7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6
  #  sTitle = 'title: {text: \'By Application\'}'
 #   sTooltip = 'tooltip: {pointFormat: \'{series.name}: <b>${point.y:.1f} ({point.percentage:.1f}%)</b>\'}'
#    sSeries = 'series: [{name: \'Cost\',colorByPoint: true,data: [{name: \'ATG\',y: ' + str(c_atg) + '},{name: \'IDM\',y: ' + str(c_idm) + '},{name: \'OAG\',y: ' + str(c_oag) + '},{name: \'Merlin\',y: ' + str(c_merlin) + '},{name: \'Endeca\',y: ' + str(c_endeca) + '},{name: \'OracleDB\',y: ' + str(c_oracledb) + '},{name: \'MySQL\',y: ' + str(c_mysql) + '},{name: \'BI\',y: ' + str(c_bi) + '},{name: \'EBS\',y: ' + str(c_ebs) + '},{name: \'Sabrix\',y: ' + str(c_sabrix) + '},{name: \'Digital\',y: ' + str(c_digi) + '},{name: \'Pioneer\',y: ' + str(c_pio) + '},{name: \'SOA\',y: ' + str(c_soa) + '},{name: \'TBB\',y: ' + str(c_tbb) + '},{name: \'MCT\',y: ' + str(c_cga) + '},{name: \'Other\',y: ' + str(c_other) + '}]}]'
#    sRenderto = 'histChart'
#    return ('{chart: {renderTo: ' + sRenderto + ', type: "pie",plotBackgroundColor: null,plotBorderWidth: null,plotShadow: false,}' + ',' + sSeries + ',' + sTooltip + ',' + sPlotOptions + ',' + sTitle + ',' + sLegend + '}')


  #return lrows
