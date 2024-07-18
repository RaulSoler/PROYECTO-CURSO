import pandas as pd
from unidecode import unidecode
from sklearn.preprocessing import LabelEncoder

#Funcion para buscar en resultados2000_2023 dos equipos y nos devuelve historico, media goles y % quien se llevo cada partido
def encuentros_entre_equipos(df, equipo1, equipo2):
    # Filtrar los partidos donde equipo1 es local y equipo2 es visitante
    encuentros1 = df[(df['Local'] == equipo1) & (df['Visitante'] == equipo2)]
    # Filtrar los partidos donde equipo2 es local y equipo1 es visitante
    encuentros2 = df[(df['Local'] == equipo2) & (df['Visitante'] == equipo1)]
    # Unir los resultados
    encuentros = pd.concat([encuentros1, encuentros2]).sort_values(by='Date')
    print(f"Numero de goles de media en estos partidos son {round(encuentros["Numero_Goles_Total"].mean(),1)}")
    print(f"En % de Victorias {round(encuentros["Resultado"].value_counts(normalize=True),2)}")
    return encuentros



#Funcion sacar columnas por correlacion 

def filter_columns_by_correlation(data, target_column, min_correlation):
 
    # Calculate the correlation matrix
    corr_matrix = data.corr()
    
    # Get the absolute correlation with the target column
    target_corr = corr_matrix[target_column].abs()
    
    # Filter columns based on the minimum correlation value
    filtered_columns = target_corr[target_corr >= min_correlation].index.tolist()
    
    # Remove the target column from the list
    if target_column in filtered_columns:
        filtered_columns.remove(target_column)
    
    return filtered_columns

#Funcion quitar acentos y normalizar texto

def remove_accents(text):
    if isinstance(text, str):
        return unidecode(text)
    return text

#Funcion determinar resultado

def determinar_resultado(row):
    if row['Goles_Local'] > row['Goles_Visitantes']:
        return "Local"
    elif row['Goles_Local'] < row['Goles_Visitantes']:
        return 'Visitante'
    else:
        return 'Empate'
    



def calcular_resultado(fila, equipo):
    if fila['Local'] == equipo:
        if fila['Resultado'] == 'Local':
            return 'G'
        elif fila['Resultado'] == 'Visitante':
            return 'P'
        else:
            return 'E'
    elif fila['Visitante'] == equipo:
        if fila['Resultado'] == 'Visitante':
            return 'G'
        elif fila['Resultado'] == 'Local':
            return 'P'
        else:
            return 'E'


 # Clasificacion dependiendo del estado de forma
def clasificador_rendimiento_forma(form):
    if 'GGG' in form:
        return 'Excelente'
    elif any(seq in form for seq in ['GGE', 'EGG','GEG']):
        return 'Muy Buena'
    elif any(seq in form for seq in ['GGP', 'PGG', 'GPG']):
        return 'Buena'
    elif any(seq in form for seq in ['GEE', 'EGE', 'EEG', 'GPE', 'GEP', 'EPG', 'EGP', 'PGE', 'PEG']):
        return 'Regular'
    elif any(seq in form for seq in ['PPP', 'EPP', 'PEP','PPE']):
        return 'Mala'
    else:
        return 'Irregular'


