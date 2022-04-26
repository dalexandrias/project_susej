import { NewRegisterComponent } from './clientes/new-register/new-register.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login-page/login/login.component';
import { ListarComponent } from './clientes/listar/listar.component';

const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'cadastro', component: NewRegisterComponent },
  { path: 'login', component: LoginComponent  },
  { path: 'clientes', component: ListarComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
