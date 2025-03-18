import { Component, OnInit } from '@angular/core';
import { HeaderChatComponent } from './header-chat/header-chat.component';
import { HttpClient } from '@angular/common/http';
import { response } from 'express';

interface Mensaje {
  text: String;
  esUsuario: boolean;
}

@Component({
  selector: 'app-chat-box',
  imports: [HeaderChatComponent],
  templateUrl: './chat-box.component.html',
  styleUrl: './chat-box.component.scss'
})

export class ChatBoxComponent {
  /*mensajes: Mensaje[] = []; //Almacena los mensajes del chat
  nuevoMensaje: string = ''; //Almacena el mensaje actual del usuario
  private apiUrl = 'https://url-de-tu-api.com'; // URL de la API que interactúa con la IA

  constructor(private http: HttpClient) { }

  // Opcional si queremos que el bot envíe un mensaje opcional
  ngOnInit(): void {
      
  }

  enviarMensaje(): void {
    if (this.nuevoMensaje.trim() == '') {
      return;   // No enviar mensajes vacíos
    }

    // Agregar mensaje del usuario al chat
    this.mensajes.push({ text: this.nuevoMensaje, esUsuario: true });

    // Enviar mensaje a la API
    this.http.post<any>(`${this.apiUrl}/chat`, {mensaje: this.nuevoMensaje})
      .subscribe(
        (response) => {
          // Agregar la respuesta de la IA al chat
          this.mensajes.push({ text: response.respuesta, esUsuario: false });
        },
        (error) => {
          console.error('Error al enviar el mensaje', error);
          this.mensajes.push({ text: 'Hubo un error al procesar tu mensaje.', esUsuario: false });
        }
      );

    // Limpia el campo de entrada
    this.nuevoMensaje = '';
  }*/
}