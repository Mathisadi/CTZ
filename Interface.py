# On modélisera l'environement sous forme d'une matrice : 3 = fin de la route 2 = trotoir
# 1 = voiture 0 = route
# Un chiffre correspondra à un rectangle de route de largeur 3m (largeur d'une route) et de longeur
# variable L au début on prendra 1m (précison)
# On cherche à créer une interface qui permet de créer rapidement toutes sortes d'intersections
# Pour tester modéliser la route en .png
import tkinter

import customtkinter
import math

from customtkinter import *
from PIL import Image, ImageTk

# Thème
set_appearance_mode("System")


# Crétion de l'appli

class CityZen(CTk):
    def __init__(self):
        super().__init__()

        # On définit notre appli
        self.title("CityZen")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")

        # Créer le canvas
        self.nbr_canvas = 3
        self.canvas_width = 2 * self.nbr_canvas * self.winfo_screenwidth()
        self.canvas_height = 2 * self.nbr_canvas * self.winfo_screenheight()
        self.canvas_onscreen_width = 2 * self.winfo_screenwidth()
        self.canvas_onscreen_height = 2 * self.winfo_screenheight()

        self.canvas = CTkCanvas(width=self.canvas_width, height=self.canvas_height)
        self.canvas.place(x=- (self.canvas_width - self.canvas_onscreen_width) / 2,
                          y=- (self.canvas_height - self.canvas_onscreen_height) / 2, anchor="nw")

        self.interval = self.canvas_width / 40
        self.scale = 1

        # Créer les frames
        self.tool = CTkFrame(self, width=self.winfo_screenwidth() + 2, height=78, bg_color="lightgrey",
                             fg_color="lightgrey", corner_radius=0,
                             border_color="black", border_width=1)
        self.tool.place(x=-1, y=0, anchor="nw")

        # On introduit les variables
        self.stylo = None  # Stylo en cours d'utilisation
        self.orientation = 0
        self.drag_x = 0  # Position de la souris au moment du clic
        self.drag_y = 0  # Position de la souris au moment du clic
        self.route_haute = None  # Tracé de la portion haute de la route
        self.route_pointille = None  # Tracé de la ligne centrale de la route
        self.route_basse = None  # Tracé de la portion basse de la route
        self.nbr_points_place_avant_trace = None
        self.ID_fig = []  # ID des figures
        self.coord = []  # Coordonées des extrémités des figures
        self.direction_feu = [0, 0, 0]

        # On lance nos fonction
        self.toolbar()
        self.grid()

        #### Bind

        self.canvas.bind("<MouseWheel>", self.zoom)
        self.canvas.bind("<ButtonPress-1>", self.init_drag)
        self.canvas.bind("<B1-Motion>", self.drag)

    def toolbar(self):
        ########################################## On crée la toolbar  ###################################

        ############### Bouton route #################

        self.Icon_Route = Image.open(
            "C:/Users/adino/PycharmProjects/pythonProject/Banque d'image interface/Icone_Route.png")
        self.Icon_Route = CTkImage(self.Icon_Route, size=(45, 45))

        self.Stylo_Route = CTkButton(self.tool, width=45, height=45, text="", image=self.Icon_Route,
                                     command=self.stylo_route, bg_color="lightgrey", corner_radius=3, border_width=2,
                                     border_color="#1F6AA5", hover_color="yellow")

        self.Stylo_Route.place(x=10, y=10.5, anchor="nw")

        # On crée les zones de texte utile pour le bouton route

        self.Text_Route_Info_1 = CTkTextbox(self.tool, width=25, height=10, corner_radius=0, fg_color="lightgrey",
                                            bg_color="lightgrey", font=("Arial", 10), text_color="black")

        self.Text_Route_Info_1.insert("0.1", " N °")
        self.Text_Route_Info_1.configure(state="disabled")
        self.Text_Route_Info_1.place(x=80, y=9.2)

        # On crée les combobox du nombre de voie
        self.Combobox_Route_Info_1 = CTkComboBox(self.tool, width=36, height=16, values=['0', '1', '2', '3'],
                                                 text_color="black", bg_color="lightgrey", fg_color="lightgrey",
                                                 corner_radius=4, border_width=1, dropdown_fg_color="lightgrey",
                                                 dropdown_text_color="black", border_color="black", font=("Arial", 10))
        self.Combobox_Route_Info_1.place(x=110, y=10.8)

        # Zone de texte

        self.Box_Longeur_Route = CTkTextbox(self.tool, width=58, height=21, corner_radius=3,
                                           fg_color="lightgrey", border_color="black", border_width=1,
                                           bg_color="lightgrey", font=("Arial", 8), text_color="black")

        self.Box_Longeur_Route.insert("0.1", " Longeur m")
        self.Box_Longeur_Route.place(x=183, y=10.5)

        # On crée le bouton qui permet de faire une rotation

        self.Icon_Rotation = Image.open(
            "C:/Users/adino/PycharmProjects/pythonProject/Banque d'image interface/Icone_rotation.png")
        self.Icon_Rotation = CTkImage(self.Icon_Rotation, size=(15, 15))

        self.Route_Rotation = CTkButton(self.tool, width=58, height=15, text="", image=self.Icon_Rotation,
                                        command=self.route_rotation, bg_color="lightgrey", corner_radius=3,
                                        border_width=1,
                                        border_color="black", hover_color="yellow", fg_color="lightgrey")

        self.Route_Rotation.place(x=183, y=40.5, anchor="nw")

        # On crée les checkbox pour les cas spéciaux

        self.Checkbox_Route = CTkCheckBox(self.tool, text='Double sens', text_color='black', checkbox_width=8,
                                            checkbox_height=8, corner_radius=1, border_width=1, bg_color="lightgrey",
                                            width=2, border_color='black', checkmark_color='black', font=('Arial', 10))
        self.Checkbox_Route.place(x=86.8, y=40.2)

        ################ Bouton rond point #####################
        self.Icon_Rond_Point = Image.open(
            "C:/Users/adino/PycharmProjects/pythonProject/Banque d'image interface/Icone_Rond_Point.png")
        self.Icon_Rond_Point = CTkImage(self.Icon_Rond_Point, size=(45, 45))

        self.Stylo_Rond_Point = CTkButton(self.tool, width=45, height=45, text="", image=self.Icon_Rond_Point,
                                          command=self.stylo_rond_point, bg_color="lightgrey", corner_radius=3,
                                          border_width=2,
                                          border_color="#1F6AA5", hover_color="yellow")

        self.Stylo_Rond_Point.place(x=270, y=10.5, anchor="nw")

        # On crée les combobox pour le nombre de voies et d'insertion

        self.Combobox_Rond_Point_Info_1 = CTkComboBox(self.tool, width=36, height=14, values=['1', '2', '3'],
                                                      text_color="black", bg_color="lightgrey", fg_color="lightgrey",
                                                      corner_radius=3, border_width=1, dropdown_fg_color="lightgrey",
                                                      dropdown_text_color="black", border_color="black",
                                                      font=("Arial", 9))
        self.Combobox_Rond_Point_Info_1.place(x=350, y=10.2)

        self.Combobox_Rond_Point_Info_2 = CTkComboBox(self.tool, width=36, height=14,
                                                      values=['1', '2', '3', '4', '5', '6'],
                                                      text_color="black", bg_color="lightgrey", fg_color="lightgrey",
                                                      corner_radius=3, border_width=1, dropdown_fg_color="lightgrey",
                                                      dropdown_text_color="black", border_color="black",
                                                      font=("Arial", 9))
        self.Combobox_Rond_Point_Info_2.place(x=350, y=33.2)

        self.Box_Longeur_Rond_Point = CTkTextbox(self.tool, width=58, height=21, corner_radius=3,
                                            fg_color="lightgrey", border_color="black", border_width=1,
                                            bg_color="lightgrey", font=("Arial", 8), text_color="black")

        self.Box_Longeur_Rond_Point.insert("0.1", " Rayon m")
        self.Box_Longeur_Rond_Point.place(x=183, y=10.5)

        # On rajoute le nom des boutons

        self.Text_RP_Voies = CTkTextbox(self.tool, width=70, height=10, corner_radius=0, fg_color="lightgrey",
                                        bg_color="lightgrey", font=("Arial", 10), text_color="black")

        self.Text_RP_Voies.insert("0.1", "Nbr de voies")
        self.Text_RP_Voies.configure(state="disabled")
        self.Text_RP_Voies.place(x=390, y=8.2)

        self.Text_RP_Inser = CTkTextbox(self.tool, width=80, height=10, corner_radius=0, fg_color="lightgrey",
                                        bg_color="lightgrey", font=("Arial", 10), text_color="black")

        self.Text_RP_Inser.insert("0.1", "Nbr d'insertion")
        self.Text_RP_Inser.configure(state="disabled")
        self.Text_RP_Inser.place(x=390, y=43.2)

        #################### Bouton feu rouge #####################

        self.Icon_Feux_Rouge = Image.open(
            "C:/Users/adino/PycharmProjects/pythonProject/Banque d'image interface/Icone_feux_rouge.png")
        self.Icon_Feux_Rouge = CTkImage(self.Icon_Feux_Rouge, size=(45, 45))

        self.Stylo_FeuxRouge = CTkButton(self.tool, width=45, height=45, text="", image=self.Icon_Feux_Rouge,
                                         command=self.stylo_feuxrouge, bg_color="lightgrey", corner_radius=3,
                                         border_width=2,
                                         border_color="#1F6AA5", hover_color="yellow")

        self.Stylo_FeuxRouge.place(x=480, y=10.5, anchor="nw")

        self.Checkbox_direction_feux_haut = CTkCheckBox(self.tool, text='', text_color='black', checkbox_width=8,
                                                        checkbox_height=8, corner_radius=1, border_width=1,
                                                        bg_color="lightgrey",
                                                        width=2, border_color='black', checkmark_color='black',
                                                        font=('Arial', 10))

        self.Checkbox_direction_feux_haut.place(x=596.25, y=5, anchor="nw")

        self.Checkbox_direction_feux_droite = CTkCheckBox(self.tool, text='', text_color='black', checkbox_width=8,
                                                          checkbox_height=8, corner_radius=1, border_width=1,
                                                          bg_color="lightgrey",
                                                          width=2, border_color='black', checkmark_color='black',
                                                          font=('Arial', 10))

        self.Checkbox_direction_feux_droite.place(x=617, y=5, anchor="nw")

        self.Checkbox_direction_feux_gauche = CTkCheckBox(self.tool, text='', text_color='black', checkbox_width=8,
                                                          checkbox_height=8, corner_radius=1, border_width=1,
                                                          bg_color="lightgrey",
                                                          width=2, border_color='black', checkmark_color='black',
                                                          font=('Arial', 10))

        self.Checkbox_direction_feux_gauche.place(x=577, y=5, anchor="nw")

        self.Checkbox_direction_feux_tout = CTkCheckBox(self.tool, text='Toutes directions', text_color='black',
                                                        checkbox_width=8,
                                                        checkbox_height=8, corner_radius=1, border_width=1,
                                                        bg_color="lightgrey",
                                                        width=2, border_color='black', checkmark_color='black',
                                                        font=('Arial', 10))

        self.Checkbox_direction_feux_tout.place(x=555, y=45, anchor="nw")

        self.Icon_Direction_feux_haut = Image.open(
            "C:/Users/adino/PycharmProjects/pythonProject/Banque d'image interface/Icone_direction_haut.png")
        self.Icon_Direction_feux_haut = CTkImage(self.Icon_Direction_feux_haut, size=(16, 16))
        self.Icon_Direction_feux_haut = CTkLabel(self.tool, image=self.Icon_Direction_feux_haut, text='',
                                                 bg_color='lightgrey', height=8)
        self.Icon_Direction_feux_haut.place(x=592, y=25)

        self.Icon_Direction_feux_droite = Image.open(
            "C:/Users/adino/PycharmProjects/pythonProject/Banque d'image interface/Icone_direction_droite.png")
        self.Icon_Direction_feux_droite = CTkImage(self.Icon_Direction_feux_droite, size=(16, 16))
        self.Icon_Direction_feux_droite = CTkLabel(self.tool, image=self.Icon_Direction_feux_droite, text='',
                                                   bg_color='lightgrey', height=8)
        self.Icon_Direction_feux_droite.place(x=612, y=25)

        self.Icon_Direction_feux_gauche = Image.open(
            "C:/Users/adino/PycharmProjects/pythonProject/Banque d'image interface/Icone_direction_gauche.png")
        self.Icon_Direction_feux_gauche = CTkImage(self.Icon_Direction_feux_gauche, size=(16, 16))
        self.Icon_Direction_feux_gauche = CTkLabel(self.tool, image=self.Icon_Direction_feux_gauche, text='',
                                                   bg_color='lightgrey', height=8)
        self.Icon_Direction_feux_gauche.place(x=572, y=25)

        ############### Bouton Passage piéton ################################

        self.Icon_Passage = Image.open(
            "C:/Users/adino/PycharmProjects/pythonProject/Banque d'image interface/Icone_Passage_pieton.png")
        self.Icon_Passage = CTkImage(self.Icon_Passage, size=(45, 45))

        self.Stylo_Passage = CTkButton(self.tool, width=45, height=45, text="", image=self.Icon_Passage,
                                       command=self.stylo_passage, bg_color="lightgrey", corner_radius=3,
                                       border_width=2,
                                       border_color="#1F6AA5", hover_color="yellow")

        self.Stylo_Passage.place(x=670, y=10.5, anchor="nw")

        self.Text_Debit_Haut_Gauche = CTkTextbox(self.tool, width=60, height=10, corner_radius=0,
                                                 fg_color="lightgrey",
                                                 bg_color="lightgrey", font=("Arial", 10), text_color="black")

        self.Text_Debit_Haut_Gauche.insert("0.1", "Débit H/G")
        self.Text_Debit_Haut_Gauche.configure(state="disabled")
        self.Text_Debit_Haut_Gauche.place(x=740, y=10.2)

        self.Text_Debit_Bas_Droite = CTkTextbox(self.tool, width=60, height=10, corner_radius=0,
                                                fg_color="lightgrey",
                                                bg_color="lightgrey", font=("Arial", 10), text_color="black")

        self.Text_Debit_Bas_Droite.insert("0.1", "Débit B/D")
        self.Text_Debit_Bas_Droite.configure(state="disabled")
        self.Text_Debit_Bas_Droite.place(x=740, y=43.2)

        self.Box_Debit_Haut_Gauche = CTkTextbox(self.tool, width=40, height=1, corner_radius=4,
                                                fg_color="lightgrey", border_color="black", border_width=1,
                                                bg_color="lightgrey", font=("Arial", 8), text_color="black")

        self.Box_Debit_Haut_Gauche.insert("0.1", "V/Min")
        self.Box_Debit_Haut_Gauche.place(x=795, y=10.2)

        self.Box_Debit_Bas_Droite = CTkTextbox(self.tool, width=40, height=1, corner_radius=4,
                                               fg_color="lightgrey", border_color="black", border_width=1,
                                               bg_color="lightgrey", font=("Arial", 8), text_color="black")

        self.Box_Debit_Bas_Droite.insert("0.1", "V/Min")
        self.Box_Debit_Bas_Droite.place(x=795, y=43.2)

        ############### Bouton Départ ###############################

        self.Icon_Depart = Image.open(
            "C:/Users/adino/PycharmProjects/pythonProject/Banque d'image interface/Icone_depart.png")
        self.Icon_Depart = CTkImage(self.Icon_Depart, size=(45, 45))

        self.Stylo_Depart = CTkButton(self.tool, width=45, height=45, text="", image=self.Icon_Depart,
                                      command=self.stylo_depart, bg_color="lightgrey", corner_radius=3,
                                      border_width=2,
                                      border_color="#1F6AA5", hover_color="yellow")

        self.Stylo_Depart.place(x=865, y=10.5)

        self.Text_Debit_Depart = CTkTextbox(self.tool, width=60, height=10, corner_radius=0,
                                            fg_color="lightgrey",
                                            bg_color="lightgrey", font=("Arial", 10), text_color="black")

        self.Text_Debit_Depart.insert("0.1", "Débit V/min")
        self.Text_Debit_Depart.configure(state="disabled")
        self.Text_Debit_Depart.place(x=930, y=10.2)

        self.Box_Debit_Depart = CTkTextbox(self.tool, width=53, height=1, corner_radius=4,
                                           fg_color="lightgrey", border_color="black", border_width=1,
                                           bg_color="lightgrey", font=("Arial", 8), text_color="black")

        self.Box_Debit_Depart.insert("0.1", "V/Min")
        self.Box_Debit_Depart.place(x=933, y=43.2)

        ############ Bouton Arivée #########################

        self.Icon_Arrivee = Image.open(
            "C:/Users/adino/PycharmProjects/pythonProject/Banque d'image interface/Icone_arrivee.png")
        self.Icon_Arrivee = CTkImage(self.Icon_Arrivee, size=(45, 45))

        self.Stylo_Arrivee = CTkButton(self.tool, width=45, height=45, text="", image=self.Icon_Arrivee,
                                       command=self.stylo_arrivee, bg_color="lightgrey", corner_radius=3,
                                       border_width=2,
                                       border_color="#1F6AA5", hover_color="yellow")

        self.Stylo_Arrivee.place(x=1010, y=10.5)

        ################### Bouton priorité ######################

        self.Icon_Priorite = Image.open(
            "C:/Users/adino/PycharmProjects/pythonProject/Banque d'image interface/Icone_Priorite.png")
        self.Icon_Priorite = CTkImage(self.Icon_Priorite, size=(45, 45))

        self.Stylo_Priorite = CTkButton(self.tool, width=45, height=45, text="", image=self.Icon_Priorite,
                                        command=self.stylo_priorite, bg_color="lightgrey", corner_radius=3,
                                        border_width=2,
                                        border_color="#1F6AA5", hover_color="yellow")

        self.Stylo_Priorite.place(x=1138, y=10.5, anchor="nw")

        ################### Bouton paramétre ######################

        self.Icon_Parametre = Image.open(
            "C:/Users/adino/PycharmProjects/pythonProject/Banque d'image interface/Icone_parametre.png")
        self.Icon_Parametre = CTkImage(self.Icon_Parametre, size=(45, 45))

        self.Stylo_Parametre = CTkButton(self.tool, width=45, height=45, text="", image=self.Icon_Parametre,
                                         command=self.stylo_parametre, bg_color="lightgrey", corner_radius=3,
                                         border_width=2,
                                         border_color="#1F6AA5", hover_color="yellow")

        self.Stylo_Parametre.place(x=1268, y=10.5, anchor="nw")

        ################### Bouton Départ ######################

        self.Icon_Launch = Image.open(
            "C:/Users/adino/PycharmProjects/pythonProject/Banque d'image interface/Icone_launch.png")
        self.Icon_Launch = CTkImage(self.Icon_Launch, size=(60, 60))

        self.Stylo_Launch = CTkButton(self.tool, width=60, height=60, text="", image=self.Icon_Launch,
                                      bg_color="lightgrey", fg_color="lightgrey", corner_radius=3,
                                      border_color="lightgrey", hover_color="lightgrey")

        self.Stylo_Launch.place(x=1370, y=3.5, anchor="nw")

    def grid(self):

        # Lignes verticales

        for i in range(1, int(self.canvas_width / self.interval)):
            self.canvas.create_line(i * self.interval, 0, i * self.interval, self.canvas_height,
                                    fill="black", width=1, smooth=True, dash=(2, 2))

        # Lignes horizontales

        for i in range(1, int(self.canvas_height / self.interval)):
            self.canvas.create_line(0, i * self.interval, self.canvas_width, i * self.interval,
                                    fill="black", width=1, smooth=True, dash=(2, 2))

        # Dessine les canvas

        for i in range(1, self.nbr_canvas):
            self.canvas.create_line(i * 2 * self.winfo_screenwidth(), 0, i * 2 * self.winfo_screenwidth(),
                                    self.canvas_height,
                                    fill="red", width=3)

        for i in range(1, self.nbr_canvas):
            self.canvas.create_line(0, i * 2 * self.winfo_screenheight(), self.canvas_width,
                                    i * 2 * self.winfo_screenheight(),
                                    fill="red", width=3)

    def zoom(self, event):

        factor = 1.1 if event.delta > 0 else 1 / 1.1
        x = self.canvas_width / 2
        y = self.canvas_height / 2

        self.canvas.scale("all", x, y, factor, factor)

    def init_drag(self, event):
        self.drag_x = event.x
        self.drag_y = event.y

    def drag(self, event):
        dx = event.x - self.drag_x
        dy = event.y - self.drag_y

        self.drag_x = event.x
        self.drag_y = event.y

        self.canvas.move("all", dx, dy)

    def stylo_route(self):
        self.stylo = "Stylo_Route"

    def stylo_rond_point(self):
        self.stylo = "Stylo_Rond_Point"

    def stylo_feuxrouge(self):
        self.stylo = "Stylo_FeuxRouge"

    def stylo_priorite(self):
        self.stylo = "Stylo_Priorite"

    def stylo_passage(self):
        self.stylo = "Stylo_PassagePieton"

    def stylo_depart(self):
        self.stylo = "Stylo_Depart"

    def stylo_arrivee(self):
        self.stylo = "Stylo_Arrivee"

    def stylo_parametre(self):
        self.stylo = "Stylo_Parametre"

    def route_rotation(self):
        self.orientation = (self.orientation + 90) % 380


app = CityZen()
app.mainloop()
