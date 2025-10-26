from manim import *
from utils import *


class Template(Scene):
    def construct(self):
        axes = getAxis().shift(DOWN)

        theta = ValueTracker(PI / 3)
        z_vector = always_redraw(
            lambda: Arrow(
                axes.get_origin(),
                axes.get_origin()
                + 2.5 * np.sin(theta.get_value()) * UP
                + 2.5 * np.cos(theta.get_value()) * RIGHT,
                color=BLACK,
                buff=0,
            )
        )

        labelz1 = nMath("z = r\\cdot e^{i\\mathbf{\\theta}}").to_edge(UP)
        # self.add(axes)
        # self.add(labelz1)

        # self.add(z_vector)

        axes2 = getAxis(
            [-2, 2],
            [-14, 14],
        ).shift(DOWN + RIGHT)

        angle = always_redraw(
            lambda: Arc(
                0.5, 0, theta.get_value(), arc_center=axes.get_center(), color=BLACK
            )
        )

        label1 = nMath("\\mathbf{\\theta} = \\;").to_edge(UP).shift(LEFT * 0.5)
        label2 = always_redraw(
            lambda: nText(
                "" + str(round(theta.get_value(), 2)),
            ).next_to(label1, RIGHT, buff=0.2)
        )

        labelAngle = (
            nMath(
                "\\mathbf{\\theta}",
            )
            .next_to(angle, RIGHT)
            .shift(UP * 0.2)
        )

        labelR = nMath("r").next_to(z_vector, LEFT, buff=-0.4).shift(UP * 0.2)

        labelZ = always_redraw(
            lambda: nMath("z").move_to(
                axes.get_origin()
                + 2.85 * np.sin(theta.get_value()) * UP
                + 2.85 * np.cos(theta.get_value()) * RIGHT,
            )
        )

        self.add(axes, z_vector, angle, label1, label2, labelAngle, labelR, labelZ)

        # dot = always_redraw(
        #     lambda: Dot(axes2.c2p(1, theta.get_value()), color=GREEN_N200)
        # )

        # path = TracedPath(lambda: axes2.c2p(1, theta.get_value()), stroke_color=BLACK)

        # self.add(dot, axes, z_vector, path)

        # self.play(axes.animate.shift(LEFT * 2 + UP * 2).scale(0.8))
        # self.play(theta.animate.set_value(4 * PI))
        self.wait(5)


class Statements(Scene):
    def construct(self):
        stmt1 = nMath("f(z)", "=", "ln(", "z", ")").to_edge(UP)
        stmt2 = nMath("z = r\\cdot e^{i\\mathbf{\\theta}}").next_to(
            stmt1, DOWN, buff=0.7
        )
        stmt3 = nMath(
            "f(z)", "=", "ln(", "r", "\\cdot", "e^{i\\mathbf{\\theta}}", ")"
        ).next_to(stmt1, 0)
        stmt4 = nMath(
            "f(z)",
            "=",
            "ln(",
            "r",
            ")",
            "+",
            "i\\mathbf{\\theta}",
        ).next_to(stmt1, 0)

        self.play(fadeInTex(stmt1))
        self.wait(1)

        self.play(fadeInTex(stmt2))
        hgl = highlight(
            self, stmt2, buff=0.2, color=RED_N100, wait_time=4, unhighlight=False
        )
        hgl = hgl[0]
        self.play(FadeOut(stmt2, hgl))
        self.wait(1)
        self.play(TransformMatchingTex(stmt1, stmt3), run_time=1.5)
        self.wait(0.5)
        self.play(TransformMatchingTex(stmt3, stmt4), run_time=1.5)

        self.wait(5)


