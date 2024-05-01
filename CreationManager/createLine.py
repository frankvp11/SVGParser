
from nicegui import ui
from GraphicMaker.main import SVG, Line

class CreateLine:
    def __init__(self, svg_instance):
        self.x1 = 0
        self.y1 = 0 
        self.fill = "red"
        self.x2 = 0
        self.y2 = 0
        self.stroke_width = 1
        self.svg = svg_instance
        self.held = False

        with self.svg:

            self.shape = Line(self.x1, self.y1, self.x2, self.y2 , fill=self.fill)
            self.shape.on("svg:pointerdown", self.handle_pointerdown)
            self.shape.on("svg:pointerup", self.handle_pointerup)
            self.shape.on("svg:pointermove", self.handle_pointermove)
            self.shape.on("svg:pointerleave", self.handle_pointerup)

        self.ui_updater()

    def handle_pointermove(self, e):
        if self.held:
            print(e)
            temp_x = e.args["image_x"]
            temp_y = e.args["image_y"]
            dx = temp_x - self.x1
            dy = temp_y - self.y1
            self.x2 += dx
            self.y2 +=  dy
            self.x1 = temp_x
            self.y1 = temp_y
            self.x1_slider.value = self.x1
            self.y1_slider.value = self.y1
            self.x2_slider.value = self.x2
            self.y2_slider.value = self.y2
            
            

            self.update()

    def handle_pointerdown(self):
        self.held = True
    
    def handle_pointerup(self):
        self.held = False

    def update(self):
        self.shape._props["x1"] = self.x1
        self.shape._props["y1"] = self.y1
        self.shape._props["x2"] = self.x2
        self.shape._props["y2"] = self.y2
        self.shape._props['stroke-width'] = self.stroke_width
        self.shape._props["fill"] = self.fill
        self.shape.update()
    
    def update_props(self, prop, value):
        setattr(self, prop, value)
        self.update()
    
    
    def ui_updater(self):
        with ui.row().style("width: 100%;"):
            ui.label("X1")
            self.x1_slider = ui.slider(value=0, min=0, max=1000, step=1, on_change=lambda e : self.update_props("x1", e.sender.value)).style("width: 90%;")
        with ui.row().style("width: 90%;"):
            ui.label("Y1")
            self.y1_slider = ui.slider(value=0, min=0, max=1000, step=1, on_change=lambda e : self.update_props("y1", e.sender.value)).style("width: 90%;")
        with ui.row().style("width: 90%;"):
            ui.label("X2")
            self.x2_slider = ui.slider(value=0, min=0, max=1000, step=1, on_change=lambda e : self.update_props("x2", e.sender.value)).style("width: 90%;")
        with ui.row().style("width: 90%;"):
            ui.label("Y2")
            self.y2_slider = ui.slider(value=0, min=0, max=1000, step=1, on_change=lambda e : self.update_props("y2", e.sender.value)).style("width: 90%;")
        with ui.row().style("width: 90%;"):
            ui.label("Stroke Width")
            ui.slider(value=0, min=0, max=100, step=1, on_change=lambda e : self.update_props("stroke_width", e.sender.value)).style("width: 90%;")
        with ui.row():
            ui.label("Fill")
            with ui.button(icon='colorize') as button:
                ui.color_picker(on_pick=lambda e : self.update_props("fill", e.color))
        with ui.row():
            ui.button("Delete", on_click=lambda : self.svg.remove_child(self.shape))

        # with ui.row():
        #     ui.button("Keep", on_click=self.svg.add_child(self.shape))




