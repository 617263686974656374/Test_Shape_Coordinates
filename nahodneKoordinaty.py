import tkinter as tk
from tkinter import messagebox
import random

# Príklady s tvarmi a odpoveďami
examples = [
    # 1-10: Štvorce so zvyšnými možnosťami obdĺžniky
    {
        "shape": "square",
        "coordinates": (50, 50, 150, 150),  # Správna odpoveď
        "options": [
            (60, 60, 160, 100),  # Obdĺžnik
            (50, 50, 150, 150),  # Štvorec
            (40, 40, 120, 80)    # Obdĺžnik
        ]
    },
    {
        "shape": "square",
        "coordinates": (100, 100, 200, 200),
        "options": [
            (150, 150, 270, 180),  # Obdĺžnik
            (50, 60, 150, 120),    # Obdĺžnik
            (100, 100, 200, 200)   # Štvorec
        ]
    },
    {
        "shape": "square",
        "coordinates": (200, 200, 300, 300),
        "options": [
            (200, 200, 350, 250),  # Obdĺžnik
            (190, 190, 260, 220),  # Obdĺžnik
            (200, 200, 300, 300)   # Štvorec
        ]
    },
    {
        "shape": "square",
        "coordinates": (150, 50, 250, 150),
        "options": [
            (150, 50, 250, 150),  # Štvorec
            (200, 60, 320, 120),  # Obdĺžnik
            (100, 50, 180, 90)    # Obdĺžnik
        ]
    },
    {
        "shape": "square",
        "coordinates": (300, 100, 400, 200),
        "options": [
            (250, 100, 380, 130),  # Obdĺžnik
            (300, 100, 400, 200),  # Štvorec
            (310, 110, 410, 140)   # Obdĺžnik
        ]
    },
    {
        "shape": "square",
        "coordinates": (50, 250, 150, 350),
        "options": [
            (40, 250, 130, 290),  # Obdĺžnik
            (60, 260, 160, 300),  # Obdĺžnik
            (50, 250, 150, 350)   # Štvorec
        ]
    },
    {
        "shape": "square",
        "coordinates": (200, 50, 300, 150),
        "options": [
            (220, 60, 320, 120),  # Obdĺžnik
            (200, 50, 300, 150),  # Štvorec
            (180, 50, 280, 100)   # Obdĺžnik
        ]
    },
    {
        "shape": "square",
        "coordinates": (250, 250, 350, 350),
        "options": [
            (260, 260, 400, 280),  # Obdĺžnik
            (240, 250, 330, 300),  # Obdĺžnik
            (250, 250, 350, 350)   # Štvorec
        ]
    },
    {
        "shape": "square",
        "coordinates": (100, 300, 200, 400),
        "options": [
            (110, 310, 190, 340),  # Obdĺžnik
            (100, 300, 200, 400),  # Štvorec
            (90, 300, 180, 330)    # Obdĺžnik
        ]
    },
    {
        "shape": "square",
        "coordinates": (50, 50, 100, 100),
        "options": [
            (60, 60, 120, 90),     # Obdĺžnik
            (50, 50, 100, 100),    # Štvorec
            (40, 40, 110, 70)      # Obdĺžnik
        ]
    },

    # 11-20: Obdĺžniky so zvyšnými možnosťami štvorce
    {
        "shape": "rectangle",
        "coordinates": (50, 100, 150, 250),
        "options": [
            (50, 50, 150, 150),    # Štvorec
            (60, 60, 160, 160),    # Štvorec
            (50, 100, 150, 250)    # Obdĺžnik
        ]
    },
    {
        "shape": "rectangle",
        "coordinates": (100, 200, 300, 400),
        "options": [
            (100, 200, 300, 400),  # Obdĺžnik
            (150, 150, 250, 250),  # Štvorec
            (120, 120, 220, 220)   # Štvorec
        ]
    },
    {
        "shape": "rectangle",
        "coordinates": (200, 150, 400, 300),
        "options": [
            (250, 250, 350, 350),  # Štvorec
            (200, 200, 300, 300),  # Štvorec
            (200, 150, 400, 300)   # Obdĺžnik
        ]
    },
    {
        "shape": "rectangle",
        "coordinates": (50, 50, 250, 150),
        "options": [
            (100, 100, 150, 150),  # Štvorec
            (50, 50, 250, 150),    # Obdĺžnik
            (120, 120, 200, 200)   # Štvorec
        ]
    },
    {
        "shape": "rectangle",
        "coordinates": (150, 100, 350, 250),
        "options": [
            (200, 200, 300, 300),  # Štvorec
            (150, 100, 350, 250),  # Obdĺžnik
            (50, 50, 150, 150)     # Štvorec
        ]
    },
    {
        "shape": "rectangle",
        "coordinates": (300, 50, 500, 150),
        "options": [
            (300, 300, 400, 400),  # Štvorec
            (150, 150, 250, 250),  # Štvorec
            (300, 50, 500, 150)    # Obdĺžnik
        ]
    },
    {
        "shape": "rectangle",
        "coordinates": (50, 300, 250, 500),
        "options": [
            (60, 60, 160, 160),    # Štvorec
            (100, 100, 200, 200),  # Štvorec
            (50, 300, 250, 500)    # Obdĺžnik
        ]
    },
    {
        "shape": "rectangle",
        "coordinates": (100, 50, 400, 100),
        "options": [
            (120, 120, 170, 170),  # Štvorec
            (30, 300, 80, 350),    # Štvorec
            (100, 50, 400, 100)    # Obdĺžnik
        ]
    },
    {
        "shape": "rectangle",
        "coordinates": (150, 150, 350, 300),
        "options": [
            (150, 150, 350, 300),  # Obdĺžnik
            (150, 50, 250, 150),   # Štvorec
            (50, 50, 150, 150)     # Štvorec
        ]
    },
    {
        "shape": "rectangle",
        "coordinates": (200, 200, 300, 450),
        "options": [
            (10, 10, 110, 110),    # Štvorec
            (200, 200, 300, 450),  # Obdĺžnik
            (300, 300, 400, 400)   # Štvorec
        ]
    }
]




