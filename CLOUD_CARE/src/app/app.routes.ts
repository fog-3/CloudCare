import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { ListPatientsComponent } from './pages/list-patients/list-patients.component';
import { PatientsComponent } from './pages/patients/patients.component';
import { ChatBoxComponent } from './pages/chat-box/chat-box.component';

export const routes: Routes = [
    { path: 'home', component: HomeComponent },
    { path: 'list-patients', component: ListPatientsComponent },
    { path: 'patients', component: PatientsComponent },
    { path: 'chat-box', component: ChatBoxComponent },
    { path: '**', redirectTo: 'home', pathMatch: 'full' }
];
