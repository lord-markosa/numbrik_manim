from manim import *
from utils import *


class RotatingLiquid(ThreeDScene):
    def construct(self):
        # Step 1: Show 3D paraboloid

        axes3d = ThreeDAxes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            z_range=[0, 4],
            x_length=7,
            y_length=7,
            z_length=3.5,
            axis_config={
                "include_ticks": False,
                "include_numbers": False,
                "color": GRAY_D,
                "font_size": 24,
                "tip_shape": StealthTip,
            },
        )

        paraboloid = Surface(
            lambda u, v: np.array([u * np.cos(v), u * np.sin(v), 0.2 * u**2]),
            u_range=[0, 3.4],
            v_range=[0, TAU],
            checkerboard_colors=[NUMBRIK_COLOR, NUMBRIK_COLOR_50],
            fill_opacity=0.7,
        )

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Create(axes3d), FadeIn(paraboloid))
        self.wait(2)

        # Step 2: Transition to 2D cross-section
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=3)
        self.wait(1)

        axes2d = Axes(
            x_range=[-3, 3],
            y_range=[0, 3],
            x_length=6,
            y_length=3,
            axis_config={"include_tip": False},
        )
        parabola = axes2d.plot(lambda x: 0.2 * x**2, x_range=[-3, 3], color=BLUE)
        parabola_label = axes2d.get_graph_label(
            parabola, "y=ax^2", x_val=2, direction=UR
        )

        self.play(
            FadeOut(axes3d),
            FadeOut(paraboloid),
            FadeIn(axes2d),
            Create(parabola),
            Write(parabola_label),
        )
        self.wait(2)

        # Step 3: Pick a point on parabola and draw tangent
        x0 = 2
        y0 = 0.2 * x0**2
        point = axes2d.coords_to_point(x0, y0)
        dot = Dot(point, color=YELLOW)

        # tangent_line = axes2d.get_tangent_line(x0, parabola, length=4, color=ORANGE)

        # self.play(FadeIn(dot), Create(tangent_line))
        self.wait(1)

        # Step 4: Show forces
        gravity = Arrow(point, point + DOWN * 1.5, buff=0.1, color=RED)
        grav_label = MathTex("mg").next_to(gravity, LEFT)
        centrifugal = Arrow(point, point + RIGHT * 1.5, buff=0.1, color=GREEN)
        cent_label = MathTex("m\\omega^2 r").next_to(centrifugal, UP)

        self.play(GrowArrow(gravity), Write(grav_label))
        self.play(GrowArrow(centrifugal), Write(cent_label))
        self.wait(2)

        # Step 5: Emphasize balance
        balance_text = Text(
            "Surface aligns so forces balance along tangent", font_size=28
        ).to_edge(DOWN)
        self.play(Write(balance_text))
        self.wait(3)


class RotatingLiquid2dScene(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-4, 4],
            y_range=[-1, 5],
            x_length=10,
            y_length=7,
            tips=True,
            axis_config={
                "include_ticks": False,
                "include_numbers": False,
                "color": GRAY_D,
                "font_size": 24,
                "tip_shape": StealthTip,
            },
        )

        parabola = axes.plot(
            lambda x: x**2 / 2, x_range=[-3.1, 3.1], color=NUMBRIK_COLOR
        )

        angular_velocity = CurvedArrow(
            axes.c2p(-0.5, 4), axes.c2p(0.6, 4.1), color=BLACK
        )
        angular_velocity_label = (
            MathTex(
                "\\omega",
                color=BLACK,
            )
            .move_to(axes.c2p(0.5, 3.4))
            .scale(1.3)
        )

        x0 = 1.7
        y0 = x0**2 / 2
        r = 3
        theta = np.arctan(x0)
        pt = axes.c2p(x0, y0)
        tangent = DashedLine(
            axes.c2p(x0 - r * np.cos(theta), y0 - r * np.sin(theta)),
            axes.c2p(x0 + r * np.cos(theta), y0 + r * np.sin(theta)),
            color=BLACK,
        )
        dot = Dot(pt, color=BLACK)

        arrow1 = Arrow(pt, pt + 1.5 * RIGHT, buff=0, color=BLACK)
        arrow2 = Arrow(pt, pt + 2.2 * DOWN, buff=0, color=BLACK)

        angle = Angle(arrow1, tangent, color=BLACK, radius=0.7)
        angle_label = (
            MathTex(
                "\\theta",
                color=BLACK,
            )
            .next_to(angle.get_center(), RIGHT, buff=0.35)
            .shift(0.3 * UP)
            .scale(1.3)
        )

        centri_force = nMath("m\omega^2x").next_to(arrow1, RIGHT)
        grav = nMath("mg").next_to(arrow2, DOWN)

        self.play(
            LaggedStart(
                FadeIn(axes),
                Create(parabola),
                FadeIn(angular_velocity, angular_velocity_label),
                lag_ratio=0.5,
            )
        )

        self.play(
            LaggedStart(
                Create(dot),
                Create(tangent),
                GrowArrow(arrow1),
                GrowArrow(arrow2),
                FadeIn(angle),
                FadeIn(angle_label),
                lag_ratio=0.5,
            )
        )

        self.play(LaggedStart(FadeIn(centri_force), FadeIn(grav), lag_ratio=0.5))

        self.add(
            axes,
            parabola,
            angular_velocity,
            angular_velocity_label,
            tangent,
            dot,
            arrow1,
            arrow2,
            angle,
            angle_label,
            centri_force,
            grav,
        )
        self.wait(10)


class Statements(Scene):
    def construct(self):
        stmt1 = nMath("m\\omega^2x\\cos{\\theta} = mg\\sin{\\theta}").to_edge(UP)
        stmt2 = nMath("\\tan{\\theta} = \\frac{\\omega^2x}{g}").next_to(
            stmt1, DOWN, buff=0.5
        )
        stmt3 = nMath("\\Rightarrow \\frac{dy}{dx} = \\frac{\\omega^2x}{g}").next_to(
            stmt2, DOWN, buff=0.5
        )
        stmt4 = nMath("y = \\frac{\\omega^2}{2g}x^2").next_to(stmt3, DOWN, buff=0.5)

        self.play(fadeInTex(stmt1))
        self.wait(1)
        self.play(fadeInTex(stmt2))
        self.wait(1)
        self.play(fadeInTex(stmt3))
        self.wait(1)
        self.play(fadeInTex(stmt4))
        self.wait(10)
