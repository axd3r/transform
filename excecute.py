import pandas as pd

# Cargar los datos
restaurants_df = pd.read_csv('restaurants.csv')
reviews_df = pd.read_csv('reviews.csv')

# Verificar las primeras filas de cada DataFrame para asegurar que las columnas son correctas
print(restaurants_df.head())
print(reviews_df.head())

# Unir los DataFrames en base al id del restaurante
merged_df = pd.merge(restaurants_df, reviews_df, left_on='id', right_on='service')

# Verificar los datos después de la unión
print(merged_df.head())

# Calcular el score promedio por restaurante
average_scores = merged_df.groupby('id')['score'].mean().reset_index()

# Renombrar la columna para claridad
average_scores.rename(columns={'score': 'average_score'}, inplace=True)

# Función para asignar una recomendación basada en el promedio del score
def get_recommendation(score):
    if score >= 4.5:
        return 'Restaurante 100% recomendado'
    elif score >= 4:
        return 'Restaurante recomendado'
    elif score >= 3:
        return 'Restaurante bueno'
    elif score >= 2:
        return 'Restaurante por mejorar'
    elif score >= 1:
        return 'Mucho por mejorar'
    else:
        return 'Restaurante no recomendado'

# Aplicar la función para agregar una columna con las recomendaciones
average_scores['recommendation'] = average_scores['average_score'].apply(get_recommendation)

# Mostrar todos los resultados
pd.set_option('display.max_rows', None)  # Muestra todas las filas
pd.set_option('display.max_columns', None)  # Muestra todas las columnas
print(average_scores)
