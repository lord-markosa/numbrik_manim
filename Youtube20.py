from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        f = 0.8
        R = 4 * f
        r1 = 2.5 * f
        r2 = R - r1

        circle_temp = Circle(radius=R, stroke_color=BLACK)
        circle = Circle(
            radius=R, color=YELLOW, stroke_color=BLACK, fill_opacity=1, z_index=-20
        )
        circle2 = Circle(
            radius=r1,
            color=WHITE,
            stroke_color=BLACK,
            fill_opacity=1,
        ).shift(DOWN * (R - r1))
        circle3 = Circle(
            radius=r2, color=WHITE, stroke_color=BLACK, fill_opacity=1
        ).shift(UP * (R - r2))

        chord_dist = 2 * r1 - R
        chord_len_half = np.sqrt(R**2 - chord_dist**2)

        line = Line(
            chord_dist * UP + chord_len_half * LEFT,
            chord_dist * UP + chord_len_half * RIGHT,
            color=BLACK,
        )

        lineLength = lengthMarkerV2(
            line.get_start(), line.get_end(), "12", 0.4 * DOWN, scale=0.8
        )

        questionLabel = nText("Area = ?").move_to(2 * UP + 1.5 * R * RIGHT)
        questionLabelHighlighter = SurroundingRectangle(
            questionLabel, corner_radius=0.1, buff=0.2, color=RED_N100
        )

        questionLabelPointer = CurvedArrow(
            questionLabel.get_bottom() + 0.3 * DOWN,
            2.5 * RIGHT + 0.5 * DOWN,
            color=RED_N100,
            angle=-PI / 2,
        )

        piby4 = PI / 4

        # radius = radiusMarker(
        #     circle.get_center(),
        #     circle.get_center() + LEFT * R,
        #     "R",
        # )

        radius1 = radiusMarker(
            circle2.get_center(),
            circle2.get_center()
            + RIGHT * np.cos(piby4) * r1
            + DOWN * np.sin(piby4) * r1,
            "R_1",
        )

        radius1[0].z_index = 10
        radius1[1].shift(UP * 0.4 + RIGHT * 0.2).scale(0.8)

        radius2 = radiusMarker(
            circle3.get_center(),
            circle3.get_center() + RIGHT * np.cos(piby4) * r2 + UP * np.sin(piby4) * r2,
            "R_2",
        )

        radius2[0].z_index = 10
        radius2[1].shift(DOWN * 0.4 + RIGHT * 0.2).scale(0.8)

        line2 = DashedLine(UP * R, DOWN * R, color=BLACK)

        highlighterchord = Line(
            line.get_start(), line.get_end(), color=RED_N100, stroke_width=6
        )

        I = UP * (2 * r1 - R)

        highlighter1 = Line(I, UP * R, color=RED_N100, stroke_width=6)
        highlighter2 = Line(I, DOWN * R, color=RED_N100, stroke_width=6)
        highlighter3 = Line(I, line.get_end(), color=RED_N100, stroke_width=6)
        highlighter4 = Line(I, line.get_start(), color=RED_N100, stroke_width=6)

        highlighterline = Line(
            line2.get_start(), line2.get_end(), color=RED_N100, stroke_width=6
        )

        pointerLine = CurvedArrow(
            UP * R + LEFT * R, LEFT * 0.2, color=RED_N, angle=piby4
        )

        pointer1 = CurvedArrow(
            UP * R + LEFT * R, UP * (r1 - 0.5) + LEFT * 0.2, color=RED_N, angle=piby4
        )

        pointer2 = CurvedArrow(
            DOWN * R + LEFT * R,
            DOWN * (r1 - 0.5) + LEFT * 0.2,
            color=RED_N,
            angle=-piby4,
        )

        pointer3 = CurvedArrow(
            UP * R + RIGHT * R + 0.5 * RIGHT,
            (I + line.get_end()) / 2 + 0.5 * RIGHT + 0.2 * UP,
            color=RED_N,
            angle=piby4,
        )

        pointer4 = CurvedArrow(
            UP * R + LEFT * R + 0.5 * LEFT,
            (I + line.get_start()) / 2 + 0.5 * LEFT + 0.2 * UP,
            color=RED_N,
            angle=-piby4,
        )

        rightTriangle = Polygon(
            ORIGIN, I, line.get_start(), color=RED_N100, stroke_width=6
        )
        rightAngle = RightAngle(
            Line(I, line.get_start()), Line(I, ORIGIN), length=0.3, color=BLACK
        )

        self.play(LaggedStart(Create(circle2), Create(circle3), lag_ratio=0.5))
        self.wait(1)
        self.play(Create(circle_temp))
        self.wait(1)
        self.play(Create(line))
        self.wait(1)
        self.play(
            GrowArrow(lineLength[0]), GrowArrow(lineLength[1]), FadeIn(lineLength[2])
        )
        self.wait(1)
        self.play(FadeIn(circle))
        self.wait(1)
        self.play(
            fadeInTex(questionLabel),
            Create(questionLabelHighlighter),
            Create(questionLabelPointer),
        )
        self.wait(5)

        self.play(
            FadeOut(questionLabel, questionLabelHighlighter, questionLabelPointer)
        )
        self.wait(2)
        self.play(
            LaggedStart(
                GrowArrow(radius1[0]),
                FadeIn(radius1[1]),
                GrowArrow(radius2[0]),
                FadeIn(radius2[1]),
                lag_ratio=0.5,
            )
        )
        self.wait(1)
        self.play(FadeOut(lineLength[0], lineLength[1], lineLength[2]))
        self.play(Create(line2))
        self.wait(0.5)
        self.play(FadeIn(highlighterchord))
        self.wait(0.5)
        self.play(FadeOut(highlighterchord))
        self.wait(1)
        self.play(Create(pointerLine), FadeIn(highlighterline))
        self.wait(2)
        self.play(FadeOut(pointerLine, highlighterline))
        self.wait(2)
        self.play(Create(rightTriangle), Create(rightAngle))
        self.wait(1)
        self.play(FadeOut(rightAngle, rightTriangle))
        self.wait(2)
        self.play(FadeOut(radius1[1], radius1[0], radius2[1], radius2[0]))
        self.play(
            circle.animate.set_opacity(0),
            circle2.animate.set_opacity(0),
            circle3.animate.set_opacity(0),
        )
        self.wait(1)
        self.play(Create(pointer1), FadeIn(highlighter1))
        self.play(FadeOut(pointer1, highlighter1), run_time=0.5)
        self.play(Create(pointer2), FadeIn(highlighter2))
        self.play(FadeOut(pointer2, highlighter2), run_time=0.5)
        self.play(Create(pointer3), FadeIn(highlighter3))
        self.play(FadeOut(pointer3, highlighter3), run_time=0.5)
        self.play(Create(pointer4), FadeIn(highlighter4))
        self.play(FadeOut(pointer4, highlighter4), run_time=0.5)
        self.wait(1)
        self.play(
            circle.animate.set_opacity(1),
            circle2.animate.set_opacity(1),
            circle3.animate.set_opacity(1),
        )
        self.play(
            LaggedStart(
                GrowArrow(radius1[0]),
                FadeIn(radius1[1]),
                GrowArrow(radius2[0]),
                FadeIn(radius2[1]),
                lag_ratio=0.5,
            )
        )
        self.wait(1)
        self.play(FadeIn(highlighter2), run_time=0.75)
        self.play(FadeOut(highlighter2), run_time=0.5)

        self.play(FadeIn(highlighter1), run_time=0.75)
        self.play(FadeOut(highlighter1), run_time=0.5)

        self.play(FadeIn(highlighter3), run_time=0.75)
        self.play(FadeOut(highlighter3), run_time=0.5)

        self.play(FadeIn(highlighter4), run_time=0.75)
        self.play(FadeOut(highlighter4), run_time=0.5)

        self.wait(5)


