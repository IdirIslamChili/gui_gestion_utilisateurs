from data.data_utilisateur import DataUtilisateur
from models.utilisateur import Utilisateur
from services.services_utilisateur import ServiceUtilisateur
data_user=DataUtilisateur()
con=data_user.connecter_db()
print(con)

user1=Utilisateur(10013, "ali", "sarah", 24)
user2=Utilisateur(10014, "Anis", "Hsissou", 20)
user3=Utilisateur(10015, "jiji", "kiki", 17)
service = ServiceUtilisateur()
print(service.inscrire_utilisateur(user1))
print(service.inscrire_utilisateur(user2))
print(service.inscrire_utilisateur(user3))

utilisateurs = service.lister_utilisateurs()

print("Liste des utilisateurs :")

for u in utilisateurs:
    u.afficher_infos()



