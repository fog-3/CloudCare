package com.CloudCare.CloudCareSpring.entities;

import java.io.Serializable;

import jakarta.persistence.*;

@Entity
public class lab_iniciales {
    @Id
    private Integer paciente_id;

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

    public Integer getPacienteId() { return paciente_id; }
    public void setPacienteId(Integer pacienteId) { this.paciente_id = pacienteId; }
}
