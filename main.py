import xml.etree.ElementTree as ET
from GraphicMaker.main import SVG, Circle, Rectangle, Line, NGon, Group, Polygon, PolyLine, Oval, Text
from nicegui import ui
from CreationManager.createCircle import CreateCircle
from CreationManager.createRectangle import CreateRectangle
from CreationManager.createLine import CreateLine
from CreationManager.createNgon import CreateNgon
from CreationManager.createText import CreateText



class Canvas:
    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.manager = None
        self.viewBox = {"x":0, "y":0, "width":1000, "height":1000}
        with ui.row().style("width: 100vw; height: 100vh;") as row:
            self.svg = SVG(self.width, self.height, self.viewBox).style("border: 1px solid black; ")
            self.open_drawer()


    def open_drawer(self):
        def handle_change(e):
            if e.value == 'Circle':
                with circle_panel:
                    circle_panel.clear()
                    self.manager = CreateCircle(self.svg)        
                    self.last_shape = self.manager.shape                   
                    # print(self.manager)
            elif e.value == 'Rectangle':
                with rectangle_panel:
                    rectangle_panel.clear()
                    self.manager = CreateRectangle(self.svg)
                    self.last_shape = self.manager.shape
            elif e.value == 'Line':
                with line_panel:
                    line_panel.clear()
                    self.manager = CreateLine(self.svg)
                    self.last_shape = self.manager.shape
            elif e.value == 'NGon':
                with ngon_panel:
                    ngon_panel.clear()
                    self.manager = CreateNgon(self.svg)
                    self.last_shape = self.manager.shape
            elif e.value == 'Text':
                with text_panel:
                    text_panel.clear()
                    self.manager = CreateText(self.svg)
                    self.last_shape = self.manager.shape

        
        with ui.splitter(value=10).style("height: 100%; width: 50%;") as splitter:
            with splitter.before:
                with ui.tabs().props('vertical') as tabs:
                    tabs.style("width: 100%;")
                    circle = ui.tab('Circle', icon='circle')
                    rectangle = ui.tab('Rectangle', icon='rectangle')
                    line = ui.tab('Line', icon='polyline')
                    ngon = ui.tab('NGon', icon='pentagon')
                    # polygon = ui.tab('Polygon', icon='rectangle')
                    text = ui.tab('Text', icon='title')

            with splitter.after:
                with ui.tab_panels(tabs, value=circle, on_change=lambda e: handle_change(e)) \
                        .props('vertical').style("width: 100%;") as tab_panels:
                    with ui.tab_panel(circle).style("width: 100%;") as circle_panel:
                        self.manager = CreateCircle(self.svg)        
                        self.last_shape = self.manager.shape                   

                        print("hello")
                    with ui.tab_panel(rectangle) as rectangle_panel:
                        print("hello")
                    with ui.tab_panel(line) as line_panel:
                        print("Hello")
                    with ui.tab_panel(ngon) as ngon_panel:
                        print("Hello")
                    with ui.tab_panel(text) as text_panel:
                        print("Hello")




# with ui.row():
Canvas()



from svgBox import SVGBox
SVGBox(0, 0, 1000, 1000)







ui.run()

