/*
 This entity is an object class which defines all the objects of the sections data such as 
 section_name and content
 */
package com.cmich.ebook.models;

import org.springframework.data.mongodb.core.mapping.Document;

//@Document- we provide the collection name 'book2_chapter3_section'
@Document(collection="book2_chapter3_section")	
public class Ebook_book2_chapter3_section {

	String section_name;
	String content;

	public String getSection_name() {
		return section_name;
	}

	public void setSection_name(String section_name) {
		this.section_name = section_name;
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}

}





