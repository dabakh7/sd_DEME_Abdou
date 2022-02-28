import csv
import json
import yaml
import xml
from csv import *
from dict2xml import *
def conversion_donnee (fichier):
    ext = fichier.split('.')[-1]
    ext = str(ext).lower()
    try:
        if ext in ["csv","json","yaml","xml"]:
            dicExt = []
            fich = open(fichier,"r")
            if ext == "csv":
                fichiers_csv = DictReader(fich)
                for d in fichiers_csv:
                    dicExt.append(d)
                return dicExt
            elif ext == "json":
                fichier_json = DictReader(fich)
                for d in fichier_json:
                    dicExt.append(d)
                return dicExt
            elif ext == "yaml":
                fichier_yaml = DictReader(fich)
                for d in fichier_yaml:
                    dicExt.append(d)
                return dicExt
            elif ext == "xml":
                fichier_xml = DictReader(fich)
                for d in fichier_xml:
                    dicExt.append(d)
                return dicExt
        else:
            print("votre fichier est invalide veuillez réessayer:")
            Entrer = input("Donnez un fichier à traiter:")
            return False
    except ValueError:
        print("votre fichier est invalide veuillez réessayer:")
        Entrer = input("Donnez un fichier à traiter:")
        return False
def conv_json(a):
    with open("fiche_json.json","w") as f:
        json_fich = json.dumps(a,indent=3)
        f.write(json_fich)
    print("Fichier convertit en json avec succés")
def conv_yaml(a):
    with open("yaml_fich.yaml","w") as f:
        yaml_fich = yaml.dump(a,indent=3)
        f.write(yaml_fich)
    print("Fichier convertit en yaml avec succés")
def conv_csv(d):
    for k in range(len(d)):
        fich = d[k]
        column = list(fich.keys())
    with open("fiche_csv.csv","w") as f:
        csv_fich = DictWriter(f,fieldnames = column)
        csv_fich.writeheader()
        for m in d:
            csv_fich.writerow(m)
    print("Fichier convertit en csv avec succés")
def conv_xml(d):
    with open("xml_fich.xml","w") as f:
        fich_xml = dict2xml(d)
        f.write(fich_xml)
    print("Fichier convertit en xml avec succés")

    


