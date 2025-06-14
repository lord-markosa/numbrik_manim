from manim import *
from utils import *
import math


class ExponentialProblem(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        shots = [
            self.problemStatement,
            self.intro,
            self.solving,
            self.problem,
            self.solution,
            self.graph,
        ]

        for shot in shots:
            shot()
            clearScreen(self)

    def problemStatement(self):
        self.play(
            Write(
                MathTex("3^x = x^9", color=NUMBRIK_COLOR)
                .move_to(TITLE_TEXT_POSITION)
                .scale(3.5)
            ),
            run_time=1.5,
        )

    def intro(self):
        displayTitle(self, "Simple Problem")

        animateTextSeq(
            self,
            [
                MathTex(r"3^x = x^3", color=GREEN_N100),
                MathTex(r"3^{\frac{x}{3x}} = x^{\frac{3}{3x}}"),
                MathTex(r"3^{\frac{1}{3}} = x^{\frac{1}{x}}"),
                MathTex(r"\Rightarrow x = 3", color=YELLOW),
            ],
        )

    def solving(self):
        lines = [
            MathTex(r"3^x = x^9", color=BLUE),
            MathTex(r"3^{\frac{1}{9}} = x^{\frac{1}{x}}", color=BLUE),
            MathTex(r"(3^k)^{\frac{1}{9k}} = x^{\frac{1}{x}}"),
            MathTex(r"k = 3^\alpha"),
            MathTex(r"(3^{3^\alpha})^{\frac{1}{9 \cdot 3^\alpha}}"),
            MathTex(r"3^{3^\alpha} = 9 \cdot 3^\alpha = 3^{\alpha+2}"),
            MathTex(r"3^\alpha = \alpha+2"),
        ]

        self.play(Write(lines[0].move_to(TITLE_TEXT_POSITION + 1.5 * UP)))
        self.wait(1)
        self.play(Transform(lines[0], lines[1].next_to(lines[0], 0)))
        self.wait(1)
        self.play(Write(lines[2].next_to(lines[0], DOWN, buff=0.5)))
        self.wait(1)
        self.play(Write(lines[3].next_to(lines[2], DOWN, buff=0.5)))
        self.wait(1)
        self.play(Write(lines[4].next_to(lines[3], DOWN, buff=0.5)))
        self.wait(1)
        self.play(Write(lines[5].next_to(lines[4], DOWN, buff=0.5)))
        self.wait(1)
        self.play(Write(lines[6].next_to(lines[5], DOWN, buff=0.5)))

    def solution(self):
        animateTextSeq(
            self,
            [
                MathTex(r"(3^{3^\alpha})^{\frac{1}{9 \cdot 3^\alpha}}"),
                MathTex(r"(3^{3^1})^{\frac{1}{9 \cdot 3^1}}"),
                MathTex(r"27^{\frac{1}{27}} = 3^{\frac{1}{9}} = x^{\frac{1}{x}}"),
                MathTex(r"\Rightarrow x = 27", color=YELLOW),
            ],
        )

    def problem(self):
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-1, 10],
            x_length=8,
            y_length=6,
            axis_config={"include_numbers": True},
        )

        exp_graph = axes.plot(lambda x: 3**x, x_range=[-3.5, 2], color=GREEN_N100)
        exp_label = MathTex("y = 3^x", color=GREEN_N100).next_to(exp_graph, UP + RIGHT)

        line_graph = axes.plot(lambda x: x + 2, x_range=[-3.5, 3], color=RED)
        line_label = MathTex("y = x + 2", color=RED).next_to(line_graph, UP + RIGHT)

        solutionPoint = axes.c2p(1, 3)
        point_a = Dot(solutionPoint, color=NUMBRIK_COLOR)

        dashed_line_x = DashedLine(
            start=solutionPoint, end=axes.c2p(0, 3), color=GREEN_N100
        )
        dashed_line_y = DashedLine(
            start=solutionPoint, end=axes.c2p(1, 0), color=GREEN_N100
        )

        self.play(Create(axes))
        self.play(Create(exp_graph), Write(exp_label))
        self.play(Create(line_graph), Write(line_label))
        self.wait(1)
        self.play(Create(point_a))
        self.play(Create(dashed_line_x), Create(dashed_line_y))
        self.wait(3)

        solutionPoint2 = axes.c2p(-1.85, 0.15)

        self.play(self.camera.frame.animate.scale(0.5).move_to(solutionPoint2))

        point_b = Dot(solutionPoint2, color=YELLOW)

        self.play(Create(point_b))

        self.wait(1)

        self.play(Restore(self.camera.frame), run_time=2)
        self.wait(2)

    def graph(self):
        axes = Axes(
            x_range=[-1, 30],
            y_range=[-0.5, 3],
            x_length=12,
            y_length=6,
            axis_config={"include_numbers": False},
        )

        func = lambda x: x ** (1 / x)

        exp_graph = axes.plot(func, x_range=[0.2, 29], color=NUMBRIK_COLOR)
        exp_label = MathTex("y = x^{\\frac{1}{x}}").next_to(exp_graph, UP).shift(UP)

        dashed_line_x = DashedLine(
            end=axes.c2p(30, 1), start=axes.c2p(0, 1), color=YELLOW_E
        )

        self.play(Create(axes))
        self.play(Create(exp_graph), Write(exp_label))
        self.wait(1)
        self.play(Create(dashed_line_x))
        self.wait(2)

        y_peak = func(math.e)
        solutionPoint = axes.c2p(math.e, y_peak)
        point_a = Dot(solutionPoint, color=YELLOW)
        label_a = MathTex("\\left(e, e^{\\frac{1}{e}}\\right)", color=YELLOW).next_to(
            solutionPoint, UP
        )

        dashed_line_x = DashedLine(
            start=solutionPoint, end=axes.c2p(0, y_peak), color=YELLOW
        )

        self.play(Create(point_a), Write(label_a))
        self.play(Create(dashed_line_x))

        self.wait(1)

        y1 = func(27)
        point1 = axes.c2p(27, y1)

        point1Dot = Dot(point1, color=RED)

        labely1 = MathTex("27^{\\frac{1}{27}}").next_to(axes.c2p(0, y1), LEFT)
        labelx1 = MathTex("27").next_to(axes.c2p(27, 0), DOWN)

        dashed_line_x1 = DashedLine(start=point1, end=axes.c2p(0, y1), color=RED)
        dashed_line_y1 = DashedLine(start=point1, end=axes.c2p(27, 0), color=RED)

        self.play(Create(point1Dot))
        self.play(Write(labelx1), Create(dashed_line_y1))

        self.play(Create(dashed_line_x1))
        self.play(Write(labely1))
        self.wait(1)

        x2 = 1.1508
        point2 = axes.c2p(x2, y1)
        point2Dot = Dot(point2, color=RED)

        dashed_line_y2 = DashedLine(start=point2, end=axes.c2p(x2, 0), color=RED)
        labelx2 = MathTex("?").next_to(axes.c2p(x2, 0), DOWN)

        self.play(self.camera.frame.animate.scale(0.7).move_to(point2), run_time=1.75)
        self.play(Create(point2Dot))
        self.play(Create(dashed_line_y2), Write(labelx2))
        self.wait(1)
        self.play(Restore(self.camera.frame), run_time=2)

        self.wait(1)
