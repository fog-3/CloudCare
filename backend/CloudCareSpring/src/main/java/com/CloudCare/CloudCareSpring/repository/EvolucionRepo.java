package com.CloudCare.CloudCareSpring.repository;

import com.CloudCare.CloudCareSpring.entities.EvolucionId;
import com.CloudCare.CloudCareSpring.entities.Pacientes;
import com.CloudCare.CloudCareSpring.entities.evolucion;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;
import java.util.Optional;

public interface EvolucionRepo extends JpaRepository<evolucion, EvolucionId> {
    @Query("SELECT e FROM evolucion e where e.id.paciente_id = :id ")
    Optional<List<evolucion>> findEvolucionById(@Param("id") Integer id);
}
