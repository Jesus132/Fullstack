from flask import Flask, render_template
import sqlite3 as sql

app= Flask(__name__)

data=None

def Base_Datos():
  con = sql.connect("Data.db")
  bdguarda= con.cursor()
  query='''SELECT *
			FROM Users'''
  bdguarda.execute(query)
  return(bdguarda.fetchall())

class scheduleData():
	def __init__(self):
		self.var={'Data':'Hola mundo'}

	def get(self):
		return self.var

@app.route("/api")
def root():
	global data
	data=scheduleData()
	return data.get()

@app.route("/api/v1/users/")
def getUsers():
  global data
  aux=Base_Datos()
  result=[]
  for i in range(len(aux)):
    result.append({'Id':aux[i][0],'First Name':aux[i][1],'Last Name':aux[i][2],'User Name':aux[i][3],'Mail':aux[i][4],'Password':aux[i][5]})
  
  return {'Data':result}

@app.route('/')
def index():
  SQLITE= Base_Datos()
  print(SQLITE)
  return render_template('index.html', matriz = SQLITE)


if __name__== '__main__':
    app.run(debug = True, host='0.0.0.0', port=80)
