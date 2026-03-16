def startegie_litissia(joueur, cartes_restantes, pieges_vus, manche, joueurs):
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

    