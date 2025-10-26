from manim import *
from utils import *


class Template(Scene):
    def construct(self):
        a = 3
        square = Square(a * 2, stroke_color=GREY_N400, fill_opacity=0.5, color=WHITE)
        square2 = (
            Square(a, stroke_color=GREY_N400, fill_opacity=1)
            .shift(UP * a / 2 + RIGHT * a / 2)
            .set_color_by_gradient([WHITE, YELLOW])
            .set_stroke(GREY_N400)
        )

        radius = a * np.sqrt(2) * (np.sqrt(2) - 1)

        labelArea = nMath("4", color=BLACK).move_to(square2.get_center())

        circle = (
            Circle(
                radius,
                stroke_color=GREY_N400,
                arc_center=DOWN * radius / np.sqrt(2) + LEFT * radius / np.sqrt(2),
                fill_opacity=1,
                color=WHITE,
            )
            .set_color_by_gradient([WHITE, GREEN_N100])
            .set_stroke(GREY_N400)
        )

        radiusMarker = Arrow(
            circle.get_center(),
            circle.get_center() + radius * DOWN,
            color=GREY_N400,
            buff=0,
        )

        radiusLabel = (
            nMath("r=\\,?", color=BLACK)
            .next_to(radiusMarker, RIGHT, buff=0.15)
            .shift(UP * 0.2)
        )

        self.add(square, square2, circle, labelArea, radiusMarker, radiusLabel)

        self.wait(5)


class Intro(Scene):
    def construct(self):
        a = 3
        square = Square(a * 2, stroke_color=GREY_N400, fill_opacity=0.5, color=WHITE)
        square2 = (
            Square(a, stroke_color=GREY_N400, fill_opacity=1)
            .shift(UP * a / 2 + RIGHT * a / 2)
            .set_color_by_gradient([WHITE, BLUE_B])
            .set_stroke(GREY_N400)
        )

        radius = a * np.sqrt(2) * (np.sqrt(2) - 1)

        labelArea = nMath("4", color=BLACK).move_to(square2.get_center())

        midPointMarks = createMidPointMarks(Line(a * (UP + RIGHT), a * (UP + LEFT)))
        midPointMarks2 = createMidPointMarks(Line(a * (UP + RIGHT), a * (DOWN + RIGHT)))

        circle = (
            Circle(
                radius,
                stroke_color=GREY_N400,
                arc_center=DOWN * radius / np.sqrt(2) + LEFT * radius / np.sqrt(2),
                fill_opacity=1,
                color=WHITE,
            )
            .set_color_by_gradient([WHITE, GREEN_N100])
            .set_stroke(GREY_N400)
        )

        radiusMarker = Arrow(
            circle.get_center(),
            circle.get_center() + radius * DOWN,
            color=GREY_N400,
            buff=0,
        )

        radiusLabel = (
            nMath("r=\\,?", color=BLACK)
            .next_to(radiusMarker, RIGHT, buff=0.15)
            .shift(UP * 0.2)
        )

        # self.add(square, square2, circle, labelArea, midPointMarks, midPointMarks2)

        self.add(square)
        self.play(
            LaggedStart(
                Create(square2, stroke_width=4, stroke_color=GREY_N400),
                FadeIn(midPointMarks, midPointMarks2),
                FadeIn(labelArea),
                DrawBorderThenFill(circle, stroke_width=4, stroke_color=GREY_N400),
                GrowArrow(radiusMarker),
                FadeIn(radiusLabel),
                lag_ratio=0.6,
            ),
        )
        highlight(self, radiusLabel, buff=0.2, color=RED_N100)
        self.wait(5)