class Intro(Scene):
    def construct(self):
        axes = getAxis()

        theta = ValueTracker(PI / 3)

        z_vector = always_redraw(
            lambda: Arrow(
                axes.get_origin(),
                axes.get_origin()
                + 2.5 * np.sin(theta.get_value()) * UP
                + 2.5 * np.cos(theta.get_value()) * RIGHT,
                buff=0,
            )
            .set_color_by_gradient([GREEN_N100, GREEN_N200])
            .set_sheen_direction(
                np.sin(theta.get_value()) * UP + np.cos(theta.get_value()) * RIGHT,
            )
        )

        labelz1 = nMath("z = r\\cdot e^{i\\mathbf{\\theta}}").to_edge(UP)

        axes2 = getAxis(
            [-2, 2],
            [-14, 14],
        ).shift(DOWN + RIGHT)

        angle = always_redraw(
            lambda: Arc(
                0.5, 0, theta.get_value(), arc_center=axes.get_center(), color=GREY_N400
            )
        )

        label1 = nMath("\\mathbf{\\theta} = \\;").to_edge(UP).shift(LEFT)
        label2 = always_redraw(
            lambda: nText(
                "" + str(round(theta.get_value(), 2)) + " rad",
            ).next_to(label1, RIGHT, buff=0.2)
        )

        labelAngle = (
            nMath(
                "\\mathbf{\\theta}",
            )
            .next_to(angle, RIGHT)
            .shift(UP * 0.2)
        )

        labelR = nMath("r").next_to(z_vector, LEFT, buff=-0.4).shift(UP * 0.2)

        labelZ = always_redraw(
            lambda: nMath("z").move_to(
                axes.get_origin()
                + 2.85 * np.sin(theta.get_value()) * UP
                + 2.85 * np.cos(theta.get_value()) * RIGHT,
            )
        )

        dot = always_redraw(
            lambda: Dot(axes2.c2p(1, theta.get_value()), color=GREEN_N200)
        )
        labelDot = always_redraw(
            lambda: nText("ln(z)")
            .move_to(axes2.c2p(1, theta.get_value()) + 0.7 * RIGHT)
            .scale(0.8)
        )

        path = TracedPath(lambda: axes2.c2p(1, theta.get_value()), stroke_color=BLACK)

        # self.add(dot, axes, z_vector, path)

        # self.play(axes.animate.shift(LEFT * 2 + UP * 2).scale(0.8))
        # self.play(theta.animate.set_value(4 * PI))

        self.play(LaggedStart(Create(axes), GrowArrow(z_vector), lag_ratio=0.7))
        self.play(
            LaggedStart(
                FadeIn(labelZ),
                FadeIn(labelR),
                Create(angle),
                FadeIn(labelAngle),
                lag_ratio=0.5,
            )
        )
        self.wait(1)
        self.play(
            FadeOut(labelR, labelAngle),
            axes.animate.shift(DOWN),
            FadeIn(label1, label2, shift=UP * 0.5),
        )
        self.play(
            theta.animate.increment_value(PI / 2), run_time=5, rate_func=there_and_back
        )
        self.wait(1)

        self.play(
            LaggedStart(
                AnimationGroup(
                    axes.animate.scale(0.6).shift(LEFT * 1.5).set_color(GREY_N200),
                ),
                Create(axes2),
                Create(dot),
                FadeIn(labelDot),
                lag_ratio=0.5,
            )
        )
        dotZ = Dot(z_vector.get_end(), color=GREY_N200)
        self.add(path)
        self.wait(1)

        def mark():
            markerDot = Dot(dot.get_center(), color=GREY_N200, z_index=-0.1)
            marker0 = Circle(arc_center=dot.get_center(), color=RED_N100, radius=0.3)
            markerPointer0 = Arrow(
                z_vector.get_end(), dot.get_center(), color=GREY_N100, buff=0.3
            )
            self.play(Create(marker0), GrowArrow(markerPointer0), Create(markerDot))

        self.play(FadeOut(labelZ), FadeIn(dotZ))

        mark()

        self.play(theta.animate.increment_value(2 * PI), run_time=2)
        mark()

        self.play(theta.animate.increment_value(2 * PI), run_time=2)
        mark()

        self.play(theta.animate.set_value(-2 * PI + PI / 3), run_time=4)
        mark()

        self.wait(5)


class PrincipalBranch(Scene):
    def construct(self):
        axes = getAxis(y_range=[-5, 7.5], y_length=5)

        theta = ValueTracker(PI / 3)

        z_vector = always_redraw(
            lambda: Arrow(
                axes.get_origin(),
                axes.get_origin()
                + 2.5 * np.sin(theta.get_value()) * UP
                + 2.5 * np.cos(theta.get_value()) * RIGHT,
                buff=0,
            )
            .set_color_by_gradient([GREEN_N100, GREEN_N200])
            .set_sheen_direction(
                np.sin(theta.get_value()) * UP + np.cos(theta.get_value()) * RIGHT,
            )
        )

        angle = always_redraw(
            lambda: Arc(
                0.5, 0, theta.get_value(), arc_center=axes.get_origin(), color=GREY_N400
            )
        )

        principalBranch = nMath("\\text{Principal Branch}", color=GREY_N800).scale(1.1)
        self.play(Write(principalBranch))
        self.play(
            LaggedStart(
                principalBranch.animate.to_edge(UP),
                Create(axes),
                GrowArrow(z_vector),
                Create(angle),
                lag_ratio=0.5,
            )
        )

        label1 = nMath("\\mathbf{\\theta} = \\;").to_edge(UP).shift(LEFT).shift(DOWN)
        label2 = always_redraw(
            lambda: nText(
                "" + str(round(theta.get_value(), 2)) + " rad",
            ).next_to(label1, RIGHT, buff=0.2)
        )
        self.wait(1)
        self.play(
            axes.animate.shift(DOWN),
            FadeIn(label1, label2, shift=UP * 0.5),
        )
        self.play(theta.animate.set_value(-PI), run_time=3)

        self.play(theta.animate.set_value(PI), run_time=2.5)
        self.wait(5)


class MultivaluedFunctions(Scene):
    def construct(self):
        set1 = Ellipse(
            1.5,
            4,
            stroke_color=[GREY_N200, GREY_N500],
            sheen_direction=UP + RIGHT,
            stroke_width=6,
        ).shift(1.5 * LEFT)
        label1 = (
            nMath(
                "z \\in \\mathbb{C}",
            )
            .next_to(set1, UP, buff=0.5)
            .shift(UP * 0.05)
        )
        set2 = Ellipse(
            1.5,
            4,
            stroke_color=[GREY_N200, GREY_N500],
            sheen_direction=UP + RIGHT,
            stroke_width=6,
        ).shift(1.5 * RIGHT)
        label2 = nMath("f(z) \\in \\mathbb{C}").next_to(set2, UP, buff=0.5)
        self.add(label1, label2)
        self.add(set1, set2)

        z1 = nMath("z_1", color=GREEN_N200).move_to(set1.get_center())

        fz2 = nMath("p_2", color=GREEN_N200).move_to(set2.get_center())
        fz1 = nMath("p_1", color=GREEN_N200).next_to(fz2, UP, buff=0.5)
        fz3 = nMath("p_3", color=GREEN_N200).next_to(fz2, DOWN, buff=0.5)

        self.add(z1, fz1, fz2, fz3)

        def mark(fz):
            markerPointer0 = Arrow(
                z1.get_right(), fz.get_left(), color=RED_N100, buff=0.3
            )
            self.play(GrowArrow(markerPointer0))

        mark(fz1)
        mark(fz2)
        mark(fz3)

        self.wait(5)
