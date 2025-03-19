package com.CloudCare.CloudCareSpring.service;

import com.CloudCare.CloudCareSpring.entities.evolucion;
import com.CloudCare.CloudCareSpring.entities.lab_iniciales;
import com.CloudCare.CloudCareSpring.exception.PacienteNotFoundException;
import com.CloudCare.CloudCareSpring.repository.EvolucionRepo;
import com.CloudCare.CloudCareSpring.repository.LabInicialesRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class LabInicialesService {
    private  final LabInicialesRepo labInicialesRepo;

    @Autowired
    public LabInicialesService(LabInicialesRepo labInicialesRepo) {
        this.labInicialesRepo = labInicialesRepo;
    }

    public List<lab_iniciales> findLabInicialesById(Integer pacienteId) {
        return labInicialesRepo.findLabInicialesById(pacienteId)
                .orElseThrow(() -> new PacienteNotFoundException("Paciente con id " + pacienteId + "no ha sido encotrado"));
    }
}
