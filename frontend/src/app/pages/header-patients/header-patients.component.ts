import { Component } from '@angular/core';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { PacientesService } from '../../services/pacientes.service';
import { CommonModule } from '@angular/common';
import { HttpClientModule, HttpErrorResponse } from '@angular/common/http';
import { Paciente } from '../../types/pacientes';

@Component({
  selector: 'app-header-patients',
  imports: [CommonModule, HttpClientModule],
  providers: [PacientesService],
  templateUrl: './header-patients.component.html',
  styleUrl: './header-patients.component.scss'
})
export class HeaderPatientsComponent {
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

    ngOnInit(): void {
      this.route.queryParams.subscribe((params) => {
        const termino = params['q']; // Obtén el término de búsqueda
        this.getPacientesById(termino);
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

  public goChatBoxPaciente(pacienteid: number) {
    // Navega a la página de resultados con el término de búsqueda
    this.router.navigate(['/chat-box'], { queryParams: { q: pacienteid } });
  }
}
