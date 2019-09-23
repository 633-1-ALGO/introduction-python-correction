# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]

#Solution :

for j in range(1,len(B)):           #Parcours la liste entière
    cle = B[j]                      #On stocke la clef que l'on consulte
    k = j - 1                       #On stocke l'indice précédant (k)
    while k >= 0 and B[k] > cle:    #Tant que l'indice précédant est >= à 0 (que l'on est pas sorti de la liste)
                                    #et que l'indice precédant est plus grand que la clef que l'on consulte
        B[k+1] = B[k]               #On déplace l'élément à l'emplaçement de la cle consultée
        k += -1                     #On déplace l'indice précédant de -1
    B[k+1] = cle                    #On insère la clef consultée à son nouvel emplaçement
print("Tableau B trié : ", *B)
