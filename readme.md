# Readme

## Proyecto Individual I

### Descripcion,analisis y sistemas de recomendacion knn en films
<br />
<br />

<br />

### <strong>1. Identificación de problemas y formulación de objetivos</strong>.

<br />
   Un objetivo bien definido ayuda a determinar los datos requeridos, realizados por medio del ETL, EDA ,Y seleccionar los modelos de aprendizaje automático apropiados y evaluar el rendimiento del sistema de recomendación.
   definir claramente el problema que resolverá el sistema de recomendación.
<br />


###  <strong>2. Recopilación y preprocesamiento de datos</strong>

<br />


   El siguiente paso es recopilar datos sobre el comportamiento .
   Después de la recopilación de datos, los  datos se preprocesan y analizan . Este paso implica limpiar los datos, eliminar duplicados y controlar los valores que faltan. Además,  de transforman estos datos en un formato adecuado para algoritmos de aprendizaje automático.
<br />
   algunas bibliotecas utilizados para el preprocesamiento de datos basadas en Python:
<br />
```pandas
    numpy
    literal_eval
```
<br />

###  <strong>3. Análisis exploratorio de datos</strong>
<br />

    El análisis exploratorio de datos (EDA) ayuda a comprender la distribución de datos y las relaciones entre las variables que se pueden utilizar para generar mejores recomendaciones.
   
    por ejemplo ,puede visualzar el promedio de presupuesto y ganancia que se obtuvo por pelicula, una descripcion estadistica general  . la fecuencia mas alta en produccion de peliculas por pais es  estados unidos. la pelicula mas frecuente es cinderella.y el actor con mas participacion es Bless Flowers

    - algunas bibliotecas  para llevar a cabo análisis de datos exploratorios:
    
```
     matplotlib
     seaborn
     Pandas
     wargnings
```
<br />

###  <strong>4. Ingeniería de características</strong>
<br />
   La ingeniería de características implica seleccionar las características más adecuadas para entrenar el modelo de aprendizaje automático. Este paso implica crear nuevas características o transformar las existentes para hacerlas más adecuadas para el sistema de recomendación.

   Por ejemplo, dentro de los datos de los movies, las características como genero , tagline o frase celebre asociada a la pelicula y vote_average  son más relevantes para crear un sistema de recomendación .

   algunas bibliotecas  de Python para utilizados:

```Scikit-learn
    matplotlib
    WordCloud
    scipy
    pandas
    numpy
```
<br />
<br />

###  <strong>5. modelado</strong>
<br />
   El objetivo de la selección de modelos es elegir el mejor algoritmo de aprendizaje automático que pueda predecir con precisión  .

   algoritmo :

   i. Filtrado basado en contenido
        utiliza caracteristicas de un elemento  para recomendar elementos adicionales con propiedades similares
<br />

###  <strong>6. Implementación del modelo </strong>
<br />
   KNN es un modelo perfecto y también una muy buena línea para el desarrollo de sistemas de recomendación. Utiliza una base de datos en la que los puntos de datos se separan en varios clústeres para hacer inferencias para nuevas muestras.se basa en la similitud de características de los elementos .KNN calculará la "distancia" entre la película de destino y cualquier otra película en su base de datos,luego clasifica sus distancias y devuelve las mejores películas de vecinos más cercanas .
    
    - se necesita los datos estén en una matriz
    - Nuestro marco de datos de película es una matriz extremadamente dispersa
    - usaremos la similitud del coseno para la búsqueda del vecino más cercano
    
<br />

###  <strong>7. sistema de recomendacion </strong>
<br />   
   Después de preprocesar los datos y transformar el marco de datos de las clasificaciones en una matriz dispersa de características de película, necesitamos configurar nuestro modelo KNN con los hiperparámetros adecuados:

```
from sklearn.neighbors import NearestNeighbors
model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=5, n_jobs=-1)
```
  Finalmente podemos hacer algunas recomendaciones de películas .
    

###  <strong>8. conclusiones </strong>
<br />  
   al realizar el EDA en los datos llegamos a algunas conlusiones:<br />  
   - para algunas variables numericas se les define como una distribucion muy cercana a la normal
   - las variables que dependen de variables independientes . se les atribuira modificaciones de orden de    representacion en el tratamiento outliers
   - Del heatmap se puede concluir que  hay variables fuertemente correlacionadas como budget y revenue en numericas y en categoricas title y tagline

<br />  

### <strong>enlace del deploy consultas </strong>



 ### <strong>enlaces recomendados </strong>    
<br /> 
https://towardsdatascience.com/prototyping-a-recommender-system-step-by-step-part-1-knn-item-based-collaborative-filtering-637969614ea