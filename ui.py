from ursina import Entity, Text, color, camera, load_texture
from blocks import BLOCK_ORDER, BLOCKS

# Try to import unlit shader in a version-compatible way
try:
    from ursina.shaders import unlit_shader
except Exception:
    from ursina.shaders.unlit_shader import unlit_shader


class HUD:
    def __init__(self):
        # Crosshair
        self.crosshair = Text(text="+", origin=(0, 0), scale=2, color=color.white)

        # Hint
        self.hint = Text(
            text="1-9 / Scroll  |  F5 Save  |  F9 Load  |  ESC Menu",
            position=(-0.88, 0.45),
            scale=1.2,
            background=True
        )
        self.hint.background.color = color.rgba(0, 0, 0, 140)

        # Hotbar container
        self.hotbar = Entity(parent=camera.ui, y=-0.42)

        self.slots = []
        self.n = min(9, len(BLOCK_ORDER))

        slot_size = 0.085
        gap = 0.012
        total_w = self.n * slot_size + (self.n - 1) * gap
        start_x = -total_w / 2 + slot_size / 2

        for i in range(self.n):
            x = start_x + i * (slot_size + gap)

            slot = Entity(
                parent=self.hotbar,
                model='quad',
                scale=(slot_size, slot_size),
                x=x,
                color=color.rgba(20, 20, 20, 200),
                z=0.01
            )
            self.slots.append(slot)

            block_name = BLOCK_ORDER[i]
            tex_path = BLOCKS[block_name]["texture"]

            # Load texture reliably
            tex = load_texture(tex_path)
            if not tex:
                tex = load_texture(tex_path.replace("assets/", ""))

            Entity(
                parent=slot,
                model='quad',
                texture=tex,
                scale=(0.78, 0.78),
                color=color.white,
                z=-0.01,
                shader=unlit_shader,  # ✅ not affected by lighting
            )

            # number label
            Text(
                text=str(i + 1),
                parent=slot,
                origin=(-0.5, 0.5),
                x=-0.42,
                y=0.42,
                scale=0.9,
                color=color.white
            )

        # Selection outline (doesn't hide icon)
        self.selector = Entity(
            parent=self.hotbar,
            model='quad',
            scale=(slot_size + 0.01, slot_size + 0.01),
            color=color.white,
            wireframe=True,
            z=-0.02
        )

        self.selected_name = Text(text="", parent=camera.ui, y=-0.335, scale=1.4)
        self.set_selected(0)

    def set_selected(self, idx: int):
        idx = max(0, min(idx, self.n - 1))
        self.selector.x = self.slots[idx].x
        self.selected_name.text = f"Selected: {BLOCK_ORDER[idx]}"
