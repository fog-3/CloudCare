package es.uma.informatica.jpa.demo;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;
import jakarta.persistence.Query;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.List;

public class Main {
	public static void main(String[] args) {
		EntityManagerFactory emf = Persistence.createEntityManagerFactory("jpa.demo");
		EntityManager em = emf.createEntityManager();

		Query q = em.createQuery("SELECT p.nombre FROM Pacientes p");
		List<Pacientes> ps = q.getResultList();
		for(int i = 0; i < ps.size(); ++i) {
			System.out.println(ps.get(i));
		}

		em.close();
		emf.close();
	}

}
