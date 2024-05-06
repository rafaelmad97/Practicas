// se importan las librerías para leer la consola
import "dart:io";

String generarBandera(sizey, sizex) {
  // Se inicializan las variables de control para el ciclo
  int x = 0, y = 0;
  // Se incializa una variable bandera la cual almacenará el lienzo de la bandera
  String bandera = "";
  // se prosigue a obtener los puntos medios para dibujar los caracteres que arman las cruz
  //(para redondear divisiones se usa el operador [ ~/ ] )
  int midx = sizex ~/ 2;
  int midy = sizey ~/ 2;
  //mientras que las variables de control sean menores a el largo y ancho sigue iterando
  while (x < sizex && y < sizey) {
    //si la variables de control x ó y sean iguales a los puntos medios dibuja la el carácter que conforma la cruz
    if (x == midx || y == midy) {
      bandera += " + ";
    } else {
      // si no dibuja el cuerpo de la bandera
      bandera += " 0 ";
    }
    //realiza un incremento hacia lo largo en una de las variables de control
    x++;
    if (x == sizex) {
      //si llegas a el tope maximo del largo
      bandera += "\n";
      //agrega salto de linea
      x = 0;
      //regresa el inicio de la bandera
      y++;
      //bajas una casilla de la bandera realizando un incremento en la otra variable de control
    }
  }
  //devuelveme el valor de la bandera
  return bandera;
}

String readLine(String inputMessage) {
  String? line; // iniciamos la variable line como nula pero que admita Strings
  do {
    // dibujamos el mensaje
    print(inputMessage);
    // leemos la linea ingresada en la terminal
    line = stdin.readLineSync();
    // estamos en un ciclo donde se repite cuando line es nula o su largo es 0
  } while (line == null || line.length == 0);
  return line;
}

void main() {
  int size_x = 0,
      size_y = 0; // se supone que los valores del largo y el ancho son cero
  bool x = false,
      y = false; // se supone que los valores del largo y el ancho son incorrectos
  while (size_x % 2 == 0 || size_y % 2 == 0) {
    // itera mientras que los valores del largo y el ancho sean impares
    if (x == false) {
      //parece que el valor de ancho lo debes reescribir
      //print("Ingrese el x tamaño de la bandera");
      size_x = int.parse(readLine("Ingrese el x tamaño de la bandera"));
    }
    if (y == false) {
      //parece que el valor de largo lo debes reescribir
      //print("Ingrese el y tamaño de la bandera")
      size_y = int.parse(readLine("Ingrese el y tamaño de la bandera"));
    }
    y = size_y % 2 != 0 &&
        size_y < 200 &&
        size_y > 0; //validamos que el valor del "largo" esté "correcto"

    x = size_x % 2 != 0 &&
        size_x < 200 &&
        size_x > 0; //validamos que el valor del "ancho" esté "correcto"

    if (x && y) {
      //los valores del largo están buenos
      break; // te libro de la cadena de odio de iterar
    } else {
      // vuelve a intentarlo me dijo coca cola en sus latas
      print(
          "el valor debe ser impar, no debe exceder a 200 y debe ser mayor a cero");
    }
  }
  print(
      "\n"); // hago un salto de linea para indicar que todo lo de arriba ya dejo de ejecutarse
  print(
      "x={$size_x} y={$size_y}\n"); //muestro los valores que pasaron el filtro

  print(generarBandera(size_y, size_x)); //dibujame la bandera
}
