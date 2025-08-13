from manim import *


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

        trace = TracedPath(rod2.get_end, stroke_color=BLUE_D)
        # trace = TracedPath(rod3.get_end)

        t_final = 10

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
