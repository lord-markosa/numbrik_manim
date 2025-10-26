from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        addBackground(self)

        A = ORIGIN + 3 * DOWN
        B = A + 4 * RIGHT
        C = A + 1.5 * LEFT + 4 * UP
        D = C + 2 * UP
        E = D + 1.5 * RIGHT
        shape = Polygon(A, B, C, D, E, color=BLACK)

        lengthAB = lengthMarkerV2(A, B, "7", DOWN * 0.4, scale=0.8)

        lengthCD = lengthMarker(D + 0.4 * LEFT, C + 0.4 * LEFT, "3", scale=0.8)

        lengthDE = lengthMarker(E + 0.4 * UP, D + 0.4 * UP, "1", scale=0.8)

        lengthBC = lengthMarker(
            B + 0.35 * UP + 0.2 * RIGHT,
            C + 0.35 * UP + 0.2 * RIGHT,
            "10",
            scale=0.8,
            buff=0.4,
        )

        rt1 = getRightAngle(B, A, E, length=0.3)
        rt2 = getRightAngle(D, E, A, length=0.3)
        rt3 = getRightAngle(C, D, E, length=0.3)

        temp1 = DashedLine(E, E + 4 * RIGHT + 0.7 * RIGHT, color=GREY_N400)
        temp2 = DashedLine(B, B + 0.7 * RIGHT, color=GREY_N400)

        lengthAE = lengthMarkerV2(
            temp1.get_end(), temp2.get_end(), "?", shift=0.3 * LEFT, scale=0.8
        )
        lengthAE[2].scale(1.2).set_color(RED)

        temp3 = DashedLine(C, C + RIGHT * 1.5, color=NUMBRIK_COLOR, stroke_width=5)
        temp4 = DashedLine(A, A + LEFT * 1.5, color=NUMBRIK_COLOR, stroke_width=5)
        temp5 = DashedLine(C, C + DOWN * 4, color=NUMBRIK_COLOR, stroke_width=5)

        tempLength1 = lengthMarkerV2(A + LEFT * 1.5, B, "8", DOWN * 0.4, scale=0.8)
        tempLenght2 = lengthMarkerV2(C, A + 1.5 * LEFT, "6", LEFT * 0.4, scale=0.8)

        self.add(
            shape,
            lengthAB,
            *lengthCD,
            *lengthDE,
            *lengthBC,
            rt1,
            rt2,
            rt3,
            temp1,
            temp2,
            lengthAE,
        )

        self.wait(4)

        answerMarker = CurvedArrow(
            lengthAE[2].get_left() + 2 * UP + 2 * LEFT,
            lengthAE[2].get_left() + 0.5 * LEFT,
            color=RED,
        )

        hgl = solidHighlight(self, lengthAE[2], buff=0.2, animate=0)
        self.play(Create(answerMarker), FadeIn(*hgl))

        self.wait(0.5)
        self.play(
            FadeOut(answerMarker),
            lengthBC[0].animate.set_opacity(0),
        )
        self.wait(0.5)
        self.play(Create(temp3))
        self.wait(0.5)
        self.play(FadeIn(temp4, shift=4 * DOWN), run_time=2)
        self.play(FadeIn(temp5, shift=1.5 * LEFT), run_time=2)
        self.play(Transform(lengthAB, tempLength1))
        self.play(
            GrowArrow(tempLenght2[0]), GrowArrow(tempLenght2[1]), FadeIn(tempLenght2[2])
        )

        self.wait(0.25)
        self.play(
            LaggedStart(
                Create(answerMarker),
                Transform(lengthAE[2], nMath("9").next_to(lengthAE[2], 0)),
                lag_ratio=0.6,
            )
        )

        self.wait(10)


class Statements(Scene):
    def construct(self):
        self.play(fadeInTex(nMath("\\sqrt{10^2 - 8^2} = 6")), run_time=3)
        self.wait(4)
