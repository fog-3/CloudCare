package es.uma.informatica.jpa.demo;

import java.io.Serializable;

import jakarta.persistence.*;

/**
 * Entity implementation class for Entity: Book
 *
 */
@Entity
public class Lab_Iniciales {
	@Id  // Usamos pacienteId como clave primaria
	private Integer pacienteId;

	private Float glucosa;
	private Float ph;
	private Float cetonas;
	private Float creatinina;
	private Float hemoglobina;
	private Float leucocitos;
	private Float sodio;
	private Float potasio;
	private Float urea;
	private Float amilasa;

	@OneToOne
	@MapsId
	@JoinColumn(name = "pacienteId")
	private Pacientes paciente;

	public Float getGlucosa() { return glucosa; }
	public void setGlucosa(Float glucosa) { this.glucosa = glucosa; }

	public Float getPh() { return ph; }
	public void setPh(Float ph) { this.ph = ph; }

	public Float getCetonas() { return cetonas; }
	public void setCetonas(Float cetonas) { this.cetonas = cetonas; }

	public Float getCreatinina() { return creatinina; }
	public void setCreatinina(Float creatinina) { this.creatinina = creatinina; }

	public Float getHemoglobina() { return hemoglobina; }
	public void setHemoglobina(Float hemoglobina) { this.hemoglobina = hemoglobina; }

	public Float getLeucocitos() { return leucocitos; }
	public void setLeucocitos(Float leucocitos) { this.leucocitos = leucocitos; }

	public Float getSodio() { return sodio; }
	public void setSodio(Float sodio) { this.sodio = sodio; }

	public Float getPotasio() { return potasio; }
	public void setPotasio(Float potasio) { this.potasio = potasio; }

	public Float getUrea() { return urea; }
	public void setUrea(Float urea) { this.urea = urea; }

	public Float getAmilasa() { return amilasa; }
	public void setAmilasa(Float amilasa) { this.amilasa = amilasa; }

	//public Integer getPacienteId() { return pacienteId; }
	//public void setPacienteId(Integer pacienteId) { this.pacienteId = pacienteId; }
}
