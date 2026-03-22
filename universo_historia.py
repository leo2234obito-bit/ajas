from __future__ import annotations

import os
import sys
import textwrap
import time
from dataclasses import dataclass


@dataclass(frozen=True)
class Etapa:
    titulo: str
    tiempo: str
    descripcion: str


ETAPAS = [
    Etapa(
        "El gran comienzo",
        "Hace 13.800 millones de años",
        (
            "Todo lo que hoy existe estaba comprimido en un estado extremadamente "
            "denso y caliente. Entonces ocurrió la expansión inicial que conocemos "
            "como Big Bang. No fue una explosión en un punto del espacio: fue el "
            "propio espacio empezando a expandirse."
        ),
    ),
    Etapa(
        "Las primeras partículas",
        "Primeros segundos",
        (
            "Mientras el universo se enfriaba, aparecieron partículas como protones, "
            "neutrones y electrones. La energía empezó a transformarse en materia y "
            "se formaron las piezas básicas de los átomos."
        ),
    ),
    Etapa(
        "Nacen los átomos",
        "380.000 años después",
        (
            "Los electrones pudieron unirse a los núcleos y nacieron los primeros "
            "átomos, sobre todo de hidrógeno y helio. La luz comenzó a viajar con más "
            "libertad, dejando una huella que hoy detectamos como radiación de fondo."
        ),
    ),
    Etapa(
        "La edad oscura",
        "Decenas de millones de años",
        (
            "Todavía no había estrellas. El universo estaba lleno de gas y lentamente "
            "la gravedad fue reuniendo materia en regiones más densas, preparando el "
            "escenario para encender las primeras luces cósmicas."
        ),
    ),
    Etapa(
        "Las primeras estrellas",
        "100 a 200 millones de años después",
        (
            "La gravedad comprimió grandes nubes de gas hasta que nacieron las "
            "primeras estrellas. En sus núcleos comenzó la fabricación de elementos "
            "más pesados que el hidrógeno y el helio."
        ),
    ),
    Etapa(
        "Galaxias y reciclaje cósmico",
        "Cientos de millones a miles de millones de años",
        (
            "Las estrellas se agruparon en galaxias. Algunas murieron en explosiones "
            "enormes, esparciendo carbono, oxígeno, hierro y otros elementos que más "
            "adelante formarían planetas, océanos y seres vivos."
        ),
    ),
    Etapa(
        "El nacimiento del Sistema Solar",
        "Hace 4.600 millones de años",
        (
            "Una nube de gas y polvo colapsó y formó el Sol. A su alrededor, el resto "
            "del material se fue uniendo para crear planetas, lunas, asteroides y "
            "cometas. Entre ellos apareció la Tierra."
        ),
    ),
    Etapa(
        "La Tierra y la vida",
        "Hace más de 3.500 millones de años",
        (
            "Nuestro planeta se enfrió, aparecieron océanos y, con el tiempo, surgieron "
            "las primeras formas de vida. Tras una historia larguísima de cambios, la "
            "evolución dio lugar a la diversidad biológica que conocemos hoy."
        ),
    ),
    Etapa(
        "Humanidad y conciencia cósmica",
        "Presente",
        (
            "Muchísimo tiempo después, los seres humanos empezamos a observar el cielo, "
            "a construir telescopios y a preguntarnos por nuestro origen. Al estudiar "
            "el universo, el universo se contempla a sí mismo a través de nosotros."
        ),
    ),
]


ANCHO = 74


def imprimir_bloque(texto: str) -> None:
    print(textwrap.fill(texto, width=ANCHO))



def pausa_animada(segundos: float = 1.0, pasos: int = 3) -> None:
    espera = max(segundos / max(pasos, 1), 0)
    for _ in range(pasos):
        print(".", end="", flush=True)
        time.sleep(espera)
    print("\n")



def mostrar_etapa(numero: int, etapa: Etapa) -> None:
    print("=" * ANCHO)
    print(f"Etapa {numero}: {etapa.titulo}")
    print(f"Momento: {etapa.tiempo}")
    print("-" * ANCHO)
    imprimir_bloque(etapa.descripcion)
    print()



def pedir_modo() -> str:
    print("Descubramos poco a poco la historia del universo.")
    print("Elige cómo quieres avanzar:")
    print("  1. Paso a paso (tú decides cuándo continuar)")
    print("  2. Automático (el programa hace pequeñas pausas)")
    while True:
        opcion = input("Selecciona 1 o 2: ").strip()
        if opcion in {"1", "2"}:
            return opcion
        print("Opción no válida. Escribe 1 o 2.")



def recorrer_historia(modo: str) -> None:
    for indice, etapa in enumerate(ETAPAS, start=1):
        mostrar_etapa(indice, etapa)
        if indice == len(ETAPAS):
            continue

        if modo == "1":
            input("Pulsa Enter para descubrir la siguiente etapa... ")
            print()
        else:
            print("Preparando la siguiente etapa", end="", flush=True)
            pausa_animada(1.2)



def mostrar_cierre() -> None:
    print("=" * ANCHO)
    imprimir_bloque(
        "La historia del universo sigue escribiéndose. Cada nueva observación, "
        "cada misión espacial y cada pregunta que hacemos añade una pequeña pieza "
        "a un relato inmenso."
    )
    print("=" * ANCHO)



def main() -> None:
    modo = pedir_modo()
    print()
    recorrer_historia(modo)
    mostrar_cierre()


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.stdout = None  # type: ignore[assignment]
        os._exit(1)
