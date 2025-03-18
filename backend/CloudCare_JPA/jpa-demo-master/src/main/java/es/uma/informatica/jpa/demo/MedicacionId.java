package es.uma.informatica.jpa.demo;

import jakarta.persistence.Embeddable;

import java.util.Objects;

@Embeddable
public class MedicacionId {
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
