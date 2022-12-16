let lista =[];
for (let i=0;i<10; i++){
    let dato=Math.random()
    dato=dato * 100 +1
    dato=  Math.trunc(dato)
    lista[i]=dato;

}
document.write("los elemnetos de la listas son: <br>" + lista)
var lista_reversa=lista.reverse()
document.write("<br> el roden inverso seria <br>"+ lista_reversa)