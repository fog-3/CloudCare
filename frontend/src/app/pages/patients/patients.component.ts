import { Component } from '@angular/core';
import { HeaderPatientsComponent } from './header-patients/header-patients.component';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-patients',
  imports: [HeaderPatientsComponent, RouterLink],
  templateUrl: './patients.component.html',
  styleUrl: './patients.component.scss'
})

export class PatientsComponent {

}
