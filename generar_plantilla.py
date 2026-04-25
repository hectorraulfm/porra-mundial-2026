import json
import os

TRADUCCION = {
    "Mexico": "México", "South Africa": "Sudáfrica", "South Korea": "Corea del Sur",
    "Czech Republic": "República Checa", "Canada": "Canadá", "Bosnia & Herzegovina": "Bosnia y Herzegovina",
    "Qatar": "Catar", "Switzerland": "Suiza", "Brazil": "Brasil", "Morocco": "Marruecos",
    "Haiti": "Haití", "Scotland": "Escocia", "USA": "EE.UU.", "Paraguay": "Paraguay",
    "Australia": "Australia", "Turkey": "Turquía", "Germany": "Alemania", "Curaçao": "Curazao",
    "Ivory Coast": "Costa de Marfil", "Ecuador": "Ecuador", "Netherlands": "Países Bajos",
    "Japan": "Japón", "Sweden": "Suecia", "Tunisia": "Túnez", "Belgium": "Bélgica",
    "Egypt": "Egipto", "Iran": "Irán", "New Zealand": "Nueva Zelanda", "Spain": "España",
    "Cape Verde": "Cabo Verde", "Saudi Arabia": "Arabia Saudí", "Uruguay": "Uruguay",
    "France": "Francia", "Senegal": "Senegal", "Iraq": "Irak", "Norway": "Noruega",
    "Argentina": "Argentina", "Algeria": "Argelia", "Austria": "Austria", "Jordan": "Jordania",
    "Portugal": "Portugal", "DR Congo": "R.D. del Congo", "Uzbekistan": "Uzbekistán",
    "Colombia": "Colombia", "England": "Inglaterra", "Croatia": "Croacia", "Ghana": "Ghana",
    "Panama": "Panamá"
}

def traducir(nombre):
    return TRADUCCION.get(nombre, nombre)

def crear_plantilla():
    ruta_json = 'data/worldcup.json'
    ruta_plantilla = 'data/plantilla.txt'

    with open(ruta_json, 'r', encoding='utf-8') as f:
        data = json.load(f)

    matches = []
    if 'rounds' in data:
        for r in data['rounds']:
            matches.extend(r.get('matches', []))
    elif 'matches' in data:
        matches = data['matches']

    with open(ruta_plantilla, 'w', encoding='utf-8') as p:
        p.write("🏆 PORRA MUNDIAL 2026 🏆\n")
        p.write("========================\n\n")
        
        # --- BLOQUE DE SISTEMA DE PUNTOS ---
        p.write("📜 SISTEMA DE PUNTUACIÓN:\n")
        p.write("- Fase de Grupos: 1 punto por cada acierto (1, X, 2).\n")
        p.write("- Octavos de Final: 2 puntos por cada país acertado.\n")
        p.write("- Cuartos de Final: 3 puntos por cada país acertado.\n")
        p.write("- Semifinales: 4 puntos por cada país acertado.\n")
        p.write("- Finalistas: 5 puntos por cada país acertado.\n")
        p.write("- Campeón: 10 puntos por acertar el ganador.\n")
        p.write("- Líder Goleador: 5 puntos.\n")
        p.write("--------------------------------------------------\n\n")
        
        p.write("NOMBRE: [TU NOMBRE]\n\n")
        p.write("INSTRUCCIONES FASE GRUPOS:\n")
        p.write("Escribe 1 (Local), X (Empate) o 2 (Visitante) después de los dos puntos.\n\n")

        p.write("--- FASE DE GRUPOS ---\n")
        for i, match in enumerate(matches, 1):
            num = match.get('num', i)
            # Solo los 72 partidos de fase de grupos
            if num <= 72:
                t1 = traducir(match.get('team1', {}).get('name', 'TBD') if isinstance(match.get('team1'), dict) else match.get('team1', 'TBD'))
                t2 = traducir(match.get('team2', {}).get('name', 'TBD') if isinstance(match.get('team2'), dict) else match.get('team2', 'TBD'))
                p.write(f"Partid_{num:03}, {t1} vs {t2}: \n")

        p.write("\n--- FASE ELIMINATORIA (Escribe los países que clasifican) ---\n")
        p.write("8vos (Escribe 16 países separados por comas): \n")
        p.write("4tos (Escribe 8 países separados por comas): \n")
        p.write("Semis (Escribe 4 países separados por comas): \n")
        p.write("Final (Escribe 2 países separados por comas): \n")
        p.write("CAMPEÓN: \n\n")
        
        p.write("LÍDER GOLEADOR: \n")

    print(f"✅ Plantilla actualizada generada en {ruta_plantilla}")

if __name__ == "__main__":
    crear_plantilla()