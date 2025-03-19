package com.CloudCare.CloudCareSpring.repository;

import com.CloudCare.CloudCareSpring.entities.Pacientes;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;
import java.util.Optional;

public interface PacientesRepo extends JpaRepository<Pacientes, Integer> {
    void deletePacientesBypacienteId(Integer pacienteId);

    Optional<Pacientes> findPacienteBypacienteId(Integer pacienteId);

    @Query("SELECT p FROM Pacientes p where p.nombre like %:nombre% ")
    Optional<List<Pacientes>> findPacienteByNombre(@Param("nombre") String nombre);
}
