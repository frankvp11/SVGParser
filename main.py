import xml.etree.ElementTree as ET
from GraphicMaker.main import SVG, Circle, Rectangle, Line, NGon, Group, Polygon, PolyLine, Oval, Text

def parse_svg(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    return root

def generate_svg_from_element(element):
    if element.tag == "{http://www.w3.org/2000/svg}svg":
        width = float(element.attrib.get("width", 0))
        height = float(element.attrib.get("height", 0))
        svg = SVG(width, height)
        with svg:
            for child in element:
                print(child.tag)
                generate_svg_from_element(child)
        return svg
    
    if element.tag == "{http://www.w3.org/2000/svg}circle":
        x = float(element.attrib.get("cx", 0))
        y = float(element.attrib.get("cy", 0))
        r = float(element.attrib.get("r", 0))
        fill = element.attrib.get("fill", "black")
        return Circle(x, y, r, fill=fill)
        
    if element.tag == "{http://www.w3.org/2000/svg}rect":
        x = float(element.attrib.get("x", 0))
        y = float(element.attrib.get("y", 0))
        width = float(element.attrib.get("width", 0))
        height = float(element.attrib.get("height", 0))
        fill = element.attrib.get("fill", "black")
        return Rectangle(x, y, width, height, fill=fill)
         
    if element.tag == "{http://www.w3.org/2000/svg}line": #     <line x1="300" y1="50" x2="400" y2="100" stroke="orange" stroke-width="4"/>

        x1 = float(element.attrib.get("x1", 0))
        y1 = float(element.attrib.get("y1", 0))
        x2 = float(element.attrib.get("x2", 0))
        y2 = float(element.attrib.get("y2", 0))
        stroke = element.attrib.get("stroke", "black")
        stroke_width = float(element.attrib.get("stroke-width", 1))
        return Line(x1, y1, x2, y2, stroke=stroke, stroke_width=stroke_width)
    
    if element.tag == "{http://www.w3.org/2000/svg}polygon":
        points = element.attrib.get("points", "")
        fill = element.attrib.get("fill", "black")
        return Polygon(points, fill=fill)

    if element.tag == "{http://www.w3.org/2000/svg}polyline":
        points = element.attrib.get("points", "")
        fill = element.attrib.get("fill", "black")
        return PolyLine(points, fill=fill)
    
    if element.tag == "{http://www.w3.org/2000/svg}ellipse":
        cx = float(element.attrib.get("cx", 0))
        cy = float(element.attrib.get("cy", 0))
        rx = float(element.attrib.get("rx", 0))
        ry = float(element.attrib.get("ry", 0))
        fill = element.attrib.get("fill", "black")
        return Oval(cx, cy, rx, ry, fill=fill)
    
    if element.tag == "{http://www.w3.org/2000/svg}g":
        group = Group()
        with group:
            for child in element:
                print(child.tag)
                generate_svg_from_element(child)
        return group

    if element.tag == "{http://www.w3.org/2000/svg}text":
        x = float(element.attrib.get("x", 0))
        y = float(element.attrib.get("y", 0))
        font_size = float(element.attrib.get("font-size", 12))

        text = str(element.text)
        return Text(x, y, text, font_size=font_size)
    
root = parse_svg("svgSample.svg")
svg_instance = generate_svg_from_element(root)


from nicegui import ui

with ui.row():
    svg_instance


ui.run()


# print(svg_instance.to_string())  # Output the generated SVG code
