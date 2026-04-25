import os
import re

def parsear_archivo(ruta):
    """
    Extrae los datos de un archivo .txt.
    Retorna un diccionario con 'grupos' (IDs y signos), 'fases' (listas de países) y 'goleador'.
    """
    datos = {'grupos': {}, 'fases': {}, 'goleador': ''}
    
    if not os.path.exists(ruta):
        return datos

    with open(ruta, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        for linea in lineas:
            linea = linea.strip()
            
            # 1. Extraer 1, X, 2 de la fase de grupos
            if 'Partid_' in linea and ':' in linea:
                # Separamos por ',' para el ID y por ':' para el resultado
                id_partido = linea.split(',')[0].strip()
                resultado = linea.split(':')[-1].strip().upper()
                if resultado in ['1', 'X', '2']:
                    datos['grupos'][id_partido] = resultado
            
            # 2. Extraer listas de países de las fases eliminatorias
            for fase in ['8vos', '4tos', 'Semis', 'Final', 'CAMPEÓN', 'LÍDER GOLEADOR']:
                if fase + ':' in linea or fase in linea:
                    if ':' in linea:
                        contenido = linea.split(':')[-1].strip()
                        # Limpiamos espacios y pasamos a minúsculas para comparar fácil
                        if ',' in contenido:
                            lista = [p.strip().lower() for p in contenido.split(',')]
                        else:
                            lista = [contenido.strip().lower()]
                        
                        if 'GOLEADOR' in fase:
                            datos['goleador'] = lista[0]
                        elif 'CAMPEÓN' in fase:
                            datos['fases']['CAMPEÓN'] = lista
                        else:
                            datos['fases'][fase] = lista
    return datos

def calcular_puntuacion_total(real, pred):
    puntos = 0
    
    # 1. Puntos Grupos: 1 pto por acierto (1X2)
    for p_id, signo_real in real['grupos'].items():
        if p_id in pred['grupos'] and pred['grupos'][p_id] == signo_real:
            puntos += 1
            
    # 2. Puntos por fases eliminatorias (por país acertado)
    config_puntos = {
        '8vos': 2,
        '4tos': 3,
        'Semis': 4,
        'Final': 5,
        'CAMPEÓN': 10
    }
    
    for fase, valor in config_puntos.items():
        if fase in real['fases'] and fase in pred['fases']:
            # Comparamos cuántos países de la predicción están en la lista real
            for pais in pred['fases'][fase]:
                if pais != '' and pais in real['fases'][fase]:
                    puntos += valor

    # 3. Punto Goleador: 5 ptos
    if real['goleador'] != '' and real['goleador'] == pred['goleador']:
        puntos += 5
        
    return puntos

def generar_ranking():
    ruta_real = 'data/resultados_reales_oficiales.txt'
    
    if not os.path.exists(ruta_real):
        return print(f"Error: No existe el archivo {ruta_real}")

    # Cargamos la verdad absoluta
    real = parsear_archivo(ruta_real)
    ranking_final = {}
    
    # Procesamos a los amigos
    folder_preds = 'data/predicciones/'
    for file in os.listdir(folder_preds):
        if file.endswith(".txt") and file != "plantilla.txt":
            nombre_amigo = file.replace(".txt", "").upper()
            pred_amigo = parsear_archivo(os.path.join(folder_preds, file))
            
            puntos_totales = calcular_puntuacion_total(real, pred_amigo)
            ranking_final[nombre_amigo] = puntos_totales

    # Imprimir resultados
    print("\n🏆 CLASIFICACIÓN DE LA PORRA MUNDIAL 2026 🏆")
    print("-" * 45)
    print(f"{'NOMBRE':<20} | {'PUNTOS':<10}")
    print("-" * 45)
    
    sorted_ranking = sorted(ranking_final.items(), key=lambda x: x[1], reverse=True)
    for nombre, pts in sorted_ranking:
        print(f"{nombre:<20} | {pts} puntos")

if __name__ == "__main__":
    generar_ranking()