/*This controller class contains the request mapping, GET requests received by the 
 * service are handled in this module
 */
package com.cmich.ebook.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import com.cmich.ebook.models.Ebook_book1_chaptersRepository;
import com.cmich.ebook.models.Ebook_booksRepository;

@RestController
@RequestMapping("/")
public class Ebook_book1_chaptersController {

	@Autowired
	private Ebook_book1_chaptersRepository repository;

	//GET method /book1_chapters --> Reads list of chapters from the database.

	@RequestMapping(value="/book1_chapters", method=RequestMethod.GET)
	public ModelAndView books(){

		ModelAndView modelAndView = new ModelAndView();
		// We set the view name 'book1_chapters' to which the data need to be rendered
		modelAndView.setViewName("book1_chapters");
		// This operation will list all the chapters present in the 'book1_chapters'
		// collection in the database
		List lt = repository.findAll();
		modelAndView.addObject("book1_chapters", lt);
		return modelAndView;

	}	
}