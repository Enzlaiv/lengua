function saludar(){
    return document.write("hola mundo")
}
function calcular_doble(n){
    doble=n*2
    return doble;
}
function triplicar(n){
    triple=n*3
    return triple;
}

document.write("llamando a la funcion saludar <br>");
saludar();

var n=prompt("ingrese valor para n ");
document.write("<br>","llamamos ala funcion calcular doble")
document.write("<br>","el doble de "+ n+ " es " +parseInt(calcular_doble(n)))
document.write("<br>","el valor original de n es: " +n)

document.write("<br>","llamando a la funcion triplicar =>")
document.write(triplicar(n))
document.write("<br>","el nuevo valor de n es " + parseInt(triplicar(n)))