class Statements(Scene):
    def construct(self):
        main1 = nMath("Area", "= \\pi(R_0^2 - R_1^2 - R_2^2)").to_edge(UP)

        main2 = nMath("= \\pi\\left((R_1 + R_2)^2 - R_1^2 - R_2^2\\right)").next_to(
            main1[1], DOWN, buff=0.5, aligned_edge=LEFT
        )

        main3 = nMath("=", "2 \\pi R_1 R_2").next_to(
            main2, DOWN, buff=0.5, aligned_edge=LEFT
        )

        main4 = nMath("Area", "=", "2 \\pi R_1 R_2").to_edge(UP)

        main5 = nMath("= 2 \\pi (9)").next_to(
            main4[1], DOWN, buff=0.65, aligned_edge=LEFT
        )

        main_final = nMath("=", "18\\pi").next_to(
            main5, DOWN, buff=0.5, aligned_edge=LEFT
        )

        self.play(fadeInTex(main1))
        self.wait(1)
        self.play(fadeInTex(main2))
        self.wait(1)
        self.play(fadeInTex(main3))
        self.wait(1)
        self.play(Transform(main1[0], main4[0]), FadeOut(main1[1:], main2))
        self.play(Transform(main3[1], main4[2]), Transform(main3[0], main4[1]))
        self.wait(4)
        self.play(fadeInTex(main5))
        self.wait(1)
        self.play(fadeInTex(main_final))
        highlight(
            self, main_final, color=RED, buff=0.18, wait_time=4, unhighlight=False
        )
        clearScreen(self, 1)

        # construct that dashed line

        stmt1 = nMath("\\text{Outer-circle radius} = R_0").to_edge(UP)

        stmt2_ = nMath("2", "R_0", "=", "2", "R_1", "+", "2R_2").next_to(
            stmt1, DOWN, buff=0.5
        )
        stmt2 = nMath("R_0", "=", "R_1", "+", "R_2").next_to(
            stmt1,
            DOWN,
            buff=0.5,
        )

        stmt3 = nMath("2R_1", "\\times", "2R_2", "=", "6", "\\times", "6").to_edge(UP)
        stmt4 = nMath("\\Rightarrow R_1 R_2 = 9").next_to(stmt3, DOWN, buff=0.5)

        self.play(fadeInTex(stmt1))
        self.wait(1)
        self.play(fadeInTex(stmt2_))
        self.wait(1)
        self.play(TransformMatchingTex(stmt2_, stmt2))

        clearScreen(self, 4)

        self.play(FadeIn(stmt3[0]))
        self.play(LaggedStart(FadeIn(stmt3[1]), FadeIn(stmt3[2]), lag_ratio=0.5))
        self.play(FadeIn(stmt3[3]))
        self.play(FadeIn(stmt3[4]))
        self.play(LaggedStart(FadeIn(stmt3[5]), FadeIn(stmt3[6]), lag_ratio=0.5))
        self.wait(1)
        self.play(fadeInTex(stmt4))
        self.wait(5)


class Thumbnail(Scene):
    def construct(self):
        f = 0.8
        R = 4 * f
        r1 = 2.5 * f
        r2 = R - r1

        circle = Circle(
            radius=R,
            color=GREEN_N100,
            stroke_color=BLACK,
            fill_opacity=1,
            z_index=-20,
            stroke_width=7,
        )

        circle2 = Circle(
            radius=r1,
            color=WHITE,
            stroke_color=BLACK,
            fill_opacity=1,
            stroke_width=7,
        ).shift(DOWN * (R - r1))

        circle3 = Circle(
            radius=r2,
            color=WHITE,
            stroke_color=BLACK,
            fill_opacity=1,
            stroke_width=7,
        ).shift(UP * (R - r2))

        chord_dist = 2 * r1 - R
        chord_len_half = np.sqrt(R**2 - chord_dist**2)

        line = Line(
            chord_dist * UP + chord_len_half * LEFT,
            chord_dist * UP + chord_len_half * RIGHT,
            stroke_width=7,
            color=BLACK,
        )

        self.add(circle, circle2, circle3, line)
        self.wait(10)
