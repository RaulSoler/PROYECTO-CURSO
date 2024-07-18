# Memoria del Proyecto

## Índice
1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [Introducción](#introducción)
3. [Metodología](#metodología)
4. [Desarrollo del Proyecto](#desarrollo-del-proyecto)
5. [Resultados](#resultados)
6. [Discusión](#discusión)
7. [Conclusiones](#conclusiones)
8. [Recomendaciones](#recomendaciones)

## Resumen Ejecutivo
Este proyecto presenta un modelo predictivo para los resultados de fútbol de la liga española. Se utilizan datos históricos para entrenar un modelo de aprendizaje automático.


## Introducción
### Contexto del Proyecto
En el ámbito del análisis de datos deportivos, la predicción de resultados de partidos de fútbol se ha convertido en un área de gran interés . Mi proyecto se centra en la predicción de resultados de los partidos de la liga española de fútbol, utilizando datos históricos que abarcan desde la temporada 2000 hasta la temporada 2022.

### Objetivos
- Desarrollar un Modelo Predictivo Preciso: Crear y entrenar un modelo que pueda predecir con precisión los resultados de los partidos de la liga española utilizando datos históricos desde la temporada 2000 hasta la 2022.
- Evaluar Diferentes Algoritmos: Comparar y evaluar la eficacia de diferentes algoritmos y técnicas de aprendizaje automático para la predicción de resultados de partidos de fútbol.
- Ofrecer Predicciones Futuras: Utilizar el modelo desarrollado para ofrecer predicciones de los resultados de futuros partidos, permitiendo validar y mejorar continuamente el modelo con nuevos datos.
### Alcance y Limitaciones

Recopilación de Datos Históricos: Reunir datos detallados de los partidos de la liga española desde la temporada 2000 hasta la temporada 2022. Esto incluye resultados de los partidos, estadísticas de los equipos y jugadores, y otras variables relevantes.

Desarrollo de un Modelo Predictivo: Crear un modelo de aprendizaje automático capaz de predecir los resultados de los partidos futuros. Esto implica seleccionar y ajustar algoritmos adecuados, entrenar el modelo con los datos recopilados y evaluar su precisión.

Análisis de Factores Influyentes: Identificar y analizar los factores que más afectan los resultados de los partidos, proporcionando una mejor comprensión de las dinámicas del fútbol profesional.

Visualización de Resultados: Desarrollar herramientas de visualización para representar los resultados del modelo y las estadísticas de manera clara y accesible, facilitando la interpretación de los datos y los resultados.

Generación de Informes y Recomendaciones: Elaborar informes detallados que resuman los hallazgos del proyecto y ofrezcan recomendaciones basadas en los resultados del análisis.

Falta de Datos de Partidos: La disponibilidad de datos históricos puede ser incompleta o inexacta, especialmente para las primeras temporadas (2000-2010). Esto puede afectar la precisión del modelo predictivo y la calidad del análisis.

Variabilidad en el Rendimiento de los Equipos: El rendimiento de los equipos y jugadores puede variar significativamente de una temporada a otra debido a diversos factores como lesiones, transferencias de jugadores, cambios de entrenadores, etc. Esta variabilidad puede dificultar la precisión de las predicciones.

Factores Externos No Cuantificados: Factores como el clima, las condiciones del terreno de juego, la moral del equipo, y otros aspectos psicológicos no siempre están disponibles en los datos y pueden influir en los resultados de los partidos.

Limitaciones Técnicas: La elección y ajuste de algoritmos de aprendizaje automático pueden presentar desafíos técnicos, y el rendimiento del modelo puede depender de la calidad y cantidad de los datos disponibles.


## Metodología

Para llevar a cabo el proyecto de predicción de resultados de los partidos de la liga española de fútbol, se siguieron una serie de pasos metodológicos bien definidos. A continuación, se describen las etapas clave del proceso:

### 1. Recopilación de Datos

**Fuentes de Datos:**
- Recolección de datos históricos de partidos de la liga española desde la temporada 2000 hasta la temporada 2022.
- Link recogida de datos [Base de datos](https://fbref.com/es/?lang=es)
- [Muestra datos](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#Predicción-de-partidos-de-fútbol-de-la-liga-española)



**Tipos de Datos:**
- Resultados de los partidos (victoria, empate, derrota).
- Fecha, Goles a favor, Goles en contra.
- [Parte mención datos](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#CARGA-DEL-CSV-PARA-CONVERTIRLO-EN-DATAFRAME)

### 2. Preprocesamiento de Datos

**Limpieza de Datos:**
- [Borrado de duplicados](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#VEMOS-QUE-LAS-COLUMNAS-CON-@-SON-DUPLICADOS-Y-LAS-BORRAMOS)
- [Borrado de nulos y limpieza de columnas](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#BORRAMOS-LAS-COLUMNAS-NO-NECESARIAS-Y-QUE-TIENEN-NULOS.-REALMENTE-SOLO-NOS-QUEDAMOS-CON-LOS-EQUIPOS,-FECHA-Y-RESULTADO)
- [Cambio nombre columnas y tipo de las columnas](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#VAMOS-A-CAMBIAR-LOS-NOMBRES-DE-LAS-COLUMNAS)

**Transformación de Datos:**
- He generado diversas y multiples columnas con las casi todas la combinaciones posibles, voy a destacar las mas importantes.
- [Equipo ganador](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#Funcion-para-determinar-que-equipo-ha-ganado)
- [Generacion temporada y jornada](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#Generar-temporada-y-jornada,-sabiendo-la-duracion-de-las-temporadas-de-unos-8-meses-aproximados,-y-para-jornada-que-tiene-que-ser-10-partidos-por-jornada)
- [Generacion posiciones](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#Aqui-lo-que-hacemos-es-Generar-un-data-para-almacenar-las-posiciones-dependiendo-de-los-puntos-de-cada-equipo-por-jornada.)
- [Genera puntos](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#Aqui-generamos-la-suma-en-cada-jornada-de-los-3-puntos-o-1-punto-dependiendo-del-resultado,-primero-creamos-las-columnas-correspondientes-con-valor-0)
- [Saber racha de partidos](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#Extraer-el-resultado-del-partido-para-saber-quien-ha-ganado-o-perdido,-y-luego-acumarlo-en-una-racha-de-3-partidos-para-saber-la-forma)
- [Transformación del data a númericas para combinar y generar mas columnas](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#TRANSFORMAMOS-NUESTRO-DATA-TODO-A-NUMERICAS-PARA-VER-NUEVAS-COLUMNAS-QUE-PODEMOS-GENERAR-YA-QUE-TENEMOS-UNA-CORRELACION-MUY-BAJITA)
### 3. Análisis Exploratorio de Datos (EDA)

**Visualización de Datos:**
- [Distribución de Resultado](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#Distribución-de-Resultado)
- [Evolución de Local, Visitante y Empate a lo largo de las temporadas](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#Resultados-por-temporada)
- [Resultados en funcion de la posición Local](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#Distribución-de-Resultados-en-Función-de-la-Posición-del-Equipo-Local)
- [Resultados en funcion de la posición Visitante](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#Distribución-de-Resultados-en-Función-de-la-Posición-del-Equipo-Visitante)
- [Distribución resultados de los todos los equipos](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#Distribución-de-de-resultados-por-todos-los-equipos)

### 4. Selección de Características

**Identificación de Variables Relevantes:**
- [Visualización de las features mas importantes](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA.ipynb#Con-el-data-ya-transformado-vamos-a-ver-las-features-mas-importantes-por-el-target)
- Probando el modelo hemos seleccionado finalmente todas la caracteristicas, ya que con solo las mas importante nos daba peores valores.

### 5. Desarrollo del Modelo Predictivo

**Entrenamiento del Modelo:**
- [Aplicación SMOTE. División de los datos en conjuntos de entrenamiento y prueba](../Modelos/Modelos_3.ipynb###**Separación-X_Train-e-Y_Train**)
- [Construcción de los modelos](../Modelos/Modelos_3.ipynb#**Construcción-de-los-modelos**)
- [Stacking para mejorar el rendimiento](../Modelos/Modelos_3.ipynb#**Stacking-de-los-modelos**) Es una forma de ensamblaje de modelos (model ensembling) que busca mejorar el rendimiento predictivo general.

### 6. Evaluación del Modelo

**Métricas de Evaluación:**
- Cálculo de métricas de rendimiento como precisión, recall, F1-score y área bajo la curva ROC (AUC-ROC).
- Evaluación del modelo en el conjunto de prueba para determinar su capacidad predictiva.

**Validación del Modelo:**
- F1-Score como metrica de evaluación. Se encuentran dentro de cada modelo con su matriz de correlacion.

### 7. Implementación y Visualización

**Despliegue del Modelo:**
- [Evaluamos el modelo contra Test, es un dataframe sin el target.](../Predicciones/Predicciones.ipynb)
- Para saber si realmente el modelo funciona bien, hemos cogido los partidos de la temporada 2023 que no estan incluidos en nuestro train.

### 8. Comunicación de Resultados
- Tras ver los resultados obtenidos con nuestro modelo de predicción. Vemos que la predicción para Empate es muy mala y baja el rendimiento a las demas clases. Aqui vemos una nueva oportuniad de negocio.
## Nueva oportunidad
- La nueva oportunidad se basa en la predicción de solamente si el ganador es Local o Visitante, ya que en las casas de apuesta nos dan esa opción de apuesta vamos intentar crear un modelo que sea mas eficiente para esos resultados.
- El procedimiento ha sido el mismo que la anterior parte, lo único que ha cambiado que hemos entrenado el modelo solo para Local o Visitante. A continuación voy a dejar los enlaces a los notebooks:
- [Limpieza sin Empate.](../BASESDEDATOS/Limpiezas/Resultados/Limpieza_EDA_2PRUEBA.ipynb).
- [Modelos entrenados.](../Modelos/Modelos_3_2PRUEBA.ipynb).
- [Predicciones contra test](../Predicciones/Predicciones_PRUEBA.ipynb)
## Desarrollo del Proyecto
- La dificultad de conseguir los datos de los resultados de los partidos, ya que me ha tocado hacerlo semimanual, copiando en bloques de 200 resultados.
- Escasez de datos estadisticos por partido.
- Ver el data que tenemos y como generar mas columnas que nos genere información relevante.

Una vez estos tres puntos claros, decidimos a generar todas esas columnas con sus transformaciones, vi que a partir de esos datos podria sacar quien es el ganador del partido, de la fecha y sabiendo la duración de una temporada generamos jornadas y temporadas... 

Tras la generación de nuestras columnas, decido transformalo a númericas con Label Encoder para asi poder generar mas columnas entre ellas, cuando tengo todas las que creo suficientes, durante el proceso he entrenado con diferentes números de features y viendo los resultados decido quedarme con todas las features.

Separación X_train e y_train, separo ambos y aplico un SMOTE para el balanceo de clases, ya que durante el proceso vemos ese desbalanceo.
A la hora del entrenamiento del modelo, al ser un problema bastante complejo de predecir, decido aplicar 11 tipos de modelos de clasificación para probarlos y aplicar un ensamblaje de todos los modelos para mejorar su rendimiento. 

Y finalmente con el modelo entrenado, pruebo contra Test que es una temporada entera que no teniamos incluida para poder predecirla.

## Resultados
Al ver que el modelo a la hora de predecir resultados es bastante pobre con los empates, decido dar un cambio al final para predicer solamente ganador local o visitante, este cambio es predecido por una oportunidad que veo en la cassas de apuestas que ofrecen la variante de acertar un resultado sin contar el empate. Entonces intento entrenar este modelo para que sea mas eficiente y mejor en esos resultados.

## Conclusiones
Ambos modelos tanto para predecir 3 posibles resultados como 2 resultados, tienen bastate buena proyección a falta de mas datos especificos para mejorar su rendimiento.

## Recomendaciones
- Añadir datos nuevos para su reentreno para predecir encuentros futuros.

