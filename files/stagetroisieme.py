print("Programme de resolution d'une equation du type ax + b = cx + d\n")

# Entree des coefficients
a = float(input("Entrez la valeur de a : "))
b = float(input("Entrez la valeur de b : "))
c = float(input("Entrez la valeur de c : "))
d = float(input("Entrez la valeur de d : "))

if a - c == 0:
    print("Erreur : il est imperatif que a ≠ c.")
    print("Arret du programme.")
    exit()


#---------------------------------------------------------------------------------------------------------------------------------
    
# Resolution exacte de l'equation
x_ex = (d - b) / (a - c)       # Solution theorique obtenue apres manipulations algebriques.

#---------------------------------------------------------------------------------------------------------------------------------

# Resolution numerique de l'equation

# Fonction associee a l'equation
def f(x):
    return a * x + b - c * x - d
# Cette fonction calcule la valeur de f(x) = ax + b - cx - d pour une valeur specifique de x.

# Methode de la bissection
x_min, x_max = -1000, 1000  # Definit un large intervalle initial pour la recherche de la racine, de -1000 a 1000.
tolerance = 1e-6            # Definit la tolerance pour la precision de la solution. La methode s'arretera si l'ecart est inferieur a cette valeur.
max_iter = 100              # Definit le nombre maximum d'iterations pour eviter une boucle infinie.
compteur = 0                # Initialise un compteur pour suivre le nombre d'iterations effectuees.

while compteur < max_iter:             # Debut d'une boucle qui continue jusqu'a ce que le nombre d'iterations atteigne le maximum.
    x_mid = (x_min + x_max) / 2        # Trouve le point moyen de l'intervalle actuel.

    if abs(f(x_mid)) < tolerance:      # Verifie si la valeur de l'equation a ce point median est suffisamment proche de zero (en fonction de la tolerance definie).
        break                          # Si la condition est remplie, sort de la boucle (solution trouvee).

    elif f(x_min) * f(x_mid) < 0:      # Verifie si le signe de la fonction change entre x_min et x_mid.
        x_max = x_mid                  # Si le signe de f(x_min) * f(x_mid) est negatif, cela signifie que la racine est entre x_min et x_mid. Ajuste x_max au point median.

    else:
        x_min = x_mid                  # Sinon, ajuste x_min au point median (la racine est entre x_mid et x_max).
        
    compteur += 1                      # Incremente le compteur d'iterations.

x_num = x_mid                          # Affecte la valeur finale du point moyen a x_num, qui est la solution approximative de l'equation.


#---------------------------------------------------------------------------------------------------------------------------------

# Affichage de l'equation
print(f"\nL'equation est {a}x + {b} = {c}x + {d}.")

# Affichage de la solution exacte
print(f"\nLa solution exacte de l'equation est x = {x_ex}")

# Affichage de la solution numerique
print(f"\nLa solution numerique de l'equation est x ≈ {x_num} au bout de {compteur} iteration(s).")
