# Consigne : Rechercher le nombre d'occurence du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

# Solution
print(texte)
print("Le nombre d'occurence du mot 'exemple' est : ", texte.count("exemple"))
texte = texte.replace('est', 'représente')
print(texte[::-1])
