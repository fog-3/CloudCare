import { Component } from '@angular/core';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { PacientesService } from '../../../services/pacientes.service';
import { Paciente } from '../../../types/pacientes';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-header-chat',
  imports: [RouterLink],
  templateUrl: './header-chat.component.html',
  styleUrl: './header-chat.component.scss'
})
export class HeaderChatComponent {
  paciente: any = {};

  constructor(
        private pacienteService: PacientesService,
        private route: ActivatedRoute
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
}
