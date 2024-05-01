
from nicegui import ui
from GraphicMaker.main import SVG, Text


class CreateText:
    def __init__(self, svg_instance):
        self.x = 0
        self.y = 0 
        self.fill = "red"
        self.text = ""
        self.font_size = 0


        self.svg = svg_instance
        self.held = False

        with self.svg:

            self.shape = Text(self.x, self.y, self.text, self.font_size, fill=self.fill)
        self.ui_updater()


    def update(self):
        self.shape._props["x"] = self.x
        self.shape._props["y"] = self.y
        self.shape._props["text"] = self.text
        self.shape._props["font-size"] = self.font_size
        self.shape._props["fill"] = self.fill
        self.shape.update()
    
    def update_props(self, prop, value):
        setattr(self, prop, value)
        self.update()
    
    
    def ui_updater(self):
        with ui.row().style("width: 100%;"):
            ui.label("X")
            self.x_slider = ui.slider(value=0, min=0, max=1000, step=1, on_change=lambda e : self.update_props("x", e.sender.value)).style("width: 90%;")
        with ui.row().style("width: 90%;"):
            ui.label("Y")
            self.y_slider = ui.slider(value=0, min=0, max=1000, step=1, on_change=lambda e : self.update_props("y", e.sender.value)).style("width: 90%;")
        with ui.row():
            ui.label("Font Size")
            self.font_size_slider = ui.slider(value=0, min=0, max=1000, step=1, on_change=lambda e : self.update_props("font_size", e.sender.value)).style("width: 90%;")
        with ui.row():
            ui.label("Text")
            ui.textarea(placeholder="Text", on_change=lambda e : self.update_props("text", e.value))
        with ui.row():
            ui.label("Fill")
            with ui.button(icon='colorize') as button:
                ui.color_picker(on_pick=lambda e : self.update_props("fill", e.color))
        with ui.row():
            ui.button("Delete", on_click=lambda : self.svg.remove_child(self.shape))





 