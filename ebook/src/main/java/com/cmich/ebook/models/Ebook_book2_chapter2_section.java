package com.cmich.ebook.models;

import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection="book2_chapter2_section")	//@Document provides the collection name
public class Ebook_book2_chapter2_section {

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




