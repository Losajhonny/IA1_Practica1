import { Component } from '@angular/core';
import { Conexion } from "./Conexion";

class Nota {
   proyecto1: Number;
   proyecto2: Number;
   proyecto3: Number;
   proyecto4: Number;
   final: Number;
}

@Component({
   selector: 'app-root',
   templateUrl: './app.component.html',
   styleUrls: ['./app.component.css']
})
export class AppComponent {
   title = 'AppWeb';
   notas = [];

   finModos = [false, false, true]
   selModos = [false, false, true]

   nota = { proyecto1: 0, proyecto2: 0, proyecto3: 0, proyecto4: 0 }
   nombre = ""

   upload(event: any) {
      const files = event.target.files;
      if (files.length == 0) return;

      const reader = new FileReader();
      const file = files[0];
      this.nombre = file.name
      this.notas = []

      reader.onload = (e) => {
         const file = e.target.result;
         const lines = file.toString().split('\n');

         for (let i = 1; i < lines.length; i++) {
            const line = lines[i];

            const individuo = line.split(',');

            if(individuo.length == 5) {
               const nota = new Nota()
               nota.proyecto1 = parseFloat(individuo[0]);
               nota.proyecto2 = parseFloat(individuo[1]);
               nota.proyecto3 = parseFloat(individuo[2]);
               nota.proyecto4 = parseFloat(individuo[3]);
               nota.final = parseFloat(individuo[4]);
               this.notas.push(nota);
            }
         }
      };

      reader.readAsText(file);
   }

   cargar() {
      Conexion.getInstance().POST('load', { notas: this.notas, nombre: this.nombre });
   }

   getFinModos(noModo, event) {
      for(let i = 0; i < this.finModos.length; i++) {
         this.finModos[i] = false;
      }
      this.finModos[noModo] = event.target.checked;
   }

   getSelModos(noModo, event) {
      for(let i = 0; i < this.selModos.length; i++) {
         this.selModos[i] = false;
      }
      this.selModos[noModo] = event.target.checked;
   }

   async generar() {
      /*if (this.notas.length == 0) {
         alert("Cargar csv");
         return;
      }*/

      let finModo = -1
      for(let i = 0; i < this.finModos.length; i++) {
         if(this.finModos[i]) {
            finModo = i;
            break;
         }
      }

      let selModo = -1
      for(let i = 0; i < this.selModos.length; i++) {
         if(this.selModos[i]) {
            selModo = i;
            break;
         }
      }

      let res = await Conexion.getInstance().POST('generar', { fin: finModo, sel: selModo });

      if (res != null) {
         if (res.status == 200)
            alert('Modelo Generado...');
         else
            alert("Cargar csv");
      }
   }

   async calcular() {
      let res = await Conexion.getInstance().POST('calcular', this.nota);

      if (res != null) {
         if (res.status == 500)
            alert('Debe generar el modelo');
         else
            alert(res.nota);
      }
   }
}
