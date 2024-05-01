from nicegui import ui
from GraphicMaker.main import SVG, Rectangle



class CreateRectangle:
    def __init__(self, svg_instance):
        self.x = 0
        self.y = 0 
        self.fill = "red"
        self.width = 0
        self.height = 0
        self.svg = svg_instance
        self.held = False

        with self.svg:

            self.shape = Rectangle(self.x, self.y, self.width, self.height , fill=self.fill)
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
        self.shape._props["x"] = self.x
        self.shape._props["y"] = self.y
        self.shape._props["width"] = self.width
        self.shape._props["height"] = self.height
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
            ui.label("Width")
            ui.slider(value=0, min=0, max=100, step=1, on_change=lambda e : self.update_props("width", e.sender.value)).style("width: 90%;")
        with ui.row().style("width: 90%;"):
            ui.label("Height")
            ui.slider(value=0, min=0, max=100, step=1, on_change=lambda e : self.update_props("height", e.sender.value)).style("width: 90%;")
        with ui.row():
            ui.label("Fill")
            with ui.button(icon='colorize') as button:
                ui.color_picker(on_pick=lambda e : self.update_props("fill", e.color))
        with ui.row():
            ui.button("Delete", on_click=lambda : self.svg.remove_child(self.shape))

        # with ui.row():
        #     ui.button("Keep", on_click=self.svg.add_child(self.shape))




