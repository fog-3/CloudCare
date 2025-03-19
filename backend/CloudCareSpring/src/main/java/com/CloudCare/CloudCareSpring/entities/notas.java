package com.CloudCare.CloudCareSpring.entities;

import jakarta.persistence.*;

import java.io.Serializable;
import java.util.Date;
import java.util.Objects;

@Entity
public class notas implements Serializable {
    @EmbeddedId
    private NotasId id;

    private String nota;

    public NotasId getId() { return id; }
    public void setId(NotasId id) { this.id = id; }

    public String getNota() { return nota; }
    public void setNota(String nota) { this.nota = nota; }
}