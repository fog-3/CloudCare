package com.CloudCare.CloudCareSpring.service;

import com.CloudCare.CloudCareSpring.entities.medicacion;
import com.CloudCare.CloudCareSpring.entities.notas;
import com.CloudCare.CloudCareSpring.exception.PacienteNotFoundException;
import com.CloudCare.CloudCareSpring.repository.NotasRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class NotasService {
    private final NotasRepo notasRepo;

    @Autowired
    public NotasService(NotasRepo notasRepo) {
        this.notasRepo = notasRepo;
    }

    public List<notas> findNotasById(Integer pacienteId) {
        return notasRepo.findNotasById(pacienteId)
                .orElseThrow(() -> new PacienteNotFoundException("Paciente con id " + pacienteId + "no ha sido encotrado"));
    }
}