# Generacion de Categorica para saber en que situacion de la tabla se encuentra
def clasificacion(data):
    seasons = data['Temporada'].unique()
    jornadas = data['Jornada'].unique()

    for season in seasons:
        for jornada in jornadas:
            jornada_data = data[(data['Temporada'] == season) & (data['Jornada'] == jornada)]          #Esta parte esta porque probe hacerlo dependiendo la diferencia de puntos y jornada que me dijese si el equipo
                                                                                                    #estuviera descendido, clasificado...
                                                                                                    #Pero me genereba muchos mas campos que luego tenian muy poca relevancia y prefiero reducir esas "categorias"
            pos_17_points = jornada_data[
                (jornada_data['Posicion_Local'] == 17) |
                (jornada_data['Posicion_Visitante'] == 17)
            ][['Puntos_Acumulados_Local', 'Puntos_Acumulados_Visitantes']].min().min()

            pos_1_points = jornada_data[
                (jornada_data['Posicion_Local'] == 1) |
                (jornada_data['Posicion_Visitante'] == 1)
            ][['Puntos_Acumulados_Local', 'Puntos_Acumulados_Visitantes']].max().max()

            pos_2_points = jornada_data[
                (jornada_data['Posicion_Local'] == 2) |
                (jornada_data['Posicion_Visitante'] == 2)
            ][['Puntos_Acumulados_Local', 'Puntos_Acumulados_Visitantes']].max().max()

            pos_18_points = jornada_data[
                (jornada_data['Posicion_Local'] == 18) |
                (jornada_data['Posicion_Visitante'] == 18)
            ][['Puntos_Acumulados_Local', 'Puntos_Acumulados_Visitantes']].max().max()

            for index, row in jornada_data.iterrows():
                local_position = row['Posicion_Local']
                visitante_position = row['Posicion_Visitante']
                local_points = row['Puntos_Acumulados_Local']
                visitante_points = row['Puntos_Acumulados_Visitantes']
                remaining_matches = 38 - jornada

                max_local_points = local_points + remaining_matches * 3
                max_visitante_points = visitante_points + remaining_matches * 3

                if local_position in [1, 2, 3, 4]:
                    local_status = 'Champions'
                elif local_position in [5, 6, 7, 8]:
                    local_status = 'Parte Alta'
                elif 9 <= local_position <= 13:
                    local_status = 'Mitad de Tabla'
                elif 14 <= local_position <= 17:
                    local_status = 'Parte Baja'
                elif local_position in [18, 19, 20]:
                    local_status = 'Zona Descenso'

                if visitante_position in [1, 2, 3, 4]:
                    visitante_status = 'Champions'
                elif visitante_position in [5, 6, 7, 8]:
                    visitante_status = 'Parte Alta'
                elif 9 <= visitante_position <= 13:
                    visitante_status = 'Mitad de Tabla'
                elif 14 <= visitante_position <= 17:
                    visitante_status = 'Parte Baja'
                elif visitante_position in [18, 19, 20]:
                    visitante_status = 'Zona Descenso'

                data.at[index, 'Estado_Tabla_Local'] = local_status
                data.at[index, 'Estado_Tabla_Visitante'] = visitante_status

    return data
    
       


def calcular_resultado(fila, equipo):
    if fila['Local'] == equipo:
        if fila['Resultado'] == 'Local':
            return 'G'
        elif fila['Resultado'] == 'Visitante':
            return 'P'
        else:
            return 'E'
    elif fila['Visitante'] == equipo:
        if fila['Resultado'] == 'Visitante':
            return 'G'
        elif fila['Resultado'] == 'Local':
            return 'P'
        else:
            return 'E'


forma_local = {}
forma_visitante = {}

def actualizar_forma(forma, equipo, resultado):                 #Actulizamos para formar la racha del equipo.
    if equipo not in forma:
        forma[equipo] = []
    forma_actual = ''.join(forma[equipo])
    if len(forma_actual) < 3:
        forma_actual = forma_actual.rjust(3, '-')
    forma[equipo].append(resultado)
    if len(forma[equipo]) > 3:
        forma[equipo].pop(0)
    return forma_actual

# Clasificacion dependiendo del estado de forma
def clasificador_rendimiento_forma(form):
    if 'GGG' in form:
        return 'Excelente'
    elif any(seq in form for seq in ['GGE', 'EGG','GEG']):
        return 'Muy Buena'
    elif any(seq in form for seq in ['GGP', 'PGG', 'GPG']):
        return 'Buena'
    elif any(seq in form for seq in ['GEE', 'EGE', 'EEG', 'GPE', 'GEP', 'EPG', 'EGP', 'PGE', 'PEG']):
        return 'Regular'
    elif any(seq in form for seq in ['PPP', 'EPP', 'PEP','PPE']):
        return 'Mala'
    else:
        return 'Irregular'