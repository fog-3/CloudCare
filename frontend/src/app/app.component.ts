import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Paciente } from './types/pacientes';
import { PacientesService } from './services/pacientes.service';
import { HttpClient, HttpClientModule, HttpErrorResponse } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';

@Component({
  selector: 'app-root',
  standalone: true, 
  imports: [CommonModule, RouterOutlet],
  providers: [PacientesService],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})  
export class AppComponent {
  public onOpenModal(){

  }
}
