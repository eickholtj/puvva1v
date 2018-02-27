import pymongo
from pymongo import MongoClient
from random import randint
#Connect to MongoDB 
client = MongoClient('localhost')
db=client.Ebook
#Create sample data
names = ['PROGRAMMING WITH LISTS','OBJECTS IN JAVA PROGRAMMING','PROGRAMMING WITH FUNCTIONS', 'FUNDAMENTAL CLOUD COMPUTING','WORKING WITH CLOUDS', 'INTRODUCTION TO DATABASE SYSTEMS','THE RELATIONAL MODEL','SQL: QUERIES', 'WRITING SIMPLE PROGRAMS','CONTROL STRUCTURES', 'COMPUTER SECURITY CONCEPTS','CRYPTOGRAPHIC TOOLS AND ALGORITHMS','SECURITY THREATS AND COUNTERMEASURES', 'DATA MODEL FOR BIG DATA','A NEW PARADIGM FOR BIG DATA']

details = ['This chapter deals with creation of lists and its usage with examples in JAVA programming', 'This chapter deals with usage of objects in Java programming', 'This chapter deals with creation and usage of functions along with some examples', 'This chapter deals with few basic concepts in Database management Systems', 'This chapter deals with the organization of data items within the database', 'This chapter deals with several operations with the data in the database', 'This chapter deals with writing basic samples programs in python language', 'This chapter deals with different types of control structures and their usage with examples', 'This chapter deals with basic concepts in computer security', 'This chapter deals with several types of algorithms and tools that exists in the cryptography','This chapter deals with various attacks and security breaches, also deals with the measures that handle these attacks and breaches', 'This chapter deals with the introduction of big data and also few basic concepts in the big data', 'This chapter deals with properties of data along with different models for presenting the data and the usage of Graph Schemas', 'This chapter deals with fundamentals and basic concepts in Cloud Computing', 'This chapter deals with cloud delivery model considerations, cost metrics and pricing as well as security quality measures and SLAs']
for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'chapter_name' : names[randint(0, (len(names)-1))],
        'chapter_details' : details[randint(0, (len(details)-1))] 
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book1_chap.insert_one(Ebook),
book1_chap = db.Ebook

book1_chap = db.book1_chap.insert_many(
		(
			{
				"id":"1",
				"chapter_name":"PROGRAMMING WITH LISTS",
				"chapter_details":"This chapter deals with creation of lists and its usage with examples in JAVA programming"
			},
			{
				"id":"2",
				"chapter_name":"OBJECTS IN JAVA PROGRAMMING",
				"chapter_details":"This chapter deals with usage of objects in Java programming"
			},
			{
				"id":"3",
				"chapter_name":"PROGRAMMING WITH FUNCTIONS",
				"chapter_details":"This chapter deals with creation and usage of functions along with some examples"
			}
		)
	);
	
    #Tell that database has been created successfully
print('Successfully Created chapters in book 1!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'chapter_name' : names[randint(0, (len(names)-1))],
        'chapter_details' : details[randint(0, (len(details)-1))] 
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book2_chap.insert_one(Ebook),
	
book2_chap = db.Ebook

book2_chap = db.book2_chap.insert_many(
		(
			{
				"id":"1",
				"chapter_name":"INTRODUCTION TO DATABASE SYSTEMS",
				"chapter_details":"This chapter deals with few basic concepts in Database management Systems"
			},
			{
				"id":"2",
				"chapter_name":"THE RELATIONAL MODEL",
				"chapter_details":"This chapter deals with the organization of data items within the database"
			},
			{
				"id":"3",
				"chapter_name":"SQL: QUERIES",
				"chapter_details":"This chapter deals with several operations with the data in the database"
			}
		)
	);
	
    #Tell that database has been created successfully
print('Successfully Created chapters in book 2!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'chapter_name' : names[randint(0, (len(names)-1))],
        'chapter_details' : details[randint(0, (len(details)-1))] 
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book3_chap.insert_one(Ebook),
	
book3_chap = db.Ebook

book3_chap = db.book3_chap.insert_many(
		(
			{
				"id":"1",
				"chapter_name":"WRITING SIMPLE PROGRAMS",
				"chapter_details":"This chapter deals with writing basic samples programs in python language"
			},
			{
				"id":"2",
				"chapter_name":"CONTROL STRUCTURES",
				"chapter_details":"This chapter deals with different types of control structures and their usage with examples"
			}
		)
	);
	
    #Tell that database has been created successfully
print('Successfully Created chapters in book 3!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'chapter_name' : names[randint(0, (len(names)-1))],
        'chapter_details' : details[randint(0, (len(details)-1))] 
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book4_chap.insert_one(Ebook),
	
book4_chap = db.Ebook

book4_chap = db.book4_chap.insert_many(
		(
			{
				"id":"1",
				"chapter_name":"COMPUTER SECURITY CONCEPTS",
				"chapter_details":"This chapter deals with basic concepts in computer security"
			},
			{
				"id":"2",
				"chapter_name":"CRYPTOGRAPHIC TOOLS AND ALGORITHMS",
				"chapter_details":"This chapter deals with several types of algorithms and tools that exists in the cryptography"
			},
			{
				"id":"3",
				"chapter_name":"SECURITY THREATS AND COUNTERMEASURES",
				"chapter_details":"This chapter deals with various attacks and security breaches, also deals with the measures that handle these attacks and breaches"
			}
		)
	);
	
    #Tell that database has been created successfully
print('Successfully Created chapters in book 4!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'chapter_name' : names[randint(0, (len(names)-1))],
        'chapter_details' : details[randint(0, (len(details)-1))] 
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book5_chap.insert_one(Ebook),
	
book5_chap = db.Ebook

book5_chap = db.book5_chap.insert_many(
		(
			{
				"id":"1",
				"chapter_name":" A NEW PARADIGM FOR BIG DATA",
				"chapter_details":"This chapter deals with the introduction of big data and also few basic concepts in the big data"
			},
			{
				"id":"2",
				"chapter_name":"DATA MODEL FOR BIG DATA",
				"chapter_details":"This chapter deals with properties of data along with different models for presenting the data and the usage of Graph Schemas"
			}
		)
	);
	
    #Tell that database has been created successfully
print('Successfully Created chapters in book 5!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'chapter_name' : names[randint(0, (len(names)-1))],
        'chapter_details' : details[randint(0, (len(details)-1))] 
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book6_chap.insert_one(Ebook),

book6_chap = db.Ebook

book6_chap = db.book6_chap.insert_many(
		(
			{
				"id":"1",
				"chapter_name":"FUNDAMENTAL CLOUD COMPUTING",
				"chapter_details":"This chapter deals with fundamentals and basic concepts in Cloud Computing"
			},
			{
				"id":"2",
				"chapter_name":"WORKING WITH CLOUDS",
				"chapter_details":"This chapter deals with cloud delivery model considerations, cost metrics and pricing as well as security quality measures and SLA's"
			}
		)
	);

    #Tell that database has been created successfully
print('Successfully Created chapters in book 6!')
