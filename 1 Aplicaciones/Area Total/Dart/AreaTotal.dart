// se importa una librería para leer datos por consola
import "dart:io";

// Se implementa un método para el calculo del area total
double calcularArea(int lotes, double longMin, double increment) {
  // se inicializan las variables
  int iteration = 0;
  double controlIncremento = 0;
  double areaTotal = 0;
  // corremos un ciclo que va mientras el numero de iteraciones de cada
  //calculo de los lotes sea menor al numero de lotes que se ingresaron
  while (iteration < lotes) {
    // se va acumulando en la variable area total el calculo:
    // longitud mínima del lote + el valor incrementado(longitud) por iteración
    // multiplicado
    // longitud mínima + el valor incrementado(longitud) por iteración
    areaTotal += (longMin + controlIncremento) * (longMin + controlIncremento);
    // se hacen los incrementos
    controlIncremento += increment;
    iteration++;
  }
  return areaTotal;
}

// Se crea un metodo para leer la consola
String inputConsole(String inputMessage) {
  String? line; // se inicializa como null
  do {
    print(inputMessage); // se muestra un mensaje
    line = stdin.readLineSync(); // se lee la consola
  } while (line == null ||
      line.length ==
          0); // se itera si el valor es null o no tiene un largo mayor a 0
  return line; // retornamos lo que se ingresa
}

void main() {
  // se piden valores
  int lotes = int.parse(inputConsole("Ingrese el numero de lotes"));
  double longMin = double.parse(inputConsole("Ingrese el valor Mínimo"));
  double increment = double.parse(inputConsole("Ingrese el incremento"));
  // se hace el calculoArea
  double res = calcularArea(lotes, longMin, increment);
  // se muestra en pantalla
  print("El area total es de $res metros cuadrados.");
}
