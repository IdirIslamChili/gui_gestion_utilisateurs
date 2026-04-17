import json
import mysql.connector
class DataUtilisateur:
    def __init__(self):
        pass

    def connecter_db(self):
        with open("./data/config.json", "r", encoding="utf-8") as f:
            config=json.load(f)
        connexion=mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return connexion

    def ajouter_utilisateur(self, utilisateur):
        connexion=self.connecter_db()
        crs=connexion.cursor()
        crs.execute(
            "INSERT INTO utilisateurs VALUES(%s,%s,%s,%s)",
            (utilisateur.numero_enregistrement, utilisateur.nom, utilisateur.prenom, utilisateur.age)
        )
        connexion.commit()
        crs.close()
        connexion.close()

    def recuperer_utilisateur(self):
        connexion=self.connecter_db()
        crs=connexion.cursor()

        crs.execute("SELECT * FROM utilisateurs ")
        data=crs.fetchall()

        crs.close()
        connexion.close()
        return data

