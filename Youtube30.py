from manim import *
from utils import *


class Template(Scene):
    def construct(self):
        scale = np.sqrt(2) / 5
        r = 5
        a = 4 * scale
        b = 3 * scale
        quarterCircle = Sector(
            radius=r,
            angle=PI / 2,
            stroke_color=GREY_N800,
            stroke_width=4,
        ).move_to(ORIGIN)

        O = quarterCircle.get_corner(DL)

        chord = Line(O + r * UP, O + r * RIGHT, color=GREY_N800)

        # Point on the chord at a distance a from the corner
        A = O + RIGHT * r + a * (UP + LEFT) / np.sqrt(2)
        # Point on the arc at a distance b from A
        B = A + b * (RIGHT + UP) / np.sqrt(2)

        # line of length b perpendicular to the chord
        lineA = Line(A, B, color=GREY_N800)

        # Mid point of the chord
        P = chord.get_center()
        lineOP = Line(O, P, color=GREY_N800)

        # radius line connecting O and B
        radius1 = DashedLine(O, B, color=GREY_N800, dash_length=0.2, dashed_ratio=0.8)

        self.add(
            quarterCircle,
            chord,
            lineA,
            lineOP,
            radius1,
        )

        self.wait(5)
