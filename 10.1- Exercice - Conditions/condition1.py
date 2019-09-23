# Problème : Etant donné deux variables c et d, on veut savoir si leur produit est négatif ou positif ou nul.
# Contrainte : Ne pas calculer le produit des deux nombres.
# Résultat attendu : Un message affichant "Produit positif" ou "Produit négatif" ou "Produit nul".
# Indication : Vous pouvez changer les valeurs des variables pour vos tests.
c = 42
d = 31

# Solution
if (c == 0) or (d == 0):
    print("Produit nul")
elif (c > 0 and d > 0) or (c < 0 and d < 0):
    print("Produit positif")
else:
    print("Produit négatif")
