import sys
import pymongo
from pymongo import MongoClient

def main():
	client = MongoClient('localhost')
	print (client)
	db = client.Ebook
	annotations = db.Ebook

	annotations = db.annotations.insert(
		(
			{
				"id":" ",
				"annotation_name":" ",
				"note":" "
			}
		)
	);
	print ("Successfully Created")
if __name__ == "__main__":
    main()

