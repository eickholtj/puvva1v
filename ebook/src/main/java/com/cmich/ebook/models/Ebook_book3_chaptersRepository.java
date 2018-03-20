/*This is an interface which allows us to perform various operations using 
data objects in Spring Data
*/
package com.cmich.ebook.models;


import org.springframework.data.mongodb.repository.MongoRepository;


public interface Ebook_book3_chaptersRepository extends MongoRepository<Ebook_book3_chapters, String> {

}