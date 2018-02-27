/* This method method uses Spring Boot’s SpringApplication.run() method to launch the application*/
package com.cmich.ebook;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class EbookApplication {

	public static void main(String[] args) {
		SpringApplication.run(EbookApplication.class, args);

	}
}
