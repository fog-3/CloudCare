import { Component } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { Paciente } from '../../types/pacientes';
import { PacientesService } from '../../services/pacientes.service';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-search',
  imports: [],
  templateUrl: './search.component.html',
  styleUrl: './search.component.scss'
})
export class SearchComponent {
  terminoBusqueda: string = '';

  constructor(private router: Router) {}

  getPacienteByName(term: string) {
    this.terminoBusqueda = term;
    if (this.terminoBusqueda.trim()) {
      // Navega a la página de resultados con el término de búsqueda
      this.router.navigate(['/list-patients'], { queryParams: { q: this.terminoBusqueda } });
    }
  }
}
