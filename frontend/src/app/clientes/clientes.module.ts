import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { NewRegisterComponent } from './new-register/new-register.component';
import { ListarComponent } from './listar/listar.component';


@NgModule({
  declarations: [
    NewRegisterComponent,
    ListarComponent
  ],
  imports: [
    CommonModule,
    FormsModule
  ],
  exports: [
    NewRegisterComponent
  ]
})
export class ClientesModule { }
