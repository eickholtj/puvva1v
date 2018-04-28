#Importing pymongo to connect to the MongoDB
import pymongo
from pymongo import MongoClient
#Importing random fucntion to create the sample random data in the database
from random import randint
#Connecting to MongoDB 
client = MongoClient('localhost')
#Ebook is the database that is created within MongoDB
db=client.Ebook
#Creating sample data
names = ['PROGRAMMING WITH LISTS','OBJECTS IN JAVA PROGRAMMING','PROGRAMMING WITH FUNCTIONS', 'FUNDAMENTAL CLOUD COMPUTING','WORKING WITH CLOUDS', 'INTRODUCTION TO DATABASE SYSTEMS','THE RELATIONAL MODEL','SQL: QUERIES', 'WRITING SIMPLE PROGRAMS','CONTROL STRUCTURES', 'COMPUTER SECURITYCONCEPTS','CRYPTOGRAPHIC TOOLS AND ALGORITHMS','SECURITY THREATS AND COUNTERMEASURES', 'DATA MODEL FOR BIG DATA','A NEW PARADIGM FOR BIG DATA']
details = ['This section deals with creation of lists and its usage with examples in JAVA programming', 'This section deals with usage of objects in Java programming', 'This section deals with creation and usage of functions along with some examples', 'This section deals with few basic concepts in Database management Systems', 'This section deals with the organization of data items within the database', 'This section deals with several operations with the data in the database', 'This section deals with writing basic samples programs in python language', 'This section deals with different types of control structures and their usage with examples', 'This section deals with basic concepts in computer sectionurity', 'This section deals with several types of algorithms and tools that exists in the cryptography','This section deals with various attacks and security breaches, also deals with the measures that handle these attacks and breaches', 'This section deals with the introduction of big data and also few basic concepts in the big data', 'This section deals with properties of data along with different models for presenting the data and the usage of Graph Schemas', 'This section deals with fundamentals and basic concepts in Cloud Computing', 'This section deals with cloud delivery model considerations, cost metrics and pricing as well as SECURITYquality measures and SLAs']
for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book1_chapter1_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 1 chapter 1!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book1_chapter2_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 1 chapter 2!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book1_chapter3_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 1 chapter 3!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book1_chapter4_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 1 chapter 4!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book1_chapter5_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 1 chapter 5!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book1_chapter6_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 1 chapter 6!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book2_chapter1_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 2 chapter 1!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book2_chapter2_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 2 chapter 2!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book2_chapter3_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 2 chapter 3!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book2_chapter4_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 2 chapter 4!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book2_chapter5_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 2 chapter 5!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book2_chapter6_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 2 chapter 6!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book3_chapter1_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 3 chapter 1!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book3_chapter2_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 3 chapter 2!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book3_chapter3_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 3 chapter 3!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book3_chapter4_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 3 chapter 4!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book3_chapter5_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 3 chapter 5!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book4_chapter1_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 4 chapter 1!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book4_chapter2_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 4 chapter 2!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book4_chapter3_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 4 chapter 3!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book4_chapter4_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 4 chapter 4!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book4_chapter5_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 4 chapter 5!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book4_chapter6_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 4 chapter 6!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book5_chapter1_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 5 chapter 1!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book5_chapter2_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 5 chapter 2!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book5_chapter3_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 5 chapter 3!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book5_chapter4_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 5 chapter 4!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book5_chapter5_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 5 chapter 5!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book6_chapter1_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 6 chapter 1!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book6_chapter2_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 6 chapter 2!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book6_chapter3_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 6 chapter 3!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book6_chapter4_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 6 chapter 4!')

for x in range(1, 4):
    Ebook = {
		'id' : randint(1, 3),
        'section_name' : names[randint(0, (len(names)-1))],
        'content' : details[randint(0, (len(details)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))] + ' ' + details[randint(0, (len(names)-1))]
    }
    #Insert Ebook object directly into MongoDB via insert_one
    db.book6_chapter5_section.insert_one(Ebook),
	
    #Tell that database has been created successfully
print('Successfully Created sections in book 6 chapter 5!')
