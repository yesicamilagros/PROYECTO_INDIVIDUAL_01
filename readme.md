# Readme

## Proyecto Individual I



<h1 align="center"> Analisis exploratorio y sistema de recomendacion en peliculas </h1>

<p align ="center" width="100%">
    <img width="60%" src="image\descargar.png">
</p>

*[Índice](#índice)

*[Descripción del proyecto](#descripción_del_proyecto)

*[Características de la aplicación y demostración](#Características_de_la_aplicación_y_demostración)

*[Acceso al proyecto](#acceso_al_proyecto)

*[Paquetes utilizadas](#paquetes_utilizados)

*[Conclusión](#conclusión)

*[Personas-Desarrolladores del Proyecto](#personas_desarrolladores)

# descripción_del_proyecto

Para tener un objetivo preciso del comportamiento de los datos se ha realizado la limpieza y exploracion de los mismos
 primero se hizo el proceso de tranformacion sobre **los dataset movies y credits**  , la carga  de los datasets y luego el proceso del ETL finalmente el archivo esta lista para ser archivo fuente del **proceso EDA** el proceso de EDA precede al modelamiento, se formula supuestos o hipotesis . se realiza un descripcion estadistico sobre variables numericas y categoricas , se propone inferencias ,supuestos, las cuales son validadas con los diagramas de dispersion , barras, caja , histograma ,heatmap, etc. estas se detallan en el notebook.se analiza las correlaciones entre variables para  luego realizar el modelo que ejecute recomendaciones de peliculas similares a una al respecto.



# Características_de_la_aplicación_y_demostración

-  **ETL:** se hace la carga de los datasets , vista previa de los mismos, se elimina fila duplicados o nulas , filas no relacionadas ,recuento de vacios y nulos, reemplazo de datos vacios o nulos  por 0 en el caso de columnas numericas ,columnas categoricas  con una cadena de texto "sin_dato" , y en las anidadas con diccionarios . se toma esa decicion puesto que en algunas columnas los datos nulos representa menos del 1 % de la columna,y se necesita realizar calculos con alguna de ellas, se modifica el tipo de dato por columna, se elimina algunas columnas no muy predominantes en el analisis descriptivo estadistico y modelamiento


<p align ="center" width="100%">
    <img width="60%" src="image\etl.png">
</p>
   
- **EDA:** efectuado el proceso anterior , el proceso EDA precisa de estos datos para analizar , proponer supuestos o inferencias a partir de la descripcion estadistica , y extraer informacion .caracteristicas principales de los datos ,en variables numericas solo hay una variable que sigue una distribucion simetrica o normal, en variables categoricas en idioma original el ingles es el mas frecuente y ello se verifica en los diagramas, en status es released, y  cinderella es la pelicula mas frecuente. en las variables numericas existen datos atipicos . al realizar el tratamiento de los mismos .se llega a un conjunto de datos sin outliers. pero ello tiene implicancias en los resultados estadisticos de la variable numerica(p.ej. cambios en la popularidad de las peliculas) y finalmente se analiza el nivel de correlacion por cada par de variables

 <p align ="center" width="100%">
    <img width="60%" src="image\eda.png">
</p>

- **sistema de recomendacion** respecto al tipo de modelo a usar para recomendacion de peliculas , se ha utilizado el modelo KNN  , ademas se utilizo la funcion coseno de similitud, la similitud es muy alta cuando la distancia es poca , es decir cuando la distancia entre dos vectores tiende a 0 .las peliculas seran mas similares, las peliculas a relacionar, poseen genero y en este caso clasificaremos las películas según sus géneros. se crea la columna genres_bin que define vectores a los cuales se aplica funcion coseno de similitud


# acceso_proyecto
 
  - link de notebook ETL: https://colab.research.google.com/drive/1XfszVglinoqwGMzrbd8kbZvVsl0Nv3qW?usp=sharing
  - link de notebook EDA : https://colab.research.google.com/drive/1BWuVdzdm7hrBuPtbIDKb6DiwP_d4ZkFN?usp=sharing
  - link de notebook ML : https://colab.research.google.com/drive/1P-Faq-dc2WKEyAVMIns-X0rcaifOz-2t?usp=sharing
  - link del deploy : https://proyecto01-qgmc.onrender.com/docs#/

# paquetes_utilizados

    - fastapi
    - pandas 
    - matplotlib.pyplot 
    - seaborn 
    - numpy 
    - uvicorn
    - scipy

# conclusión

<br />al realizar el EDA en los datos llegamos a algunas conlusiones:<br />  

   - para algunas variables numericas se les define como una distribucion muy cercana a la normal
   - las variables que dependen de variables independientes . se les atribuira modificaciones de orden de    representacion en el tratamiento outliers
   - Del heatmap se puede concluir que  hay variables correlacionadas como budget y revenue en numericas y en categoricas title y genres
   -  se puede concluir que la imputacion de outliers tiene un efecto significativo en la variable popularidad de las peliculas (constante en los 8 primeros ) 
   - la funcion del coseno de similitud influye en el modelo de ML y en la recomendacion de films en este caso se creo una columna con listas de elementos binarios para aplicar la funcion, genres_bin.

<br />  

# personas_desarrolladores

 - Yesica Milagros Leon Ccahuana
