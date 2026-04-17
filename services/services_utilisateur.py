from data.data_utilisateur import DataUtilisateur
from models.utilisateur import Utilisateur
class ServiceUtilisateur:
    def __init__(self):
        self.data = DataUtilisateur()

    def inscrire_utilisateur(self, utilisateur):
        try:
            if not utilisateur.numero_enregistrement or not utilisateur.nom or not utilisateur.prenom or not utilisateur.age:
                raise ValueError("Tous les champs doivent être remplis")
            if utilisateur.age < 18:
                raise ValueError("L'utilisateur doit avoir au moins 18 ans")
            self.data.ajouter_utilisateur(utilisateur)
            print("Utilisateur inscrit avec succès")
        except Exception as e:
            print(f"Erreur lors de l'inscription : {str(e)}")

    def lister_utilisateurs(self):
        try:
            utilisateurs_data = self.data.recuperer_utilisateur()
            utilisateurs = []
            for u in utilisateurs_data:
                utilisateur = Utilisateur(
                    num_enreg=u[0],
                    nom=u[1],
                    prenom=u[2],
                    age=u[3]
                )
                utilisateurs.append(utilisateur)
            return utilisateurs
        except Exception as e :
            print("Erreur :", e)
        return []

service = ServiceUtilisateur()

