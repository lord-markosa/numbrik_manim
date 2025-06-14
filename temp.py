from manim import *
from utils import *
import numpy as np


class thankyouScene(Scene):
    def construct(self):
        expression = (
            Text("Like, Subscribe and Share!", color=ManimColor("#1099FF"))
            .scale(1.2)
            .move_to(ORIGIN + UP)
        )
        self.play(Write(expression), run_time=2)
        self.wait(4)


class temp(Scene):
    def construct(self):
        lines = [
            Text("Keep doing", font="Pristina", font_size=54),
            Text("to get better...", font="Pristina", font_size=54),
        ]

        self.play(Write(lines[0].move_to(TITLE_TEXT_POSITION)))
        self.play(Write(lines[1].next_to(lines[0], DOWN, buff=0.25)))

        self.wait(1)


# HELPERS FOR COMPLEX SCENES, you can always create your own :)
def get_horizontal_line_to_graph(axes, function, x, width, color):
    result = VGroup()
    line = DashedLine(
        start=axes.c2p(0, function.underlying_function(x)),
        end=axes.c2p(x, function.underlying_function(x)),
        stroke_width=width,
        stroke_color=color,
    )
    dot = Dot().set_color(color).move_to(axes.c2p(x, function.underlying_function(x)))
    result.add(line, dot)
    return result


class Derivatives(Scene):
    def construct(self):
        k = ValueTracker(-3)  # Tracking the end values of stuff to show

        # Adding Mobjects for the first plane
        plane1 = (
            NumberPlane(x_range=[-3, 4, 1], x_length=5, y_range=[-8, 9, 2], y_length=5)
            .add_coordinates()
            .shift(LEFT * 3.5)
        )

        func1 = plane1.plot(lambda x: (1 / 3) * x**3, x_range=[-3, 3], color=RED_C)
        func1_lab = (
            MathTex("f(x)=\\frac{1}{3} {x}^{3}")
            .set(width=2.5)
            .next_to(plane1, UP, buff=0.2)
            .set_color(RED_C)
        )

        moving_slope = always_redraw(
            lambda: plane1.get_secant_slope_group(
                x=k.get_value(),
                graph=func1,
                dx=0.05,
                secant_line_length=4,
                secant_line_color=YELLOW,
            )
        )

        dot = always_redraw(
            lambda: Dot(color=ORANGE).move_to(
                plane1.c2p(k.get_value(), func1.underlying_function(k.get_value()))
            )
        )

        # Adding Mobjects for the second plane
        plane2 = (
            NumberPlane(x_range=[-3, 4, 1], x_length=5, y_range=[0, 11, 2], y_length=5)
            .add_coordinates()
            .shift(RIGHT * 3.5)
        )

        func2 = always_redraw(
            lambda: plane2.plot(
                lambda x: x**2, x_range=[-3, k.get_value()], color=GREEN
            )
        )
        func2_lab = (
            MathTex("f'(x)={x}^{2}")
            .set(width=2.5)
            .next_to(plane2, UP, buff=0.2)
            .set_color(GREEN)
        )

        moving_h_line = always_redraw(
            lambda: get_horizontal_line_to_graph(
                axes=plane2, function=func2, x=k.get_value(), width=4, color=YELLOW
            )
        )

        # Adding the slope value stuff
        slope_value_text = (
            Tex("Slope value: ")
            .next_to(plane1, DOWN, buff=0.1)
            .set_color(YELLOW)
            .add_background_rectangle()
        )

        slope_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1)
            .set_value(func2.underlying_function(k.get_value()))
            .next_to(slope_value_text, RIGHT, buff=0.1)
            .set_color(YELLOW)
        ).add_background_rectangle()

        # Playing the animation
        self.play(
            LaggedStart(
                DrawBorderThenFill(plane1),
                DrawBorderThenFill(plane2),
                Create(func1),
                Write(func1_lab),
                Write(func2_lab),
                run_time=5,
                lag_ratio=0.5,
            )
        )
        self.add(moving_slope, moving_h_line, func2, slope_value, slope_value_text, dot)
        self.play(k.animate.set_value(3), run_time=15, rate_func=linear)
        self.wait()


class TracedPathExample(Scene):
    def construct(self):
        t = ValueTracker(0)

        l1 = 2
        l2 = 2

        omega1 = 2 * PI / 4
        omega2 = np.sqrt(7) * omega1
        omega3 = 8 * omega2

        plane = NumberPlane(
            x_range=[-4, 4, 1], x_length=5, y_range=[-4, 4, 2], y_length=5
        ).add_coordinates()

        # Define rotating lines
        rod1 = always_redraw(
            lambda: Line(
                start=plane.get_origin(),
                end=plane.c2p(
                    l1 * np.cos(omega1 * t.get_value()),
                    l1 * np.sin(omega1 * t.get_value()),
                ),
                color=BLUE,
            )
        )

        rod2 = always_redraw(
            lambda: Line(
                start=rod1.get_end(),
                end=plane.c2p(
                    l1 * np.cos(omega1 * t.get_value())
                    + l2 * np.cos(omega2 * t.get_value()),
                    l1 * np.sin(omega1 * t.get_value())
                    + l2 * np.sin(omega2 * t.get_value()),
                ),
                color=ORANGE,
            )
        )

        # rod3 = always_redraw(
        #     lambda: Line(
        #         start=rod2.get_end(),
        #         end=plane.c2p(
        #             2 * np.cos(omega1 * t.get_value())
        #             + np.cos(omega2 * t.get_value())
        #             + 0.5 * np.cos(omega3 * t.get_value()),
        #             2 * np.sin(omega1 * t.get_value())
        #             + np.sin(omega2 * t.get_value())
        #             + 0.5 * np.sin(omega3 * t.get_value()),
        #         ),
        #         color=ORANGE,
        #     )
        # )

        trace = TracedPath(rod2.get_end, stroke_color=NUMBRIK_COLOR)
        # trace = TracedPath(rod3.get_end)

        t_final = 500

        # self.add(rod1, rod2, rod3, trace)
        self.play(FadeIn(rod1, rod2, trace))
        self.wait(1)
        self.play(t.animate.set_value(t_final), run_time=2 * t_final, rate_func=linear)
        self.wait(1)
        # circ = Circle(color=RED).shift(4 * LEFT)
        # dot = Dot(color=RED).move_to(circ.get_start())
        # rolling_circle = VGroup(circ, dot)
        # trace = TracedPath(circ.get_start)
        # rolling_circle.add_updater(lambda m: m.rotate(-0.3))
        # self.add(trace, rolling_circle)
        # self.play(rolling_circle.animate.shift(8 * RIGHT), run_time=4, rate_func=linear)


class Question(Scene):
    def construct(self):
        animateTextSeq(
            self,
            [
                MathTex("\\text{Solve:}"),
                MathTex("x(y+z) = 44"),
                MathTex("y(z+x) = 50"),
                MathTex("z(x+y) = 54"),
            ],
            wait_time=0.1,
        )
        self.wait(1)


class Temp(Scene):
    def construct(self):
        self.play(Write(MathTex("E=mc^2")))
        self.wait(1)
