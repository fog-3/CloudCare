package es.uma.informatica.jpa.demo;

import jakarta.persistence.*;

import java.util.Date;
import java.util.Objects;

@Entity
public class Notas {
	@Embeddable
	public static class NotasId {
		@Temporal(TemporalType.DATE)
		private Date fecha;

		private Integer pacienteId;

		@Override
		public boolean equals(Object o) {
			if (o == null || getClass() != o.getClass()) return false;
			NotasId that = (NotasId) o;
			return Objects.equals(fecha, that.fecha) && Objects.equals(pacienteId, that.pacienteId);
		}

		@Override
		public int hashCode() {
			return Objects.hash(fecha, pacienteId);
		}
	}

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