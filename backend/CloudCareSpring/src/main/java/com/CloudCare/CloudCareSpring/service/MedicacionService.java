package com.CloudCare.CloudCareSpring.service;

import com.CloudCare.CloudCareSpring.entities.lab_iniciales;
import com.CloudCare.CloudCareSpring.entities.medicacion;
import com.CloudCare.CloudCareSpring.exception.PacienteNotFoundException;
import com.CloudCare.CloudCareSpring.repository.MedicacionRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class MedicacionService {
    private final MedicacionRepo medicacionRepo;

    @Autowired
    public MedicacionService(MedicacionRepo medicacionRepo) {
        this.medicacionRepo = medicacionRepo;
    }

    public List<medicacion> findMedicacionById(Integer pacienteId) {
        return medicacionRepo.findMedicacionById(pacienteId)
                .orElseThrow(() -> new PacienteNotFoundException("Paciente con id " + pacienteId + "no ha sido encotrado"));
    }
}
