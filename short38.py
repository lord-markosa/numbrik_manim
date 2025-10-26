from manim import *
from utils import *


class Template(Scene):
    def construct(self):
        question = nMath("\\sqrt{\\frac{81}{9-\\sqrt{80}}}", color=BLACK)

        hgl81 = solidHighlight(self, question[0][2:4], buff=0.15, animate=False)
        hglDenom = solidHighlight(self, question[0][5:], buff=0.14, animate=False)

        question2 = nMath("\\frac{9}{\\sqrt{9-\\sqrt{80}}}", color=BLACK)

        # self.add(question2)
        # self.add(*hgl81, *hglDenom)

        # self.play(TransformMatchingTex(question, question2))

        # self.play(
        #     Transform(question[0][0:2], question2[0][2:4]),
        #     Transform(question[0][2:4], question2[0][0]),
        #     Transform(question[0][5:], question2[0][4:]),
        #     Transform(question[0][4], question2[0][1]),
        # )

        rationalize = nMath(
            "\\frac{9}{\\sqrt{9-\\sqrt{80}}}",
            "\\times",
            "\\frac{\\sqrt{9+\\sqrt{80}}}{\\sqrt{9+\\sqrt{80}}}",
            color=BLACK,
        )

        rationalize2 = nMath(
            "\\frac{9\\sqrt{9+\\sqrt{80}}}{\\sqrt{9^2-{\\sqrt{80}}^2}}",
            color=BLACK,
        )

        rationalize3 = nMath(
            "\\frac{9\\sqrt{9+\\sqrt{80}}}{\\sqrt{81-80}}",
            color=BLACK,
        )

        rationalize4 = nMath(
            "\\frac{9\\sqrt{9+\\sqrt{80}}}{\\sqrt{1}}",
            color=BLACK,
        )

        preFinal1 = nMath(
            "9\\sqrt{9+\\sqrt{80}}",
            color=BLACK,
        )

        preFinal2 = nMath(
            "9\\sqrt{9+\\sqrt{16\\cdot 5}}",
            color=BLACK,
        )

        preFinal3 = nMath(
            "9\\sqrt{9+2\\cdot 2\\cdot\\sqrt{5}}",
            color=BLACK,
        )

        subscript1 = nMath("x").scale(0.7).next_to(preFinal3[0][7], DOWN, buff=0.35)
        subscript2 = nMath("y").scale(0.7).next_to(preFinal3[0][9:12], DOWN, buff=0.35)
        subscript3 = (
            nMath("x^2 + y^2")
            .scale(0.7)
            .next_to(preFinal3[0][3], DOWN, buff=0.2)
            .shift(RIGHT * 0.2)
        )

        context1 = nMath("x^2 + y^2 + 2xy")
        context2 = nMath("(x+y)^2")

        preFinal4 = nMath(
            "9\\sqrt{(2+\\sqrt{5})^2}",
            color=BLACK,
        )

        preFinal5 = nMath(
            "9\\times(2+\\sqrt{5})",
            color=BLACK,
        )

        preFinal7 = nMath(
            "18 + 9\\sqrt{5}",
            color=BLACK,
        )

        self.add(preFinal7)

        self.wait(5)


