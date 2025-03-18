package es.uma.informatica.jpa.demo;

import jakarta.persistence.Embeddable;
import jakarta.persistence.Temporal;
import jakarta.persistence.TemporalType;

import java.util.Date;
import java.util.Objects;

@Embeddable
public class NotasId {
    @Temporal(TemporalType.DATE)
    private Date fecha;

    private Integer pacienteId;

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        NotasId that = (NotasId) o;
        return Objects.equals(fecha, that.fecha) && Objects.equals(pacienteId, that.pacienteId);
    }

    @Override
    public int hashCode() {
            return Objects.hash(fecha, pacienteId);
        }
}
