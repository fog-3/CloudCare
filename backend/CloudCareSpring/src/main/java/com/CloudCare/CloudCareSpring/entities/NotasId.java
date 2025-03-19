package com.CloudCare.CloudCareSpring.entities;

import jakarta.persistence.Column;
import jakarta.persistence.Embeddable;
import jakarta.persistence.Temporal;
import jakarta.persistence.TemporalType;

import java.util.Date;
import java.util.Objects;

@Embeddable
public class NotasId {
    @Temporal(TemporalType.DATE)
    private Date fecha;

    private Integer paciente_id;

    public Date getFecha() {
        return fecha;
    }

    public void setFecha(Date fecha) {
        this.fecha = fecha;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        NotasId that = (NotasId) o;
        return Objects.equals(fecha, that.fecha) && Objects.equals(paciente_id, that.paciente_id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(fecha, paciente_id);
    }
}
