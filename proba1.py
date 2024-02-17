import random

urne=["r","j","j","v","v","v","v"]
count_r=[]
count_j=[]
count_r_apres_v=[]
count_autre_apres_v=[]


def proba(tentatives):
    y=tentatives
    points = 0
    while tentatives>0:
        choix=random.choice(urne)
        if(choix=="r"):
            count_r.append(choix)
            points+=10
            tentatives-=1
        elif(choix=="j"):
            count_j.append(choix)
            points-=10
            tentatives-=1
        elif(choix=="v"):
            urne.remove(choix)
            choix2=random.choice(urne)
            if(choix2=="r"):
                count_r_apres_v.append(choix2)
                urne.append(choix)
                points+=8
                tentatives-=1
            else:
                count_autre_apres_v.append(choix2)
                urne.append(choix)
                points-=4
                tentatives-=1
    print(f"{points} points apres {y} tentatives")
    print(f"probabilité d'avoir une rouge dans {y} tentatives est {len(count_r) / y}")
    print(f"probabilité d'avoir une jaune dans {y} tentatives est {len(count_j) / y}")
    print(f"probabilité d'avoir une vert et apres une rouge dans {y} tentatives est {len(count_r_apres_v) / y}")
    print(f"probabilité d'avoir une vert et apres non rouge dans {y} tentatives est {len(count_autre_apres_v) / y}")

proba(10000000)
