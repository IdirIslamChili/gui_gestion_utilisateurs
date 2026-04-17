class Utilisateur:
    def __init__(self, num_enreg, nom, prenom, age):
        self.numero_enregistrement=num_enreg
        self.nom=nom
        self.prenom=prenom
        self.age=age
    def afficher_infos(self):
        print(f"Numéro d'enregistrement : {self.numero_enregistrement}, nom : {self.nom}, prénom : {self.prenom} et âge : {self.age}")

