from manim import *
import numpy as np
from utils import *


class StandingWave(Scene):
    def construct(self):
        addBackground(self)
        # Parameters
        num_points = 48

        x_min, x_max = -4, 4
        k = PI / 2  # wave number
        omega = 2  # angular frequency
        amplitude = 1  # wave amplitude

        # Create ValueTracker for time
        t = ValueTracker(0)

        # x positions of the arrows
        xs = np.linspace(x_min, x_max, num_points)

        # Function to create arrows dynamically
        def get_arrows():
            return VGroup(
                *[
                    Arrow(
                        start=[x, 0, 0],
                        end=[
                            x,
                            amplitude * np.sin(k * x) * np.cos(omega * t.get_value()),
                            0,
                        ],
                        buff=0,
                        tip_length=0.12,
                        color=NUMBRIK_COLOR,
                    )
                    for x in xs
                ]
            )

        # Wave equation function
        def wave_func(x):
            return amplitude * np.sin(k * x) * np.cos(omega * t.get_value())

        wave_graph = always_redraw(
            lambda: FunctionGraph(
                wave_func,
                x_range=[x_min, x_max],
                color=BLUE,
                stroke_color=GREEN_N100,
                stroke_width=6,
            )
        )

        nodes = VGroup()
        for x in range(-2, 3, 1):
            nodes.add(Circle(0.25, arc_center=2 * x * RIGHT, color=RED_N100))

        self.add(wave_graph)

        # Arrows on the x-axis representing oscillating particles
        xs = np.linspace(x_min, x_max, num_points)

        # Always redraw the arrows as t changes
        arrows = always_redraw(get_arrows)

        # Draw a base line for reference
        base_line = Line([x_min - 0.5, 0, 0], [x_max + 0.5, 0, 0], color=GREY_N400)

        # Add everything to the scene
        self.add(base_line, arrows)

        # Animate t increasing smoothly
        # Animate t increasing smoothly while creating nodes
        self.play(
            t.animate.increment_value(PI),
            Create(nodes),
            run_time=3,
            rate_func=linear,
        )
        self.play(t.animate.increment_value(PI), run_time=3, rate_func=linear)
        self.wait()


class CosineModePlot(Scene):
    def construct(self):
        # Parameters
        addBackground(self)
        L = 2

        # Axes setup
        ax = Axes(
            x_range=[-L, L, 1],
            y_range=[-L, L, 1],
            x_length=6,
            y_length=6,
            tips=False,
            axis_config={"color": GREY_D},
        ).add_coordinates()

        # Function definition

        # Generate points where f(x, y) ≈ 0
        # We'll sample a grid of points to approximate the contour
        step = 0.03

        def getdots(n, m):
            def f(x, y):
                return np.cos(n * np.pi * x / L) * np.cos(m * np.pi * y / L) - np.cos(
                    m * np.pi * x / L
                ) * np.cos(n * np.pi * y / L)

            val = VGroup()
            for x in np.arange(-L, L, step):
                for y in np.arange(-L, L, step):
                    if abs(f(x, y)) < 0.05:  # near-zero threshold
                        dot = Dot(
                            ax.coords_to_point(x, y),
                            radius=0.06,
                            color=GREY_N500,
                            fill_opacity=0.5,
                        )
                    val.add(dot)
            return val

        dots = getdots(2, 5)
        self.play(FadeIn(dots), run_time=1.5)
        self.wait(0.5)
        dots2 = getdots(3, 4)

        dots3 = getdots(2, 5)
        self.wait(0.5)
        self.play(Transform(dots, dots2), run_time=1.5)
        self.wait(0.5)
        self.play(Transform(dots, dots3), run_time=1.5)

        # Labels and title
        # eq = MathTex(
        #     r"\cos\left(\frac{n\pi x}{L}\right)\cos\left(\frac{m\pi y}{L}\right)"
        #     r"-\cos\left(\frac{m\pi x}{L}\right)\cos\left(\frac{n\pi y}{L}\right)=0",
        #     color=WHITE
        # ).scale(0.6).to_edge(UP)

        # Add and animate
        # self.play(Write(eq))
        # self.play(FadeIn(dots3))
        # self.wait(1)
        # self.play(Transform(dots, dots2))
        # # self.wait(1)

        # self.play(Transform(dots, dots3))
        self.wait(1)
