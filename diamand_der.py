import random

def demander_nombre_joueurs():
    while True:
        try:
            nb = int(input("Combien de joueurs ? (entre 3 et 8) : "))
            if 3 <= nb <= 8:
                print(f"Nombre de joueurs accepté : {nb}")
                return nb
            else:
                print("Le jeu Diamant se joue entre 3 et 8 joueurs.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

def initialiser(nb_joueurs, nb_manches):
    return [{"id": i, "coffre": [0]*nb_manches, "sac": 0, "is_active": True} for i in range(nb_joueurs)]

def decision(joueur, cartes_restantes, pieges_vus, manche, joueurs):
    rubis_sac = joueur["sac"]
    nb_actifs = sum(1 for j in joueurs if j["is_active"])
    nb_pieges_vus = len(pieges_vus)
    
    tres_dangereux = nb_pieges_vus >= 2
    peu_dangereux = nb_pieges_vus == 0
    
    if manche < 2:
        if rubis_sac >= 12:
            return True
        elif rubis_sac >= 8:
            if tres_dangereux:
                return True
            return random.random() < 0.6
        return False
            
    elif manche < 4:
        if rubis_sac >= 15:
            return True
        elif rubis_sac >= 10:
            if peu_dangereux:
                return random.random() < 0.4
            return random.random() < 0.7
        return False
            
    else:
        if rubis_sac >= 20:
            return True
        elif rubis_sac >= 15:
            if peu_dangereux:
                return random.random() < 0.3
            return random.random() < 0.8
        elif rubis_sac >= 10:
            return random.random() < 0.5
        return False

    

def init_manche(joueurs, cartes, pieges_vus, manche):
    
    actifs = []
    id_joueurs_sortant = []
    
    for joueur in joueurs:
        if decision(joueur, cartes, pieges_vus, manche, joueurs):
            joueur["sac"] = 0
            joueur["is_active"] = True
            actifs.append(joueur)
        else:
            joueur["is_active"] = False
            id_joueurs_sortant.append(joueur["id"])
    
    return  actifs, id_joueurs_sortant

def gerer_cartes(cartes, actifs, defausse, rubis_au_sol, pieges_vus):
    manche_en_cours = True
    val_relique = 0
    
    while manche_en_cours and cartes and actifs:
        carte = cartes.pop(0)
        defausse.append(carte)
        
        if carte.isdigit():
            valeur = int(carte)
            part = valeur // len(actifs)
            reste = valeur % len(actifs)
            for j in actifs:
                j["sac"] += part
            rubis_au_sol += reste
        elif carte in pieges_vus:
            print(f"Deuxième piège {carte} ! Les joueurs actifs perdent tout.")
            for j in actifs:
                j["sac"] = 0
            manche_en_cours = False
        elif carte in ["serpents", "boulets", "pics", "araignées", "lave"]:
            pieges_vus.add(carte)
        elif carte.startswith("R"):
            print(f"Une relique est trouvée : {carte}")
            val_relique = int(carte.split("_")[1])
    
    return rubis_au_sol, cartes, pieges_vus, val_relique, defausse

def fin_manche(joueurs, manche, rubis_au_sol, actifs, val_relique, id_joueurs_sortant):
    if len(id_joueurs_sortant) == 1:
        joueurs[id_joueurs_sortant[0]]["sac"] += val_relique
    
    if actifs and rubis_au_sol > 0:
        part = rubis_au_sol // len(actifs)
        for j in actifs:
            j["sac"] += part
    
    for j in joueurs:
        j["coffre"][manche] = j["sac"]
        j["sac"] = 0

def main():
    nb_manches = 5
    cartes = ["1", "2", "3", "4", "5", "5", "7", "7", "9", "11", "11", "13", "14", "15", "17",
              "serpents", "boulets", "pics", "araignées", "lave",
              "serpents", "boulets", "pics", "araignées", "lave",
              "serpents", "boulets", "pics", "araignées", "lave"]
    
    reliques = ["R_5", "R_7", "R_8", "R_10", "R_12"]


    nombre_joueurs = demander_nombre_joueurs()
    joueurs = initialiser(nombre_joueurs, nb_manches)
    
    cartes.append(reliques.pop(0))
    random.shuffle(cartes)

    pieges_vus = set()

    for manche in range(nb_manches):
        print(f"\n=== Début de la manche {manche+1} ===")

        defausse = []
        rubis_au_sol = 0

        
        
        actifs, id_joueurs_sortant = init_manche(joueurs, cartes, pieges_vus, manche)
        
        
        rubis_au_sol , cartes , pieges_vus , val_relique , defausse = gerer_cartes(
            cartes, actifs, defausse, rubis_au_sol, pieges_vus)
        
        fin_manche(joueurs, manche, rubis_au_sol, actifs, val_relique, id_joueurs_sortant)
        

        reliques = [r for r in reliques if r not in defausse]
        
        

        if reliques and manche < nb_manches - 1:
            cartes.append(reliques.pop(0))
            random.shuffle(cartes)

if __name__ == "__main__":
    main()