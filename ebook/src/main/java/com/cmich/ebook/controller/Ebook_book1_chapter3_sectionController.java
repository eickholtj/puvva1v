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

import com.cmich.ebook.models.Ebook_book1_chapter1_sectionRepository;
import com.cmich.ebook.models.Ebook_book1_chapter3_sectionRepository;
import com.cmich.ebook.models.Ebook_book1_chaptersRepository;

@RestController
@RequestMapping("/")
public class Ebook_book1_chapter3_sectionController {

	@Autowired
	private Ebook_book1_chapter3_sectionRepository repository;

	//GET method /book1_chapter3_section --> Reads list of sections from the database.

	@RequestMapping(value="/book1_chapter3_section", method=RequestMethod.GET)
	public ModelAndView books(){

		ModelAndView modelAndView = new ModelAndView();
		// We set the view name 'book1_chapter3_section' to which the data need to be rendered
		modelAndView.setViewName("book1_chapter3_section");
		// This operation will list all the sections present in the 'book1_chapter3_section'
		// collection in the database
		List lt = repository.findAll();
		modelAndView.addObject("book1_chapter3_section", lt);
		return modelAndView;

	}
}
