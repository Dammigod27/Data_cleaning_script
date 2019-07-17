import csv
import pymysql 
import datetime

with open('sample_data.txt', 'rt') as f:
	reader = csv.reader(f, delimiter = ',', skipinitialspace=True)
	lineData = list()
	cols = next(reader)

	for line in reader:
		if line != []:
			lineData.append(line)
#data base connection
cnx = pymysql.connect(user = 'root', password = '',
						  host = '127.0.0.1',
						  database = 'emp')
cursor = cnx.cursor()
query = ("INSERT INTO emp_details "
		 "(ID, First_name, Last_name, department, salary) "
		 "VALUES (%s, %s, %s, %s, %s)")

#Change every item in the sub list into the correct data type and store it in a directory
for i in range(len(lineData)):
	employ = (lineData[i][0], lineData[i][1], lineData[i][2], lineData[i][3], lineData[i][4])
	cursor.execute(query, employ) 

cnx.commit()
cnx.close()