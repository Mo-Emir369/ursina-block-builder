from ursina import Entity, Button, Text, application, mouse, color, camera

class PauseMenu(Entity):
    def __init__(self, player, on_save, on_load):
        super().__init__(parent=camera.ui, enabled=False)  # camera.ui
        self.player = player
        self.on_save = on_save
        self.on_load = on_load

        self.bg = Entity(parent=self, model='quad', scale=(2, 1.2), color=color.rgba(0,0,0,160))
        Text("Paused", parent=self, y=0.35, scale=2)

        Button(text="Resume", parent=self, y=0.12, scale=(0.4,0.08), on_click=self.hide)
        Button(text="Save (F5)", parent=self, y=0.02, scale=(0.4,0.08), on_click=self.on_save)
        Button(text="Load (F9)", parent=self, y=-0.08, scale=(0.4,0.08), on_click=self.on_load)
        Button(text="Quit", parent=self, y=-0.22, scale=(0.4,0.08), on_click=application.quit)

    def show(self):
        self.enabled = True
        self.player.enabled = False
        mouse.locked = False
        mouse.visible = True

    def hide(self):
        self.enabled = False
        self.player.enabled = True
        mouse.locked = True
        mouse.visible = False
