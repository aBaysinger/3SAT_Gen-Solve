"""
Austin Baysinger
Project 1
6/24/16
Collaboration with Adam Siefkas
"""

import random

def clauseGen():	#generates random clauses of random variables
	varNum = random.randrange(3, 11, 1)	#number of variables from 3-10 in x sub i
	clauseNum = random.randrange(1, 21, 1)	#number of clauses in statement
	clauseLst = []
	varUsed = []	#list of variables used in generated statement
	for i in range(1, clauseNum + 1):	#for each clause, generate 3 variables
		var1 = random.randrange(1, varNum + 1, 1)
		var2 = random.randrange(1, varNum + 1, 1)
		var3 = random.randrange(1, varNum + 1, 1)
		while (var1 == var2):	#checks to make sure equal variables aren't used in same clause
			var2 = random.randrange(1, varNum + 1, 1)
		while (var1 == var3) or (var2 == var3):
			var3 = random.randrange(1, varNum + 1, 1)
		varUsed.append(var1)
		varUsed.append(var2)
		varUsed.append(var3)
		tuple1 = (var1, random.randrange(0, 2)) #store variable in tuple where second index generates 50/50 chance of negation
		tuple2 = (var2, random.randrange(0, 2))
		tuple3 = (var3, random.randrange(0, 2))
		clauseLst.append([tuple1, tuple2, tuple3]) #add generated clauses to list of entire statement
	return (clauseLst, varUsed)
	
def expressionGen(lst):	#function to print properly formatted expression
	expStr = ""
	counter1 = 0
	for clause in lst:
		expStr += "("
		counter2 = 0
		for var in clause:
			x = "x"
			x += str(var[0])
			if var[1] == 0:
				neg = False
			else:
				neg = True
			if neg == False:
				expStr += x
			else:
				expStr += "~" + x
			counter2 += 1
			if counter2 < 3:
				expStr += " v "
		counter1 += 1
		if counter1 < len(lst):
			expStr += ") ^ "	
	expStr += ")"
	return expStr
	
def userIn(lst):	#takes user input of TF values for variables used in expression
	lstTF = []
	newLst = list(set(lst))	#gets rid of duplicate variable values and orders variables
	for i in newLst:
		x = ""
		while x != "T" and x != "t" and x!= "F" and x != "f":
			x = raw_input("Please enter a value (T/F) for variable x" + str(i) + ":")
		if x == "t" or x == "T":
			x = True
		elif x == "f" or x == "F":
			x = False
		lstTF.append((i, x)) #store in list of tuples (x, y) where x is variable and y is truth value assigned
	return lstTF

def adjustClause(lstTF, clauseLst):	#adjusts variable truth values according to user input and negation
	clst_copy = clauseLst
	for clause in range(len(clst_copy)):	#for each clause
		for i in range(0, len(clst_copy[clause])):		#for each variable tuple in each clause
			tup = clst_copy[clause][i]
			for var in lstTF:	#for each tuple in lstTF
				if var[0] == tup[0]:	#if variables equal each other
					if tup[1] == 1:
						if var[1] == False:
							var = (var[0], True)
						else:
							var = (var[0], False)
					clst_copy[clause][i] = (tup[0], var[1])
	return clst_copy
	
def eval(clst_copy):	#evaluates total expression and looks for clauses where all three variables are false
	f_count = 0
	for i in range(len(clst_copy)):
		for j in range(len(clst_copy[i])):
			if clst_copy[i][j][1] == False:
				f_count += 1
		if f_count == 3:
			f_clause = str(i + 1)
			print "This assignment is incorrect."
			print "Clause number " + f_clause + " is false."
			return
		else:
			f_count = 0
	print "This assignment is correct."
				
tup = clauseGen()
clauseLst = tup[0]
varUsed = tup[1]
print expressionGen(clauseLst)
lstTF = userIn(varUsed)
clst_copy = adjustClause(lstTF, clauseLst)
eval(clst_copy)
