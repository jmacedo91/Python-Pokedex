from tkinter import *
from tkinter import messagebox
import requests.exceptions
from pokemon import Pokemon
import urllib.request


# Constants
ENTRY_BG = "#3AB47D"
SCREEN_BG = "#98CB98"
BUTTON_BG = "#5E5F5B"

# Creating User Interface
window = Tk()
window.title("Python Pokedex")
window.minsize(width=340, height=493)
window.maxsize(width=340, height=493)

# Pokédex Canvas
pokedex_canvas = Canvas(width=338, height=491, highlightthickness=0)
pokedex_img = PhotoImage(file="pokedex.png")
pokedex_canvas.create_image(169, 245, image=pokedex_img)
pokedex_canvas.place(x=0, y=0)

# Pokédex Entry
pokemon_entry = Entry(width=14, background=ENTRY_BG, justify="center")
pokemon_entry.place(x=97, y=424)
pokemon_entry.focus()

# Pokedex Info
name = Label(text="Name:", bg=SCREEN_BG, font=("Arial", 10, "bold"))
name.place(x=82, y=245)

number = Label(text="ID:", bg=SCREEN_BG, font=("Arial", 10, "bold"))
number.place(x=82, y=265)

element = Label(text="Element:", bg=SCREEN_BG, font=("Arial", 10, "bold"))
element.place(x=82, y=285)

# Pokedex Button


def search():
    global pokemon_img
    pokemon_name = pokemon_entry.get().lower()
    if len(pokemon_name) == 0:
        messagebox.showinfo(title="Empty", message="Please insert the Pokémon name!")
    else:
        try:
            pkm = Pokemon(pokemon_name)
        except requests.exceptions.JSONDecodeError:
            messagebox.showerror(title="Not Found!", message="This Pokémon doesn't exist! Please, review entries!")
        else:
            name.config(text=f"Name: {pkm.specie}")
            number.config(text=f"ID: {pkm.id}")
            element.config(text=f"Element: {pkm.type}")
            pokemon_canvas = Canvas(width=96, height=96, bg=SCREEN_BG, highlightthickness=0)
            urllib.request.urlretrieve(f"{pkm.get_sprite()}", f"pokemon_sprites/{pkm.id}-{pkm.specie}.png")
            pokemon_img = PhotoImage(file=f"pokemon_sprites/{pkm.id}-{pkm.specie}.png")
            pokemon_canvas.create_image(48, 48, image=pokemon_img)
            pokemon_canvas.place(x=120, y=153)


button_img = PhotoImage(file="button.png")

pokedex_btn = Button(image=button_img, command=search, bg=BUTTON_BG, highlightthickness=0)
pokedex_btn.place(x=10, y=356)

window.bind("<Return>",lambda event:search())
window.mainloop()
