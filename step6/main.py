def is_triangle(a, b, c):
    
    if (a + b > c) and (c + a > b) and (b + c > a):
        return True
    else:
        return False
    

# sur cette exercise j'ai utiliser la fonction is triangle qui prend en entrée trois nombres (a,b et c) qui represent les longueurs des côtés d'un triangle
# sur ce code j'utilise une conditionnelle "if" pour vérifier si la somme de deux côtés est strictement supérieure au troisième côté, ce qui est une condition nécessaire pour qu'un triangle puisse être formé
# si il s'avère que cette condition est vrai pour tout les côtés la fonction renvoie true (vrai) si c'est pas le cas elle envoie false (faux)