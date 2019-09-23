# Problème : Créer une fonction affichant la fréquence des lettres d'une chaine de caractère.
# Données : Un texte d'essai et un tableau de caractère et leur fréquences.
texte = "ceci est un texte que vous pouvez modifier mais gare aux caracteres speciaux et aux majuscules"
tab_lettres = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', ' '], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


# Solution :
def freq(chaine):
    for i in range(0, len(texte)):
        for j in range(0, len(tab_lettres[0])):
            if tab_lettres[0][j] == texte[i]:
                tab_lettres[1][j] = tab_lettres[1][j] + 1
    for i in range(0, len(tab_lettres[0])):
        print("Caractère '", tab_lettres[0][i], "' : ", tab_lettres[1][i], "  ", sep='')

freq(texte)