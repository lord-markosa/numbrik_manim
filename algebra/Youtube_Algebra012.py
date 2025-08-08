from manim import *
from utils import *
import math


class Logarithms(Scene):
    def construct(self):
        shots = [self.part1, self.logGraph, self.part2, self.grahpicalIllus, self.part3]
        for shot in shots:
            shot()
            clearScreen(self)

    def part1(self):
        displayTitle(self, "Make logs simple!")
        eqn = [
            MathTex("\\log", "_a", "{x}", "=", "y")
            .scale(2)
            .move_to(TITLE_TEXT_POSITION)
            .set_color_by_tex_to_color_map(
                {"log": NUMBRIK_COLOR, "a": RED, "x": GREEN_N100, "y": BLUE}
            ),
            MathTex("x", "=", "a", "^y")
            .scale(2)
            .set_color_by_tex_to_color_map({"x": GREEN_N100, "a": RED, "^y": BLUE}),
        ]

        eqn[1].next_to(eqn[0], DOWN, buff=1)

        self.play(Write(eqn[0]))
        self.play(TransformFromCopy(eqn[0][2], eqn[1][0]))
        self.play(TransformFromCopy(eqn[0][3], eqn[1][1]))
        self.play(TransformFromCopy(eqn[0][1], eqn[1][2]))
        self.play(TransformFromCopy(eqn[0][4], eqn[1][3]))

    def part2(self):
        # Minor Rules
        displayTitle(self, "Some minor stuffs!")

        animateTextSeq(
            self,
            [
                MathTex("\\log_a(a) = 1"),
                MathTex("\\log_a(1) = 0"),
                MathTex(
                    "\\log_a\\left(\\frac{1}{x}\\right) = -\\log_a(x)",
                ),
            ],
            line_buffer=0.75,
        )

        clearScreen(self, 1)

        title2 = Text("Proof").to_edge(UP)
        self.play(Write(title2))

        animateTextSeq(
            self,
            [
                MathTex("\\log_a(a) = 1", color=NUMBRIK_COLOR),
                MathTex("LHS = l =  log_a(a)"),
                MathTex("\\Rightarrow a^l = a"),
                MathTex("\\Rightarrow l = 1 = RHS"),
            ],
            next_reference=title2,
        )

    # Graphical illustration of monotonic functions:

    def part3(self):
        displayTitle(self, "Three Rules")
        animateTextSeq(
            self,
            [
                MathTex("\\log_a(mn) = \\log_a(m) + \\log_a(n)"),
                MathTex("\\log_{a^n}{b^m} = \\frac{m}{n} \\log_a(b)"),
                MathTex("\\log_b(a) = \\frac{\\log_k(a)}{\\log_k(b)}"),
            ],
            line_buffer=1,
            iterative_callback=lambda line: self.play(
                line.animate.set_color(GREEN_N100),
                Create(SurroundingRectangle(line, buff=0.25)),
            ),
        )

        clearScreen(self, 2)

        # Product rule proof
        animateTextSeq(
            self,
            [
                MathTex("\\log_a(mn) = \\log_a(m) + \\log_a(n)", color=NUMBRIK_COLOR),
                MathTex("RHS = r = log_a(mn) \\Rightarrow a^r = mn"),
                MathTex("\\text{Let } log_a(m) = x \\Rightarrow m = a^x"),
                MathTex("\\text{Let } log_a(n) = y \\Rightarrow n = a^y"),
                MathTex("mn = a^x \\cdot a^y = a^{x+y}"),
                MathTex("a^r = a^{x+y} \\Rightarrow r = x+y = LHS"),
            ],
        )

        clearScreen(self, 2)

        # Power Rule Proof
        animateTextSeq(
            self,
            [
                MathTex(
                    "\\log_{a^n}(b^m) = \\frac{m}{n} \\log_a(b)", color=NUMBRIK_COLOR
                ),
                MathTex("LHS = l = \\log_{a^n}(b^m) \\Rightarrow a^{nl} = b^m"),
                MathTex(
                    "\\Rightarrow a^{\\frac{nl}{m}} = b \\Rightarrow \\frac{nl}{m} = \\log_a(b)"
                ),
                MathTex("\\Rightarrow l = \\frac{m}{n} \\log_a(b) = RHS"),
            ],
        )

        clearScreen(self, 2)

        # Change of base formula proof
        animateTextSeq(
            self,
            [
                MathTex(
                    "\\log_b(a) = \\frac{\\log_k(a)}{\\log_k(b)}", color=NUMBRIK_COLOR
                ),
                MathTex("\\text{Let } log_k(a) = x \\Rightarrow a = k^x"),
                MathTex("\\text{Let } log_k(b) = y \\Rightarrow b = k^y"),
                MathTex("LHS = l = \\log_b(a) = log_{k^y}(k^x)"),
                MathTex("log_{k^y}(k^x) = \\frac{x}{y}log_k(k) = \\frac{x}{y} = RHS"),
            ],
        )

    def grahpicalIllus(self):
        # Axes setup
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-1, 16, 2],
            x_length=7,
            y_length=6,
            axis_config={"include_numbers": False},
        ).to_edge(LEFT)

        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))

        # Plot the exponential function f(x) = 2^x
        graph = axes.plot(lambda x: 2**x, color=NUMBRIK_COLOR)
        graph_label = axes.get_graph_label(graph, label="y = 2^x")
        self.play(Create(graph), Write(graph_label))
        self.wait(1)

        # Highlight two points: x1 and x2 such that x1 < x2
        x1, x2 = 1, 3
        y1, y2 = 2**x1, 2**x2

        dot1 = Dot(axes.coords_to_point(x1, y1), color=YELLOW)
        dot2 = Dot(axes.coords_to_point(x2, y2), color=RED)

        line1 = DashedLine(axes.coords_to_point(x1, 0), axes.coords_to_point(x1, y1))
        line2 = DashedLine(axes.coords_to_point(x2, 0), axes.coords_to_point(x2, y2))
        hline1 = DashedLine(axes.coords_to_point(0, y1), axes.coords_to_point(x1, y1))
        hline2 = DashedLine(axes.coords_to_point(0, y2), axes.coords_to_point(x2, y2))

        self.play(FadeIn(dot1), FadeIn(dot2))
        self.play(Create(line1), Create(line2), Create(hline1), Create(hline2))

        # Labels
        label_x1 = MathTex("x_1", font_size=36).next_to(line1, DOWN)
        label_x2 = MathTex("x_2", font_size=36).next_to(line2, DOWN)
        label_fx1 = MathTex("f(x_1)", font_size=36).next_to(hline1, LEFT)
        label_fx2 = MathTex("f(x_2)", font_size=36).next_to(hline2, LEFT)

        self.play(Write(label_x1), Write(label_x2), Write(label_fx1), Write(label_fx2))
        self.wait(1)

        # Add inequality and explanation
        lines = animateTextSeq(
            self,
            [
                Text("Monotonic, 1-1 function", font_size=32),
                MathTex("x_1 < x_2 \\Rightarrow f(x_1) < f(x_2)"),
                MathTex("f(x_1) = f(x_2) \\Rightarrow x_1 = x_2"),
                MathTex("2^{x_1} = 2^{x_2} \\Rightarrow x_1 = x_2", color=GREEN_N100),
            ],
            shift_val=4 * RIGHT,
        )

        self.play(Create(SurroundingRectangle(lines[3], buff=0.25)))

    def logGraph(self):
        # Axes setup
        axes = Axes(
            x_range=[-8, 8, 1],
            y_range=[-8, 8, 2],
            x_length=7,
            y_length=6,
            axis_config={"include_numbers": False, "include_ticks": False},
        )

        dashed_line = DashedLine(
            start=axes.c2p(-6, -6), end=axes.c2p(6, 6), color=YELLOW
        )
        exp = axes.plot(lambda x: 2**x, x_range=[-8, 3], color=NUMBRIK_COLOR)
        log = axes.plot(lambda x: math.log(x, 2), x_range=[2**-8, 8], color=GREEN_N100)
        labelExp = axes.get_graph_label(log, label="y = 2^x")
        labelLog = axes.get_graph_label(exp, label="y = \\log_{2}(x)")
        self.play(Create(axes), Create(log), Create(exp), Create(dashed_line))
        self.play(Write(labelExp), Write(labelLog))
        self.wait(2)
