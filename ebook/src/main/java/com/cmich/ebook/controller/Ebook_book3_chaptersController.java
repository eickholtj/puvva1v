package com.cmich.ebook.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import com.cmich.ebook.models.Ebook_book1_chaptersRepository;
import com.cmich.ebook.models.Ebook_book2_chaptersRepository;
import com.cmich.ebook.models.Ebook_book3_chaptersRepository;
import com.cmich.ebook.models.Ebook_booksRepository;

@RestController
@RequestMapping("/")
public class Ebook_book3_chaptersController {
	
	@Autowired
	private Ebook_book3_chaptersRepository repository;
	
	 //GET method /list--> Reads list of books from the database.
	 
	@RequestMapping(value="/book3_chapters", method=RequestMethod.GET)
	public ModelAndView books(){
		
		ModelAndView modelAndView = new ModelAndView();
        modelAndView.setViewName("book3_chapters");

		List lst = repository.findAll();
        modelAndView.addObject("book3_chapters", lst);
        return modelAndView;
		
	}
	
	
	
}