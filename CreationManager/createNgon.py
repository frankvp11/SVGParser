
from nicegui import ui
from GraphicMaker.main import SVG, NGon


class CreateNgon:
    def __init__(self, svg_instance):
        self.x = 0
        self.y = 0 
        self.fill = "red"
        self.radius = 10
        self.sides = 5
        self.svg = svg_instance
        self.held = False

        with self.svg:
            self.shape = NGon(self.x, self.y, self.radius, self.sides, fill=self.fill)
            self.shape.on("svg:pointerdown", self.handle_pointerdown)
            self.shape.on("svg:pointerup", self.handle_pointerup)
            self.shape.on("svg:pointermove", self.handle_pointermove)
            self.shape.on("svg:pointerleave", self.handle_pointerup)

        self.ui_updater()

    def handle_pointermove(self, e):
        if self.held:
            self.x = e.args["image_x"]
            self.y = e.args["image_y"]
            self.x_slider.value = self.x
            self.y_slider.value = self.y

            self.update()

    def handle_pointerdown(self):
        self.held = True
    
    def handle_pointerup(self):
        self.held = False

    def update(self):
        self.shape.x = self.x
        self.shape.y = self.y
        self.shape.radius = self.radius
        self.shape.sides = self.sides
        self.shape._props["cx"] = self.x
        self.shape._props["cy"] = self.y
        self.shape._props["radius"] = self.radius
        self.shape._props["sides"] = self.sides
        self.shape._props['points'] = self.shape.get_points()
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
        with ui.row().style("width: 90%;"):
            ui.label("Radius")
            ui.slider(value=0, min=0, max=100, step=1, on_change=lambda e : self.update_props("radius", e.sender.value)).style("width: 90%;")
        with ui.row().style("width: 90%;"):
            ui.label("Sides")
            ui.slider(value=0, min=0, max=100, step=1, on_change=lambda e : self.update_props("sides", e.sender.value)).style("width: 90%;")
        with ui.row():
            ui.label("Fill")
            with ui.button(icon='colorize') as button:
                ui.color_picker(on_pick=lambda e : self.update_props("fill", e.color))
        with ui.row():
            ui.button("Delete", on_click=lambda e : self.svg.remove_child(self.shape))
