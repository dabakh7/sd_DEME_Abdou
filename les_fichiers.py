from fonction_transform import *
Entrer = input("Donnez un fichier à traiter:")
conversion_donnee(Entrer)
if conversion_donnee(Entrer) != False:
    fvalide = conversion_donnee(Entrer)
    print("***********MENU**********")
    print("1 pour convertir en csv")
    print("2 pour convertir en yaml")
    print("3 pour convertir en json")
    print("4 pour convertir en xml")
    print("5 pour choisir un autre fichier")
    choix = input("Veuillez faire votre choix: ")
    if choix == "1" :
        conv_csv(fvalide)
    elif choix == "2":
        conv_yaml(fvalide)
    elif choix == "3":
        conv_json(fvalide)
    elif choix == "4" :
        conv_xml(fvalide)
    elif choix == "5":
        Entrer = input("Donnez un fichier à traiter:")
