def basic_op(operator, value1, value2):
    #your code here
    if operator == "+":
        result = value1 + value2
        return result
    elif operator == "-":
        result = value1 - value2
        return result
    elif operator == "*":
        result = value1 * value2
        return result
    elif operator == "/":
        result = value1 / value2
        return result
    
     #pour ce calcul j'ai mis des condition sur la variable operator si operator par exemple = "+" il return la valeur1 + la valeur2 