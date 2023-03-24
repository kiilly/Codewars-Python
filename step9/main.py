def tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature[:n]
# La fonction utilise une boucle pour ajouter des termes à la liste signature 
# en calculant la somme des trois derniers termes à chaque itération
# la fonction retourne les n premiers termes de la liste signature