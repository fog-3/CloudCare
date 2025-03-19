package com.CloudCare.CloudCareSpring.entities;

import jakarta.persistence.*;

import java.io.Serializable;
import java.util.Date;
import java.util.Objects;

@Entity
public class medicacion implements Serializable {
    @EmbeddedId
    private MedicacionId id;

    private String dosis;
    private String via;

    public MedicacionId getId() { return id; }
    public void setId(MedicacionId id) { this.id = id; }

    public String getDosis() { return dosis; }
    public void setDosis(String dosis) { this.dosis = dosis; }

    public String getVia() { return via; }
    public void setVia(String via) { this.via = via; }
}
