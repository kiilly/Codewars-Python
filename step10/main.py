def score(dice):
    score = 0
    counts = [0] * 6
    
    for value in dice:
        counts[value - 1] += 1
        
    for i in range(6):
        if counts[i] >= 3:
            if i == 0:
                score += 1000
            else:
                score += (i + 1) * 100
            counts[i] -= 3
        
    score += counts[0] * 100
    score += counts[4] * 50
    
    return score

# le code compte le nombre d'occurrences de chaque valeur du dé 
# et cherche des combinaisons de trois puis calcule le score en fonction 
# des règles et return le score final



