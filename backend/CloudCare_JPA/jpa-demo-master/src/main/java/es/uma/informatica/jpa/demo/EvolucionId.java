package es.uma.informatica.jpa.demo;

import jakarta.persistence.Embeddable;
import jakarta.persistence.Temporal;
import jakarta.persistence.TemporalType;

import java.util.Date;
import java.util.Objects;

@Embeddable
public class EvolucionId {
    @Temporal(TemporalType.DATE)
    private Date fecha;

    @Temporal(TemporalType.DATE)
    private Date hora;

    private Integer pacienteId;

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        EvolucionId that = (EvolucionId) o;
        return Objects.equals(fecha, that.fecha) && Objects.equals(hora, that.hora);
    }

        @Override
        public int hashCode() {
            return Objects.hash(fecha, hora);
        }
}
