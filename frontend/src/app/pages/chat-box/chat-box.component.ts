import { Component } from '@angular/core';
import { HeaderChatComponent } from './header-chat/header-chat.component';

@Component({
  selector: 'app-chat-box',
  imports: [HeaderChatComponent],
  templateUrl: './chat-box.component.html',
  styleUrl: './chat-box.component.scss'
})
export class ChatBoxComponent {

}
