import tkinter as tk
import random

# Liste de mots prédéfinis
word_list = ["python", "informatique", "programmation", "jeu", "ordinateur", "gagner", "apprentissage"]

# Fonction pour choisir un mot aléatoire
def choose_word():
    return random.choice(word_list)

# Fonction pour commencer un nouveau jeu
def new_game():
    global word_to_guess
    word_to_guess = choose_word()
    update_display()

# Fonction pour vérifier la tentative du joueur
def check_guess():
    user_guess = guess_entry.get()
    if user_guess == word_to_guess:
        result_label.config(text="Bravo ! Vous avez deviné le mot.")
    else:
        result_label.config(text="Essayez à nouveau. Vous avez {} tentatives restantes.".format(max_attempts - attempts.get()))
        attempts.set(attempts.get() + 1)
        if attempts.get() >= max_attempts:
            result_label.config(text="Vous avez atteint le nombre maximal de tentatives. Le mot était '{}'.".format(word_to_guess))

# Fonction pour mettre à jour l'affichage
def update_display():
    word_display.config(text="Mot à deviner: " + "*" * len(word_to_guess))
    attempts.set(1)
    result_label.config(text="Un nouveau jeu a commencé. Vous avez {} tentatives.".format(max_attempts))

# Configuration du nombre maximal de tentatives
max_attempts = 5

# Création de la fenêtre principale
window = tk.Tk()
window.title("Jeu de devinette de mots")

# Sélection d'un mot aléatoire pour commencer
word_to_guess = choose_word()

# Création des widgets
word_display = tk.Label(window, text="Mot à deviner: " + "*" * len(word_to_guess))
guess_label = tk.Label(window, text="Entrez votre devinette :")
guess_entry = tk.Entry(window)
check_button = tk.Button(window, text="Vérifier", command=check_guess)
result_label = tk.Label(window, text="Bienvenue ! Vous avez {} tentatives.".format(max_attempts))
new_game_button = tk.Button(window, text="Nouveau jeu", command=new_game)

# Variable pour le suivi du nombre de tentatives
attempts = tk.IntVar()

# Placement des widgets dans la fenêtre
word_display.pack()
guess_label.pack()
guess_entry.pack()
check_button.pack()
result_label.pack()
new_game_button.pack()

# Démarrer un nouveau jeu à l'ouverture de la fenêtre
new_game()

# Démarrer la boucle principale de l'interface graphique
window.mainloop()
