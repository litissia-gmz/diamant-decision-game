import random
from typing import List, Dict, Set, Tuple

# Constantes du jeu
MIN_JOUEURS = 3
MAX_JOUEURS = 8
NB_MANCHES = 5

CARTES_TRESOR = ["1", "2", "3", "4", "5", "5", "7", "7", "9", "11", "11", "13", "14", "15", "17"]
CARTES_PIEGES = ["serpents", "boulets", "pics", "araignées", "lave"]
RELICS = ["R_5", "R_7", "R_8", "R_10", "R_12"]

class Joueur:
    def __init__(self, id_joueur: int, nb_manches: int):
        self.id = id_joueur
        self.coffre = [0] * nb_manches
        self.sac = 0
        self.est_actif = True
    
    def __str__(self):
        return f"Joueur {self.id}: Coffre={self.coffre}, Sac={self.sac}, Actif={self.est_actif}"

class JeuDiamant:
    def __init__(self):
        self.joueurs: List[Joueur] = []
        self.nb_manches = NB_MANCHES
        self.initialiser_jeu()
    
    def initialiser_jeu(self):
        """Initialise le jeu en demandant le nombre de joueurs et créant les instances Joueur"""
        nb_joueurs = self.demander_nombre_joueurs()
        self.joueurs = [Joueur(i+1, self.nb_manches) for i in range(nb_joueurs)]
    
    @staticmethod
    def demander_nombre_joueurs() -> int:
        """Demande le nombre de joueurs avec validation"""
        while True:
            try:
                nb = int(input(f"Combien de joueurs ? (entre {MIN_JOUEURS} et {MAX_JOUEURS}) : "))
                if MIN_JOUEURS <= nb <= MAX_JOUEURS:
                    print(f"Nombre de joueurs accepté : {nb}")
                    return nb
                print(f"Le jeu Diamant se joue entre {MIN_JOUEURS} et {MAX_JOUEURS} joueurs.")
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")
    
    def preparer_manche(self, manche: int) -> Tuple[List[str], Set[str]]:
        """Prépare le deck de cartes pour la manche et les pièges vus"""
        cartes = CARTES_TRESOR * 3 + CARTES_PIEGES * 3
        if manche < len(RELICS):
            cartes.append(RELICS[manche])
        random.shuffle(cartes)
        return cartes, set()
    
    def strategie_sortie(self, joueur: Joueur, defausse: List[str], manche: int) -> bool:
        """Stratégie décidant si un joueur doit quitter la mine"""
        nb_pieges_vus = sum(1 for carte in defausse if carte in CARTES_PIEGES)
        rubis_sac = joueur.sac
        nb_actifs = sum(1 for j in self.joueurs if j.est_actif)
        
        if manche < 2:  # Manches précoces
            if rubis_sac >= 12:
                return True
            elif rubis_sac >= 8:
                return nb_pieges_vus >= 2 or random.random() < 0.6
        elif manche < 4:  # Manches intermédiaires
            if rubis_sac >= 15:
                return True
            elif rubis_sac >= 10:
                return nb_pieges_vus > 0 or random.random() < 0.4
        else:  # Manches tardives
            if rubis_sac >= 20:
                return True
            elif rubis_sac >= 15:
                return nb_pieges_vus > 0 or random.random() < 0.3
            elif rubis_sac >= 10:
                return random.random() < 0.5
        return False
    
    def initialiser_manche(self, defausse: List[str], cartes: List[str], manche: int) -> Tuple[List[Joueur], List[int]]:
        """Détermine quels joueurs restent dans la mine"""
        actifs = []
        sortants = []
        
        for joueur in self.joueurs:
            if self.strategie_sortie(joueur, defausse, manche):
                joueur.est_actif = False
                sortants.append(joueur.id)
            else:
                joueur.est_actif = True
                actifs.append(joueur)
        
        return actifs, sortants
    
    def gerer_carte(self, carte: str, actifs: List[Joueur], pieges_vus: Set[str]) -> Tuple[int, int, bool]:
        """Gère l'effet d'une carte tirée"""
        rubis_ajoutes = 0
        val_relique = 0
        fin_manche = False
        
        if carte.isdigit():
            valeur = int(carte)
            part = valeur // len(actifs)
            reste = valeur % len(actifs)
            for j in actifs:
                j.sac += part
            rubis_ajoutes = reste
        
        elif carte in CARTES_PIEGES:
            if carte in pieges_vus:
                print(f"Deuxième piège {carte} ! Les joueurs actifs perdent tout.")
                for j in actifs:
                    j.sac = 0
                fin_manche = True
            else:
                pieges_vus.add(carte)
        
        elif carte.startswith("R"):
            print(f"Une relique est trouvée : {carte}")
            val_relique = int(carte.split("_")[1])
        
        return rubis_ajoutes, val_relique, fin_manche
    
    def jouer_manche(self, manche: int):
        """Joue une manche complète du jeu"""
        print(f"\n=== Début de la manche {manche+1} ===")
        
        cartes, pieges_vus = self.preparer_manche(manche)
        defausse = []
        rubis_au_sol = 0
        val_relique = 0
        
        actifs, sortants = self.initialiser_manche(defausse, cartes, manche)
        print(f"Joueurs actifs: {[j.id for j in actifs]}")
        
        while cartes and actifs and not (len(pieges_vus) >= 2 and any(c in defausse[-2:] for c in pieges_vus)):
            carte = cartes.pop(0)
            defausse.append(carte)
            print(f"\nCarte tirée: {carte}")
            
            rubis, relique, fin = self.gerer_carte(carte, actifs, pieges_vus)
            rubis_au_sol += rubis
            val_relique = max(val_relique, relique)
            
            if fin:
                break
            
            print(f"État actuel - Rubis au sol: {rubis_au_sol}, Pièges vus: {pieges_vus}")
            for j in actifs:
                print(f"  Joueur {j.id}: {j.sac} rubis")
        
        self.fin_manche(manche, actifs, sortants, rubis_au_sol, val_relique)
    
    def fin_manche(self, manche: int, actifs: List[Joueur], sortants: List[int], rubis_au_sol: int, val_relique: int):
        """Finalise une manche et attribue les gains"""
        # Distribuer les rubis restants
        if actifs and rubis_au_sol > 0:
            part = rubis_au_sol // len(actifs)
            for j in actifs:
                j.sac += part
        
        # Attribuer la relique si un seul joueur est sorti
        if len(sortants) == 1:
            joueur_id = sortants[0]
            for j in self.joueurs:
                if j.id == joueur_id:
                    j.coffre[manche] += val_relique
        
        # Mettre à jour les coffres
        for j in self.joueurs:
            if not j.est_actif or not actifs:  # Ceux qui sont sortis ou tous si fin de manche
                j.coffre[manche] = j.sac
            j.sac = 0
            j.est_actif = True  # Réactiver pour la prochaine manche
        
        # Afficher les résultats
        print(f"\nRésultats après la manche {manche + 1}:")
        for j in self.joueurs:
            print(f"Joueur {j.id}: Coffre={j.coffre}")
    
    def afficher_resultats(self):
        """Affiche les résultats finaux du jeu"""
        print("\n= RESULTATS FINAUX =")
        scores = []
        
        for joueur in self.joueurs:
            total = sum(joueur.coffre)
            print(f"Joueur {joueur.id}:")
            print(f"  Gains par manche: {joueur.coffre}")
            print(f"  SCORE FINAL: {total}\n")
            scores.append((joueur.id, total))
        
        meilleur_score = max(score for _, score in scores)
        gagnants = [id_j for id_j, score in scores if score == meilleur_score]
        
        if len(gagnants) == 1:
            print(f"Le gagnant est le joueur {gagnants[0]} avec {meilleur_score} points !")
        else:
            print(f"Égalité entre les joueurs {', '.join(map(str, gagnants))} avec {meilleur_score} points chacun !")
    
    def jouer(self):
        """Lance le jeu complet"""
        for manche in range(self.nb_manches):
            self.jouer_manche(manche)
        self.afficher_resultats()

if __name__ == "__main__":
    jeu = JeuDiamant()
    jeu.jouer()
