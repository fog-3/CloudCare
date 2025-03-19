package com.CloudCare.CloudCareSpring.service;

import com.CloudCare.CloudCareSpring.entities.Pacientes;
import com.CloudCare.CloudCareSpring.exception.PacienteNotFoundException;
import com.CloudCare.CloudCareSpring.repository.PacientesRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.UUID;

@Service
public class PacientesService {
    private  final PacientesRepo pacientesRepo;

    @Autowired
    public PacientesService(PacientesRepo pacientesRepo) {
        this.pacientesRepo = pacientesRepo;
    }

    public Pacientes addPaciente(Pacientes paciente){
        paciente.setPaciente_id(Integer.valueOf(UUID.randomUUID().toString()));
        return pacientesRepo.save(paciente);
    }

    public List<Pacientes> findAllPacientes() {
        return pacientesRepo.findAll();
    }

    public Pacientes updatePaciente(Pacientes paciente) {
        return pacientesRepo.save(paciente);
    }

    public Pacientes findPacienteById(Integer pacienteId){
        return pacientesRepo.findPacienteBypacienteId(pacienteId)
                .orElseThrow(() -> new PacienteNotFoundException("Paciente con id " + pacienteId + "no ha sido encotrado"));
    }

    public List<Pacientes> findPacienteByNombre(String nombre){
        return pacientesRepo.findPacienteByNombre(nombre)
                .orElseThrow(() -> new PacienteNotFoundException("Paciente con nombre " + nombre + "no ha sido encotrado"));
    }

    public void deletePaciente(Integer pacienteId){
        pacientesRepo.deletePacientesBypacienteId(pacienteId);
    }
}