# Globálne premenné na sledovanie stavu
current_example = 0  # Poradie aktuálneho príkladu
correct_count = 0  # Počet správnych odpovedí
incorrect_count = 0  # Počet nesprávnych odpovedí
random.shuffle(examples)  # Zamiešanie príkladov

def reset_game():
    """Resetuje test na začiatok."""
    global current_example, correct_count, incorrect_count, examples
    current_example = 0
    correct_count = 0
    incorrect_count = 0
    random.shuffle(examples)  # Zamieša príklady
    draw_example()
    update_options()
    restart_button.pack_forget()  # Skryje tlačidlo Reštart

def draw_example():
    """Nakreslí aktuálny príklad na plátno a zobrazí poradie."""
    global current_example
    example = examples[current_example]
    canvas.delete("all")  # Vymaže predchádzajúci tvar

    # Nakreslí tvar podľa typu
    if example["shape"] == "square":
        canvas.create_rectangle(*example["coordinates"], fill="lightblue")
    elif example["shape"] == "rectangle":
        canvas.create_rectangle(*example["coordinates"], fill="lightgreen")

    # Zobrazí aktuálne poradie
    status_label["text"] = f"Objekt {current_example + 1}/{len(examples)}: {example['shape'].capitalize()}"


def check_answer(selected_option):
    """Skontroluje odpoveď študenta."""
    global current_example, correct_count, incorrect_count
    example = examples[current_example]
    if example["options"][selected_option] == example["coordinates"]:
        correct_count += 1
        messagebox.showinfo("Výborne!", "Správna odpoveď!")
    else:
        incorrect_count += 1
        messagebox.showerror("Nesprávne", "Viac sa snaž!")

    current_example += 1
    if current_example < len(examples):
        draw_example()
        update_options()
    else:
        # Zobrazenie výsledkov
        messagebox.showinfo("Koniec!", f"Správne: {correct_count}, Nesprávne: {incorrect_count}")
        restart_button.pack()  # Zobrazí tlačidlo Reštart


def update_options():
    """Aktualizuje možnosti odpovedí."""
    global current_example
    example = examples[current_example]
    for i, btn in enumerate(option_buttons):
        btn["text"] = f"Súradnice: {example['options'][i]}"


# Vytvorenie hlavného okna
window = tk.Tk()
window.title("Test - Súradnice tvarov")

# Vytvorenie plátna
canvas = tk.Canvas(window, width=600, height=600, bg="white")
canvas.pack()

# Zobrazí stav (poradie)
status_label = tk.Label(window, text="")
status_label.pack()

# Tlačidlá s možnosťami
option_buttons = []
for i in range(3):
    btn = tk.Button(window, text="", command=lambda i=i: check_answer(i))
    btn.pack(pady=5)
    option_buttons.append(btn)
    
# Tlačidlo Reštart
restart_button = tk.Button(window, text="Reštart", command=reset_game)

# Spustenie prvého príkladu
draw_example()
update_options()

# Spustenie hlavnej slučky
window.mainloop()
