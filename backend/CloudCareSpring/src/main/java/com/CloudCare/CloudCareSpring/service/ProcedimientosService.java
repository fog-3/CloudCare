package com.CloudCare.CloudCareSpring.service;

import com.CloudCare.CloudCareSpring.entities.medicacion;
import com.CloudCare.CloudCareSpring.entities.procedimientos;
import com.CloudCare.CloudCareSpring.exception.PacienteNotFoundException;
import com.CloudCare.CloudCareSpring.repository.ProcedimientosRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProcedimientosService {
    private final ProcedimientosRepo procedimientosRepo;

    @Autowired
    public ProcedimientosService(ProcedimientosRepo procedimientosRepo) {
        this.procedimientosRepo = procedimientosRepo;
    }

    public List<procedimientos> findProcedimientosById(Integer pacienteId) {
        return procedimientosRepo.findProcedimientosById(pacienteId)
                .orElseThrow(() -> new PacienteNotFoundException("Paciente con id " + pacienteId + "no ha sido encotrado"));
    }
}
