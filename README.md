# Compilador


<h1>Sañudito</h1>
Genaro Sañudo

<h2>Avance 4</h2>
Mayo 7 2023

Durante esta semana se desarrollo y entrego la propuesta original del proyecto. Despues de unos cambios indicados por la maestra se acepto la propuesta final. Ademas se genero la gramatica formal y en base a esta se programo el parser y el lexer utilizando PLY. Una vez que se acabo con estas clases se agrego el cubo semantico y el directorio de funciones para poder empezar a agregar los puntos neuralgicos necesarios para guardar la infromación importante.

<h2>Avance 5</h2>
Mayo 14 2023

Durante esta semana se acabo el directorio de funciones y la tabla de variables. Se agrego la clase de cuadruplos y se hicieron correcciones a la gramatica. Además se agregaron puntos neuralgicos para las siguientes funciones: READ, WRITE, ASIGNAR al igual que los puntos necesarios para la aritmetica básica del programa.

<h2>Avance 6</h2>
Mayo 21 2023

Durante esta semana se acabaron de agregar los puntos neuralgicos para los estatutos lineales. Ademas se agregaron los puntos neuralgicos necesarios para los loops (for, if, y while). Se hicieron muchos cambios necesarios en la gramatica y los diagramas para lograr que todo funcionara como debe. Los cambios mas grandes fueron el cambio de return a estatuto, lo cual permitio que se simplificara la gramatica de funciones. Otro cambio fue que se agrego la funcion regex que permite el uso de "letreros" esto se hizo para lograr que el write pudiera imprimir strings. Se agregaron las siguientes variables al directorio de funciones: num_vars : Es una lista que permite llevar conteo de la cantidad y tipo de variables en una funcion, num_temp_vars : Lo mismo pero de variables temporales, num_params : un contador de los parametros y finalmente quad_counter : que permite saber en que cuadruplo empiezan los estatutos de esa funcion.