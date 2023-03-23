def square_digits(num):
    x = ''
    for y in str(num):
     x = x + str((int(y))**2)
    return int(x) 

# en utilisant une boucle "for" et en le convertissant en une chaîne de caractères à l'aide de la fonction "str"
# Pour chaque chiffre, le code calcule le carré du chiffre en utilisant la fonction "**2" et le convertit à nouveau en chaîne de caractères en utilisant "str".
# Le chiffre carré est ensuite ajouté à une chaîne vide appelée "x" en utilisant l'opérateur de concaténation "+".
# la fonction renvoie la valeur entiere de la chaine "x" en utilisant la fonction "int", ce qui donne le nombre obtenu en remplaçant chaque chiffre par son carré.