/* This is the user defined configuration class where we define resolvers 
 * that can resolve the different view technology. It helps in rendering the data
 * that is being from the database on to the required template that we define*/
package com.cmich.ebook;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.mustache.MustacheResourceTemplateLoader;
import org.springframework.boot.autoconfigure.mustache.web.MustacheViewResolver;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ResourceLoader;
import org.springframework.web.servlet.ViewResolver;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.view.mustache.MustacheTemplateLoader;

@EnableWebMvc
@Configuration
@ComponentScan
public class WebConfig {
	@Autowired
	ResourceLoader resourceLoader;

	@Bean
	public ViewResolver viewResolver() {
		// MustacheViewResolver resolves the Mustache template architecture.
		MustacheViewResolver mustacheViewResolver = new MustacheViewResolver();
		// Specifies the path where the templates are located
		mustacheViewResolver.setPrefix("/Ebook/src/main/resources/templates");
		mustacheViewResolver.setSuffix(".html");
		mustacheViewResolver.setCache(false);
		mustacheViewResolver.setContentType("text/html;charset=utf-8");
		
		//MustacheTemplateLoader loads the templates with the data
		MustacheTemplateLoader mustacheTemplateLoader = new MustacheTemplateLoader();
		mustacheTemplateLoader.setResourceLoader(resourceLoader);        
		return mustacheViewResolver;
	}
}