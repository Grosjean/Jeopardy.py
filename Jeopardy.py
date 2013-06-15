import sqlite3
import texttable

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

def get_random_categories():
	"""build a query of random category names from database and prints them out"""
	query = "SELECT id, name FROM category ORDER BY RANDOM() LIMIT %i" % 5
	randCats = build_query_results(query)
	return randCats

def print_categories(randCats):
	print "\n"
	for (counter,cat) in enumerate(randCats):
		print "%s : %s (%s)" % (counter+1,cat[1],cat[0])
	print "\n"
	
def get_questions_from_category(catNum):	
	query = "SELECT text, answer, value, isDD FROM clue WHERE category=%s LIMIT %i" % (catNum, 10)
	questions = build_query_results(query)
	return questions
	
randCats = get_random_categories()
print_categories(randCats)

category = int(raw_input("Which category: ")) -1

catQuestions = get_questions_from_category(randCats[category][0])

for cat in catQuestions:
	print "QUESTION: %s " % cat[0]
	print "ANSWER: %s " % cat[1]
	print "VALUE: %s " % cat[2]
	if cat[3] == "1":
		print "Daily Double!!" % cat[3]
	print "=" * 20

connection.close()

#59 founding fathers

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
