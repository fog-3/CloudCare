import { Component } from '@angular/core';
import { HeaderPatientsComponent } from '../header-patients/header-patients.component';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { PacientesService } from '../../services/pacientes.service';
import { Paciente } from '../../types/pacientes';
import { HttpClientModule, HttpErrorResponse } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { Evolucion } from '../../types/evolucion';
import { Notas } from '../../types/notas';
import { Medicacion } from '../../types/medicacion';
import { Procedimientos } from '../../types/procedimientos';
import { LabIniciales } from '../../types/lab_iniciales';

@Component({
  selector: 'app-patients',
  imports: [HeaderPatientsComponent, CommonModule, HttpClientModule],
  providers: [PacientesService],
  templateUrl: './patients.component.html',
  styleUrl: './patients.component.scss'
})

export class PatientsComponent {
  public evoluciones: Evolucion[] = [];
  public laboratorios: LabIniciales[] = [];
  public medicaciones: Medicacion[] = [];
  public notas: Notas[] = [];
  public procedimientos: Procedimientos[] = [];
  public paciente: Paciente = {
    nombre: "",
    edad: 0,
    sexo: "M",
    alergias: null,
    motivoingreso: "",
    diagnosticoprincipal: "",
    condicionesprevias: "",
    fechaingreso: "",
    servicio: "",
    estadoalingreso: "",
    pacienteid: 0
  };

  constructor(
      private pacienteService: PacientesService,
      private route: ActivatedRoute,
      private router: Router
  ) {}

  ngOnInit() {
    this.route.queryParams.subscribe((params) => {
      const termino = params['q']; // Obtén el término de búsqueda
      this.getPacientesById(termino);
      this.getEvolucionesById(termino);
      this.getLaboratoriosById(termino);
      this.getNotasById(termino);
      this.getMedicacionById(termino);
      this.getProcedimientosById(termino);
    });
  }

  public getPacientesById(pacienteid: number): void {
    this.pacienteService.getPacienteById(pacienteid).subscribe(
      (response: Paciente) => {
        this.paciente = response;
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    );
  }

  public getEvolucionesById(pacienteid: number): void {
    this.pacienteService.getEvolucionById(pacienteid).subscribe(
      (response: Evolucion[]) => {
        this.evoluciones = response;
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    );
  }

  public getLaboratoriosById(pacienteid: number): void {
    this.pacienteService.getLabIniciales(pacienteid).subscribe(
      (response: LabIniciales[]) => {
        this.laboratorios = response;
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    );
  }

  public getNotasById(pacienteid: number): void {
    this.pacienteService.getNotas(pacienteid).subscribe(
      (response: Notas[]) => {
        this.notas = response;
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    );
  }
  
  public getMedicacionById(pacienteid: number): void {
    this.pacienteService.getMedicacion(pacienteid).subscribe(
      (response: Medicacion[]) => {
        this.medicaciones = response;
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    );
  }

  public getProcedimientosById(pacienteid: number): void {
    this.pacienteService.getProcedimientos(pacienteid).subscribe(
      (response: Procedimientos[]) => {
        this.procedimientos = response;
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    );
  }

  public goEvolucionPaciente(pacienteid: number, fecha: string, nombre: string) {
    // Navega a la página de resultados con el término de búsqueda
    this.router.navigate(['/evolution-patient'], { queryParams: { q: pacienteid, p: fecha, r: nombre } });
  }

  public normalizarString(c: string): string {
    return c.replace(/;/g, ', ');
  }

  public normalizarStringAsterisco(c: string): string {
    return c.replace(/\*/g, '');
  }

  public normalizarStringFecha(fechaOriginal: string): string {
    return fechaOriginal
    .replace('T', ' ') // Reemplazar "T" por un espacio
    .replace(/\.\d{3}\+\d{2}:\d{2}$/, ''); // Eliminar milisegundos y zona horaria
  }
}