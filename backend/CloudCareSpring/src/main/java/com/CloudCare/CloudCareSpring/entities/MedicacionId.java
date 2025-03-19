package com.CloudCare.CloudCareSpring.entities;

import jakarta.persistence.Column;
import jakarta.persistence.Embeddable;

import java.util.Date;
import java.util.Objects;

@Embeddable
public class MedicacionId {

    private String medicamento;

    private Integer paciente_id;

    public String getMedicamento() {
        return medicamento;
    }

    public void setMedicamento(String medicamento) {
        this.medicamento = medicamento;
    }


    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        MedicacionId that = (MedicacionId) o;
        return Objects.equals(medicamento, that.medicamento) && Objects.equals(paciente_id, that.paciente_id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(medicamento, paciente_id);
    }
}
