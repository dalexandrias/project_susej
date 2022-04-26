import { Component } from '@angular/core';

@Component({
  selector: 'app-new-register',
  templateUrl: './new-register.component.html',
  styleUrls: ['./new-register.component.scss']
})
export class NewRegisterComponent {

  constructor() { }

  eventButtonRegister(
    register: {
      nome: string,
      sobrenome: string,
      rua: string,
      bairro: string,
      cidade: string,
      estado: string,
      cep: string
    }
  ){
    console.log(register)
  }

}
