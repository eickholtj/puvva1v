#Importing pymongo to connect to the MongoDB
import pymongo
from pymongo import MongoClient
#Importing the random fucntion inorder to genrate random sample data in the database
from random import randrange
from random import randint
#Connecting to MongoDB 
client = MongoClient('localhost')
#Ebook is the datbase that is created within the MongoDB
db=client.Ebook
#Creating random sample data
names = ['PROGRAMMING WITH LISTS','OBJECTS IN JAVA PROGRAMMING','PROGRAMMING WITH FUNCTIONS', 'FUNDAMENTAL CLOUD COMPUTING','WORKING WITH CLOUDS', 'INTRODUCTION TO DATABASE SYSTEMS','THE RELATIONAL MODEL','SQL: QUERIES', 'WRITING SIMPLE PROGRAMS','CONTROL STRUCTURES', 'COMPUTER SECURITY CONCEPTS','CRYPTOGRAPHIC TOOLS AND ALGORITHMS','SECURITY THREATS AND COUNTERMEASURES', 'DATA MODEL FOR BIG DATA','A NEW PARADIGM FOR BIG DATA']

details = ['This chapter deals with creation of lists and its usage with examples in JAVA programming', 'This chapter deals with usage of objects in Java programming', 'This chapter deals with creation and usage of functions along with some examples', 'This chapter deals with few basic concepts in Database management Systems', 'This chapter deals with the organization of data items within the database', 'This chapter deals with several operations with the data in the database', 'This chapter deals with writing basic samples programs in python language', 'This chapter deals with different types of control structures and their usage with examples', 'This chapter deals with basic concepts in computer security', 'This chapter deals with several types of algorithms and tools that exists in the cryptography','This chapter deals with various attacks and security breaches, also deals with the measures that handle these attacks and breaches', 'This chapter deals with the introduction of big data and also few basic concepts in the big data', 'This chapter deals with properties of data along with different models for presenting the data and the usage of Graph Schemas', 'This chapter deals with fundamentals and basic concepts in Cloud Computing', 'This chapter deals with cloud delivery model considerations, cost metrics and pricing as well as security quality measures and SLAs']

urls = ['book1_chapter1_section','book2_chapter2_section','book1_chapter2_section','book1_chapter3_section']
book1_chapters = db.Ebook
#Inserting data into the collection
book1_chapters = db.book1_chapters.insert_many(
		(
			{
				"id":"1",
				"book_url":"book1_chapter1_section",				
				"chapter_name":"PROGRAMMING WITH LISTS",
				"chapter_details":"This chapter deals with creation of lists and its usage with examples in JAVA programming"
			},
			{
				"id":"2",
				"book_url":"book1_chapter2_section",
				"chapter_name":"OBJECTS IN JAVA PROGRAMMING",
				"chapter_details":"This chapter deals with usage of objects in Java programming"
			},
			{
				"id":"3",
				"book_url":"book1_chapter3_section",
				"chapter_name":"PROGRAMMING WITH FUNCTIONS",
				"chapter_details":"This chapter deals with creation and usage of functions along with some examples"
			}
		)
	);

