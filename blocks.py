from ursina import color

BLOCKS = {
    "grass": {"texture": "assets/grass.png", "tint": color.white},
    "stone": {"texture": "assets/stone.png", "tint": color.white},
    "wood":  {"texture": "assets/wood.png",  "tint": color.white},
    "sand":  {"texture": "assets/sand.png",  "tint": color.white},
}

BLOCK_ORDER = list(BLOCKS.keys())
