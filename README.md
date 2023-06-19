# plantilla_proyectos_python

La esctrutura de proyectos debería ser la siguuiente:
(además en cada carpeta dejé un archivo txt q explica el contenido que debe llevar la carpeta)

## Recuerden que se aceptan sugerencias de todo tipo...respecto a la estructura de carpetas

├── data  
│   ├── external                          __Data de fuentes de 3eras partes__  
│   ├── interim                           __Datos intermedios que han sido transformados__  
│   ├── processed                         __Datos procesados, que serán usados para el modelo__  
│   └── raw                               __Data cruda, datos descargados sin modificar__  
│     
├── docs                                  __Cualquie cosa__  
├── models/artefactos                     __Modelos entrenados o serializados, predicciones__  
├── notebooks                             __Notebooks de jupyter,deben llamar a los codigos en src o ser transformados a formato py__    
├── README.md                             __Debe tener la info relevante del proyecto__      
├── references                            __Diccionario de datos, manuales, y cualquier otro material explicativo__  
├── reports                               __análisis generados como pdf, html, latex, etc__  
│   └── figures                           __Gráficas generadas a hacer usados en los reportes__  
├── requirements.txt                      __lista de paquetes requeridos para reproducir el entorno, pip freeze > requirements.txt__  
├── src                                   __CODIGO FUENTE DEL PROYECTO__  
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
