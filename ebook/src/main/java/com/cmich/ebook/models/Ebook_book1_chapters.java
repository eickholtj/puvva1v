/*
 This entity is an object class which defines all the objects of the chapters data such as 
 chapter_name, chapter_details, book_url
 */
package com.cmich.ebook.models;

import org.springframework.data.mongodb.core.mapping.Document;

//@Document- we provide the collection name 'book1_chapters'
@Document(collection="book1_chapters")	
public class Ebook_book1_chapters {

	String chapter_name;
	String chapter_details;
	String book_url;

	public String getBook_url() {
		return book_url;
	}

	public void setBook_url(String book_url) {
		this.book_url = book_url;
	}

	public String getChapter_name() {
		return chapter_name;
	}

	public void setChapter_name(String chapter_name) {
		this.chapter_name = chapter_name;
	}

	public String getChapter_details() {
		return chapter_details;
	}

	public void setChapter_details(String chapter_details) {
		this.chapter_details = chapter_details;
	}

}




