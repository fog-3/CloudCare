package com.CloudCare.CloudCareSpring.repository;

import com.CloudCare.CloudCareSpring.entities.MedicacionId;
import com.CloudCare.CloudCareSpring.entities.NotasId;
import com.CloudCare.CloudCareSpring.entities.medicacion;
import com.CloudCare.CloudCareSpring.entities.notas;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;
import java.util.Optional;

public interface NotasRepo extends JpaRepository<notas, NotasId> {
    @Query("SELECT n FROM notas n where n.id.paciente_id = :id")
    Optional<List<notas>> findNotasById(@Param("id") Integer id);
}
