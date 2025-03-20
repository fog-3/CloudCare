import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Paciente } from '../types/pacientes';
import { Evolucion } from '../types/evolucion';
import { LabIniciales } from '../types/lab_iniciales';
import { Medicacion } from '../types/medicacion';
import { Notas } from '../types/notas';
import { Procedimientos } from '../types/procedimientos';
import { environment } from '../../environment/environment';
import { MessageE } from '../types/message_e';
import ApiResponse from '../types/message_r';
import { ChatHistory } from '../types/chat_history';

@Injectable({
  providedIn: 'root'
})
export class PacientesService {
  private apiServerUrl = environment.apiBaseUrl;
  private apiIAServerUrl = 'https://jh3hdiv0ff.execute-api.eu-central-1.amazonaws.com/qa';

  constructor(private http: HttpClient) { }

  public getPacientes(): Observable<Paciente[]>{
    return this.http.get<Paciente[]>(`${this.apiServerUrl}/pacientes/all`);
  }

  public addPaciente(paciente: Paciente): Observable<Paciente>{
    return this.http.post<Paciente>(`${this.apiServerUrl}/pacientes/add`, paciente);
  }

  public putPaciente(paciente: Paciente): Observable<Paciente>{
    return this.http.put<Paciente>(`${this.apiServerUrl}/pacientes/update`, paciente);
  }

  public deletePaciente(pacienteId: number): Observable<void>{
    return this.http.delete<void>(`${this.apiServerUrl}/pacientes/delete/${pacienteId}`);
  }

  public getPacienteById(pacienteId: number): Observable<Paciente> {
    return this.http.get<Paciente>(`${this.apiServerUrl}/pacientes/find/${pacienteId}`);
  }

  public getPacienteByName(nombre: string): Observable<Paciente[]> {
    return this.http.get<Paciente[]>(`${this.apiServerUrl}/pacientes/find-name/${nombre}`);
  }

  public getEvolucionById(pacienteId: number): Observable<Evolucion[]>{
    return this.http.get<Evolucion[]>(`${this.apiServerUrl}/pacientes/evolucion/${pacienteId}`);
  }

  public getEvolucionByIdFecha(pacienteId: number, time: string): Observable<Evolucion>{
    return this.http.get<Evolucion>(`${this.apiServerUrl}/pacientes/evolucion/${pacienteId}/${time}`);
  }

  public getLabIniciales(pacienteId: number): Observable<LabIniciales[]>{
    return this.http.get<LabIniciales[]>(`${this.apiServerUrl}/pacientes/lab-iniciales/${pacienteId}`);
  }

  public getMedicacion(pacienteId: number): Observable<Medicacion[]> {
    return this.http.get<Medicacion[]>(`${this.apiServerUrl}/pacientes/medicacion/${pacienteId}`);
  }

  public getNotas(pacienteId: number): Observable<Notas[]> {
    return this.http.get<Notas[]>(`${this.apiServerUrl}/pacientes/notas/${pacienteId}`);
  }

  public getProcedimientos(pacienteId: number): Observable<Procedimientos[]> {
    return this.http.get<Procedimientos[]>(`${this.apiServerUrl}/pacientes/procedimientos/${pacienteId}`);
  }

  public putMessage(mensaje: MessageE): Observable<ApiResponse>{
    return this.http.put<ApiResponse>(`${this.apiIAServerUrl}`, mensaje);
  }

  public getChatHistory(sessionId: string): Observable<ChatHistory[]> {
      return this.http.get<ChatHistory[]>(`${this.apiServerUrl}/pacientes/chat`);
  }
}
