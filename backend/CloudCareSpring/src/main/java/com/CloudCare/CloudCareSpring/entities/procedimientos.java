package com.CloudCare.CloudCareSpring.entities;

import java.io.Serializable;

import jakarta.persistence.*;


@Entity
public class procedimientos {
    @Id
    private Integer paciente_id;
    private String procedimientos;
    private String tratamientos;
    private String cirugias_previas;
    private String radiologia;

    public String getProcedimientos() { return procedimientos; }
    public void setProcedimientos(String procedimientos) { this.procedimientos = procedimientos; }

    public String getTratamientos() { return tratamientos; }
    public void setTratamientos(String tratamientos) { this.tratamientos = tratamientos; }

    public String getCirugiasprevias() { return cirugias_previas; }
    public void setCirugiasprevias(String cirugiasprevias) { this.cirugias_previas = cirugiasprevias; }

    public String getRadiologia() { return radiologia; }
    public void setRadiologia(String radiologia) { this.radiologia = radiologia; }

    public Integer getPacienteId() { return paciente_id; }
    public void setPacienteId(Integer pacienteId) { this.paciente_id = pacienteId; }
}
