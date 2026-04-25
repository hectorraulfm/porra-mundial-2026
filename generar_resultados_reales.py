import json
import os

def crear_archivo_resultados():
    ruta_json = 'data/worldcup.json'
    ruta_salida = 'data/resultados_reales_oficiales.txt'

    if not os.path.exists(ruta_json):
        print(f"Error: No se encuentra {ruta_json}")
        return

    with open(ruta_json, 'r', encoding='utf-8') as f:
        data = json.load(f)

    matches = []
    if 'rounds' in data:
        for r in data['rounds']:
            matches.extend(r.get('matches', []))
    elif 'matches' in data:
        matches = data['matches']

    with open(ruta_salida, 'w', encoding='utf-8') as p:
        p.write("RESULTADOS REALES DEL MUNDIAL 2026\n")
        p.write("==================================\n\n")
        p.write("--- FASE DE GRUPOS (Escribe 1, X o 2) ---\n")
        
        for i, match in enumerate(matches, 1):
            num = match.get('num', i)
            if num <= 72:
                # Aquí no necesitamos traducción, es solo para tu referencia
                t1 = match.get('team1', {}).get('name', 'TBD') if isinstance(match.get('team1'), dict) else match.get('team1', 'TBD')
                t2 = match.get('team2', {}).get('name', 'TBD') if isinstance(match.get('team2'), dict) else match.get('team2', 'TBD')
                p.write(f"Partid_{num:03}, {t1} vs {t2}: \n")

        p.write("\n--- FASE ELIMINATORIA (Escribe los países que clasificaron de verdad) ---\n")
        p.write("8vos: \n")
        p.write("4tos: \n")
        p.write("Semis: \n")
        p.write("Final: \n")
        p.write("CAMPEÓN: \n\n")
        
        p.write("LÍDER GOLEADOR: \n")

    print(f"✅ Archivo de resultados reales generado en {ruta_salida}")

if __name__ == "__main__":
    crear_archivo_resultados()