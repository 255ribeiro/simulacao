import matplotlib.pyplot as plt
fig, ax = plt.subplots()

from shapely.ops import polygonize
from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from shapely.geometry import MultiLineString
from shapely.geometry import CAP_STYLE, JOIN_STYLE
from shapely.ops import cascaded_union
from shapely.geometry import box
from shapely.geometry import LineString
from shapely.geometry import LinearRing
from shapely.geometry import Point


def plot_coords(coords):
    pts = list(coords)
    x,y = zip(*pts)
    plt.plot(x,y)

def plot_polys(polys):
    for poly in polys:
        if (not getattr(poly, "exterior", None)):
            print("got line?")

        plot_coords(poly.exterior.coords)

        for hole in poly.interiors:
            plot_coords(hole.coords)

boxes = MultiPolygon([box(0, 0, 10,100),
                          box(20,20,30,100)])
plot_polys(boxes)
plt.show()

box1 = box(0, 0, 10,100)
boxi1 = box1.buffer(7, join_style=JOIN_STYLE.mitre)
box2 = box(20,20,30,100)
boxi2 = box2.buffer(7, join_style=JOIN_STYLE.mitre)

plot_polys([box1, boxi1, box2, boxi2])
plt.show()

inter = boxi1.intersection(boxi2)

plot_polys([box1, boxi1, box2, boxi2, inter])
plt.show()