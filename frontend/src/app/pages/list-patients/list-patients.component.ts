import { Component } from '@angular/core';
import { HeaderListComponent } from './header-list/header-list.component';

@Component({
  selector: 'app-list-patients',
  imports: [HeaderListComponent],
  templateUrl: './list-patients.component.html',
  styleUrl: './list-patients.component.scss'
})
export class ListPatientsComponent {

}
