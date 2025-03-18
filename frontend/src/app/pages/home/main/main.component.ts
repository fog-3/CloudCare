import { Component } from '@angular/core';
import { SearchComponent } from '../../search/search.component';

@Component({
  selector: 'app-main',
  imports: [SearchComponent],
  templateUrl: './main.component.html',
  styleUrl: './main.component.scss'
})
export class MainComponent {

}
