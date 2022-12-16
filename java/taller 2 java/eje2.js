
var n=prompt("ingrese la cantidad de datos")
var sum=0;

for (var i=0; i<n; i++){
    sum += parseInt(prompt("ingresa tus numeros"));
}
document.write("promedio de los numeros es: " + sum/n);