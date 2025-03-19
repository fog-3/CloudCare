import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Paciente } from './types/pacientes';
import { PacientesService } from './services/pacientes.service';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true, 
  imports: [CommonModule, RouterOutlet],
  providers: [PacientesService],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  public pacientes: Paciente[] = [];

  constructor(private pacienteService: PacientesService){}

  ngOnInit() {
    this.getPacientes();
  }

  public getPacientes(): void {
    this.pacienteService.getPacientes().subscribe(
      (response: Paciente[]) => {
        this.pacientes = response;
      },

      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    )
  }
}
