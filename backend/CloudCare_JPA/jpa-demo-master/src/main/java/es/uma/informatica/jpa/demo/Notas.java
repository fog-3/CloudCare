package es.uma.informatica.jpa.demo;

import jakarta.persistence.*;

import java.util.Date;
import java.util.Objects;

@Entity
public class Notas {
	@ManyToOne
	private Pacientes paciente;

	@EmbeddedId
	private NotasId id;

	private String nota;

	public NotasId getId() { return id; }
	public void setId(NotasId id) { this.id = id; }

	public String getNota() { return nota; }
	public void setNota(String nota) { this.nota = nota; }
}