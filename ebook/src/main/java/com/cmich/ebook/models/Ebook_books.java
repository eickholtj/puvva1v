/*
 This entity is an object class which defines all the objects of the books data such as 
 book_name, book_details, book_url
 */
package com.cmich.ebook.models;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

//@Document- we provide the collection name 'books'
@Document(collection="books")	
public class Ebook_books{


	String book_name;
	String book_details;
	String book_url;

	public String getBook_url() {
		return book_url;
	}

	public void setBook_url(String book_url) {
		this.book_url = book_url;
	}


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

