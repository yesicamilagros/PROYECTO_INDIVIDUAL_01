from fastapi import FastAPI
import pandas as pd
#from fastapi import File, UploadFile, FastAPI
import uvicorn 
from datetime import datetime
from scipy import spatial
from ast import literal_eval
import operator
import ast



app=FastAPI(title='Consulta de FILMS')

@app.get("/")

def funcion():
  return "Hello World"

def conversion_listas_Dict(columna):
    o=[]
    for i in range(len(columna)):
        p=[]
        for j in range(len(ast.literal_eval(columna[i]))):
            p.append(ast.literal_eval(columna[i])[j]['name'])
        o.append(p) # lista de listas
    ser1=pd.Series(o)
    return ser1

def Similarity(movieId1, movieId2): 
    a = movie.iloc[movieId1]
    b = movie.iloc[movieId2]
    genresA = a['genres_bin']
    genresB = b['genres_bin']
    
    genreDistance = spatial.distance.cosine(genresA, genresB)

    return genreDistance

f2=pd.read_csv(r'dataset\funcion2.csv')
movies=pd.read_csv(r'dataset\peliculas.csv')
f6=pd.read_csv(r'dataset\funcion6.csv')
movie=pd.read_csv(r'dataset\machine_learning.csv')
movies=movies.drop_duplicates()
movies=movies.reset_index(drop=True)
movies['runtime']=movies['runtime'].fillna(movies['runtime'].median())
movies['belongs_to_collection']= movies.belongs_to_collection.apply(literal_eval)
movies['belongs_to_collection']=movies['belongs_to_collection'].apply(lambda x: x['name'])
movies['production_countries']=conversion_listas_Dict(movies['production_countries'])
movies['production_companies']=conversion_listas_Dict(movies['production_companies'])

@app.get('/pelicula_idioma/{idioma}')
def pelicula_idioma(idioma:str):
    '''Se ingresa el idioma en formato de 2 consonates y la funcion retorna  la cantidad de películas que fueron realizadas en ese idioma 
       p.ej : idioma : es  , out : {'cantidad de filmaciones en idioma ': 989 }'''
    
    language=idioma.lower()
    df=movies[['original_language','title']].drop_duplicates().groupby(['original_language'])['original_language'].agg([('Count','size')]).sort_values(by='Count',ascending=False).reset_index()
    if language in list(df['original_language']):
      if df['original_language'][pd.Index(df['original_language']).get_loc(language)]==language :
          return {'idioma' : language, 'cantidad de filmaciones en idioma': str(df['Count'][pd.Index(df['original_language']).get_loc(language)])}
    else:
          return ' idioma no  definida'



@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula:str):
    
    '''Se ingresa el nombre de la pelicula y la funcion retorna la duracion del film y el año de estreno del mismo
       return :  { 'Pelicula' : Jumanji , 'Duracion de Pelicula en Minutos': 104.0 , 'Año de Estreno' :1995}'''

    if pelicula in list(f2['title']):
      if  f2.iloc[pd.Index(f2['title']).get_loc(pelicula)][0]== pelicula:
              b=f2['runtime'][pd.Index(f2['title']).get_loc(pelicula)]
              c=f2['release_year'][pd.Index(f2['title']).get_loc(pelicula)]
              return {'Pelicula' : pelicula , 'Duracion de Pelicula en Minutos':str(b), 'Año de Estreno' :str(c)}
    else:
        return {'pelicula no registrada o no bien Definida'}

