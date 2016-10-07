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

    return lrows




  def genCostChart(self, type, data):
    # Global chart values
    sLegend = '"legend":{"enabled":true}'
    sPlotOptions = 'plotOptions: {pie: {allowPointSelect: true,cursor: \'pointer\',dataLabels: {enabled: true},showInLegend: false}}'
    
    if type == 'env':
      c_dev = 0
      c_qa = 0
      c_uat = 0
      c_prd = 0

      for row in data:
        # Calc cost
        c = self.genCost(row[10],row[7], row[8], row[9], 10, row[0])
        if row[6] == 'dev':
          c_dev += c
        elif  row[6] == 'qa':
          c_qa +=  c
        elif  row[6] == 'uat':
          c_uat +=  c
        elif  row[6] == 'prd':
          c_prd += c

      sTitle = 'title: {text: \'By Environment\'}'
      sTooltip = 'tooltip: {pointFormat: \'{series.name}: <b>${point.y:.1f} ({point.percentage:.1f}%)</b>\'}'
      sSeries = 'series: [{name: \'Cost\',colorByPoint: true,data: [{name: \'DEV\',y: ' + str(c_dev) + '}, {name:\'QA\',y:  ' + str(c_qa) + '}, {name: \'UAT\',y: ' + str(c_uat) + '}, {name: \'PRD\',y: ' + str(c_prd) + '}]}]'
      sRenderto = 'envChart'


    if type == 'dc':
      c_lv = 0
      c_es = 0
      c_other = 0
      for row in data:
        # Calc cost
        c = self.genCost(row[10],row[7], row[8], row[9], 10, row[0])
        if row[7] == 'LVDC':
          c_lv += c
        elif  row[7] == 'ESDC':
          c_es += c
        else:
          c_other +=  c

      sTitle = 'title: {text: \'By Datacenter\'}'
      sTooltip = 'tooltip: {pointFormat: \'{series.name}: <b>${point.y:.1f} ({point.percentage:.1f}%)</b>\'}'
      sSeries = 'series: [{name: \'Cost\',colorByPoint: true,data: [{name: \'ESDC\',y: ' + str(c_es) + '}, {name:\'LVDC\',y:  ' + str(c_lv) + '}, {name: \'Other\',y: ' + str(c_other) + '}]}]'
      sRenderto = 'dcChart'


    if type == 'app':
      c_atg = 0
      c_idm = 0
      c_oag = 0
      c_merlin = 0
      c_endeca = 0
      c_agile = 0
      c_oracledb = 0
      c_mysql = 0
      c_bi = 0
      c_ebs = 0
      c_sabrix = 0
      c_digi = 0
      c_pio = 0
      c_soa = 0 
      c_rm = 0
      c_tbb = 0
      c_cga = 0
      c_other = 0
      for row in data:
        # Calc cost
        c = self.genCost(row[10],row[7], row[8], row[9], 10, row[0])
        if row[3] == 'atg':
          c_atg += c
        elif  row[3] == 'idm':
          c_idm +=  c
        elif  row[3] == 'oag':
          c_oag +=  c
        elif  row[3] == 'merlin':
          c_merlin +=  c
        elif  row[3] == 'endeca':
          c_endeca +=  c
        elif  row[3] == 'oracledb':
          c_oracledb +=  c
        elif  row[3] == 'mysql':
          c_mysql +=  c
        elif  row[3] == 'bi':
          c_bi +=  c
        elif  row[3] == 'ebs':
          c_ebs +=  c
        elif  row[3] == 'sabrix':
          c_sabrix +=  c
        elif  row[3] == 'digi':
          c_digi +=  c
        elif  row[3] == 'pio':
          c_pio +=  c
        elif  row[3] == 'soa' or row[3] == 'bpel' or row[3] == 'osb':
          c_soa +=  c
        elif  row[3] == 'tbb' or row[3] == 'liferay':
          c_tbb +=  c
        elif  row[3] == 'cga':
          c_cga +=  c
        else:
          c_other +=  c

      sTitle = 'title: {text: \'By Application\'}'
      sTooltip = 'tooltip: {pointFormat: \'{series.name}: <b>${point.y:.1f} ({point.percentage:.1f}%)</b>\'}'
      sSeries = 'series: [{name: \'Cost\',colorByPoint: true,data: [{name: \'ATG\',y: ' + str(c_atg) + '},{name: \'IDM\',y: ' + str(c_idm) + '},{name: \'OAG\',y: ' + str(c_oag) + '},{name: \'Merlin\',y: ' + str(c_merlin) + '},{name: \'Endeca\',y: ' + str(c_endeca) + '},{name: \'OracleDB\',y: ' + str(c_oracledb) + '},{name: \'MySQL\',y: ' + str(c_mysql) + '},{name: \'BI\',y: ' + str(c_bi) + '},{name: \'EBS\',y: ' + str(c_ebs) + '},{name: \'Sabrix\',y: ' + str(c_sabrix) + '},{name: \'Digital\',y: ' + str(c_digi) + '},{name: \'Pioneer\',y: ' + str(c_pio) + '},{name: \'SOA\',y: ' + str(c_soa) + '},{name: \'TBB\',y: ' + str(c_tbb) + '},{name: \'MCT\',y: ' + str(c_cga) + '},{name: \'Other\',y: ' + str(c_other) + '}]}]'
      sRenderto = 'appChart'


    return ('{chart: {renderTo: ' + sRenderto + ', type: "pie",plotBackgroundColor: null,plotBorderWidth: null,plotShadow: false,}' + ',' + sSeries + ',' + sTooltip + ',' + sPlotOptions + ',' + sTitle + ',' + sLegend + '}')

  def genCost(self, virtual, location, cpu, mem, storage,name):
    from decimal import Decimal, ROUND_HALF_UP
    if virtual == 'true':
      c_cpu = 50
      c_mem = '0.10'
      c_storage = 10
    if virtual == 'false':
      c_cpu = 100
      c_mem = '.25'
      c_storage = 10

    if cpu is not None:
      f_cpu = Decimal(cpu) * Decimal(c_cpu)
    else:
      return(0)
    if mem is not None:
      f_mem = Decimal(mem) * Decimal(c_mem)
    else:
      return(0)
    #f_storage = storage * c_storage
    f_total = f_cpu + f_mem
    return(round(f_total,0))