from data.data_utilisateur import DataUtilisateur
from models.utilisateur import Utilisateur
data_user=DataUtilisateur()
con=data_user.connecter_db()
print(con)

user1=Utilisateur(10013, "ali", "sarah", 24)
user2=Utilisateur(10014, "Anis", "Hsissou", 24)
user3=Utilisateur(10015, "jiji", "kiki", 24)
data_user.ajouter_utilisateur(user1)
data_user.ajouter_utilisateur(user2)
data_user.ajouter_utilisateur(user3)

utilisateurs=data_user.recuperer_utilisateur()
for u in utilisateurs:
    print(u)

