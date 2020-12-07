# une fonction permettant de renvoyer la valeur du nombre de couples de valeurs
#  numériques d’un tableau à deux entrées de n couples de valeurs numériques :
#  dimmat2n(par)

def dimmat2n(par):
    count = 0
    for i in par:
        count+=1
    return count

# une fonction permettant à l’utilisateur d’implémenter une valeur numérique entière
# n strictement positive et de la renvoyer : impln()

def impln():
    user_input = float(input("Entrez une valeur numérique positive strictement entière : "))
    if ((user_input % 1) == 0) and user_input > 0:
        return int(user_input)
    else:
        print("Ce n'est pas une valeur numérique positive strictement entière !")

# une fonction permettant de renvoyer un tableau à deux entrées à n composantes où
#  chaque composante est initialisée à une valeur nulle : mat2n(par)

def mat2n(par):
    list = []
    for i in range(par):
        list.append([0,0])
    return list

# une fonction permettant d’implémenter n couples de valeurs numériques dans un tableau à
#  deux entrées et de renvoyer ce tableau : implmat2n()

def implmat2n():
    tab = []
    while True:
        user_input = input("Entrez 'stop' pour signalez que vous avez fini d'entrer des valeurs. \
        \nEntrez des couples de valeurs numériques séparé par un espace:  ")

        if user_input.lower() == "stop":
            print("Liste enregistrée ! ")
            print(tab)
            return tab
        else:
            a,b = user_input.split(" ")
            temp = [float(a)],[float(b)]
            tab.append(temp)

# une méthode permettant d’afficher les n couples de valeurs numériques d’un tableau à
#  deux entrées de n couples de valeurs numériques : affichmat2n(par)

def afffichmat2n(par):
    n = int(input("n = "))
    if n <= dimmat2n(par):
        for i in range(n):
            print(par[i])
    else:
        print("n supérieur à la longueur de la liste !")

# une fonction permettant de renvoyer un tableau de n couples de valeurs numériques
#  classées par ordre croissant par rapport à la première valeur numérique de chaque couple
#  de valeurs numériques : mat2ncrois(par)

def mat2ncrois(par):

    liste = par.copy()
    liste_finale = []

    while liste:
        min = liste[0]
        for x in liste:
            temp = x[0]
            if temp < min[0]:
                min = x
        liste_finale.append(min)
        liste.remove(min)
    return liste_finale

# une fonction permettant de renvoyer un tableau de n couples de valeurs numériques
#  classées par ordre décroissant par rapport à la première valeur numérique de
#  chaque couple de données : mat2ndecrois(par)

def mat2ndecrois(par):

    liste = par.copy()
    liste_finale = []

    while liste:
        max = liste[0]
        for x in liste:
            temp = x[0]
            if temp > max[0]:
                max = x
        liste_finale.append(max)
        liste.remove(max)
    return liste_finale

# une fonction permettant de renvoyer la valeur maximale de l’ensemble des premières
#  valeurs numériques de chaque couple ainsi que la valeur maximale de l’ensemble des
#  secondes valeurs numériques de chaque couple d’un tableau à deux entrées de n couples
#  de valeurs numériques : mat2nmax(par)

def mat2nmax(par):

    max_1_couple = par[0]
    for x in par:
        temp = x[0]
        if temp > max_1_couple[0]:
            max_1_couple = x

    max_2_couple = par[1]
    for x in par:
        temp = x[1]
        if temp > max_2_couple[1]:
            max_2_couple = x

    couple_final = [max_1_couple[0], max_2_couple[1]]
    return couple_final

# une fonction permettant de renvoyer la valeur minimale de l’ensemble des premières
#  valeurs numériques de chaque couple ainsi que la valeur minimale de l’ensemble des
#  secondes valeurs numériques de chaque couple d’un tableau à deux entrées de n couples de
#  valeurs numériques : mat2nmin(par)
def mat2nmin(par):

    min_1_couple = par[0]
    for x in par:
        temp = x[0]
        if temp < min_1_couple[0]:
            min_1_couple = x

    min_2_couple = par[1]
    for x in par:
        temp = x[1]
        if temp < min_2_couple[1]:
            min_2_couple = x

    couple_final = [min_1_couple[0], min_2_couple[1]]
    return couple_final

