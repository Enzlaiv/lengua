
do{
    var opcion=prompt("menu de recomendaciones \n 1. literatura \n 2.cine \n 3.salir")
        var opcion_escogidas={
            '1':"lecturas recomendables \n + esperandolo a tito y otros cuentos de futbol",
            '2' : "peliculas recomendadas \n skerk5",
            '3' : "hasta pronto, no vuelva"
        }
    var opcion_predeterminada="opcion no valida"
    var opcion_decidida=opcion_escogidas[opcion] || opcion_predeterminada
    alert(opcion_decidida)
}while (opcion !=3);