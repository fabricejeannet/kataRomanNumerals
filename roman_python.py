

def decomposer(valeur):
    liste_de_decomposer = []

    if 0 < valeur <= 3000:
        liste_de_decomposer.append(nombre_de_milliers(valeur))
        reste_a_decomposer = valeur % 1000;
        liste_de_decomposer.append(reduction(reste_a_decomposer, 100))
        reste_a_decomposer = reste_a_decomposer % 100;
        liste_de_decomposer.append(reduction(reste_a_decomposer, 10))
        reste_a_decomposer = reste_a_decomposer % 10;
        liste_de_decomposer.append(reste_a_decomposer)

    return liste_de_decomposer

def nombre_de_milliers(valeur):
    return reduction(valeur, 1000)

def reduction(valeur, nombre):
    return int((valeur - valeur % nombre) / nombre)

def afficher(liste):
    for item in liste:
        print(item)


def convertir_en_nombres_romains(valeur):
    conversion = ""
    liste = decomposer(valeur)
    conversion += milliers_romains[liste[0]]
    conversion += centaines_romaines[liste[1]]
    conversion += dizaines_romaines[liste[2]]
    conversion += unites_romaines[liste[3]]
    return conversion


def decomposer_nombre_romain(nombre_romain):

    liste_decomposition = []

    liste_decomposition.append(combien_de(milliers_romains, "CM", nombre_romain))
    liste_decomposition.append(combien_de(centaines_romaines, "XC", nombre_romain))
    liste_decomposition.append(combien_de(dizaines_romaines, "IX", nombre_romain))
    liste_decomposition.append(combien_de(unites_romaines, "", nombre_romain))

    return liste_decomposition


def combien_de(ordre, piege, nombre_romain):
    index_dans_l_ordre = 0
    quantite = 0
    for item in ordre:
        position_item = nombre_romain.find(item)
        if position_item != -1 and nombre_romain[position_item - 1:position_item + 1] != piege:
            quantite = index_dans_l_ordre

        index_dans_l_ordre += 1

    return quantite


unites_romaines = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
dizaines_romaines = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
centaines_romaines = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
milliers_romains = ["", "M", "MM", "MMM"]

# --------------------------------- Tests ---------------------------------

def test_retourne_une_liste_vide_si_la_valeur_est_inferieure_a_1():
    liste = decomposer(0)
    assert len(liste) == 0

def test_retourne_une_liste_vide_si_la_valeur_est_superieure_a_3000():
    liste = decomposer(0)
    assert len(liste) == 0

def test_premier_element_de_la_liste_est_0_si_valeur_inferieure_a_1000():
    liste = decomposer(789)
    assert liste == [0,7,8,9];

def test_que_chaque_valeur_est_a_la_bonne_place():
    liste = decomposer(1234)
    assert liste == [1,2,3,4];

def test_premier_element_de_la_liste_est_1_si_valeur_est_2000():
    liste = decomposer(2000)
    assert liste[0] == 2;

def test_deuxieme_element_de_la_liste_est_0_si_valeur_inferieure_a_100():
    liste = decomposer(99)
    assert liste[1] == 0;

def test_deuxieme_element_de_la_liste_est_1_si_valeur_est_100():
    liste = decomposer(100)
    assert liste[1] == 1;

def test_deuxieme_element_de_la_liste_est_1_si_valeur_est_200():
    liste = decomposer(200)
    assert liste[1] == 2;

def test_troisieme_element_de_la_liste_est_0_si_valeur_inferieure_a_10():
    liste = decomposer(9)
    assert liste[2] == 0;

def test_troisieme_element_de_la_liste_est_1_si_valeur_est_10():
    liste = decomposer(10)
    assert liste[2] == 1;

def test_troisieme_element_de_la_liste_est_1_si_valeur_est_20():
    liste = decomposer(20)
    assert liste[2] == 2;

def test_quatrieme_element_de_la_liste_est_bien_egal_aux_unites():
    liste = decomposer(234)
    assert liste[3] == 4;

def test_retourne_I_si_valeur_est_egale_a_1():
    conversion = convertir_en_nombres_romains(1)
    assert conversion == "I"

def test_retourne_II_si_valeur_est_egale_a_2():
    conversion = convertir_en_nombres_romains(2)
    assert conversion == "II"

def test_retourne_III_si_valeur_est_egale_a_3():
    conversion = convertir_en_nombres_romains(3)
    assert conversion == "III"

def test_retourne_IV_si_valeur_est_egale_a_4():
    conversion = convertir_en_nombres_romains(4)
    assert conversion == "IV"

def test_retourne_V_si_valeur_est_egale_a_5():
    conversion = convertir_en_nombres_romains(5)
    assert conversion == "V"

def test_retourne_VI_si_valeur_est_egale_a_6():
    conversion = convertir_en_nombres_romains(6)
    assert conversion == "VI"

def test_retourne_VII_si_valeur_est_egale_a_7():
    conversion = convertir_en_nombres_romains(7)
    assert conversion == "VII"

