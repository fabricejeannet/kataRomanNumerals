unites_romaines = ["","I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
dizaines_romaines = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
centaines_romaines = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
milliers_romains = ["", "M", "MM"]

def decomposition(valeur):
    liste_de_decomposition = []

    if 0 < valeur <= 3000:
        liste_de_decomposition.append(reduction(valeur, 1000))
        reste_a_decomposer = valeur % 1000;
        liste_de_decomposition.append(reduction(reste_a_decomposer, 100))
        reste_a_decomposer = reste_a_decomposer % 100;
        liste_de_decomposition.append(reduction(reste_a_decomposer, 10))
        reste_a_decomposer = reste_a_decomposer % 10;
        liste_de_decomposition.append(reste_a_decomposer)

    return liste_de_decomposition


def reduction(valeur, nombre):
    return int((valeur - valeur % nombre) / nombre)

def afficher(liste):
    for item in liste:
        print(item)


def traduire(valeur):
    traduction = ""
    liste = decomposition(valeur)
    traduction += milliers_romains[liste[0]]
    traduction += centaines_romaines[liste[1]]
    traduction += dizaines_romaines[liste[2]]
    traduction += unites_romaines[liste[3]]
    return traduction


# --------------------------------- Tests ---------------------------------

def test_retourne_une_liste_vide_si_la_valeur_est_inferieure_a_1():
    liste = decomposition(0)
    assert len(liste) == 0


def test_retourne_une_liste_vide_si_la_valeur_est_superieure_a_3000():
    liste = decomposition(0)
    assert len(liste) == 0


def test_premier_element_de_la_liste_est_0_si_valeur_inferieure_a_1000():
    liste = decomposition(999)
    assert liste[0] == 0;


def test_premier_element_de_la_liste_est_1_si_valeur_est_1000():
    liste = decomposition(1000)
    assert liste[0] == 1;


def test_premier_element_de_la_liste_est_1_si_valeur_est_2000():
    liste = decomposition(2000)
    assert liste[0] == 2;


def test_deuxieme_element_de_la_liste_est_0_si_valeur_inferieure_a_100():
    liste = decomposition(99)
    assert liste[1] == 0;


def test_deuxieme_element_de_la_liste_est_1_si_valeur_est_100():
    liste = decomposition(100)
    assert liste[1] == 1;


def test_deuxieme_element_de_la_liste_est_1_si_valeur_est_200():
    liste = decomposition(200)
    assert liste[1] == 2;


def test_troisieme_element_de_la_liste_est_0_si_valeur_inferieure_a_10():
    liste = decomposition(9)
    assert liste[2] == 0;


def test_troisieme_element_de_la_liste_est_1_si_valeur_est_10():
    liste = decomposition(10)
    assert liste[2] == 1;


def test_troisieme_element_de_la_liste_est_1_si_valeur_est_20():
    liste = decomposition(20)
    assert liste[2] == 2;


def test_quatrieme_element_de_la_liste_est_bien_egal_aux_unites():
    liste = decomposition(234)
    assert liste[3] == 4;

def test_retourne_I_si_valeur_est_egale_a_1():
    traduction = traduire(1)
    assert traduction == "I"


def test_retourne_II_si_valeur_est_egale_a_2():
    traduction = traduire(2)
    assert traduction == "II"

def test_retourne_III_si_valeur_est_egale_a_3():
    traduction = traduire(3)
    assert traduction == "III"

def test_retourne_IV_si_valeur_est_egale_a_4():
    traduction = traduire(4)
    assert traduction == "IV"

def test_retourne_V_si_valeur_est_egale_a_5():
    traduction = traduire(5)
    assert traduction == "V"

def test_retourne_VI_si_valeur_est_egale_a_6():
    traduction = traduire(6)
    assert traduction == "VI"

def test_retourne_VII_si_valeur_est_egale_a_7():
    traduction = traduire(7)
    assert traduction == "VII"

def test_retourne_VIII_si_valeur_est_egale_a_8():
    traduction = traduire(8)
    assert traduction == "VIII"

def test_retourne_IX_si_valeur_est_egale_a_9():
    traduction = traduire(9)
    assert traduction == "IX"

def test_retourne_X_si_valeur_est_egale_a_10():
    traduction = traduire(10)
    assert traduction == "X"

def test_retourne_XX_si_valeur_est_egale_a_20():
    traduction = traduire(20)
    assert traduction == "XX"

def test_retourne_XXX_si_valeur_est_egale_a_30():
    traduction = traduire(30)
    assert traduction == "XXX"

def test_retourne_XL_si_valeur_est_egale_a_40():
    traduction = traduire(40)
    assert traduction == "XL"

def test_retourne_L_si_valeur_est_egale_a_50():
    traduction = traduire(50)
    assert traduction == "L"

def test_retourne_LX_si_valeur_est_egale_a_60():
    traduction = traduire(60)
    assert traduction == "LX"

def test_retourne_LXX_si_valeur_est_egale_a_70():
    traduction = traduire(70)
    assert traduction == "LXX"

def test_retourne_LXXX_si_valeur_est_egale_a_80():
    traduction = traduire(80)
    assert traduction == "LXXX"

def test_retourne_XC_si_valeur_est_egale_a_90():
    traduction = traduire(90)
    assert traduction == "XC"