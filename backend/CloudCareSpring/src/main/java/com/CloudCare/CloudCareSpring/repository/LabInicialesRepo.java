package com.CloudCare.CloudCareSpring.repository;

import com.CloudCare.CloudCareSpring.entities.evolucion;
import com.CloudCare.CloudCareSpring.entities.lab_iniciales;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;
import java.util.Optional;

public interface LabInicialesRepo extends JpaRepository<lab_iniciales, Integer> {
    @Query("SELECT l FROM lab_iniciales l where l.paciente_id = :id ")
    Optional<List<lab_iniciales>> findLabInicialesById(@Param("id") Integer id);
}