def test_retourne_VIII_si_valeur_est_egale_a_8():
    conversion = convertir_en_nombres_romains(8)
    assert conversion == "VIII"

def test_retourne_IX_si_valeur_est_egale_a_9():
    conversion = convertir_en_nombres_romains(9)
    assert conversion == "IX"

def test_retourne_X_si_valeur_est_egale_a_10():
    conversion = convertir_en_nombres_romains(10)
    assert conversion == "X"

def test_retourne_XX_si_valeur_est_egale_a_20():
    conversion = convertir_en_nombres_romains(20)
    assert conversion == "XX"

def test_retourne_XXX_si_valeur_est_egale_a_30():
    conversion = convertir_en_nombres_romains(30)
    assert conversion == "XXX"

def test_retourne_XL_si_valeur_est_egale_a_40():
    conversion = convertir_en_nombres_romains(40)
    assert conversion == "XL"

def test_retourne_L_si_valeur_est_egale_a_50():
    conversion = convertir_en_nombres_romains(50)
    assert conversion == "L"

def test_retourne_LX_si_valeur_est_egale_a_60():
    conversion = convertir_en_nombres_romains(60)
    assert conversion == "LX"

def test_retourne_LXX_si_valeur_est_egale_a_70():
    conversion = convertir_en_nombres_romains(70)
    assert conversion == "LXX"

def test_retourne_LXXX_si_valeur_est_egale_a_80():
    conversion = convertir_en_nombres_romains(80)
    assert conversion == "LXXX"

def test_retourne_XC_si_valeur_est_egale_a_90():
    conversion = convertir_en_nombres_romains(90)
    assert conversion == "XC"

def test_retourne_C_si_valeur_est_egale_a_100():
    conversion = convertir_en_nombres_romains(100)
    assert conversion == "C"

def test_retourne_CC_si_valeur_est_egale_a_200():
    conversion = convertir_en_nombres_romains(200)
    assert conversion == "CC"

def test_retourne_CCC_si_valeur_est_egale_a_300():
    conversion = convertir_en_nombres_romains(300)
    assert conversion == "CCC"

def test_retourne_CD_si_valeur_est_egale_a_400():
    conversion = convertir_en_nombres_romains(400)
    assert conversion == "CD"

def test_retourne_D_si_valeur_est_egale_a_500():
    conversion = convertir_en_nombres_romains(500)
    assert conversion == "D"

def test_retourne_DC_si_valeur_est_egale_a_600():
    conversion = convertir_en_nombres_romains(600)
    assert conversion == "DC"

def test_retourne_DCC_si_valeur_est_egale_a_700():
    conversion = convertir_en_nombres_romains(700)
    assert conversion == "DCC"

def test_retourne_DCCC_si_valeur_est_egale_a_800():
    conversion = convertir_en_nombres_romains(800)
    assert conversion == "DCCC"

def test_retourne_CM_si_valeur_est_egale_a_900():
    conversion = convertir_en_nombres_romains(900)
    assert conversion == "CM"

def test_retourne_M_si_valeur_est_egale_a_1000():
    conversion = convertir_en_nombres_romains(1000)
    assert conversion == "M"

def test_retourne_MM_si_valeur_est_egale_a_2000():
    conversion = convertir_en_nombres_romains(2000)
    assert conversion == "MM"

def test_retourne_MMM_si_valeur_est_egale_a_3000():
    conversion = convertir_en_nombres_romains(3000)
    assert conversion == "MMM"

def test_retourne_MCCXXXIV_si_valeur_est_egale_a_1234():
    conversion = convertir_en_nombres_romains(1234)
    assert conversion == "MCCXXXIV"

def test_on_compte_0_milliers_dans_CMXCIX():
    liste_de_decomposition = decomposer_nombre_romain("CMXCIX")

def test_on_compte_1_milliers_dans_MCMXXIV():
    liste_de_decomposition = decomposer_nombre_romain("MCMXCIX")
    assert liste_de_decomposition[0] == 1;

def test_on_compte_9_centaines_dans_CMXCIX():
    liste_de_decomposition = decomposer_nombre_romain("CMXCIX")
    assert  liste_de_decomposition[1] == 9;

def test_on_compte_0_centaines_dans_MXCV():
    liste_de_decomposition = decomposer_nombre_romain("MXCV")
    assert  liste_de_decomposition[1] == 0;

def test_on_compte_0_dizaines_dans_MIX():
    liste_de_decomposition = decomposer_nombre_romain("MIX")
    assert  liste_de_decomposition[2] == 0;

def test_on_compte_2_dizaines_dans_MCXXIX():
    liste_de_decomposition = decomposer_nombre_romain("MCXXIX")
    assert  liste_de_decomposition[2] == 2;

def test_on_compte_9_unites_dans_MCMXXIV():
    liste_de_decomposition = decomposer_nombre_romain("MCMXCIX")
    assert liste_de_decomposition[3] == 9;

def test_on_compte_9_unites_dans_MCMXX():
    liste_de_decomposition = decomposer_nombre_romain("MCMXX")
    assert liste_de_decomposition[3] == 0;