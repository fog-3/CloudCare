package com.CloudCare.CloudCareSpring;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@SpringBootApplication
public class CloudCareSpringApplication {

	public static void main(String[] args) {
		SpringApplication.run(CloudCareSpringApplication.class, args);
	}

	@Bean
	public WebMvcConfigurer corsConfigurer() {
		return new WebMvcConfigurer() {
			@Override
			public void addCorsMappings(CorsRegistry registry) {
				registry.addMapping("/**")  // Permite CORS en todos los endpoints
						.allowedOrigins("http://localhost:4200")  // Dominio de Angular
						.allowedMethods("GET", "POST", "PUT", "DELETE")  // Métodos permitidos
						.allowedHeaders("*")  // Cabeceras permitidas
						.allowCredentials(true);  // Permite cookies y autenticación
			}
		};
	}
}
