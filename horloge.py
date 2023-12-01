
def afficher_heure(heure, mode_24h=True):
    if mode_24h:
        heure_str = "{:02}:{:02}:{:02}".format(heure[0], heure[1], heure[2])
    else:
        heure_str = "{:02}:{:02}:{:02} {}".format(
            (heure[0] % 12) if heure[0] % 12 != 0 else 12,
            heure[1],
            heure[2],
            "AM" if heure[0] < 12 else "PM"
        )
    return heure_str

# Exemple d'utilisation
heure = (16, 30, 0)
print("Mode affichage 12h:", afficher_heure(heure, mode_24h=False))
print("Mode affichage 24h:", afficher_heure(heure))
