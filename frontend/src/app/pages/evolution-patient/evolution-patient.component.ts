import { CommonModule, isPlatformBrowser } from '@angular/common';
import { HttpClientModule, HttpErrorResponse } from '@angular/common/http';
import { Component, Inject, PLATFORM_ID } from '@angular/core';
import { PacientesService } from '../../services/pacientes.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Evolucion } from '../../types/evolucion';
import { HeaderPatientsComponent } from '../header-patients/header-patients.component';
import { Paciente } from '../../types/pacientes';
import { BrowserModule } from '@angular/platform-browser';
import { NgChartsConfiguration} from 'ng2-charts';


@Component({
  selector: 'app-evolution-patient',
  imports: [BrowserModule, HeaderPatientsComponent, CommonModule, HttpClientModule],
  providers: [PacientesService],
  templateUrl: './evolution-patient.component.html',
  styleUrl: './evolution-patient.component.scss'
})
export class EvolutionPatientComponent {
  public evolucion: any = {};
  public evoluciones: Evolucion[] = [];
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
  rangosNormales = {
    PresionSistolica: { min: 90, max: 140, medida: 'mmHg' },
    PresionDiastolica: { min: 60, max: 90, medida: 'mmHg' },
    FrecuenciaCardiaca: { min: 60, max: 100, medida: 'lpm' },
    Temperatura: { min: 36.5, max: 39.2, medida: '°C' },
    SaturacionOxigeno: { min: 89, max: 98, medida: '%' },
    Glucosa: { min: 70, max: 180, medida: 'mg/dL' },
    Leucocitos: { min: 4000, max: 11000, medida: 'células/μL' },
    Hemoglobina: { min: 12, max: 16, medida: 'g/dL' },
    Plaquetas: { min: 150000, max: 450000, medida: 'plaquetas/μL' },
    Colesterol: { min: 0, max: 200, medida: 'mg/dL' },
    HDL: { min: 40, max: 60, medida: 'mg/dL' },
    LDL: { min: 0, max: 130, medida: 'mg/dL' },
    Trigliceridos: { min: 0, max: 150, medida: 'mg/dL' },
    Sodio: { min: 135, max: 145, medida: 'mmol/L' },
    Potasio: { min: 3.5, max: 5.1, medida: 'mmol/L' },
    Cloro: { min: 98, max: 107, medida: 'mmol/L' },
    Creatinina: { min: 0.6, max: 1.2, medida: 'mg/dL' },
    Urea: { min: 7, max: 20, medida: 'mg/dL' },
    AST: { min: 10, max: 40, medida: 'U/L' },
    ALT: { min: 7, max: 56, medida: 'U/L' },
    Bilirrubina: { min: 0.1, max: 1.2, medida: 'mg/dL' },
    pH: { min: 7.35, max: 7.45, medida: 'pH' },
    pCO2: { min: 35, max: 45, medida: 'mmHg' },
    pO2: { min: 75, max: 100, medida: 'mmHg' },
    HCO3: { min: 22, max: 28, medida: 'mmol/L' },
    Lactato: { min: 0.5, max: 2.2, medida: 'mmol/L' }
  };

  public graficos: { [key: string]: any } = {};

  constructor(
    private pacienteService: PacientesService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit() {
    this.route.queryParams.subscribe((params) => {
      const termino = params['q']; // Obtén el término de búsqueda
      const termino2 = params['p'];
      const termino3 = params['r'];
      this.paciente.pacienteid = termino;
      this.paciente.nombre = termino3;
      this.getEvolucionByIdFechaYHora(termino, termino2);
      this.getEvolucionesById(termino);
      this.cargarDatos();
    });
  }

  cargarDatos(): void {
    this.graficarFunciones(this.evolucion, this.rangosNormales);
  }

  graficarFunciones(fila: any, rangos: any): void {
    Object.keys(rangos).forEach(columna => {
      if (fila[columna] !== undefined) {
        const { min, max, medida } = rangos[columna];
        this.graficarFuncion(min, max, fila[columna], medida, columna);
      }
    });
  }

  graficarFuncion(min: number, max: number, valor: number, medida: string, titulo: string): void {
    const interval = max - min;
    let backgroundColor = 'rgba(216, 243, 220, 0.5)';
    let borderColor = 'rgba(216, 243, 220, 1)';

    if (valor < min || valor > max) {
      backgroundColor = 'rgba(255, 99, 132, 0.5)';
      borderColor = 'rgba(255, 99, 132, 1)';
    }

    this.graficos[titulo] = {
      type: 'bar',
      data: {
        labels: [titulo],
        datasets: [
          {
            label: 'Valor actual',
            data: [valor],
            backgroundColor: backgroundColor,
            borderColor: borderColor,
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: false,
            min: min - interval * 0.5,
            max: max + interval,
            title: {
              display: true,
              text: medida,
            },
          },
        },
        plugins: {
          title: {
            display: true,
            text: titulo,
          },
        },
      },
    };
  }


  public getEvolucionByIdFechaYHora(pacienteid: number, fechaYHora: string): void {
    this.pacienteService.getEvolucionByIdFecha(pacienteid, fechaYHora).subscribe(
      (response: Evolucion) => {
        this.evolucion = response;
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

  public goEvolucionPaciente(pacienteid: number, fecha: string, nombre: string) {
    // Navega a la página de resultados con el término de búsqueda
    this.router.navigate(['/evolution-patient'], { queryParams: { q: pacienteid, p: fecha, r: nombre } });
  }

  public normalizarStringFecha(fechaOriginal: string): string {
    return fechaOriginal
    .replace('T', '\n') // Reemplazar "T" por un espacio
    .replace(/\.\d{3}\+\d{2}:\d{2}$/, ''); // Eliminar milisegundos y zona horaria
  }

  objectKeys(obj: any): string[] {
    return Object.keys(obj);
  }  
}
