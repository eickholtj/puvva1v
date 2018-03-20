/*This is an interface which allows us to perform various operations using 
data objects in Spring Data
*/
package com.cmich.ebook.models;


import org.springframework.data.mongodb.repository.MongoRepository;


public interface Ebook_book2_chaptersRepository extends MongoRepository<Ebook_book2_chapters, String> {

}