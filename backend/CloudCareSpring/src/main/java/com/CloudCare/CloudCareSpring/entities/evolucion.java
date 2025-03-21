package com.CloudCare.CloudCareSpring.entities;

import jakarta.persistence.*;

import java.util.Date;
import java.util.Objects;

@Entity
public class evolucion {
    @EmbeddedId
    private EvolucionId id;

    private Integer presion_sistolica;
    private Integer presion_diastolica;
    private Integer frecuencia_cardiaca;
    private Float temperatura;
    private Integer frecuencia_respiratoria;
    private Float saturacion_oxigeno;
    private Float glucosa;
    private Float leucocitos;
    private Float hemoglobina;
    private Integer plaquetas;
    private Float colesterol;
    private Float hdl;
    private Float ldl;
    private Float trigliceridos;
    private Float sodio;
    private Float potasio;
    private Float cloro;
    private Float creatinina;
    private Float urea;
    private Float ast;
    private Float alt;
    private Float bilirrubina;
    private Float ph;
    private Float pco2;
    private Float po2;
    private Float hco3;
    private Float lactato;

    public EvolucionId getId() { return id; }
    public void setId(EvolucionId id) { this.id = id; }

    public Integer getPresionSistolica() { return presion_sistolica; }
    public void setPresionSistolica(Integer presionSistolica) { this.presion_sistolica = presionSistolica; }

    public Integer getPresionDiastolica() { return presion_diastolica; }
    public void setPresionDiastolica(Integer presionDiastolica) { this.presion_diastolica = presionDiastolica; }

    public Integer getFrecuenciaCardiaca() { return frecuencia_cardiaca; }
    public void setFrecuenciaCardiaca(Integer frecuenciaCardiaca) { this.frecuencia_cardiaca = frecuenciaCardiaca; }

    public Float getTemperatura() { return temperatura; }
    public void setTemperatura(Float temperatura) { this.temperatura = temperatura; }

    public Integer getFrecuenciarespiratoria() { return frecuencia_respiratoria; }
    public void setFrecuenciarespiratoria(Integer frecuenciarespiratoria) { this.frecuencia_respiratoria = frecuenciarespiratoria; }

    public Float getSaturacionoxigeno() { return saturacion_oxigeno; }
    public void setSaturacionoxigeno(Float saturacionoxigeno) { this.saturacion_oxigeno = saturacionoxigeno; }

    public Float getGlucosa() { return glucosa; }
    public void setGlucosa(Float glucosa) { this.glucosa = glucosa; }

    public Float getLeucocitos() { return leucocitos; }
    public void setLeucocitos(Float leucocitos) { this.leucocitos = leucocitos;}

    public Float getHemoglobina() { return hemoglobina; }
    public void setHemoglobina(Float hemoglobina) { this.hemoglobina = hemoglobina; }

    public Integer getPlaquetas() { return plaquetas; }
    public void setPlaquetas(Integer plaquetas) { this.plaquetas = plaquetas; }

    public Float getColesterol() { return colesterol; }
    public void setColesterol(Float colesterol) { this.colesterol = colesterol; }

    public Float getHdl() { return hdl; }
    public void setHdl(Float hdl) { this.hdl = hdl; }

    public Float getLdl() { return ldl; }
    public void setLdl(Float ldl) { this.ldl = ldl; }

    public Float getTrigliceridos() { return trigliceridos; }
    public void setTrigliceridos(Float trigliceridos) { this.trigliceridos = trigliceridos; }

    public Float getSodio() { return sodio; }
    public void setSodio(Float sodio) { this.sodio = sodio; }

    public Float getPotasio() { return potasio; }
    public void setPotasio(Float potasio) { this.potasio = potasio; }

    public Float getCloro() { return cloro; }
    public void setCloro(Float cloro) { this.cloro = cloro; }

    public Float getCreatinina() { return creatinina; }
    public void setCreatinina(Float creatinina) { this.creatinina = creatinina; }

    public Float getUrea() { return urea; }
    public void setUrea(Float urea) { this.urea = urea; }

    public Float getAst() { return ast; }
    public void setAst(Float ast) { this.ast = ast; }

    public Float getAlt() { return alt; }
    public void setAlt(Float alt) { this.alt = alt; }

    public Float getBilirrubina() { return bilirrubina; }
    public void setBilirrubina(Float bilirrubina) { this.bilirrubina = bilirrubina; }

    public Float getPh() { return ph; }
    public void setPh(Float ph) { this.ph = ph; }

    public Float getPco2() { return pco2; }
    public void setPco2(Float pco2) { this.pco2 = pco2; }

    public Float getPo2() { return po2; }
    public void setPo2(Float po2) { this.po2 = po2; }

    public Float getHco3() { return hco3; }
    public void setHco3(Float hco3) { this.hco3 = hco3; }

    public Float getLactato() { return lactato; }
    public void setLactato(Float lactato) { this.lactato = lactato; }
}
