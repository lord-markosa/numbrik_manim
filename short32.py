from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        problem = (
            VGroup(
                MathTex("x+\\sqrt{y} = 11"),
                MathTex("\\sqrt{x}+y = 7"),
                MathTex("\\quad x, y \\in \\mathbb{N}"),
            )
            .set_color(BLACK)
            # .set_color_by_gradient([GREY_N500, BLACK])
            # .set_sheen_direction(RIGHT)
            .arrange(DOWN, buff=0.4)
            .to_edge(UP)
            .scale(1.1)
        )
        problem[2].shift(DOWN * 0.1)

        ramanujEqn = (
            VGroup(
                MathTex("x^2+ay = b", color=BLACK),
                MathTex("x+cy^2 = d", color=BLACK),
            )
            .set_color_by_gradient([GREY_N500, BLACK])
            .set_sheen_direction(RIGHT)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            .to_edge(DOWN)
            .scale(1.1)
        )

        step1 = nMath("\\text{Let } x = p^2, y = q^2").next_to(problem, DOWN, buff=1)

        newProblem = (
            VGroup(
                nMath("p^2 + q = 11"),
                nMath("p + q^2 = 7"),
            )
            .set_color_by_gradient([GREY_N500, BLACK])
            .set_sheen_direction(RIGHT)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            .to_edge(UP)
            # .scale(1.1)
        )

        subLine = Line(
            newProblem.get_corner(DL) + 0.3 * DOWN + LEFT,
            newProblem.get_corner(DR) + 0.3 * DOWN + 0.5 * RIGHT,
            color=GREY_N400,
        )

        subSymbol = (
            MathTex("-", color=BLACK)
            .next_to(subLine.get_start(), UP, buff=0.4)
            .shift(0.3 * RIGHT)
        )

        step2 = nMath("p^2 - q^2 - p + q = 4").next_to(newProblem, DOWN, buff=0.75)
        justify = nMath("A^2 - B^2 = (A-B)(A+B)").next_to(step2, DOWN, buff=0.5)
        step3 = nMath("(p - q)", "(p + q - 1)", "=", "4").next_to(step2, DOWN, buff=0.5)
        brace1 = (
            BraceBetweenPoints(step3[0].get_corner(DL), step3[0].get_corner(DR))
            .set_color_by_gradient([GREY_N100, GREY_N500])
            .set_sheen_direction(RIGHT)
        )
        brace2 = (
            BraceBetweenPoints(step3[1].get_corner(DL), step3[1].get_corner(DR))
            .set_color_by_gradient([GREY_N100, GREY_N500])
            .set_sheen_direction(RIGHT)
        )
        sol11 = nMath("2").next_to(brace1, DOWN, buff=0.2)
        sol12 = nMath("2").next_to(brace2, DOWN, buff=0.2)
        sol1 = nMath("p=2.5, q=0.5").next_to(step3, DOWN, buff=1.5)
        sol1_ = nMath("p, q \\notin \\mathbb{N}").next_to(sol1, DOWN, buff=0.5)
        # highlight(self, sol1, buff=0.2, color=RED, unhighlight=False)
        # self.add(problem)

        sol21 = nMath("1").next_to(brace1, DOWN, buff=0.2)
        sol22 = nMath("4").next_to(brace2, DOWN, buff=0.2)
        sol2 = nMath("p=3, q=2").next_to(step3, DOWN, buff=1.5)
        sol2_ = nMath("x=9, y=4").next_to(sol2, DOWN, buff=0.5)

        justify2 = nMath("4 = 2\\cdot 2 = 4\\cdot 1").next_to(step3, DOWN, buff=0.7)
        # self.add(
        #     newProblem,
        #     subLine,
        #     subSymbol,
        #     step2,
        #     step3,
        #     brace1,
        #     brace2,
        #     sol21,
        #     sol22,
        #     sol2,
        #     sol2_,
        # )

        # ANIMATION HUB

        self.add(problem)

        self.wait(2)
        self.play(
            LaggedStart(
                fadeInTex(ramanujEqn[0]), fadeInTex(ramanujEqn[1]), lag_ratio=0.5
            )
        )

        self.wait(1)
        highlight(self, problem[2], buff=0.2)
        self.wait(1)
        self.play(FadeOut(ramanujEqn))
        self.wait(1)
        self.play(fadeInTex(step1))
        self.wait(1)
        self.play(
            LaggedStart(
                FadeOut(problem, step1),
                fadeInTex(newProblem[0]),
                fadeInTex(newProblem[1]),
                lag_ratio=0.5,
            )
        )

        self.wait(1)

        self.play(
            LaggedStart(
                Create(subLine), FadeIn(subSymbol), fadeInTex(step2), lag_ratio=0.5
            )
        )
        self.wait(1)
        self.play(fadeInTex(justify))
        self.wait(1)
        self.play(LaggedStart(FadeOut(justify), fadeInTex(step3), lag_ratio=0.6))
        self.wait(1)
        self.play(fadeInTex(justify2))
        self.wait(1)
        self.play(FadeOut(justify2))
        self.wait(1)
        self.play(FadeIn(brace1))
        self.wait(1)
        self.play(FadeIn(brace2))
        self.wait(1)
        self.play(FadeIn(sol11, sol12))
        self.wait(1)
        self.play(FadeIn(sol1))
        self.wait(1)
        self.play(FadeIn(sol1_))
        self.wait(1)
        hgl = highlight(self, sol1, buff=0.2, color=RED, unhighlight=False)
        self.wait(1)

        self.play(FadeOut(sol11, sol12, sol1, sol1_, *hgl))
        self.wait(1)
        self.play(FadeIn(sol21, sol22))
        self.wait(1)
        self.play(FadeIn(sol2))
        self.wait(1)
        self.play(FadeIn(sol2_))

        highlight(self, sol2_, buff=0.2, color=GREEN_N200, unhighlight=False)
        self.wait(10)