# une fonction permettant de renvoyer la valeur de l’étendue de l’ensemble des premières
# valeurs numériques de chaque couple ainsi que la valeur de l’étendue de l’ensemble des
# secondes valeurs numériques de chaque couple d’un tableau à deux entrées de n couples de
# valeurs numériques : mat2netend(par)

def mat2netend(par):
    couple_min = mat2nmin(par)
    couple_max = mat2nmax(par)
    etendue_1_couple = couple_max[0] - couple_min[0]
    etendue_2_couple = couple_max[1] - couple_min[1]
    etendue = [etendue_1_couple,etendue_2_couple]
    return etendue

# une fonction permettant de renvoyer la valeur de la somme de l’ensemble des premières
# valeurs numériques de chaque couple ainsi que la valeur de la somme de l’ensemble des
# secondes valeurs numériques de chaque couple d’un tableau à deux entrées de n couples de
# valeurs numériques : mat2nsom(par)

def mat2nsom(par):
    somme_1_couple = 0
    somme_2_couple = 0
    for i in par:
        somme_1_couple += i[0]
        somme_2_couple += i[1]
    return [somme_1_couple,somme_2_couple]

# une fonction permettant de renvoyer la valeur moyenne de l’ensemble des premières
# valeurs numériques de chaque couple ainsi que la valeur moyenne de l’ensemble des
# secondes valeurs numériques de chaque couple d’un tableau à deux entrées de n couples de
# valeurs numériques : mat2nmoy(par)
def mat2nmoy(par):
    somme = mat2nsom(par)
    moy_1_couple = somme[0]/dimmat2n(par)
    moy_2_couple = somme[1]/dimmat2n(par)
    return [moy_1_couple,moy_2_couple]

# une fonction permettant de renvoyer la valeur de l’écart moyen absolu de l’ensemble des
# premières valeurs numériques de chaque couple ainsi que la valeur de l’écart moyen absolu de l’ensemble des secondes valeurs numériques de chaque couple d’un tableau à
# deux entrées de n couples de valeurs numériques : mat2necma(par)

def mat2necma(par):
    ecma_1_couple = 0
    ecma_2_couple = 0
    moy = mat2nmoy(par)
    for i in par:
        ecma_1_couple += (((i[0] - moy[0])**2)**(1/2))/dimmat2n(par)
    for i in par:
        ecma_2_couple += (((i[1] - moy[1]))**2)**(1/2)/dimmat2n(par)
    return [ecma_1_couple,ecma_2_couple]

# une fonction permettant de renvoyer la valeur de la variance de l’ensemble des
# premières valeurs numériques de chaque couple ainsi que la valeur de la variance de
# l’ensemble des secondes valeurs numériques de chaque couple d’un tableau à deux entrées
# de n couples de valeurs numériques : mat2nvar(par)
def mat2nvar(par):

    var_1_couple = 0
    var_2_couple = 0
    moy = mat2nmoy(par)
    for i in par:
        var_1_couple += ((i[0] - moy[0])**2)/dimmat2n(par)
    for i in par:
        var_2_couple += ((i[1] - moy[1])**2)/dimmat2n(par)
    return [var_1_couple,var_2_couple]

# une fonction permettant de renvoyer la valeur de l’écart-type de l’ensemble des
# premières valeurs numériques de chaque couple ainsi que la valeur de l’écart-type de
# l’ensemble des secondes valeurs numériques de chaque couple d’un tableau à deux entrées
# de n couples de valeurs numériques : mat2nect(par)
def mat2nect(par):
    var = mat2nvar(par)
    return [var[0]**(1/2),var[1]**(1/2)]

# une fonction permettant de renvoyer la valeur de S(s) de l’ensemble des
# premières valeurs numériques de chaque couple ainsi que la valeur de S(s) de
# l’ensemble des secondes valeurs numériques de chaque couple d’un tableau à deux entrées
# de n couples de valeurs numériques : mat2ns(par)

