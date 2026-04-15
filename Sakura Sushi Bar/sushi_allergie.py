import json
from pathlib import Path
from typing import TypedDict

class MenuItem(TypedDict):
    id: str
    nome: str
    categoria: str
    ingredienti: list[str]
    allergeni: list[str]

class MenuTipici(TypedDict):
    id: str
    nome: str
    descrizione: str
    prezzo: float
    composizione: list[str]

class Ristorante(TypedDict):
    nome: str
    citta: str
    cucina: str

class MenuData(TypedDict):
    ristorante: Ristorante
    piatti: list[MenuItem]
    menu_tipici: list[MenuTipici]

def carica_menu(percorso: str) -> dict:
    """
    Carica il file JSON e restituisce il dizionario parsed.
    Gestisce FileNotFoundError e json.JSONDecodeError con messaggi chiari.
    """
    try:
       with open(percorso, "r", encoding="utf-8") as f:
            menu_sakura = json.load(f)
    except FileNotFoundError:
        print("File non trovato — verificare il percorso")
    except json.JSONDecodeError as e:
        print(f"JSON non valido:{e.msg} alla riga{e.lineno}, colonna{e.colno}")

    return menu_sakura

def piatti_con_allergene(piatti: list, allergene: str) -> list:
    """
    Restituisce la lista dei piatti (dict) che contengono l'allergene.
    Il confronto è case-insensitive: "Pesce" e "pesce" sono equivalenti.

    """
    allergene = allergene.lower()
    piatti_allergenici = []
    for piatto in piatti:
        # Se non c'é un allergene ritorno [] così non crasha
        # Ciclo per ogni allergene trovato e lo rendo lowercase
        allergeni_piatto = [a.lower() for a in piatto.get("allergeni", [])]
        if allergene in allergeni_piatto:
            piatti_allergenici.append(piatto)

    return piatti_allergenici

def menu_a_rischio(menu_tipici: list, piatti_per_id: dict, allergene: str) -> list:
    """
    Restituisce una lista di tuple (menu, piatti_problematici) per ogni
    menu tipico che contiene almeno un piatto con l'allergene specificato.
    - menu: il dict del menu tipico
    - piatti_problematici: lista dei dict dei piatti problematici in quel menu
    """
    menu_rischio = []

    for menu in menu_tipici:
        piatti = []
        composizione = menu.get("composizione")

        for piatto in composizione:
            piatti.append(piatti_per_id[piatto])
        allergico = piatti_con_allergene(piatti, allergene)
        if allergico:
            menu_rischio.append((menu, allergico))

    return menu_rischio

def piatti_id_lookup(piatti: list) -> dict:
    lookup = {}
    for piatto in piatti:
        # piatto["allergeni"] è una lista quindi [0]
        lookup[piatto["id"]] = piatto

    return lookup

def main():
    """Carica il menu, chiede l'allergene, stampa i risultati."""
    menu = carica_menu("menu_sakura.json")
    if menu is None:
        return
    # menu e dati sono uguali, cambia solo l'autocomplete per l'ide
    dati: MenuData = menu
    piatti = dati["piatti"]
    menu_tipici = dati["menu_tipici"]

    allergici = piatti_con_allergene(piatti,"pesce")
    lookup = piatti_id_lookup(piatti)
    rischiosi = menu_a_rischio(menu_tipici,lookup,"pesce")



if __name__ == "__main__":
    main()