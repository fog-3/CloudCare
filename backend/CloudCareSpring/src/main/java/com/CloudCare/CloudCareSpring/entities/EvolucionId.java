package com.CloudCare.CloudCareSpring.entities;

import jakarta.persistence.Column;
import jakarta.persistence.Embeddable;
import jakarta.persistence.Temporal;
import jakarta.persistence.TemporalType;

import java.io.Serializable;
import java.util.Date;
import java.util.Objects;

@Embeddable
public class EvolucionId implements Serializable {
    @Temporal(TemporalType.TIMESTAMP)
    private Date fecha_y_hora;

    private Integer paciente_id;

    public Date getFechaYHora() {
        return fecha_y_hora;
    }

    public void setFechaYHora(Date fechaYHora) {
        this.fecha_y_hora = fecha_y_hora;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        EvolucionId that = (EvolucionId) o;
        return Objects.equals(fecha_y_hora, that.fecha_y_hora) && Objects.equals(paciente_id, that.paciente_id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(fecha_y_hora, paciente_id);
    }
}
