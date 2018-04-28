/*This controller class contains the request mapping, GET requests received by the 
 * service are handled in this module
 */
package com.cmich.ebook.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.assertj.core.internal.Lists;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Example;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import com.cmich.ebook.models.Ebook_books;
import com.cmich.ebook.models.Ebook_booksRepository;

@RestController
@RequestMapping("/")
public class Ebook_booksController {

	@Autowired
	private Ebook_booksRepository repository;

	//GET method /books --> Reads list of books from the database.

	@RequestMapping(value="/books", method=RequestMethod.GET)
	public ModelAndView books(){

		ModelAndView modelAndView = new ModelAndView();
		// We set the view name 'books' to which the data need to be rendered
		modelAndView.setViewName("books");
		// This operation will list all the books present in the 'books'
		// collection in the database
		List lt = repository.findAll();
		modelAndView.addObject("books", lt);
		return modelAndView;

	}
}