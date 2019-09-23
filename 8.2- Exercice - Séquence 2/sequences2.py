# Problème : Calculer le prix TTC d'une nombre d'article de prix unitaire donné. Avec une T.V.A à 7.7%.
# Données : Nombres d'articles et prix unitaire HT
# Résultat attendu : Un message "Le prix TTC est de XXX.XXX chf." Utilisez la fonction print().

nb_articles = 13
prix_ht = 42.75

# Solution
tva = 0.077
prix_ttc = (nb_articles * prix_ht) + (nb_articles * prix_ht * tva)
print("Le prix TTC est de ", prix_ttc, " chf.")
