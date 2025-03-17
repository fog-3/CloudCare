package es.uma.informatica.jpa.demo;

import java.io.Serializable;
import java.util.Date;
import java.util.List;

import jakarta.persistence.*;

/**
 * Entity implementation class for Entity: Artist
 *
 */
@Entity

public class Pacientes implements Serializable {
	@Id
	private Integer pacienteId;

	private String nombre;
	private Integer edad;
	private Character sexo;
	private String alergias;
	private String motivoingreso;
	private String diagnosticoprincipal;
	private String condicionesprevias;

	@Temporal(TemporalType.DATE)
	private Date fechaingreso;

	private String servicio;
	private String estadoalingreso;

	@OneToMany (mappedBy = "paciente")
	private List<Evolucion> evolucion;

	@OneToMany (mappedBy = "paciente")
	private List<Medicacion> medicacion;

	@OneToMany (mappedBy = "paciente")
	private List<Notas> notas;

	public Integer getPacienteid() { return pacienteId; }
	public void setPacienteid(Integer pacienteid) { this.pacienteId = pacienteid; }

	public String getNombre() { return nombre; }
	public void setNombre(String nombre) { this.nombre = nombre; }

	public Integer getEdad() { return edad; }
	public void setEdad(Integer edad) { this.edad = edad; }

	public Character getSexo() { return sexo; }
	public void setSexo(Character sexo) { this.sexo = sexo; }

	public String getAlergias() { return alergias; }
	public void setAlergias(String alergias) { this.alergias = alergias; }

	public String getMotivoingreso() { return motivoingreso; }
	public void setMotivoingreso(String motivoingreso) { this.motivoingreso = motivoingreso; }

	public String getDiagnosticoprincipal() { return diagnosticoprincipal; }
	public void setDiagnosticoprincipal(String diagnosticoprincipal) { this.diagnosticoprincipal = diagnosticoprincipal; }

	public String getCondicionesprevias() { return condicionesprevias; }
	public void setCondicionesprevias(String condicionesprevias) { this.condicionesprevias = condicionesprevias; }

	public Date getFechaingreso() { return fechaingreso; }
	public void setFechaingreso(Date fechaingreso) { this.fechaingreso = fechaingreso; }

	public String getServicio() { return servicio; }
	public void setServicio(String servicio) { this.servicio = servicio; }

	public String getEstadoalingreso() { return estadoalingreso; }
	public void setEstadoalingreso(String estadoalingreso) { this.estadoalingreso = estadoalingreso; }
}