for x in range(1, 3):
    Ebook = {
		'id' : randint(1, 3),
		'book_url' : urls[randrange(0,len(urls))],
        'chapter_name' : names[randint(0, (len(names)-1))],
        'chapter_details' : details[randint(0, (len(details)-1))] 
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book1_chapters.insert_one(Ebook)
	
    #Tell that database has been created successfully
print('Successfully Created chapters in book 1!')

book2_chapters = db.Ebook
#Inserting data into the collection
book2_chapters = db.book2_chapters.insert_many(
		(
			{
				"id":"1",
				"book_url":"book2_chapter1_section",
				"chapter_name":"INTRODUCTION TO DATABASE SYSTEMS",
				"chapter_details":"This chapter deals with few basic concepts in Database management Systems"
			},
			{
				"id":"2",
				"book_url":"book2_chapter2_section",
				"chapter_name":"THE RELATIONAL MODEL",
				"chapter_details":"This chapter deals with the organization of data items within the database"
			},
			{
				"id":"3",
				"book_url":"book2_chapter3_section",
				"chapter_name":"SQL: QUERIES",
				"chapter_details":"This chapter deals with several operations with the data in the database"
			}
		)
	);

for x in range(1, 3):
    Ebook = {
		'id' : randint(1, 3),
		'book_url' : urls[randrange(0,len(urls))],
        'chapter_name' : names[randint(0, (len(names)-1))],
        'chapter_details' : details[randint(0, (len(details)-1))] 
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book2_chapters.insert_one(Ebook)
	
    #Tell that database has been created successfully
print('Successfully Created chapters in book 2!')
	
book3_chapters = db.Ebook
#Inserting data into the collection
book3_chapters = db.book3_chapters.insert_many(
		(
			{
				"id":"1",
				"book_url":"book3_chapter1_section",
				"chapter_name":"WRITING SIMPLE PROGRAMS",
				"chapter_details":"This chapter deals with writing basic samples programs in python language"
			},
			{
				"id":"2",
				"book_url":"book3_chapter2_section",
				"chapter_name":"CONTROL STRUCTURES",
				"chapter_details":"This chapter deals with different types of control structures and their usage with examples"
			}
		)
	);

for x in range(1, 3):
    Ebook = {
		'id' : randint(1, 3),
		'book_url' : urls[randrange(0,len(urls))],
        'chapter_name' : names[randint(0, (len(names)-1))],
        'chapter_details' : details[randint(0, (len(details)-1))] 
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book3_chapters.insert_one(Ebook)	
    #Tell that database has been created successfully
print('Successfully Created chapters in book 3!')
	
book4_chapters = db.Ebook
#Inserting data into the collection
book4_chapters = db.book4_chapters.insert_many(
		(
			{
				"id":"1",
				"book_url":"book3_chapter1_section",
				"chapter_name":"COMPUTER SECURITY CONCEPTS",
				"chapter_details":"This chapter deals with basic concepts in computer security"
			},
			{
				"id":"2",
				"book_url":"book3_chapter2_section",
				"chapter_name":"CRYPTOGRAPHIC TOOLS AND ALGORITHMS",
				"chapter_details":"This chapter deals with several types of algorithms and tools that exists in the cryptography"
			},
			{
				"id":"3",
				"book_url":"book2_chapter1_section",
				"chapter_name":"SECURITY THREATS AND COUNTERMEASURES",
				"chapter_details":"This chapter deals with various attacks and security breaches, also deals with the measures that handle these attacks and breaches"
			}
		)
	);
	
for x in range(1, 2):
    Ebook = {
		'id' : randint(1, 3),
		'book_url' : urls[randrange(0,len(urls))],
        'chapter_name' : names[randint(0, (len(names)-1))],
        'chapter_details' : details[randint(0, (len(details)-1))] 
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book4_chapters.insert_one(Ebook)
    #Tell that database has been created successfully
print('Successfully Created chapters in book 4!')
	
book5_chapters = db.Ebook
#Inserting data into the collection
book5_chapters = db.book5_chapters.insert_many(
		(
			{
				"id":"1",
				"book_url":"book1_chapter1_section",
				"chapter_name":" A NEW PARADIGM FOR BIG DATA",
				"chapter_details":"This chapter deals with the introduction of big data and also few basic concepts in the big data"
			},
			{
				"id":"2",
				"book_url":"book2_chapter2_section",
				"chapter_name":"DATA MODEL FOR BIG DATA",
				"chapter_details":"This chapter deals with properties of data along with different models for presenting the data and the usage of Graph Schemas"
			}
		)
	);

for x in range(1, 2):
    Ebook = {
		'id' : randint(1, 3),
		'book_url' : urls[randrange(0,len(urls))],
        'chapter_name' : names[randint(0, (len(names)-1))],
        'chapter_details' : details[randint(0, (len(details)-1))] 
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book5_chapters.insert_one(Ebook)	
    #Tell that database has been created successfully
print('Successfully Created chapters in book 5!')

book6_chapters = db.Ebook
#Inserting data into the collection
book6_chapters = db.book6_chapters.insert_many(
		(
			{
				"id":"1",
				"book_url":"book1_chapter3_section",
				"chapter_name":"FUNDAMENTAL CLOUD COMPUTING",
				"chapter_details":"This chapter deals with fundamentals and basic concepts in Cloud Computing"
			},
			{
				"id":"2",
				"book_url":"book3_chapter2_section",
				"chapter_name":"WORKING WITH CLOUDS",
				"chapter_details":"This chapter deals with cloud delivery model considerations, cost metrics and pricing as well as security quality measures and SLA's"
			}
		)
	);

for x in range(1, 2):
    Ebook = {
		'id' : randint(1, 3),
		'book_url' : urls[randrange(0,len(urls))],
        'chapter_name' : names[randint(0, (len(names)-1))],
        'chapter_details' : details[randint(0, (len(details)-1))] 
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book6_chapters.insert_one(Ebook)	
    #Tell that database has been created successfully
print('Successfully Created chapters in book 6!')
