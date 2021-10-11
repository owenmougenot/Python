x = int(input("x : "))  # je demande les valeurs 
y = int(input("y : "))
print(f"x vaut {x} et y vaut {y}")  # j'affiche les valeurs 
tmp = x  # j'echange les valeurs 
x = y
y = tmp
print(f"x vaut {x} et y vaut {y}")  # j'affiche les valeurs une fois changer 