
from GraphicMaker.main import SVG, Circle, Rectangle, Line, NGon, Group, Polygon, PolyLine, Oval, Text
from nicegui import ui


svg = SVG(width=400.0, height=300.0, viewBox={'x': 0, 'y': 0, 'width': 400.0, 'height': 300.0})
with svg:
  group = Group(x=0.0, y=0.0)
  with group:
      Rectangle(x=0.0, y=0.0, width=100.0, height=50.0, fill='red', stroke='black', stroke_width=1)
      Circle(x=50.0, y=100.0, radius=30.0, fill='red', stroke='black', stroke_width=1, x_scale_factor=1, y_scale_factor=1, rotate_angle=0, skew_angle_x=0, skew_angle_y=0, flip_x=False, flip_y=False)
      Oval(200.0, 100.0,rx=40.0, ry=20.0, fill='yellow', stroke='red', stroke_width=1)
      Line(x1=300.0, y1=50.0, x2=400.0, y2=100.0, fill='black', stroke='orange', stroke_width=4.0, x_scale_factor=1, y_scale_factor=1, rotate_angle=0, translate_x=0, translate_y=0, x_skew_factor=0, y_skew_factor=0, flip_x=False, flip_y=False)
      PolyLine(points='100,200 150,250 200,200 250,250', fill='none')
      Polygon(points='300,200 350,250 400,200', fill='green', stroke='black', stroke_width=1)
  Text(x=50.0, y=250.0, text='Hello, SVG!', font_size=20.0, fill='black', stroke='black', stroke_width=1, centered=False)
  group = Group(x=100, y=0.0)
  with group:
      Rectangle(x=0.0, y=0.0, width=100.0, height=50.0, fill='blue', stroke='black', stroke_width=1)
      Circle(x=50.0, y=100.0, radius=30.0, fill='red', stroke='black', stroke_width=1, x_scale_factor=1, y_scale_factor=1, rotate_angle=0, skew_angle_x=0, skew_angle_y=0, flip_x=False, flip_y=False)
      Oval(200.0, 100.0,rx=40.0, ry=20.0, fill='yellow', stroke='red', stroke_width=1)
      Line(x1=300.0, y1=50.0, x2=400.0, y2=100.0, fill='black', stroke='orange', stroke_width=4.0, x_scale_factor=1, y_scale_factor=1, rotate_angle=0, translate_x=0, translate_y=0, x_skew_factor=0, y_skew_factor=0, flip_x=False, flip_y=False)
      PolyLine(points='100,200 150,250 200,200 250,250', fill='none')
      Polygon(points='300,200 350,250 400,200', fill='green', stroke='black', stroke_width=1)


ui.run()