def mat2ns(par):
    vs_1_couple = 0
    moy = mat2nmoy(par)
    for i in par:
        vs_1_couple += (((i[0] - moy[0])**2)/(dimmat2n(par)-1))
    return vs_1_couple

# une fonction permettant de renvoyer la valeur du premier quartile 𝑞1(𝑞1) de l’ensemble
# des premières valeurs numériques de chaque couple ainsi que la valeur du premier quartile 𝑞1(𝑞1)
# de l’ensemble des secondes valeurs numériques de chaque couple d’un tableau à deux entrées de n
# couples de valeurs numériques : mat2nqu(par)


def mat2ncrois_2e_valeur(par):
    liste = par.copy()
    liste_finale = []

    while liste:
        min = liste[0]
        for x in liste:
            temp = x[1]
            if temp < min[1]:
                min = x
        liste_finale.append(min)
        liste.remove(min)
    return liste_finale

def mat2nqu(par):

    q1_1 = 0
    q1_2 = 0
    N = (dimmat2n(par)-1)/2
    par = mat2ncrois_2e_valeur(par)
    print("N = ", N)
    print("par = ",par)

    if N%2 == 0:
        q1_2 = (par[int(N/2)-1][1] + par[int(N/2)][1]) / 2
        print(par[int(N/2)-1][1])

    if N%2 != 0:
        q1_2 = par[int((N+1)/2)-1][1]


    if N%2 == 0:
        q1_1 = (par[int(N/2)-1][0] + par[int(N/2)][0]) / 2
        print(par[int(N/2)-1][0])

    if N%2 != 0:
        q1_1 = par[int((N+1)/2)-1][0]


    return [q1_1,q1_2]



# une fonction permettant de renvoyer la valeur médiane 𝑞2(𝑞2) de
# l’ensemble des secondes valeurs numériques de chaque couple d’un tableau à deux entrées
# de n couples de valeurs numériques : matn2nqd(par)

def matn2nqd(par):
    N = dimmat2n(par)
    par = mat2ncrois_2e_valeur(par)

    if N%2 != 0:
        print(int((N+1)/2))
        q1 = par[int((N+1)/2)-1][1]


    elif N%2 == 0:
        q1 = (par[int(N/2)-1][1] + par[int(N/2)][1]) / 2


    return q1

# une fonction permettant de renvoyer la valeur du troisième quartile 𝑞 (𝑞3)
# de l’ensemble des secondes valeurs numériques de chaque couple d’un
# tableau à deux entrées de n couples de valeurs numériques : mat2nq3(par)

def mat2nq3(par):
    q3 = 0

    N = (dimmat2n(par)-1)/2
    par = mat2ncrois_2e_valeur(par)
    print("N = ", N)
    print("par = ",par)
    print(N)
    if N%2 == 0:
        q3 = (par[-(int(N/2))][1] + par[-int(N/2)-1][1]) / 2

    if N%2 != 0:
        q3 = par[-(int((N+1)/2))][1]


    return q3

def mat2nq3_1_couple(par):
    q3 = 0

    N = (dimmat2n(par)-1)/2
    par = mat2ncrois_2e_valeur(par)
    print("N = ", N)
    print("par = ",par)
    print(N)
    if N%2 == 0:
        q3 = (par[-(int(N/2))][0] + par[-int(N/2)-1][0]) / 2

    if N%2 != 0:
        q3 = par[-(int((N+1)/2))][0]


    return q3
# une fonction permettant de renvoyer la valeur de l’écart interquartile iq de
# l’ensemble des premières valeurs numériques de chaque couple ainsi que la valeur
# de l’écart interquartile iq de l’ensemble des secondes valeurs numériques de
# chaque couple d’un tableau à deux entrées de n couples de valeurs numériques
# : mat2niq(par)

def mat2niq(par):
    q1 = mat2nqu(par)
    iq_1_couple = mat2nq3_1_couple(par) - q1[0]
    iq_2_couple = mat2nq3(par) - q1[1]
    return [iq_1_couple,iq_2_couple]
