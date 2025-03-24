from manim import *
from utils import *
import math


class Quadratics2(Scene):
    def construct(self):
        self.intro()
        clearScreen(self)
        self.completeTheSquare()
        clearScreen(self)
        self.graphParabola()
        clearScreen(self)
        self.introToRoots()
        clearScreen(self)
        self.quadraticEqn()
        clearScreen(self)
        self.parabolaShift()
        clearScreen(self)
        self.rootsConclusion()
        clearScreen(self)
        self.QuadraticsFormula()
        clearScreen(self)
        self.concavityDemo()
        clearScreen(self)
        self.natureOfRootsConclusion()
        clearScreen(self)

    def intro(self):
        displayTitle(self, "Quadratic Equations")

    def completeTheSquare(self):
        animateTextSeq(
            self,
            [
                MathTex("x^2 + 6x + 8", color=NUMBRIK_COLOR),
                MathTex(
                    "x^2 + 2 \\cdot 3 \\cdot x +", "3^2 - 3^2", "+ 8"
                ).set_color_by_tex("3^2", RED),
                MathTex("x^2 + 2 \\cdot 3 \\cdot x + 3^2 - 9 + 8"),
                MathTex("(x+3)^2 - 1", color=GREEN),
            ],
        )

    def graphParabola(self):
        axes = Axes(
            x_range=[-7, 2, 1],
            x_length=7,
            y_range=[-3, 10, 1],
            y_length=7,
        )

        parabola = axes.plot(
            lambda x: (x + 3) ** 2 - 1, x_range=[-6.05, 0.05], color=NUMBRIK_COLOR
        )

        vertex = Dot(axes.coords_to_point(-3, -1), color=GREEN)
        vertex_label = MathTex("(-3, -1)").next_to(vertex, DOWN).scale(0.8)

        root1 = Dot(axes.coords_to_point(-4, 0), color=RED)
        root1_label = MathTex("-4").next_to(root1, DOWN + 0.1 * LEFT).scale(0.8)
        root2 = Dot(axes.coords_to_point(-2, 0), color=RED)
        root2_label = MathTex("-2").next_to(root2, DOWN + 0.05 * RIGHT).scale(0.8)

        self.play(Create(axes), run_time=1.5)
        self.play(Create(parabola), run_time=1.5)
        self.play(FadeIn(vertex), Write(vertex_label))
        self.play(FadeIn(root1), FadeIn(root2))
        self.play(Write(root1_label), Write(root2_label))
        self.wait(2)

    def introToRoots(self):
        illus = animateTextSeq(
            self, [MathTex("y = f(x)"), MathTex("f(x) = 0")], shift_val=2 * UP
        )
        axes = Axes(
            x_range=[-1, 4, 1],
            x_length=5,
            y_range=[-3, 3, 1],
            y_length=4,
        ).next_to(illus[-1], DOWN, buff=0.5)

        cubic = axes.plot(
            lambda x: x**3 - 6 * x**2 + 11 * x - 6,
            x_range=[0.5, 3.5],
            color=NUMBRIK_COLOR,
        )

        root1 = Dot(axes.coords_to_point(1, 0), color=RED)
        root2 = Dot(axes.coords_to_point(2, 0), color=RED)
        root3 = Dot(axes.coords_to_point(3, 0), color=RED)

        self.play(Create(axes), run_time=1.5)
        self.play(Create(cubic), run_time=1.5)
        self.play(FadeIn(root1), FadeIn(root2), FadeIn(root3))
        self.wait(2)

    def quadraticEqn(self):
        animateTextSeq(
            self,
            [
                MathTex("x^2 + 6x + 8 = 0", color=NUMBRIK_COLOR),
                MathTex("(x+3)^2 - 1 = 0"),
                MathTex("using \\quad a^2 - b^2 = (a-b)(a+b)").scale(0.8),
                MathTex("(x+2)(x+4) = 0"),
                MathTex("x = -2, -4", color=GREEN),
            ],
        )

    def parabolaShift(self):
        y0 = ValueTracker(1.0)

        axes = Axes(
            x_range=[-7, 2, 1],
            x_length=7,
            y_range=[-2, 11, 1],
            y_length=7,
        )

        parabola = always_redraw(
            lambda: axes.plot(
                lambda x: (x + 3) ** 2 - y0.get_value(),
                x_range=[-6.05, 0.05],
                color=NUMBRIK_COLOR,
            )
        )

        root1 = always_redraw(
            lambda: Dot(axes.coords_to_point(-3 - math.sqrt(y0.get_value())), color=RED)
        )
        root2 = always_redraw(
            lambda: Dot(axes.coords_to_point(-3 + math.sqrt(y0.get_value())), color=RED)
        )

        self.play(Create(axes), run_time=1.5)
        self.play(Create(parabola), run_time=1.5)
        self.play(FadeIn(root1), FadeIn(root2))
        self.play(y0.animate.set_value(0), run_time=2)
        self.wait(2)
        self.play(FadeOut(root1), FadeOut(root2))
        self.remove(root1, root2)
        self.play(y0.animate.set_value(-1), run_time=2)

    def graphRootsNature(self, reference):
        axes1 = (
            Axes(
                x_range=[-1, 3, 1],
                x_length=3,
                y_range=[-1, 3, 1],
                y_length=3,
            )
            .next_to(reference, DOWN, buff=1)
            .shift(4 * LEFT)
        )

        axes2 = axes1.copy().shift(4 * RIGHT)
        axes3 = axes1.copy().shift(8 * RIGHT)

        axes = [axes1, axes2, axes3]

        parabolas = []
        y0_values = [-0.25, 0, 1]

        for i, ax in enumerate(axes):
            parabolas.append(
                ax.plot(
                    lambda x: (x - 1.5) ** 2 + y0_values[i],
                    x_range=[0.5, 2.5],
                    color=NUMBRIK_COLOR,
                )
            )

        return axes, parabolas

    def rootsConclusion(self):
        lines = animateTextSeq(
            self,
            [
                MathTex("ax^2 + bx + c = 0"),
            ],
            shift_val=UP,
        )

        axes, parabolas = self.graphRootsNature(lines[0])

        labels = [
            Text("2 real roots", color=GREEN).next_to(axes[0], DOWN),
            Text("1 real root", color=GREEN).next_to(axes[1], DOWN),
            Text("No real roots", color=GREEN).next_to(axes[2], DOWN),
        ]

        for i, ax in enumerate(axes):
            self.play(Create(ax), run_time=1)
            self.play(Create(parabolas[i]))
            self.play(Write(labels[i]), run_time=1)

    def QuadraticsFormula(self):
        displayTitle(self, "Quadratic Formula")

        animateTextSeq(
            self,
            [
                MathTex("ax^2 + bx + c"),
                MathTex("a\\left(x^2 + \\left(\\frac{b}{a}\\right)x\\right) + c"),
                MathTex("a\\left(x^2 + 2\\left(\\frac{b}{2a}\\right)x\\right) + c"),
                MathTex(
                    "a\\left(x^2 + 2\\left(\\frac{b}{2a}\\right)x + \\left(\\frac{b}{2a}\\right)^2 - \\left(\\frac{b}{2a}\\right)^2\\right) + c"
                ),
            ],
            shift_val=0.5 * UP,
        )

        clearScreen(self, 2)

        animateTextSeq(
            self,
            [
                MathTex(
                    "a\\left(x + \\frac{b}{2a}\\right)^2 + \\frac{4ac - b^2}{4a}",
                ),
                Text("Vertex of the above parabola:").scale(0.7),
                MathTex(
                    "\\left(-\\frac{b}{2a}, \\frac{4ac - b^2}{4a}\\right)",
                    color=NUMBRIK_COLOR,
                ),
            ],
        )

        clearScreen(self, 2)

        animateTextSeq(
            self,
            [
                MathTex(
                    "a\\left(x + \\frac{b}{2a}\\right)^2 + \\frac{4ac - b^2}{4a} = 0",
                ),
                MathTex("\\left(x + \\frac{b}{2a}\\right)^2 = \\frac{b^2 - 4ac}{4a^2}"),
                MathTex("x + \\frac{b}{2a} = \\pm \\sqrt{\\frac{b^2 - 4ac}{4a^2}}"),
                MathTex(
                    "x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}", color=NUMBRIK_COLOR
                ),
            ],
            shift_val=0.5 * UP,
        )

        clearScreen(self, 2)

        animateTextSeq(
            self,
            [
                Text("Discriminant:").scale(0.7),
                MathTex("D = b^2 - 4ac"),
                MathTex("Roots \ of \ ax^2 + bx + c = 0 \ are:"),
                MathTex("x = \\frac{-b \\pm \\sqrt{D}}{2a}", color=NUMBRIK_COLOR),
            ],
        )

    def concavityDemo(self):
        lines = animateTextSeq(
            self,
            [
                MathTex("ax^2 + bx + c = 0").move_to(TITLE_TEXT_POSITION + 2 * UP),
                MathTex(
                    "Vertex:\ \\left(-\\frac{b}{2a}, \\frac{4ac - b^2}{4a}\\right)",
                ),
            ],
            shift_val=2 * UP,
        )
        axes1 = (
            Axes(
                x_range=[-1, 3, 1],
                x_length=3,
                y_range=[-1, 3, 1],
                y_length=3,
            )
            .next_to(lines[-1], DOWN, buff=1)
            .shift(3 * LEFT)
        )

        axes2 = axes1.copy().shift(6 * RIGHT)

        curve1 = axes1.plot(
            lambda x: (x - 1) ** 2 - 1, x_range=[-0.5, 2.5], color=NUMBRIK_COLOR
        )
        label1 = MathTex("a > 0").next_to(axes1, DOWN)

        curve2 = axes2.plot(
            lambda x: -((x - 1) ** 2) + 1, x_range=[-0.5, 2.5], color=NUMBRIK_COLOR
        )
        label2 = MathTex("a < 0").next_to(axes2, DOWN)

        self.play(Create(axes1), Create(axes2), run_time=1)
        self.play(Create(curve1), Write(label1), run_time=1.5)
        self.play(Create(curve2), Write(label2), run_time=1.5)

    def natureOfRootsConclusion(self):
        label = (
            Text("Nature of roots:", color=NUMBRIK_COLOR)
            .scale(0.8)
            .move_to(TITLE_TEXT_POSITION + 2 * UP)
        )

        self.play(Write(label), run_time=1)

        axes, parabolas = self.graphRootsNature(label)

        labels = [
            MathTex("b^2 - 4ac > 0", color=GREEN),
            Text("2 real roots", color=GREEN),
            MathTex("b^2 - 4ac = 0", color=GREEN),
            Text("1 real root", color=GREEN),
            MathTex("b^2 - 4ac < 0", color=GREEN),
            Text("No real roots", color=GREEN),
        ]

        for i, ax in enumerate(axes):
            labels[2 * i].next_to(ax, DOWN)
            labels[2 * i + 1].scale(0.7).next_to(labels[2 * i], DOWN)
            self.play(Create(ax), run_time=1)
            self.play(Create(parabolas[i]))
            self.play(Write(labels[2 * i]), run_time=1)
            self.play(Write(labels[2 * i + 1]), run_time=1)

        self.wait(2)
