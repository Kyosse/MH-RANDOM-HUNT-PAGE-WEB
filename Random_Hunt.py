# -*- coding: utf-8 -*-

from random import randint
from browser import html, document



def randomHunt(ev):    
    """
    
    Fonction qui permet générer aléatoirement une chasse selon différentes
    conditions (pour toujours plus de fun).

    Entrée : rien
    Sortie : tirage aléatoire d'une arme, d'un monstre et d'une condition de chasse.

    """
    
    liste_armes = ["Grande épée", "Epée Longue", "Epée & Bouclier", 
                "Doubles Lames", "Marteau", "Cor de Chasse", "Lance",
                "Lance-Canon", "Morpho-Hache", "Volto-Hache", "Insectoglaive", 
                "Fusarbalète Léger", "Fusarbalète Lourd", "Arc"]


    game = document["meta-web-site"].value
        
    if game == "MH_4_Ultimate":
        liste_monstres = ["Akantor", "Basarios", "Basarios Rubis", "Brachydios",
                        "Brachysios Tempête", "Cephadrome", "Chameleos",
                        "Congalala", "Congalala Emeraude", "Dah'Ren Moran",
                        "Dalamadur", "Dalamadur Shah", "Deviljho", "Deviljho Apex",
                        "Deviljho Carnage", "Diablos", "Diablos Apex", "Diablos Noire",
                        "Fatalis", "Fatalis Blanc", "Fatalis Pourpre",
                        "Gendrome", "Gogmazios", "Gore Magala", "Gore Magala du Chaos",
                        "Grand Jaggi", "Gravios", "Gravios Apex", "Gravios Onyx",
                        "Gypcéros","Gypcéros Améthyste", "Hermitaur Daimyo",
                        "Hermitaur Daimyo Prune", "Iodrome", "Kecha Wacha",
                        "Kecha Wacha Blanc", "Khezu", "Khezu Grenat", "Kirin",
                        "Kirin Oroshi", "Kushala Daora", "Kushala Daora Rouillé",
                        "Lagombi", "Monoblos", "Monoblos Ivoire", "Najarala",
                        "Najarala du Déluge", "Najara du Déluge Apex", "Nerscylla",
                        "Nerscylla Spectrale", "Rajang", "Rajang Apex", "Rajang Orage",
                        "Rathalos", "Rathalos Azur", "Rathalos d'Argent",
                        "Rathian", "Rathian d'Or", "Rathian Sakura", "Reine Seltas",
                        "Reine Seltas du Désert","Seltas", "Seltas du Désert",
                        "Seregios", "Seregios Apex", "Shagaru Magala", "Teostra",
                        "Tetsucabra", "Tetsucabra Féroce", "Tigrex", "Tigrex Apex",
                        "Tigrex Berserk", "Tigrex Magma", "Ukanlos", "Velocidrome",
                        "Yian Garuga", "Yian Kut-Ku", "Yian Kut-Ku Bleu", "Zamtrios",
                        "Zamtrios Tigré", "Zinogre", "Zinogre Apex", "Zinogre Stygien"]
        liste_handicaps = ["sans inventaire", "sans soins", "sans armures", 
                        "avec une arme débutante", "avec une armure débutante",
                        "sans wyvpierre", "sans esquives", "sans wyvern riding",
                        "avec 50% d'HP", "sans attaquer le monstre quand il est au sol",
                        "sans bouclier ou contre", "sans munitions spéciales",
                        "sans manger", "sans gadgets", "sans guérison de statut",
                        "sans palicot", "le monstre est en mode Out-Break"]
    elif game == "MH_Generations_Ultimate":
        liste_armes.append("Miaroudeur")
        liste_monstres = ["Agnaktor", "Ahtal-Ka", "Akantor", "Alatreon", "Amatsu",
                        "Arzuros", "Arzuros Crâne-Ardent", "Astalos",
                        "Astalos Prince-Orage", "Barioth", "Barroth", "Basarios",
                        "Blangonga", "Brachydios", "Brachydios Tempête", "Bulldrome",
                        "Ceanataur Brise-Os", "Ceanataur Shogun", "Cephadrome",
                        "Chameleos", "Deviljho", "Deviljho Carnage", "Diablos",
                        "Diablos Bain-de-Sang", "Duramboros", "Fatalis",
                        "Fatalis Ancien", "Fatalis Pourpre", "Gammoth",
                        "Gammoth Givre-Ancien", "Gendrome", "Giadrome", "Glavenus",
                        "Glavenus Lame-Chaos", "Gore Magala", "Gore Magala du Chaos",
                        "Grand Maccao", "Gravios", "Gypceros", "Hermitaur Daimyo",
                        "Hermitaur Poing-Fer", "Iodrome", "Kecha Wacha", "Khezu",
                        "Kirin", "Kushala Daora", "Lagiacrus", "Lagombi",
                        "Lagombi Maître-Neige", "Lao-Shan Lung", "Lavasioth",
                        "Ludroth Royal", "Malfestio", "Malfestio Lune-Noir",
                        "Mizutsune", "Mizutsune Perce-âme", "Najarala", "Nakarkos",
                        "Nargacuga", "Nargacuga Vent-Acier", "Nerscylla", "Nibelsnarf",
                        "Plesioth", "Rajang", "Rajang Orage", "Rathalos",
                        "Rathalos Roi-Enfer", "Rathalos d'Argent", "Rathian",
                        "Rathian Reine-Poison", "Rathian d'Or", "Reine Seltas",
                        "Seltas", "Seregios", "Shagaru Magala", "Teostra",
                        "Tetsucabra", "Tetsucabra Brise-Roc", "Tigrex",
                        "Tigrex Griffe-Sombre", "Ukanlos", "Uragaan",
                        "Uragaan Roi-Cristal", "Valstrax", "Velocidrome", "Volvidon",
                        "Yian Garuga", "Yian Garuga Oeil-Mort", "Yian Kut-Ku",
                        "Zamtrios", "Zinogre", "Zinogre Feu-du-Ciel"]
        liste_handicaps = ["sans inventaire", "sans soins", "sans armures", 
                        "avec une arme débutante", "avec une armure débutante",
                        "sans arts de chasse", "en guilde", "en guerrier", 
                        "en bushido", "en voltigeur", "en vaillant", "en alchimiste",
                        "sans esquives", "sans wyvern riding", "avec 50% d'HP", 
                        "sans attaquer le monstre quand il est au sol",
                        "sans bouclier ou contre", "sans munitions spéciales",
                        "sans manger", "sans gadgets", "sans guérison de statut",
                        "sans palicot", "le monstre est en mode hyper",
                        "Sans huiles",]
    elif game == "MH_Rise":
        liste_monstres = ["Aknosom", "Almudron", "Anjanath", "Arzuros",
                        "Arzuros Apex", "Barioth", "Barroth", "Basarios", 
                        "Bazelgeuse", "Bishaten", "Chameleos", "Diablos",
                        "Diablos Apex", "Goss Harrag", "Grand Baggi",
                        "Grand Izuchi", "Grand Wroggi", "Ibushi du Vent",
                        "Jyuratodus", "Khezu", "Kulu-Ya-Ku", "Kushala Daora", 
                        "Lagombi", "Ludroth Royal", "Magnamalo","Mizutsune",
                        "Mizutsune Apex", "Nargacuga", "Narwa du Tonnerre",
                        "Pukei-Pukei", "Rajang", "Rakna-Kadaki", "Rathalos",
                        "Rathalos Apex", "Rathian", "Rathian Apex", "Somnacanthe",
                        "Teostra", "Tétranodon", "Tigrex", "Tobi-Kadachi", "Volvidon",
                        "Zinogre"]
        liste_handicaps = ["sans inventaire", "sans soins", "sans armures", 
                        "avec une arme débutante", "avec une armure débutante",
                        "sans filoptère", "avec d'autres switch skills",
                        "sans esquives", "sans wyvern riding", "avec 50% d'HP", 
                        "sans attaquer le monstre quand il est au sol",
                        "sans bouclier ou contre", "sans munitions spéciales",
                        "sans manger", "sans gadgets", "sans guérison de statut",
                        "sans pilpoils ou palicot"]
    else:
        liste_monstres = ["Alatreon", "Anjanath", "Anjanath tonnerre","Banbaro",
                        "Barioth", "Barioth Crocgivre", "Barroth",
                        "Bazelgeuse", "Bazelgeuse Vulcan", "Beotodus",
                        "Brachydios", "Brachydios Tempête", "Béhémoth",
                        "Deviljho", "Deviljho Carnage", "Diablos",
                        "Diablos noire", "Dodogama", "Fatalis", "Glavenus",
                        "Glavenus Acide", "Grand Girros", "Grand Jagras",
                        "Jyuratodus", "Kirin", "Kulu-Ya-Ku", "Kulve Taroth",
                        "Kushala Daora", "Lavasioth", "Legiana",
                        "Legiana Blizzard", "Leshen", "Lunastra", "Namielle",
                        "Nargacuga", "Nergigante", "Nergigante Chaos",
                        "Odogaron", "Odogaron Désastre", "Paolumu",
                        "Paolumu Belladone", "Pukei-Pukei",
                        "Pukei-Pukei Corail", "Radobaan", "Rajang",
                        "Rajang Orage", "Rathalos", "Rathalos Azur",
                        "Rathalos d'Argent", "Rathian d'Or", "Rathian Sakura",
                        "Safi'Jiiva", "Shara Ishvalda", "Teostra", "Tigrex",
                        "Tigrex Berserk", "Tobi-Kadachi",
                        "Tobi-Kadachi Vipère", "Tzitzi-Ya-Ku", "Uragaan",
                        "Vaal Hazak", "Vaal Hazak Fléau", "Velkhana",
                        "Vieux Leshen", "Xeno'Jiiva", "Yian Garuga",
                        "Yian Garuga Balafré", "Zinogre", "Zinogre Stygien",
                        "Zorah Magdaros"]
        liste_handicaps = ["sans inventaire", "sans soins", "sans armures", 
                        "avec une arme débutante", "avec une armure débutante",
                        "sans grappin", "sans fronde", "sans esquives",
                        "sans wyvern riding", "avec 50% d'HP", 
                        "sans attaquer le monstre quand il est au sol",
                        "sans bouclier ou contre", "sans munitions spéciales",
                        "sans manger", "sans gadgets (pièges,bombes etc...)",
                        "sans guérison de statut", "sans palicot",
                        "Sans utilisation du territoire"]
    
    

    arme = liste_armes[randint(0, len(liste_armes) - 1)]
    document['condition-arme-txt'].textContent = arme
    arme = arme.replace(' ', '_')
    arme = "Image/Icon/Icon_Armes/" + arme + ".png"
    document['content-condition-arme-img'].clear()
    document['content-condition-arme-img'] <= html.IMG(src=arme, height=200)

    monstre = liste_monstres[randint(0, len(liste_monstres) - 1)]
    document['condition-monstre-txt'].textContent = monstre
    monstre = monstre.replace(' ', '_')
    monstre = "Image/Icon/Icon_Monstres/" + monstre + ".png"
    document['content-condition-monstre-img'].clear()
    document['content-condition-monstre-img'] <= html.IMG(src=monstre, height=100)

    handicap = liste_handicaps[randint(0, len(liste_handicaps) - 1)]
    document['condition-handicap-txt'].textContent = handicap




document['content-button-random'].bind("click", randomHunt)