class Solve(Scene):
    def construct(self):
        a = 3
        square = Square(a * 2, stroke_color=GREY_N400, color=WHITE)
        square2 = (
            Square(a, stroke_color=GREY_N400, fill_opacity=1)
            .shift(UP * a / 2 + RIGHT * a / 2)
            .set_color_by_gradient([WHITE, BLUE_B])
            .set_stroke(GREY_N400)
        )

        radius = a * np.sqrt(2) * (np.sqrt(2) - 1)

        labelArea = nMath("4", color=BLACK).move_to(square2.get_center())

        circle = (
            Circle(
                radius,
                stroke_color=GREY_N400,
                arc_center=DOWN * radius / np.sqrt(2) + LEFT * radius / np.sqrt(2),
                fill_opacity=1,
                color=WHITE,
            )
            .set_color_by_gradient([WHITE, GREEN_N100])
            .set_stroke(GREY_N400)
        )

        radiusMarker = Arrow(
            circle.get_center(),
            circle.get_center() + radius * DOWN,
            color=GREY_N400,
            buff=0,
        )

        radiusLabel = (
            nMath("r", "=\\,?", color=BLACK)
            .next_to(radiusMarker, RIGHT, buff=0.15)
            .shift(UP * 0.2)
        )
        radiusLabel2 = nMath(
            "r",
        ).next_to(radiusLabel, 0, aligned_edge=LEFT + DOWN)

        midPointMarks = createMidPointMarks(Line(a * (UP + RIGHT), a * (UP + LEFT)))
        midPointMarks2 = createMidPointMarks(Line(a * (UP + RIGHT), a * (DOWN + RIGHT)))

        self.add(
            square,
            square2,
            circle,
            labelArea,
            radiusMarker,
            radiusLabel,
            midPointMarks,
            midPointMarks2,
        )

        sideLength1 = lengthMarkerV2(
            square2.get_corner(DR), square2.get_corner(UR), "2", RIGHT * 0.4
        )
        sideLength2 = lengthMarkerV2(
            square.get_corner(DR), square2.get_corner(DR), "2", RIGHT * 0.4
        )

        helper1 = DashedLine(
            circle.get_center(),
            square.get_corner(UR),
            color=GREY_N200,
            dash_length=0.2,
            dashed_ratio=0.8,
        )
        helper2 = DashedLine(
            circle.get_center(),
            circle.get_center() + DOWN * radius,
            color=GREY_N200,
            dash_length=0.2,
            dashed_ratio=0.8,
        )
        helperRightAngle1 = getRightAngle(
            circle.get_center(),
            circle.get_center() + DOWN * radius,
            square.get_corner(DL),
            color=GREY_N200,
            length=0.3,
        )

        centerDot = Dot(circle.get_center(), radius=0.05, color=GREY_N500)

        # self.add(helper1, helper2)

        self.play(Transform(labelArea, sideLength1))
        self.wait(1)
        self.play(
            TransformFromCopy(sideLength1, sideLength2),
            FadeOut(midPointMarks, midPointMarks2),
        )
        self.wait(1)
        self.play(Create(helper1))
        self.play(
            LaggedStart(
                Transform(radiusMarker, helper2),
                Transform(radiusLabel, radiusLabel2),
                Create(helperRightAngle1),
                lag_ratio=0.6,
            )
        )
        self.wait(1)

        arrows = createParallelArrows(
            RIGHT,
            circle.get_top()
            + LEFT * radius * 1.5
            + DOWN * (radius - radius / np.sqrt(2)),
            circle.get_bottom() + LEFT * radius * 1.5,
            0.8,
            8,
            NUMBRIK_COLOR,
        )
        self.play([GrowArrow(arrow) for arrow in arrows])
        self.add(arrows)

        width = ValueTracker(0)
        light = always_redraw(
            lambda: Polygon(
                square.get_corner(DL) + (radius + radius / np.sqrt(2)) * UP,
                square.get_corner(DL),
                square.get_corner(DL) + width.get_value() * RIGHT,
                square.get_corner(DL)
                + (radius + radius / np.sqrt(2)) * UP
                + width.get_value() * RIGHT,
                fill_opacity=0.6,
                color=YELLOW,
                stroke_width=0,
            )
        )

        self.add(light)
        self.play(width.animate.set_value(radius + radius / np.sqrt(2)))

        helperLine3 = DashedLine(
            square2.get_corner(DL),
            circle.get_bottom() + radius / np.sqrt(2) * RIGHT,
            color=GREY_N100,
            dash_length=0.2,
            dashed_ratio=0.8,
            z_index=0.1,
        )
        helperLine4 = DashedLine(
            circle.get_center(),
            circle.get_center() + RIGHT * radius / np.sqrt(2),
            color=GREY_N100,
            dash_length=0.2,
            dashed_ratio=0.8,
            z_index=0.1,
        )

        helperMark1 = BraceBetweenPoints(
            circle.get_center() + RIGHT * radius / np.sqrt(2),
            square2.get_corner(DL),
            color=GREY_N500,
        )

        helperMark2 = BraceBetweenPoints(
            circle.get_bottom() + radius / np.sqrt(2) * RIGHT,
            circle.get_center() + RIGHT * radius / np.sqrt(2),
            color=GREY_N500,
        )

        helperLabel1 = nMath("r/\\sqrt{2}").next_to(helperMark1, RIGHT, buff=0.3)
        helperLabel2 = nMath("r").next_to(helperMark2, RIGHT, buff=0.3)

        helperLine5 = DashedLine(
            square2.get_corner(DL),
            circle.get_center(),
            color=RED_N100,
            z_index=0.1,
            dash_length=0.2,
            dashed_ratio=0.8,
        )
        helperLine6 = DashedLine(
            circle.get_center(),
            circle.get_center() + DOWN * radius,
            color=RED_N100,
            z_index=0.1,
            dash_length=0.2,
            dashed_ratio=0.8,
        )

        self.play(FadeIn(helperLine5, helperLine6))
        self.play(
            LaggedStart(
                Create(helperLine3),
                Create(helperLine4),
                Write(helperMark1),
                fadeInTex(helperLabel1),
                Write(helperMark2),
                fadeInTex(helperLabel2),
                lag_ratio=0.5,
            )
        )
        self.play(FadeOut(light, helperLine6, helperLine5))
        self.wait(1)

        solidHighlight(self, [helperLabel1, helperLabel2], buff=0.2, unhighlight=False)
        self.wait(1)
        solidHighlight(self, sideLength2[2], buff=0.2, unhighlight=False)

        self.wait(5)


class Statements(Scene):
    def construct(self):
        eq1 = nMath("r + \\frac{r}{\\sqrt{2}}", "= 2")
        eq2 = nMath("r = \\frac{2\\sqrt{2}}{1+\\sqrt{2}}")
        self.play(FadeIn(eq1[0]))
        self.wait(1)
        self.play(FadeIn(eq1[1]))
        self.wait(1)
        self.play(LaggedStart(FadeOut(eq1, shift=UP), fadeInTex(eq2), lag_ratio=0.4))
        self.wait(10)
