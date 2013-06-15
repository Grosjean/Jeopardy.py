import sqlite3
import os, os.path, time, sys, random

"""
CATEGORY
	ID - integer
	NAME - text. Name of the category where playing with
	GAME - integer. set of numnbers?
	ROUND - integer. (0, 1, or 2)... which round we're on?
	BOARDPOSITIONS - integer (1 through 5, corresponding with 100, 200 - 500?)

CLUE
	ID - integer
	TEXT - text. The actual question we're asking
	GAME - integer (matches category)
	CATEGORY - integer. LINKS TO THE ID FROM CATEGORY
	VALUE - integer. How much is the question worth
	ANSWER - text. the answer to question
	ISDD - integer (0 or 1)
	PICKINDEX - integer. nother set of number, 1 -99?

"""

connection = sqlite3.connect('db\jeopardy.db')
cursor = connection.cursor()

def build_query_results(query):
	"""builds the query results based on input and returns the list"""
	
	cursor.execute(query)
	return cursor.fetchall()

def get_random_categories(num):
	"""build a query of random category names from database and prints them out
	takes the number of categories to query"""
	
	query = "SELECT id, name FROM category ORDER BY RANDOM() LIMIT %i" % num
	randCats = build_query_results(query)
	return randCats

def print_categories(randCats):
	"""Prints out the random categories"""
	print "\n"
	for (counter,cat) in enumerate(randCats):
		print "\t%s : %s" % (counter+1,cat[1])
	print "\t" + "-" * 25
	print "\t0 : Enter 0 to exit"
	print "\n"
	
def get_questions_from_category(catNum):
	"""Querieis the specified categoryto grab question and answer"""
	query = "SELECT text, answer, value, isDD FROM clue WHERE category=%s LIMIT %i" % (catNum, 10)
	questions = build_query_results(query)
	return questions

def print_category_questions(catQuestions):
	"""prints out the question and answers based on catQuestions query"""
	for cat in catQuestions:
		print "QUESTION: %s " % cat[0]
		print "ANSWER: %s " % cat[1]
		print "VALUE: %s " % cat[2]
		if cat[3] == "1":
			print "Daily Double!!"
		print "=" * 20
	

randCats = get_random_categories(6) #gets 6 random categories and stores as randCats list

continueGame = True

while continueGame:

	print_categories(randCats) #prints out the new rand cats
	
	try:
		category = int(raw_input("Which category: ")) - 1
	except ValueError:
		print "\nIncorrect Value!"
		break
	
	if category == -1:
		continueGame = False
	else:
		catQuestions = get_questions_from_category(randCats[category][0]) #sends the select category to print out a list of questions
		print_category_questions(catQuestions)
	
		time.sleep(2)
	
else:
	print "\n\nThanks for Playing!!\n"

connection.close()

"""
results = build_query_results("SELECT text, answer, value FROM clue LIMIT 10")

print "\nExample clues:\n"
for clue in results:
    text, answer, value = clue
    print "[$%s]" % (value,)
    print "A: %s" % (text,)
    print "Q: What is '%s'" % (answer,)
    print ""
"""

"""
def print_table(d):
	header = d.keys()
	rows = zip(*d.items())

	table = texttable.Texttable()
	table.header(header)
	table.add_rows(rows,header=True)
	print table.draw()
	
	print "\n\n"
d = {}
for cat in randCats:
	d[cat] = ["$100","$200","$300","$400","$500"]

print_table(d)
"""
