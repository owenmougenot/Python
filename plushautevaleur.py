x =int(input("valeur1: "))  # je recupere mes valeur  
y =int(input("valeur2: "))
i =int(input("valeur3: "))
if x<y and y<i:  # je compare les valuer et si c'est x,y < i donc i est la plus plus haute valeurs
    print(f"la valeur la plus haute est {i}")  # je repond que i les la plus haute valeurs
elif x<i and i<y:  # si x et i < y donc y est la valeur la plus haute
    print(f"la valeur la plus haut est {y}")  # je repond que i les la plus haute valeurs
elif y<i and i<x:  # si y et i sont < a x donc x est la plus haute valeur
    print(f"la valeur la plus haute est {x}")  # j'affiche la reponse 