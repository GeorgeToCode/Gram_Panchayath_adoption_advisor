from __future__ import print_function

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='gram' ,autocommit=True )

cur = conn.cursor()

#fetch all data into a tuple

cur.execute("SELECT * FROM data")
t=cur.fetchall()
print(t)


# cerdits

agri=10
bas_am=10
lit=9
health=10
hygene=10
san=10
nat_res=8
drink_wat=10
hosp=9
bank=9
veh=7
smart_div=7

tot_credit = agri+bas_am+lit+health+hygene+san+nat_res+drink_wat+hosp+bank+veh+smart_div

leng = len(t);
#print(len)

for i in range(0,leng):
	#for j in range(2,len(t[i]):
	tup = t[i]

	q1=tup[4]*agri
	q2=tup[5]*bas_am
	q3=tup[6]*lit
	q4=tup[7]*health
	q5=tup[8]*san
	q6=tup[9]*nat_res
	q7=tup[10]*drink_wat
	q8=tup[11]*hosp
	q9=tup[12]*bank
	q10=tup[13]*veh
	q11=tup[14]*smart_div

	q_tot=q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11
	val = q_tot/tot_credit

	

	
	#cur.execute(" UPDATE data SET value=val WHERE id=i ")
	cur.execute(""" UPDATE data set value = %s where id=%s """,(val,i+1))

	
tr = []
cur.execute("SELECT name from data order by value")
nam=cur.fetchall()

# print the order of adoption


print("__ Adoption order __")
for i in nam:
	#print(i,"\n")
	for j in i:
		tr.append(j)


q=1
for i in tr:
	print(q,"-  ",i)
	q=q+1


cur.close()
conn.close()