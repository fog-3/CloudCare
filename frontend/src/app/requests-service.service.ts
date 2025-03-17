import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class RequestsServiceService {

  private apiURL = 'https://url-de-tu-api.com';
  
  constructor(private http: HttpClient) { }

  // Método para obtener datos
  obtenerDatos(): Observable<any> {
    return this.http.get(`${this.apiURL}/endpoint`);
  }

  // Método para enviar datos
  enviarDatos(datos: any): Observable<any> {
    return this.http.post(`${this.apiURL}/endpoint`, datos);
  }

  // Método para actualizar datos
  /*actualizarDatos(id: number, datos: any): Observable<any> {
    return this.http.put(`${this.apiURL}/endpoint/${id}`, datos);
  }

  // Método para eliminar datos
  eliminarDatos(id: number): Observable<any> {
    return this.http.delete(`${this.apiURL}/endpoint`);
  }*/
}
