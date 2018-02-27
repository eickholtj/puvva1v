import pymongo
from pymongo import MongoClient
from random import randint
#Connect to MongoDB 
client = MongoClient('localhost')
db=client.Ebook
#Create sample data
names = ['PRINCIPLES OF PROGRAMMING LANGUAGE by','DATABASE MANAGEMENT SYSTEM by','PYTHON PROGRAMMING: AN INTRODUCTION TO COMPUTER SCIENCE by', 'COMPUTER SECURITY: PRINCIPLES AND PRACTICE BY WILLIAM STALLINGS by', 'BIG DATA: PRINCIPLES AND BEST PRACTICES OF SCALABLE REAL-TIME DATA SYSTEMS by','CLOUD COMPUTING: CONCEPTS, TECHNOLOGY & ARCHITECTURE BY THOMAS ERL by']
authors = ['DOWEK AND GILLES','RAGHU RAMAKRISHNAN AND JOHANNES GEHRKE','JOHN ZELLE','WILLIAM STALLINGS','NATHAN MARZ AND JAMES WARREN','THOMAS ERL']
details = ['This book mainly deals with some of the basic concepts in programming language like Java which makes it easy for the to learn for a beginner.', 'The database management systems book mainly deals with basic concepts in creating and maintaining a database for a beginner.', 'This book mainly contains the introduction concept in programming but is dealt with a unconventional programming language like Python. It contains all the concepts that deals with designing and developing a programming language as a whole.']
for x in range(1, 7):
    Ebook = {
        'book_name' : names[randint(0, (len(names)-1))] + ' ' + authors[randint(0, (len(authors)-1))],
        'book_details' : details[randint(0, (len(details)-1))] 
    }
    #Insert Ebook object directly into MongoDB via insert_one
    result=db.books.insert_one(Ebook)

books = db.Ebook
books = db.books.insert_many(
		(
			{
				"book_name":"PRINCIPLES OF PROGRAMMING LANGUAGE BY DOWEK AND GILLES",
				"book_details":"This book mainly deals with some of the basic concepts in programming language like Java which makes it easy for the to learn for a beginner."
			},
			{
				"book_name":"DATABASE MANAGEMENT SYSTEM BY RAGHU RAMAKRISHNAN AND JOHANNES GEHRKE",
				"book_details":"The database management systems book mainly deals with basic concepts in creating and maintaining a database for a beginner."
			},
			{
				"book_name":"PYTHON PROGRAMMING: AN INTRODUCTION TO COMPUTER SCIENCE BY JOHN ZELLE",
				"book_details":"This book mainly contains the introduction concept in programming but is dealt with a unconventional programming language like Python. It contains all the concepts that deals with designing and developing a programming language as a whole. "
			}
		)
	);
    #Tell that database has been created successfully
print('Successfully Created !')

