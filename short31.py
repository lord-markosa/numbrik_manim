from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        addBackground(self)

        problem = (
            VGroup(
                MathTex(
                    "\\text{Find }\\sin{\\mathbf{\\theta}}, \\text{ if:}",
                ),
                MathTex(
                    "\\sin{\\mathbf{\\theta}} + \\sqrt{\\sin{\\mathbf{\\theta}} + \\sqrt{\\sin{\\mathbf{\\theta}} + ...}}}",
                    "=",
                    "\\sec^4{\\mathbf{\\alpha}}",
                ),
            )
            .set_color_by_gradient([GREY_N500, BLACK])
            .set_sheen_direction(RIGHT)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            .to_edge(UP)
            .scale(1.1)
        )

        options = (
            VGroup(
                VGroup(
                    MathTex("A) \\ \\sec^2{\\mathbf{\\alpha}}", color=BLACK),
                    MathTex("C) \\ \\tan^4{\\mathbf{\\alpha}}", color=BLACK),
                ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
                VGroup(
                    MathTex(
                        "B) \\ \\sec^2{\\mathbf{\\alpha}}\\tan^2{\\mathbf{\\alpha}}",
                        color=BLACK,
                    ),
                    MathTex("D) \\ \\sec^4{\\mathbf{\\alpha}}", color=BLACK),
                ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            )
            .set_color_by_gradient([GREY_N500, BLACK])
            .set_sheen_direction(RIGHT)
            .arrange(RIGHT, buff=2)
            .next_to(problem, DOWN, buff=1, aligned_edge=LEFT)
            .shift(RIGHT * 0.2)
        )

        step1 = nMath(
            "\\sin{\\mathbf{\\theta}}",
            "+",
            "\\sqrt{\\sec^4{\\mathbf{\\alpha}}}",
            "=",
            "\\sec^4{\\mathbf{\\alpha}}",
            gradient_color=[NUMBRIK_COLOR, NUMBRIK_COLOR_DARK],
            sheen_direction=RIGHT,
        ).next_to(problem[1], DOWN, buff=1.5)

        step2 = nMath(
            "\\sin{\\mathbf{\\theta}}",
            "+",
            "\\sec^2{\\mathbf{\\alpha}}",
            "=",
            "\\sec^4{\\mathbf{\\alpha}}",
            gradient_color=[NUMBRIK_COLOR, NUMBRIK_COLOR_DARK],
            sheen_direction=RIGHT,
        ).next_to(problem[1], DOWN, buff=1.5)

        step1.next_to(step2, 0, aligned_edge=DOWN)

        step3 = nMath(
            "\\sin{\\mathbf{\\theta}}",
            "=",
            "\\sec^4{\\mathbf{\\alpha}}",
            "-",
            "\\sec^2{\\mathbf{\\alpha}}",
            gradient_color=[NUMBRIK_COLOR, NUMBRIK_COLOR_DARK],
            sheen_direction=RIGHT,
        ).next_to(problem[1], DOWN, buff=1.5)

        step4 = nMath(
            "\\sin{\\mathbf{\\theta}}",
            "=",
            "\\sec^2{\\mathbf{\\alpha}}",
            "\\cdot",
            "(",
            "\\sec^2{\\mathbf{\\alpha}}",
            "-",
            "1",
            ")",
            gradient_color=[NUMBRIK_COLOR, NUMBRIK_COLOR_DARK],
            sheen_direction=RIGHT,
        ).next_to(problem[1], DOWN, buff=1.5)

        step5 = nMath(
            "\\sin{\\mathbf{\\theta}}",
            "=",
            "\\sec^2{\\mathbf{\\alpha}}",
            "\\cdot",
            "\\tan^2{\\mathbf{\\alpha}}",
            gradient_color=[NUMBRIK_COLOR, NUMBRIK_COLOR_DARK],
            sheen_direction=RIGHT,
        ).next_to(problem[1], DOWN, buff=1.5)

        hgl1 = solidHighlight(self, problem[1][0], animate=False, buff=0.15)
        hgl2 = solidHighlight(self, problem[1][0][7:], animate=False, buff=0.15)

        self.add(problem, options)
        self.wait(4)
        self.play(FadeIn(*hgl1), run_time=1.5)
        self.wait(1)
        self.play(Transform(*hgl1, *hgl2), run_time=2)
        self.wait(1)
        self.play(options.animate.to_edge(DOWN), run_time=1.5)
        self.wait(1)

        self.play(fadeInTex(step1))
        self.wait(1)
        self.play(FadeOut(*hgl1), TransformMatchingTex(step1, step2), run_time=2)
        self.wait(1)
        self.play(TransformMatchingTex(step2, step3), run_time=2)
        self.wait(1)
        self.play(TransformMatchingTex(step3, step4), run_time=2)
        self.wait(1)
        self.play(
            Transform(step4[0:5], step5[0:5]),
            Transform(step4[5:], step5[5:]),
            run_time=2,
        )
        self.wait(1)
        self.play(options.animate.scale(1.1).move_to(ORIGIN + 2.5 * DOWN))

        highlight(self, options[1][0], buff=0.2, unhighlight=False, color=RED_N100)

        self.wait(10)
