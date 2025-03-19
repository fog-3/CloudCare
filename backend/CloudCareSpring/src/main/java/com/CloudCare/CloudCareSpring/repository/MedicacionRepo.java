package com.CloudCare.CloudCareSpring.repository;

import com.CloudCare.CloudCareSpring.entities.MedicacionId;
import com.CloudCare.CloudCareSpring.entities.Pacientes;
import com.CloudCare.CloudCareSpring.entities.lab_iniciales;
import com.CloudCare.CloudCareSpring.entities.medicacion;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;
import java.util.Optional;

public interface MedicacionRepo extends JpaRepository<medicacion, MedicacionId> {
    @Query("SELECT m FROM medicacion m where m.id.paciente_id = :id")
    Optional<List<medicacion>> findMedicacionById(@Param("id") Integer id);
}
