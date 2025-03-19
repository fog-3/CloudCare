package com.CloudCare.CloudCareSpring.service;

import com.CloudCare.CloudCareSpring.entities.Pacientes;
import com.CloudCare.CloudCareSpring.entities.evolucion;
import com.CloudCare.CloudCareSpring.exception.PacienteNotFoundException;
import com.CloudCare.CloudCareSpring.repository.EvolucionRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class EvolucionService {
    private  final EvolucionRepo evolucionRepo;

    @Autowired
    public EvolucionService(EvolucionRepo evolucionRepo) {
        this.evolucionRepo = evolucionRepo;
    }

    public List<evolucion> findEvolucionById(Integer pacienteId) {
        return evolucionRepo.findEvolucionById(pacienteId)
                .orElseThrow(() -> new PacienteNotFoundException("Paciente con id " + pacienteId + "no ha sido encotrado"));
    }
}
