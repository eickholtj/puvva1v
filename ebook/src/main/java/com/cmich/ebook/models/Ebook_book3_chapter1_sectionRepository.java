/*This is an interface which allows us to perform various operations using 
  data objects in Spring Data. Also it maps the objects created with the data in the MongoDB
 */
package com.cmich.ebook.models;

import org.springframework.data.mongodb.repository.MongoRepository;


public interface Ebook_book3_chapter1_sectionRepository extends MongoRepository<Ebook_book3_chapter1_section, String> {

}
