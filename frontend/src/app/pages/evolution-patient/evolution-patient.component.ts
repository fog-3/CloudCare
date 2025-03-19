import { CommonModule } from '@angular/common';
import { HttpClientModule, HttpErrorResponse } from '@angular/common/http';
import { Component } from '@angular/core';
import { PacientesService } from '../../services/pacientes.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Evolucion } from '../../types/evolucion';

@Component({
  selector: 'app-evolution-patient',
  imports: [CommonModule, HttpClientModule],
  providers: [PacientesService],
  templateUrl: './evolution-patient.component.html',
  styleUrl: './evolution-patient.component.scss'
})
export class EvolutionPatientComponent {
  public evolucion: any = {};

  constructor(
    private pacienteService: PacientesService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit() {
    this.route.queryParams.subscribe((params) => {
      const termino = params['q']; // Obtén el término de búsqueda
      const termino2 = params['p'];
      this.getEvolucionByIdFechaYHora(termino, termino2);
    });
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
}
