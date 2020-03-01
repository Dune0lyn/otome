# Déclarez les personnages utilisés dans le jeu.
define e = Character('Ezra', color="#4F8AD5")
define l = Character('Leith', color="#569578")
define j = Character('[name]', color="#ffff80")

label start:
    
    scene bg base
    with dissolve
    
    "C'est parti, on se lance et on sait pas trop comment ça fonctionne."
    
    "Mais bon ... ça va le faire."
    
    show mec trop choqué
    with dissolve

    e "Bonjour, ceci est un test."
    
    hide mec trop choqué
    with dissolve
    show leith trop bg
    with dissolve
    
    l "On espère que ce sera pas trop compliqué."
    
    hide leith trop bg
    with dissolve
    show mec trop choqué
    with dissolve
    
    e "Mais non, t'inquiètes !"
    
    hide mec trop choqué
    with dissolve
    show leith trop bg
    with dissolve
    
    l "On fait coucou à Dune svp."
    
    "COUCOU DUNE !"
    
    play music "bensound-funnysong.mp3"
    
    scene bg dehors
    with dissolve
    show leith trop bg
    with dissolve
    
    l "On va pouvoir commencer les choses sérieuses."
    
    menu:
        "Il me fixe, avec une rare intensité."
        "Je lui souris, tout en le regardant fixement.":
            jump regard1
        "Je rougis jusqu'aux oreilles en détournant la tête...":
            jump rouge1

label regard1:
    l "Tu as l'air sûre de toi, allons-y maintenant !"
jump start2    

label rouge1:
    l "Tu es plutôt mignonne comme ça, n'ai pas peur, je ne vais pas te manger."    
    
label start2:
    "Il est peut-être temps de nous donner ton prénom, tu ne penses pas ?"
    $ j = renpy.input("Du coup ton prénom à toi c'est :", "", length=15) or "Jolie fille"
    l "C'est joli, j'aime bien."
    l "Tu vois, [j], on avance !"
    j "Je suis d'accord, on fait quoi maintenant ?"
    l "Maintenant ... on arrête cette horrible musique."
    stop music
    l "C'est mieux tu trouves pas ?"
    
    scene black
    with dissolve

    return
