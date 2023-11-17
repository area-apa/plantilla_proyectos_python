## Tabla de contenidos
1. [General Info](#general-info)
2. [Tecnologias](#Tecnologias)
3. [Recursos CML](#Recursos_CML)
4. [Colaboradores](#Colaboradores)
5. [Instalacion](#Instalacion)
6. [Ejecucion](#Ejecucion)
7. [Explicacion](#Explicacion)
8. [Sugerencias y pasos siguientes](#Sugerencias)
9. [Estructura de carpetas](#plantilla_proyectos_python)
10. [Estructura de tablas y rutas](#Estructura_rutas_tablas)
### General Info
***
acá se debe escribir una breve reseña del proyecto, que es lo que hace y su salida

## Tecnologias
***
Una lista de las tecnologias mas importantes utilizadas, por ejemplo si se trata de r o python (la versión)
la versión de las librerías mas importantes por ejemplo si se trabajo con tensorflow o pytorch sería interesante saber que versiones. Aca tambien se debe señalar los recursos con que se ejecutó el proyecto (por ejemplo 8cpu's 64 Ram) a continuación una breve muestra de lo esperado
- Pandas
- Numpy
- Scikit-learn
- Matplotlib
- Seaborn
- Scipy
- joblib
## Recursos_CML
***
Acá debemos especificar, los nombres y parametros de los job, experiments u objectos models creados, como estos se ejecutan y la salida esperada. Si se desea agregar una foto, sería bueno 

## Colaboradores
***
Quienes fueron las personas que participaron en el proyecto. Nombre del cientifico de datos (o similar) experto del negocio etc

## Instalacion
***
Los pasos para instalar el proyecto y sus configuraciones en un entorno nuevo en caso que sea necesario, por ejemplo:
1. Instalar paquetes
    - Ingresar a la carpeta package_requeriment y abrir la terminal 
    - Escribir el siguiente comando: pip install -r requirements.txt
2. Configurar archivo config_types.yml
    - Escribir el nombre de la variable, seguido del tipo de dato el cual debería ser, esto con el fin de dar el formato desde un comienzo a cada variable.
3. Ejecutar Notebooks
    - Ejecutar notebooks en el order señalado en el siguiente item para la obtencion de clusters.

## Ejecucion
***
Orden y explicación de los archivos que deben ser ejecutados para el correcto desempeño del proyecto. Por ejemplo:
1. `Main_Imputation.ipynb`: Contiene el código de la imputacion de los datos. Para poder utilizar este notebook, es necesario contar con lo siguiente:
    - Se necesita tener el dataset sin ningun procesamiento, llamado *CM_VARIABLES_EMPRESAS_SAMP_CLUS_*, en formato *.tab*, en la ruta **../data/Bronze/**.
2. `Main_Processing.ipynb`: Contiene el código del procesamiento de los datos. Para poder utilizar este notebook, es necesario contar con lo siguiente:
    - Se necesita tener el dataset filtrado por el notebook anterior, llamado *CM_VARIABLES_EMPRESAS_FILTERS*, en formato *.csv*, en la ruta **../data/Silver/**.
...

## Explicacion
***
Breve reseña de lo que deben hacer las implementaciones no mencionadas en el apartado anterior


## Sugerencias
***
Se debe explicitar alguna sugerencia que no llegó a ser implementada o especificar quese pretende incluir en una eventual etapa siguiente.

## plantilla_proyectos_python
***
La esctrutura de proyectos debería ser la siguuiente:
(además en cada carpeta dejé un archivo txt q explica el contenido que debe llevar la carpeta)

**notar que el proyecto en CML debe tener la escructura de nombre {identificador}_{proyecto} por ejemplo lr-629_identificacion_acteco**

### Recuerden que se aceptan sugerencias de todo tipo...respecto a la estructura de carpetas

├── data  
│   ├── external                          __Data de fuentes de 3eras partes__  
│   ├── interim                           __Datos intermedios que han sido transformados__  
│   ├── processed                         __Datos procesados, que serán usados para el modelo__  
│   └── raw                               __Data cruda, datos descargados sin modificar__  
│     
├── docs                                  __Cualquie cosa__  
├── models/artefactos                     __Modelos entrenados o serializados, predicciones__  
├── README.md                             __Debe tener la info relevante del proyecto__      
├── references                            __Diccionario de datos, manuales, y cualquier otro material explicativo__  
├── reports                               __análisis generados como pdf, html, latex, etc__  
│   └── figures                           __Gráficas generadas a hacer usados en los reportes__  
├── requirements.txt                      __lista de paquetes requeridos para reproducir el entorno, pip freeze > requirements.txt__  
├── src                                   __CODIGO FUENTE DEL PROYECTO__  
├── notebooks                             __Notebooks de jupyter,deben llamar a los codigos en src o ser transformados a formato py__    
│   ├── data                              __Scripts para descargar o generar datos__    
│   │   ├── __init__.py   
│   │   └── make_dataset.py    
│   ├── features                          __Scripts para convertir la data cruda a datos para el modelo__   
│   │   ├── build_features.py   
│   │   └── __init__.py   
│   ├── __init__.py  
│   ├── models                            __Scripts para entrenar el modelo y luego hacer predicciones__   
│   │   ├── __init__.py   
│   │   ├── predict_model.py   
│   │   ├── train_model.py   
│   │   └── validate_model.py  
│   │── visualization                     __Scripts para crear exploración y resultados orientados a la visualización__   
│   │   ├── __init__.py   
│   │   └── visualize.py  
│   └── inferencia                        __Scripts para inferencia, donde se usan los archivos contenidos en el resto de las carpetas__    
│       ├── mainInferencia.py            
│       
├── test_environment.py                 __aplica en caso de querer hacer test unitarios__


## Estructura_rutas_tablas
***

Lo que se busca es que todas vez que se tenga una salida intermedia importante desde el punto de vista del peso o la cantidad de tablas, esta se disponibilice en una tabla hive (se almacene en azure) para permitir su posterior observacion. Dicho esto, la ubicación de las mencionadas salidas deberá seguir el siguiente creiterio de ubicacion.

abfs://data@datalakesii.dfs.core.windows.net/DatosOrigen/{identificador}/{nombre_proyecto}/intemedia/{nombre_tabla}
y su ubicación desde el punto de vista de hive debería ser el siguiente
{namespace}.{nombre_tabla}

en el caso que sea una tabla final (resultado del modelo, por ejemplo una nomina) esta debe quedar en la siguiente ruta

abfs://data@datalakesii.dfs.core.windows.net/DatosOrigen/{identificador}/{nombre_proyecto}/final/{nombre_tabla}
y su ubicación desde el punto de vista de hive debería ser el siguiente
{namespace}.{nombre_tabla}

por ejemplo

abfs://data@datalakesii.dfs.core.windows.net/DatosOrigen/lr-629/identificacion_acteco/intermedia/tabla_intermedia
donde 

**lr-629** es el identificador del proyecto, licitacion, convenio marco etc

**identificacion_acteco** Nombre del proyecto

**tabla_intermedia**: Nombre de la tabla
luego, desde el punto de vista de hive esta debe almacenarse en:

{namespace}.{nombre_tabla}

A modo de ejemplo el código que podría implementar lo anterior es:

miDataFrame.write.mode('overwrite').option("path", "abfs://data@datalakesii.dfs.core.windows.net/DatosOrigen/lr-629/identificacion_acteco/intermedia/tabla_intermedia).saveAsTable("apa_temp.tabla_intermedia")

miDataFrame.write.mode('overwrite').option("path", "abfs://data@datalakesii.dfs.core.windows.net/DatosOrigen/lr-629/identificacion_acteco/final/tabla_intermedia).saveAsTable("apa_temp.tabla_final")

**la solicitud de carpetas debe hacerse a la persona encaragada del proyecto por parte del SII**




