from manim import *


class Tut1(Scene):
    def construct(self):
        # Create a number plane (coordinate system)
        plane = NumberPlane(x_range=[-6, 6], y_range=[-4, 6]).add_coordinates()

        # Create a box and move it to the origin
        box = Rectangle(
            width=1,
            height=1,
            color=BLUE,
            fill_opacity=0.5,
            stroke_width=2,
            stroke_color=ORANGE,
        ).move_to(DOWN)

        # Create a dot that always moves to the center of the box
        dot = always_redraw(lambda: Dot().move_to(box.get_center()))

        self.play(FadeIn(plane), run_time=4)
        self.wait()

        self.play(Create(box), run_time=2)
        self.play(Create(dot), run_time=1)
        self.wait()

        self.play(box.animate.shift(RIGHT * 3), run_time=2)
        self.wait()

        self.play(box.animate.shift(UP * 4), run_time=2)
        self.wait()

        self.play(box.animate.shift(4 * DOWN + 3 * LEFT), run_time=2)
        self.wait(2)


class Tut2(Scene):
    def construct(self):
        r = ValueTracker(0.5)  # Tracks the value of the radius

        # Create a circle with the radius r
        circle = always_redraw(
            lambda: Circle(radius=r.get_value(), stroke_color=YELLOW, stroke_width=5)
        )

        # Create a line from the center of the circle to the bottom
        line_radius = always_redraw(
            lambda: Line(
                start=circle.get_center(),
                end=circle.get_bottom(),
                stroke_color=RED_B,
                stroke_width=10,
            )
        )

        # Create a triangle from the center of the circle to the left and right
        triangle = always_redraw(
            lambda: Polygon(
                circle.get_top(),
                circle.get_left(),
                circle.get_right(),
                fill_color=GREEN_C,
            )
        )

        self.play(Create(circle), run_time=2)
        self.play(DrawBorderThenFill(line_radius), run_time=2)
        self.play(DrawBorderThenFill(triangle), run_time=2)

        self.play(r.animate.set_value(2), run_time=5)


class Tut3(Scene):
    def construct(self):
        r = ValueTracker(0.15)  # Tracks the value of the radius
        title = Text("lag_ratio = 0.25").to_edge(UP)

        dot1 = always_redraw(lambda: Dot(point=LEFT * 2 + UP, radius=r.get_value()))

        dot2 = Dot(point=LEFT * 2, radius=r.get_value())
        dot3 = Dot(point=LEFT * 2 + DOWN, radius=r.get_value())

        line_25 = DashedLine(start=LEFT + UP * 2, end=LEFT + DOWN * 2, color=RED)

        label = Text("25%", font_size=24).next_to(line_25, UP)

        self.add(title, dot1, dot2, dot3, line_25, label)

        self.play(r.animate.set_value(0.2), run_time=5)

        self.play(
            LaggedStart(
                dot1.animate.shift(RIGHT * 4),
                dot2.animate.shift(RIGHT * 4),
                dot3.animate.shift(RIGHT * 4),
                lag_ratio=0.25,
                run_time=4,
            )
        )
