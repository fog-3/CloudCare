import { Component } from '@angular/core';
import { SearchComponent } from '../../search/search.component';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-header-list',
  imports: [SearchComponent, RouterLink],
  templateUrl: './header-list.component.html',
  styleUrl: './header-list.component.scss'
})
export class HeaderListComponent {

}
