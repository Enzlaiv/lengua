var sum=0
var cont_sum=0

do{
a=new Number(prompt("ingrese el primer numero"))
b=new Number(prompt("ingrese el segundo numero"))
let resol =0
resol= a+b
document.write("la suma de " +a+ " + " +b+" es igual a " + resol)
sum=sum +resol
cont_sum=cont_sum+1
document.write(" <br> la suma total es" +sum)
document.write(" <br> este programa se ejecuto " + cont_sum +"veces")
break
}while(a!=0)