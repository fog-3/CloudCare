import { Component } from '@angular/core';
import { HeaderListComponent } from './header-list/header-list.component';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { PacientesService } from '../../services/pacientes.service';
import { HttpClientModule, HttpErrorResponse } from '@angular/common/http';
import { Paciente } from '../../types/pacientes';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-list-patients',
  imports: [HeaderListComponent, CommonModule, HttpClientModule],
  providers: [PacientesService],
  templateUrl: './list-patients.component.html',
  styleUrl: './list-patients.component.scss'
})
export class ListPatientsComponent {
  public pacientes: Paciente[] = [];

  constructor(
    private pacienteService: PacientesService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit() {
    this.route.queryParams.subscribe((params) => {
      const termino = params['q']; // Obtén el término de búsqueda
      if (termino) {
        this.getPacientesByName(termino);
      } else {
        this.getPacientes();
      }
    });
  }

  public getPacientes(): void {
    this.pacienteService.getPacientes().subscribe(
      (response: Paciente[]) => {
        this.pacientes = response;
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    );
  }

  public getPacientesByName(termino: string): void {
    this.pacienteService.getPacienteByName(termino).subscribe(
      (response: Paciente[]) => {
        this.pacientes = response;
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    );
  }

  getPacienteByName(pacienteid: number) {
    // Navega a la página de resultados con el término de búsqueda
    this.router.navigate(['/patients'], { queryParams: { q: pacienteid } });
  }
}
