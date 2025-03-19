package com.CloudCare.CloudCareSpring;

import com.CloudCare.CloudCareSpring.entities.*;
import com.CloudCare.CloudCareSpring.service.*;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/pacientes")
public class PacientesResource {
    private final PacientesService pacientesService;
    private final EvolucionService evolucionService;
    private final LabInicialesService labInicialesService;
    private final MedicacionService medicacionService;
    private final NotasService notasService;
    private final ProcedimientosService procedimientosService;

    public PacientesResource(PacientesService pacientesService, EvolucionService evolucionService, LabInicialesService labInicialesService, MedicacionService medicacionService, NotasService notasService, ProcedimientosService procedimientosService) {
        this.pacientesService = pacientesService;
        this.evolucionService = evolucionService;
        this.labInicialesService = labInicialesService;
        this.medicacionService = medicacionService;
        this.notasService = notasService;
        this.procedimientosService = procedimientosService;
    }

    @GetMapping("/all")
    public ResponseEntity<List<Pacientes>> getAllPacientes() {
        List<Pacientes> pacientes = pacientesService.findAllPacientes();
        return new ResponseEntity<>(pacientes, HttpStatus.OK);
    }

    @GetMapping("/evolucion/{id}")
    public ResponseEntity<List<evolucion>> getEvolucionById(@PathVariable("id") Integer id) {
        List<evolucion> evoluciones = evolucionService.findEvolucionById(id);
        return new ResponseEntity<>(evoluciones, HttpStatus.OK);
    }

    @GetMapping("/lab-iniciales/{id}")
    public ResponseEntity<List<lab_iniciales>> getLabinicialesById(@PathVariable("id") Integer id) {
        List<lab_iniciales> labIniciales = labInicialesService.findLabInicialesById(id);
        return new ResponseEntity<>(labIniciales, HttpStatus.OK);
    }

    @GetMapping("/medicacion/{id}")
    public ResponseEntity<List<medicacion>> getMedicacionById(@PathVariable("id") Integer id) {
        List<medicacion> medicacion = medicacionService.findMedicacionById(id);
        return new ResponseEntity<>(medicacion, HttpStatus.OK);
    }

    @GetMapping("/notas/{id}")
    public ResponseEntity<List<notas>> getNotasById(@PathVariable("id") Integer id) {
        List<notas> notas = notasService.findNotasById(id);
        return new ResponseEntity<>(notas, HttpStatus.OK);
    }

    @GetMapping("/procedimientos/{id}")
    public ResponseEntity<List<procedimientos>> getProcedimientosById(@PathVariable("id") Integer id) {
        List<procedimientos> procedimientos = procedimientosService.findProcedimientosById(id);
        return new ResponseEntity<>(procedimientos, HttpStatus.OK);
    }

    @GetMapping("/find/{id}")
    public ResponseEntity<Pacientes> getPacienteById(@PathVariable("id") Integer id) {
        Pacientes paciente = pacientesService.findPacienteById(id);
        return new ResponseEntity<>(paciente, HttpStatus.OK);
    }

    @GetMapping("/find-name/{nombre}")
    public ResponseEntity<List<Pacientes>> getPacienteByNombre(@PathVariable("nombre") String nombre) {
        List<Pacientes> pacientes = pacientesService.findPacienteByNombre(nombre);
        return new ResponseEntity<>(pacientes, HttpStatus.OK);
    }

    @PostMapping("/add")
    public ResponseEntity<Pacientes> addPacientes(@RequestBody Pacientes paciente) {
        Pacientes nuevoPaciente = pacientesService.addPaciente(paciente);
        return new ResponseEntity<>(nuevoPaciente, HttpStatus.CREATED);
    }

    @PutMapping("/update")
    public ResponseEntity<Pacientes> updatePacientes(@RequestBody Pacientes paciente) {
        Pacientes actualizarPaciente = pacientesService.updatePaciente(paciente);
        return new ResponseEntity<>(actualizarPaciente, HttpStatus.OK);
    }

    @DeleteMapping("/delete/{id}")
    public ResponseEntity<?> deletePacientes(@PathVariable("id") Integer id) {
        pacientesService.deletePaciente(id);
        return new ResponseEntity<>(HttpStatus.OK);
    }
}
