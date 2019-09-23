# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  xx  et elle se trouve à l'indice [ x ][ y ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]

# Solution
val_max = 0
for o in range(0, len(tab)):
    for p in range(0, len(tab[o])):
        if tab[o][p] > val_max:
            val_max = tab[o][p]
            best_o = o
            best_p = p
print("La valeur maximum est : ", val_max, " et elle se trouve à l'indice [", best_o, "][", best_p, "]")
