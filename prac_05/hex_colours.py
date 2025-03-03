COLOUR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "Amaranth": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Beaver": "#9f8170",
    "Beige": "#f5f5dc",
    "Black": "#000000",
    "Bole": "#79443b",
}
print(COLOUR_TO_HEX)

COLOUR_TO_HEX_LOWER = {colour.lower(): hex for colour, hex in COLOUR_TO_HEX.items()} # Convert all keys of COLOUR_TO_HEX to lowercase

colour_name = input("Enter colour name: ").lower().strip()
while colour_name != "":
    try:
        print(f"{colour_name} is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print(f"{colour_name} is not a valid colour.")
    colour_name = input("Enter colour name: ").lower().strip()
