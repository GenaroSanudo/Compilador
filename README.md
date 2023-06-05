# Compilador


<h1>Lenguaje Sañudito</h1>
<h2>Genaro Sañudo</h2>

<h3>Como correr el compilador?</h3>
Para correr el compilador primero deben de estar instaladas las siguientes librearias: pandas, matplotlib, pickle, sklearn y ply.

Una vez que se tengan instaladas esas librerias se tiene que arbrir el archivo "virtual_machine.py". Dentro de ese archivo se tiene que buscar la variable llamada: "FILE_NAME". Esa variable es el string donde se especifiac el archivo de texto que se quiere correr. Una vez especificado el archivo simplemente se tine que correr el comando `python vritual_machine.py`.

<h3>Generación de archivo de texto con el lenguaje Sañudito</h3>

Para empezar se tiene que generar un archivo de texto nuevo.

<h5>Program</h3>
En este archivo se tiene que empezar con:

```
program NOMBRE_DE_PROGRAMA :
```

Donde "NOMBRE_DE_PROGRAMA" puede ser cualquier ID valida

<h5>Declaracion de ID</h5>
Una ID puede ser cualquier combinacion de numeros y letras. La unica condicion es que tiene que comenzar con una letra o con un "_".

<h5>Tipos</h5>
El lenguaje Sañudito maneja tipos_simples y tipos_compuestos. Los tipos simples son INT y FLOAT. Mientras que los compuestos son los DATAFRAMES.

<h5>Funciones</h5>
En el lenguaje Sañudito se pueden declarar cualquier tipo de funciones mientras que sigan el siguiente formato:

```
func tipo_simple ID (tipo_simple ID){
            Var
            Estatutos
            };
```

o el siguiente:

```
func VOID ID (tipo_simple ID){ 
        Var
        Estatutos
        };
```

La unica condicion es que las funciones de tipo_simple tienen que tener por lo menos 1 estatuto RETURN mientras que las VOID no pueden tener ni uno. Además, ambos tipos de funciones deben de tener por lo menos 1 estatuto adentro. Por otro lado no hay limite de parametros, pueden tener de 0 hasta los que gusten. Las funciones tambien pueden declarar el número de variables que quieran.

<h5>Variables</h5>
En este lenguaje se manejan variables INT, FLOAT, DATAFRAME o arreglos y matrices de tipo INT o FLOAT. Para declarar una variable se siguen los siguientes pasos para variables normales:

```
var tipo ID
```

O para arreglos/matrices se puede seguir el siguiente formato:

```
var tipo_simple ID[CTE_I]
var tipo_simple ID[CTE_I][CTE_I]
```
Donde CTE_I es un INT > 0

<h5>Estatutos</h5>
En este lenguaje se manejan los siguientes estatutos:

<ul>
  <li>asigna</li>
  <li>llamada</li>
  <li>llamada_void</li>
  <li>read</li>
  <li>write</li>
  <li>if</li>
  <li>for_l</li>
  <li>while_l</li>
  <li>return</li>
  <li>funciones_especiales</li>
</ul>

A continuación se podrán ver snippets de cada uno de los estatutos, para una explicación más detallada se puede ver la documentación del proyecto

<h5>Asigna</h5>

```
variable = Exp;
```
<h5>Llamada</h5>

```
id (Exp)
id (Exp, Exp, Exp, etc)
```
<h5>Llamada_void</h5>

```
id (Exp);
id (Exp, Exp, Exp, etc);
```
<h5>Read</h5>

```
read (variable);
```
<h5>Write</h5>

```
write(Exp);
write(CTE_S);
write(Exp, CTE_S, Exp);
```
<h5>if</h5>

```
if (Exp) {Estatutos};
if (Exp) {Estatutos}else{Estatutos};
```
Donde Exp tiene que ser una comparacion
<h5>For_l</h5>

```
for (id = Exp to Exp ) {Estatutos};
```

Donde Exp tienen que ser numeros enteros
<h5>While_l</h5>

```
while(Exp){Estatutos};
```

Donde Exp tiene que ser una comparación
<h5>Return</h5>

```
return(Exp);
```
<h5>Funciones Especiales</h5>

Las funciones especiales pueden ser las siguientes:

<ul>
  <li>read_csv</li>
  <li>mean_func</li>
  <li>mode_func</li>
  <li>median_func</li>
  <li>linear_reg</li>
  <li>box_plt</li>
  <li>histogram_plt</li>
</ul>

<h5>read_csv</h5>

```
variable = csv_read(variable);
```
Donde las variables tienen que ser de tipo dataframe
<h5>mean_func</h5>

```
variable = mean(variable);
```
Donde las variables tienen que ser de tipo dataframe

<h5>mode_func</h5>

```
variable = mode(variable);
```
Donde las variables tienen que ser de tipo dataframe
<h5>median_func</h5>

```
variable = median(variable);
```
Donde las variables tienen que ser de tipo dataframe

<h5>linear_reg</h5>

```
linear_reg(variable);
```
Donde la variable tienen que ser de tipo dataframe
<h5>box_plt</h5>

```
box_plt(variable);
```
Donde la variable tienen que ser de tipo dataframe
<h5>histogram_plt</h5>

```
histogram(variable);
```
Donde la variable tienen que ser de tipo dataframe

<h5>Operaciones</h5>
En este lenguaje se permiten las siguientes operaciones:

<ul>
  <li>+</li>
  <li>-</li>
  <li>*</li>
  <li>/</li>
  <li>></li>
  <li>>=</li>
  <li><</li>
    <li><=</li>
  <li>==</li>
  <li>!=</li>
  <li>&&</li>
  <li>||</li>
</ul>

<h5>Main</h5>
Finalmente para correr un archivo es necesario tener una función main(). El formato a seguir es el siguiente:
```
main(){
    Vars
    Estatutos
};
```

<h3>Ejemplos</h3>
A continuación se presentaran algunos ejemplos combinando lo que se decribio hasta ahora.

Este primer ejemplo es algo simple pero sirve para crear un programa, declarar una variable, darle un valor e imprimirla.

```
program simple :

main(){
    var int a;
    a = 10;
    
    write(a);
};
```

Sin embargo en este lenguaje se pueden crear cosas mucho más complejas. Este segundo ejemplo es un poco más avanzado, el codigo es para sacar el numero de fibonacci de forma recursiva e iterativa:

```
program fibonacci : 


func int fibo_recur(int n){
    if (n <= 1){
        return (n);
    }else{
        return(fibo_recur(n-1) + fibo_recur(n-2));
    };
};

func int fibo_iterative(int n){
    var int a, b, c;

    a = 0;
    b = 1;

    while(n-2 >= 0){
        c=a+b;
        a = b;
        b = c;
        n=n-1;
    };
    return (c);
};

main(){
var int i, num;
num = 20;

write("Fibonacci recursive: ", fibo_recur(num));

write ("Fibonacci iterative: ");
write(fibo_iterative(num));
};
```

Finalmente, en el tercer ejemplo creamos y leemos un dataframe imprimir su contenido, y despues hacer una regresion lineal.

```
program dataF :

main(){
    var dataframe df;

    df = csv_read("./csv/winequality-red.csv");

    write(df);

    linear_reg(df);
    
};
```