class Solve(Scene):
    def construct(self):
        question = nMath("\\sqrt{\\frac{81}{9-\\sqrt{80}}}", color=BLACK)

        question2 = nMath("\\frac{9}{\\sqrt{9-\\sqrt{80}}}", color=BLACK)

        self.add(question)
        hgl1 = solidHighlight(self, question[0][2:4], buff=0.15, unhighlight=False)
        self.play(FadeOut(*hgl1))
        self.play(
            Transform(question[0][0:2], question2[0][2:4]),
            Transform(question[0][2:4], question2[0][0]),
            Transform(question[0][5:], question2[0][4:]),
            Transform(question[0][4], question2[0][1]),
        )
        self.wait(1)
        hglDenom = solidHighlight(self, question2[0][4:], buff=0.1, unhighlight=False)
        self.play(FadeOut(*hglDenom))

        rationalize = nMath(
            "\\frac{9}{\\sqrt{9-\\sqrt{80}}}",
            "\\times",
            "\\frac{\\sqrt{9+\\sqrt{80}}}{\\sqrt{9+\\sqrt{80}}}",
            color=BLACK,
        )

        self.play(
            LaggedStart(
                question[0].animate.next_to(rationalize[0], 0),
                FadeIn(rationalize[1:]),
                lag_ratio=0.5,
            )
        )
        self.wait(1)

        rationalize2 = nMath(
            "\\frac{9\\sqrt{9+\\sqrt{80}}}{\\sqrt{9^2-{\\sqrt{80}}^2}}",
            color=BLACK,
        )

        self.play(
            FadeOut(question),
            TransformMatchingTex(rationalize, rationalize2),
            run_time=1,
        )
        self.wait(0.5)

        rationalize3 = nMath(
            "\\frac{9\\sqrt{9+\\sqrt{80}}}{\\sqrt{81-80}}",
            color=BLACK,
        )

        self.play(TransformMatchingTex(rationalize2, rationalize3), run_time=1)
        self.wait(0.5)

        rationalize4 = nMath(
            "\\frac{9\\sqrt{9+\\sqrt{80}}}{\\sqrt{1}}",
            color=BLACK,
        )

        self.play(TransformMatchingTex(rationalize3, rationalize4), run_time=1)
        self.wait(0.5)

        preFinal1 = nMath(
            "9\\sqrt{9+\\sqrt{80}}",
            color=BLACK,
        )

        self.play(TransformMatchingTex(rationalize4, preFinal1), run_time=1)
        self.wait(0.5)

        solidHighlight(self, preFinal1[0][3:], buff=0.15)

        preFinal2 = nMath(
            "9\\sqrt{9+\\sqrt{16\\cdot 5}}",
            color=BLACK,
        )

        self.play(TransformMatchingTex(preFinal1, preFinal2), run_time=1)
        self.wait(0.5)

        preFinal3 = nMath(
            "9\\sqrt{9+2\\cdot 2\\cdot\\sqrt{5}}",
            color=BLACK,
        )

        self.play(TransformMatchingTex(preFinal2, preFinal3), run_time=1)
        self.wait(0.5)

        subscript1 = nMath("x").scale(0.7).next_to(preFinal3[0][7], DOWN, buff=0.35)
        subscript2 = nMath("y").scale(0.7).next_to(preFinal3[0][9:12], DOWN, buff=0.35)
        subscript3 = (
            nMath("x^2 + y^2").scale(0.7).next_to(preFinal3[0][3], DOWN, buff=0.2)
        )

        hgl1 = solidHighlight(
            self, preFinal3[0][7], buff=0.14, color=YELLOW, animate=False
        )
        hgl2 = solidHighlight(
            self, preFinal3[0][9:12], buff=0.14, color=GREEN_N100, animate=False
        )
        hgl3 = solidHighlight(
            self, preFinal3[0][3], buff=0.14, color=NUMBRIK_COLOR40, animate=False
        )

        self.play(
            FadeIn(*hgl1),
            FadeIn(subscript1),
        )
        self.play(
            FadeIn(*hgl2),
            FadeIn(subscript2),
        )
        self.wait(1)
        self.play(FadeIn(*hgl3), fadeInTex(subscript3))
        self.wait(1)

        context1 = nMath("x^2 + y^2", "+", "2", "x", "y").next_to(
            preFinal3, DOWN, buff=0.75
        )
        context2 = nMath("(x+y)^2").next_to(context1, 0, aligned_edge=DOWN)

        self.play(
            ReplacementTransform(subscript1, context1[3]),
            ReplacementTransform(subscript2, context1[4]),
            ReplacementTransform(subscript3[0], context1[0]),
            FadeIn(context1[1:3]),
        )
        self.play(TransformMatchingTex(context1, context2), run_time=1.5)

        preFinal4 = nMath(
            "9\\sqrt{(2+\\sqrt{5})^2}",
            color=BLACK,
        )

        self.play(
            TransformMatchingTex(preFinal3, preFinal4),
            FadeOut(*hgl1, *hgl2, *hgl3),
            FadeOut(context2),
            run_time=1.5,
        )
        self.wait(0.5)

        preFinal5 = nMath(
            "9\\times(2+\\sqrt{5})",
            color=BLACK,
        )
        self.play(TransformMatchingTex(preFinal4, preFinal5), run_time=1.5)
        self.wait(0.5)

        preFinal6 = nMath(
            "18 + 9\\sqrt{5}",
            color=BLACK,
        )
        self.play(TransformMatchingTex(preFinal5, preFinal6), run_time=1.5)
        self.wait(0.5)

        self.wait(5)


class Options(Scene):
    def construct(self):
        options = (
            VGroup(
                MathTex("A) \\ 18+9\\sqrt{5}", color=BLACK),
                MathTex("B) \\ 9+9\\sqrt{5}", color=BLACK),
                MathTex("C) \\ 9+18\\sqrt{5}", color=BLACK),
                MathTex("D) \\ 18+18\\sqrt{5}", color=BLACK),
            )
            .arrange(DOWN, aligned_edge=LEFT, center=False, buff=0.3)
            .to_edge(UP)
        )

        self.play(FadeIn(options))
        self.wait(4)

        self.play(Create(SurroundingRectangle(options[0], corner_radius=0.1, buff=0.1)))
        self.wait(4)
