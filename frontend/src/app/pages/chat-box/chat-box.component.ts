import { Component, OnInit } from '@angular/core';
import { HeaderChatComponent } from './header-chat/header-chat.component';
import { HttpClient, HttpClientModule, HttpErrorResponse } from '@angular/common/http';
import { response, Router } from 'express';
import { PacientesService } from '../../services/pacientes.service';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { Paciente } from '../../types/pacientes';
import ApiResponse from '../../types/message_r';
import { MessageE } from '../../types/message_e';

import { error } from 'console';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-chat-box',
  imports: [HeaderChatComponent, CommonModule, HttpClientModule],
  providers: [PacientesService],
  templateUrl: './chat-box.component.html',
  styleUrl: './chat-box.component.scss'
})

export class ChatBoxComponent implements OnInit {
  mensaje_r: ApiResponse[] = [];
  mensaje_e: MessageE[] = [];
  paciente: any = {};
  esResumen: boolean = false;
  esGrafico: boolean = false;
  terminoBusqueda: string = '';

  constructor(
      private pacienteService: PacientesService,
      private route: ActivatedRoute,
  ) {}

  // Opcional si queremos que el bot envíe un mensaje opcional
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

  public putMessage(pacienteId: number, quest: string) {
    
    this.terminoBusqueda = quest;

    const message_e: MessageE = {
      session_id: String(pacienteId),
      question: quest,
      paciente: this.paciente,
      esGrafico: this.esGrafico,
      esResumenEvolutivo: this.esResumen
    }
    this.mensaje_e.push(message_e);
    this.pacienteService.putMessage(message_e).subscribe(
      (response: ApiResponse) => {
        this.mensaje_r.push(response);
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    )
  }
}