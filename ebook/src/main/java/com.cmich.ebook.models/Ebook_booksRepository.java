/*This is an interface which allows us to perform various operations using 
 * data objects in Spring Data
 * */
package com.cmich.ebook.models;


import org.springframework.data.mongodb.repository.MongoRepository;


public interface Ebook_booksRepository extends MongoRepository<Ebook_books, String> {

}
