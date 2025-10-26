from manim import *
from utils import *


class Cycloid(Scene):
    def construct(self):
        r = 3 / PI
        corr = 1 / config.frame_rate  # missed frame correction

        BL = NumberLine().shift(DOWN * r * 2)  # Base Line

        C = Circle(r, color=GREY_N400).shift(7 * LEFT)
        DL = DashedLine(C.get_center(), C.get_top(), color="#A5ADAD")
        CP = Dot(DL.get_start(), color=GREY_N800)  # Center Point
        TP = Dot(DL.get_end(), color=RED_N).scale(1.2)  # Tracing Point

        Base = Line(r * DOWN + 8 * LEFT, r * DOWN + 8 * RIGHT, color=GREY_N400)

        RC = VGroup(C, DL, CP, TP)  # Rolling Circle

        self.dir = 1  # direction of motion

        def Rolling(m, dt):  # update_function
            theta = self.dir * -PI
            m.rotate(dt * theta, about_point=m[0].get_center()).shift(
                dt * LEFT * theta * r
            )

        Cycloid = TracedPath(TP.get_center, stroke_width=6.5, stroke_color=RED_N)

        self.add(BL, Cycloid, RC, Base)

        RC.add_updater(Rolling)
        self.wait(4.5 + corr)

        RC.suspend_updating(Rolling)
        Cycloid.clear_updaters()


class BrachistochroneDemo(Scene):
    def construct(self):
        R = 2  # radius parameter for cycloid

        # Define start and end points
        A = np.array([-3, 3, 0])
        t = 1.1 * PI
        B = np.array([A[0] + R * (t - np.sin(t)), A[1] - R * (1 - np.cos(t)), 0])

        # Labels for points
        labelA = Text("A", font="Comic Sans MS", color=GREY_N500).next_to(
            A, LEFT, buff=0.5
        )
        labelB = Text("B", font="Comic Sans MS", color=GREY_N500).next_to(
            B, RIGHT, buff=0.5
        )

        # Define curves
        # 1. Straight line
        line = Line(A, B, color=GREEN_N200)

        # 2. Arc-like curve (manually defined with function)
        arc = ArcBetweenPoints(A, B, radius=5, color=NUMBRIK_COLOR)

        # 3. Cycloid curve

        cycloid = ParametricFunction(
            lambda t: np.array(
                [A[0] + R * (t - np.sin(t)), A[1] - R * (1 - np.cos(t)), 0]
            ),
            t_range=[0, t],
            color=GREY_N800,
        )

        # Show curves
        self.play(
            FadeIn(labelA, labelB),
            Create(Dot(A, radius=0.05, color=GREY_N800)),
            Create(Dot(B, radius=0.05, color=GREY_N800)),
        )
        self.play(Create(cycloid))
        self.wait(2)

        # Animate balls moving along curves
        dot_line = Dot(A, radius=0.1, color=GREEN_N200)
        dot_arc = Dot(A, radius=0.1, color=NUMBRIK_COLOR)
        dot_cycloid = Dot(A, radius=0.1, color=RED_N)

        self.play(FadeIn(dot_cycloid))

        # Durations (approx, not actual physics)
        time_line = 6.68
        time_arc = 6
        time_cycloid = 5.5

        self.play(
            MoveAlongPath(
                dot_cycloid, cycloid, run_time=time_cycloid, rate_func=rush_into
            ),
        )

        self.wait(2)


class Equations(Scene):
    def construct(self):
        # Flip Y-axis (upside-down plane)
        plane = (
            Axes(
                x_range=[-0.5, 4],
                y_range=[-0.5, 4],
                x_length=5,
                y_length=4,
                axis_config={
                    "include_ticks": False,
                    "include_numbers": False,
                    "color": GRAY_D,
                    "font_size": 24,
                    "tip_shape": StealthTip,
                },
            )
            .scale(1)
            .flip(RIGHT)
            .to_edge(LEFT)
        )  # flips y-axis
        self.add(plane)

        # Define circle arc: center at (0,3), radius = 3
        arc = ArcBetweenPoints(
            start=plane.get_origin(),
            end=plane.c2p(3, 3),
            angle=PI / 2,
            radius=6,
            color=NUMBRIK_COLOR,
        )
        self.play(Create(arc))

        # Dot that moves along arc
        dot = Dot(ORIGIN, color=RED_N100)

        # Move dot along arc, stop halfway
        path_anim = MoveAlongPath(dot, arc, run_time=3, rate_func=linear)
        self.play(path_anim, run_time=2)  # stop before reaching the end

        point = dot.get_center()

        velocity_arrow = Arrow(
            start=point,
            end=point + 2 * (DOWN * np.sin(PI / 12) + RIGHT * np.cos(PI / 12)),
            buff=0,
            color=GREY_N400,
        )

        # Horizontal dashed line (left to y-axis)
        vert_line = DashedLine(start=point, end=plane.c2p(3, 0), color=GREY_N400)
        horiz_line = DashedLine(start=point, end=plane.c2p(0, 3), color=GREY_N400)

        labely = nText("y").next_to(vert_line, RIGHT, buff=0.4)
        labelx = nText("x").next_to(horiz_line, DOWN, buff=0.4)
        labelv = nText("v").next_to(velocity_arrow, DOWN, buff=-0.1)

        self.play(GrowArrow(velocity_arrow), FadeIn(labelv))

        # Vertical dashed line (down to x-axis)
        self.play(Create(vert_line), Create(horiz_line), FadeIn(labelx), FadeIn(labely))

        equation = nMath("\\frac{1}{2}mv^2 = mgy").to_edge(UP).shift(3.5 * RIGHT)
        equation2 = nMath("T = \\int_{A}^{B}vds").next_to(equation, DOWN, buff=0.5)
        equation3 = nMath("ds = \\sqrt{dx^2 + dy^2}").next_to(equation2, DOWN, buff=0.5)
        equation4 = nMath("T = \\int_{A}^{B}\\sqrt{\\frac{1+y'^2}{2gy}}dx").next_to(
            equation3, DOWN, buff=0.5
        )

        self.play(fadeInTex(equation))
        self.wait(1)

        self.play(fadeInTex(equation2))
        self.wait(1)

        self.play(fadeInTex(equation3))
        self.wait(1)

        self.play(fadeInTex(equation4))
        self.wait(1)

        self.wait(4)
