package com.CloudCare.CloudCareSpring.repository;

import com.CloudCare.CloudCareSpring.entities.NotasId;
import com.CloudCare.CloudCareSpring.entities.medicacion;
import com.CloudCare.CloudCareSpring.entities.notas;
import com.CloudCare.CloudCareSpring.entities.procedimientos;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;
import java.util.Optional;

public interface ProcedimientosRepo extends JpaRepository<procedimientos, Integer> {
    @Query("SELECT p FROM procedimientos p where p.paciente_id = :id")
    Optional<List<procedimientos>> findProcedimientosById(@Param("id") Integer id);
}
