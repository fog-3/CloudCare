package es.uma.informatica.jpa.demo;

import java.io.Serializable;

import jakarta.persistence.*;

/**
 * Entity implementation class for Entity: CD
 *
 */
@Entity
public class Procedimientos{
	@Id  // Usamos pacienteId como clave primaria
	private Integer pacienteId;

	private String procedimientos;
	private String tratamientos;
	private String cirugiasprevias;
	private String radiologia;

	@OneToOne
	@MapsId
	@JoinColumn(name = "pacienteId")
	private Pacientes paciente;

	public String getProcedimientos() { return procedimientos; }
	public void setProcedimientos(String procedimientos) { this.procedimientos = procedimientos; }

	public String getTratamientos() { return tratamientos; }
	public void setTratamientos(String tratamientos) { this.tratamientos = tratamientos; }

	public String getCirugiasprevias() { return cirugiasprevias; }
	public void setCirugiasprevias(String cirugiasprevias) { this.cirugiasprevias = cirugiasprevias; }

	public String getRadiologia() { return radiologia; }
	public void setRadiologia(String radiologia) { this.radiologia = radiologia; }

	//public Integer getPacienteId() { return pacienteid; }
	//public void setPacienteId(Integer pacienteId) { this.pacienteid = pacienteId; }
}