@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas de la franquicia, ganancia total y promedio
       p.ej : Franquicia : Finding Nemo Collection , 
       return : {'La Franquicia ' :Finding Nemo Collection,'Cantidad De Peliculas ' : 2  , 'Ganancia total': 1968906425.0  , 'Ganancia Promedio' : 984453212.5  }'''

    fra=franquicia               #re.sub(r'\W+', ' ', pelicula).strip()
    f3=movies[['belongs_to_collection','title','revenue']].drop_duplicates().reset_index(drop=True).groupby('belongs_to_collection').agg( cantidad = ('belongs_to_collection', 'count'),
                                 total = ('revenue', 'sum'),
                                 promedio = ('revenue', 'mean')).reset_index()
    if fra in list(f3['belongs_to_collection']):
      for i in range(len(f3['belongs_to_collection'])):
          if f3['belongs_to_collection'][i]==fra :
            return {'Franquicia ' : fra ,'Cantidad De Peliculas ' : str(f3['cantidad'][i]), 'Ganancia total': str(f3['total'][i]) , 'Ganancia Promedio' : str(f3['promedio'][i])}
    else:
        return 'franquicia no registrada o no bien definida'
    

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
   ''' Ingresar el pais, retorna la cantidad de peliculas producidas en el mismo'''

   f4=movies[['title','production_countries']].explode('production_countries').drop_duplicates().reset_index(drop=True).groupby(['production_countries']).agg( cantidad_de_peliculas = ('production_countries', 'count')
                                       ).sort_values(by='cantidad_de_peliculas',ascending=False).reset_index()
   if pais in list(f4['production_countries']):
     
       if f4.iloc[pd.Index(f4['production_countries']).get_loc(pais)][0]== pais:
          return {'pais': pais, 'cantidad': str(f4.iloc[pd.Index(f4['production_countries']).get_loc(pais)][1])}
   else:
       return {'Pais no registrado o no bien definida'}


@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora):
    '''Ingresar la compañia productora, entregandote el revenue(ganancia) total y la cantidad de peliculas que realizo 
    return {'productora':productora, 'revenue_total': respuesta,'cantidad':respuesta} '''
    f5=movies[['title','revenue','production_companies']].explode('production_companies').drop_duplicates().reset_index(drop=True).groupby(['production_companies']).agg( cantidad = ('production_companies', 'count'),
                                       total = ('revenue', 'sum')).sort_values(by='cantidad',ascending=False).reset_index()
    if productora in list(f5['production_companies']):
       if f5.iloc[pd.Index(f5['production_companies']).get_loc(productora)][0]==productora:
         return {'productora':productora, 
                 'revenue_total': str(f5.iloc[pd.Index(f5['production_companies']).get_loc(productora)][2]),
                 'cantidad': str(f5.iloc[pd.Index(f5['production_companies']).get_loc(productora)][1])}
    else:
       return {'compañia productora no registrada o no definida'}

@app.get('/get_director/{nombre_director}')
def get_director(nombre_director:str):
    ''' Se ingresa el nombre de un director que se encuentre dentro de dataset devuelve el éxito del mismo medido a través del retorno. 
    Además, devuelve el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma. En formato lista
     considerar que en ganancias muchos datos se han reemplazado los nulos o vacios por 0 . '''
    try:
      p=0
      o=0
      l=[]
    
      for i in range(len(f6['title'])):
            if  f6['crew'][i]== nombre_director:
                l.append(dict(zip(['filmacion','fecha_estreno','retorno','costo','ganancia'],[f6['title'][i],f6['release_date'][i],f6['return'][i],f6['budget'][i],f6['revenue'][i]])))
                p=p + f6['return'][i]
                o=o + 1
      return {'nombre del director':nombre_director,'retorno de exito':str(p/o),'cantidad de filmaciones':str(len(l)),'filmaciones':l}  
    except:
          return {'director no registrado'}

# ML
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    '''Ingresar un nombre de pelicula y recomienda las similares en una lista'''
    #return {'lista recomendada': respuesta}
    name=titulo
    try:
      movie['genres_bin'] = movie.genres_bin.apply(lambda x: literal_eval(str(x)))
      movie['genres'] = movie.genres.apply(lambda x: literal_eval(str(x)))
      new_movie = movie[movie['title'].str.contains(name)].iloc[0].to_frame().T
    #print('eleccion de la pelicula: ',new_movie.title.values[0])
      def getNeighbors(baseMovie, K):
          distances = []
      
          for index, mov in movie.iterrows():
              if mov['new_id'] != baseMovie['new_id'].values[0]:
                  dist = Similarity(baseMovie['new_id'].values[0], mov['new_id'])
                  distances.append((mov['new_id'], dist))
      
          distances.sort(key=operator.itemgetter(1))
          neighbors = []
      
          for x in range(K):
              neighbors.append(distances[x])
          return neighbors
      K = 5
      avgRating = 0
      neighbors = getNeighbors(new_movie, K)
      
      #print('\n peliculas recomendadas: \n')
      
      p=[]
      for i in range(len(neighbors)):
            p.append(dict(zip(['pelicula','genero','vote_average o rating'],[movie.iloc[neighbors[i][0]][0],str(movie.iloc[neighbors[i][0]][1]).strip('[]').replace(' ',''),str(movie.iloc[neighbors[i][0]][2])])))
        #for neighbor in neighbors:
            #avgRating = avgRating+movie.iloc[neighbor[0]][2]  
            #p.append(movie.iloc[neighbor[0]][0]+" | Generos: "+ str(movie.iloc[neighbor[0]][1]).strip('[]').replace(' ','')+" | Rating: "+ str(movie.iloc[neighbor[0]][2]))
            #print(str(movie.iloc[neighbor[0]][1]))
            #print(movie.iloc[neighbor[0]][0]+" | Generos: "+ str(movie.iloc[neighbor[0]][1]).strip('[]').replace(' ','')+" | Rating: "+ str(movie.iloc[neighbor[0]][2]))
            #,'peliculas recomendadas':[movie.iloc[neighbors[0]],movie.iloc[neighbors[1]],movie.iloc[neighbors[2]],movie.iloc[neighbors[3]],movie.iloc[neighbors[4]]]
      return {'pelicula':titulo , 'peliculas recomendadas':p}
    except:
      return {'pelicula no registrada o no bien definida'}