/*
 *  This entity is an object class which defines all the objects of the books data such as Id, 
 *   book_name, book_details.
 *    */
package com.cmich.ebook.models;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;


@Document(collection="books")	//@Document provides the collection name
public class Ebook_books{

	
	String book_name;
	String book_details;
	
	
		
	public String getBook_name() {
		return book_name;
	}

	public void setBook_name(String book_name) {
		this.book_name = book_name;
	}

	public String getBook_details() {
		return book_details;
	}

	public void setBook_details(String book_details) {
		this.book_details = book_details;
	}
	
}
