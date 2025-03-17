package es.uma.informatica.jpa.demo;

import jakarta.persistence.*;

import java.util.Date;
import java.util.Objects;

@Entity
public class Medicacion {
	@Embeddable
	public static class MedicacionId {
		private String medicamento;

		private Integer pacienteId;

		@Override
		public boolean equals(Object o) {
			if (o == null || getClass() != o.getClass()) return false;
			MedicacionId that = (MedicacionId) o;
			return Objects.equals(medicamento, that.medicamento) && Objects.equals(pacienteId, that.pacienteId);
		}

		@Override
		public int hashCode() {
			return Objects.hash(medicamento, pacienteId);
		}
	}

	@ManyToOne
	private Pacientes paciente;

	@EmbeddedId
	private MedicacionId id;

	private String dosis;
	private String via;

	public MedicacionId getId() { return id; }
	public void setId(MedicacionId id) { this.id = id; }

	public String getDosis() { return dosis; }
	public void setDosis(String dosis) { this.dosis = dosis; }

	public String getVia() { return via; }
	public void setVia(String via) { this.via = via; }
}
