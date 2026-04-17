import customtkinter as ctk
from services.services_utilisateur import ServiceUtilisateur
from models.utilisateur  import Utilisateur
from tkinter import ttk

class ViewUtilisateur (ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestion Utilisateurs")
        self.geometry("600x500")

        self.service = ServiceUtilisateur()

        self.creer_frame_informations()
        self.creer_frame_actions()
        self.creer_frame_liste()
        self.charger_utilisateurs()
        self.creer_frame_liste()

    def creer_frame_informations(self):
        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.pack(pady=20, padx=20, fill="x")

        self.num_entry = ctk.CTkEntry(self.frame_info, placeholder_text="Numéro enregistrement")
        self.num_entry.pack(pady=5)

        self.nom_entry = ctk.CTkEntry(self.frame_info, placeholder_text="Nom")
        self.nom_entry.pack(pady=5)

        self.prenom_entry = ctk.CTkEntry(self.frame_info, placeholder_text="Prénom")
        self.prenom_entry.pack(pady=5)

        self.age_entry = ctk.CTkEntry(self.frame_info, placeholder_text="Âge")
        self.age_entry.pack(pady=5)

    def creer_frame_actions(self):
        self.frame_actions = ctk.CTkFrame(self)
        self.frame_actions.pack(pady=10)

        self.btn_inscrire = ctk.CTkButton(
            self.frame_actions,
            text="Inscrire",
            command=self.inscrire_utilisateur
        )
        self.btn_inscrire.pack(pady=10)

    def inscrire_utilisateur(self):
        try:
            utilisateur = Utilisateur(
                num_enreg=self.num_entry.get(),
                nom=self.nom_entry.get(),
                prenom=self.prenom_entry.get(),
                age=int(self.age_entry.get())
            )
            self.service.inscrire_utilisateur(utilisateur)

            self.num_entry.delete(0, "end")
            self.nom_entry.delete(0, "end")
            self.prenom_entry.delete(0, "end")
            self.age_entry.delete(0, "end")

            self.charger_utilisateurs()

        except Exception as e:
            print("Erreur :", e)

    def creer_frame_liste(self):
        self.frame_liste = ctk.CTkFrame(self)
        self.frame_liste.pack(pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(
            self.frame_liste,
            columns=("num", "nom", "prenom", "age"),
            show="headings"
        )

        self.tree.heading("num", text="Numéro d'enregistrement")
        self.tree.heading("nom", text="Nom")
        self.tree.heading("prenom", text="Prénom")
        self.tree.heading("age", text="Âge")

        self.tree.column("num", width=60)
        self.tree.column("nom", width=150)
        self.tree.column("prenom", width=150)
        self.tree.column("age", width=120)
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

    def charger_utilisateurs(self):
        utilisateurs = self.service.lister_utilisateurs()

        for row in self.tree.get_children():
            self.tree.delete(row)

        for u in utilisateurs:
            self.tree.insert("", "end", values=(
                u.numero_enregistrement,
                u.nom,
                u.prenom,
                u.age
            ))