import { Component } from '@angular/core';
import { HeaderPatientsComponent } from './header-patients/header-patients.component';

@Component({
  selector: 'app-patients',
  imports: [HeaderPatientsComponent],
  templateUrl: './patients.component.html',
  styleUrl: './patients.component.scss'
})

export class PatientsComponent {

}
