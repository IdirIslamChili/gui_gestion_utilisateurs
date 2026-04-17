from data.data_utilisateur import DataUtilisateur
from models.utilisateur import Utilisateur
from services.services_utilisateur import ServiceUtilisateur
from views.view_utilisateur import ViewUtilisateur

data_user=DataUtilisateur()
con=data_user.connecter_db()
print(con)

user1=Utilisateur(10013, "Idir", "Chili", 24)
user2=Utilisateur(10014, "Anis", "Hacene", 20)
user3=Utilisateur(10015, "Lyes", "Gulissa", 17)
service = ServiceUtilisateur()
service.inscrire_utilisateur(user1)
service.inscrire_utilisateur(user2)
service.inscrire_utilisateur(user3)

utilisateurs = service.lister_utilisateurs()

print("Liste des utilisateurs :")
for u in utilisateurs:
    u.afficher_infos()

app = ViewUtilisateur()
app.mainloop()


