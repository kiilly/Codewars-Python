def shortcut( s ):
    # ...
    vowels = ['a','e','i','o','u']
    s = [letter for letter in s if letter not in vowels]
    s = ''.join(s)
    return(s)

# j'ai initialiser une liste de voyelles en muniscules ensuite j'utilise une liste en compréhension pour créer une nouvelle liste "s" 
# où chaque lettre de la chaîne originale qui n'est pas une voyelle est ajoutée qui en meme temps exclu les voyelles
# j'utilise la méthode "join()" pour combiner tous les éléments de la liste "s" en une chaîne unique, qui est ensuite stockée dans la variable "s"
# pour la return sur la derniere ligne de ce code 