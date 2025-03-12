import { Component } from '@angular/core';
import { HeaderListComponent } from './header-list/header-list.component';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-list-patients',
  imports: [HeaderListComponent, RouterLink],
  templateUrl: './list-patients.component.html',
  styleUrl: './list-patients.component.scss'
})

export class ListPatientsComponent {

}
