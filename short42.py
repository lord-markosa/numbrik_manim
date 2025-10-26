from manim import *
from utils import *


class Template(Scene):
    def construct(self):
        problemStatement = MathTex(
            "\\text{Find the shaded area:}", color=BLACK
        ).to_edge(UP)
        self.add(problemStatement)

        a = ValueTracker(1.8)
        L = 6

        getB = lambda: L - a.get_value()

        getC = lambda: (getB() - a.get_value()) / 2

        getCenter = lambda: L / 2 * LEFT + a.get_value() * RIGHT + DOWN * 3

        baseLine = Line(
            L / 2 * RIGHT + 3 * DOWN, L / 2 * LEFT + 3 * DOWN, color=GREY_N400
        )

        shadeColor = NUMBRIK_COLOR40

        circleA = always_redraw(
            lambda: Sector(
                radius=a.get_value(),
                arc_center=getCenter(),
                color=shadeColor,
                angle=-PI / 2,
                start_angle=PI,
                stroke_width=0,
                z_index=-0.1,
            )
        )
        outerArcA = always_redraw(
            lambda: Arc(
                radius=a.get_value(),
                arc_center=getCenter(),
                color=GREY_N400,
                angle=-PI / 2,
                start_angle=PI,
            )
        )

        circleB = always_redraw(
            lambda: Sector(
                radius=getB(),
                arc_center=getCenter(),
                color=shadeColor,
                angle=PI / 2,
                stroke_width=0,
                z_index=-0.1,
            )
        )
        outerArcB = always_redraw(
            lambda: Arc(
                radius=L - a.get_value(),
                arc_center=getCenter(),
                color=GREY_N400,
                angle=PI / 2,
            )
        )

        circleC = always_redraw(
            lambda: Sector(
                radius=getC(),
                arc_center=getCenter() + UP * getB() + DOWN * getC(),
                color=WHITE,
                angle=PI,
                start_angle=-PI / 2,
                stroke_width=0,
            )
        )
        outerArcC = always_redraw(
            lambda: Arc(
                radius=getC(),
                arc_center=getCenter() + UP * getB() + DOWN * getC(),
                color=GREY_N400,
                angle=PI,
                start_angle=-PI / 2,
                z_index=0.1,
            )
        )

        refLine = always_redraw(
            lambda: DashedLine(getB() * UP + getCenter(), getCenter(), color=GREY_N400)
        )

        lengthLabel = lengthMarkerV3(
            baseLine.get_end(), baseLine.get_start(), "12", DOWN * 0.4, centerDist=0.4
        )

        # self.add(
        #     circleA,
        #     outerArcA,
        #     circleB,
        #     outerArcB,
        #     circleC,
        #     outerArcC,
        #     baseLine,
        #     refLine,
        #     lengthLabel,
        # )

        self.add(circleC)
        self.play(
            LaggedStart(
                Create(outerArcA, run_time=0.5),
                Create(outerArcC, run_time=0.5),
                Create(outerArcB, run_time=0.5),
                Create(baseLine, run_time=0.5),
                Create(refLine, run_time=0.5),
                FadeIn(circleA, circleB),
                lag_ratio=0.4,
            )
        )
        self.wait(2)

        highlighterCircleB = circleB.copy()
        highlighterCircleB.set_z_index(0.2).set_opacity(0.3).set_color(
            GREY_N400
        ).set_stroke(YELLOW, width=8, opacity=1)
        highlighterCircleA = circleA.copy()
        highlighterCircleA.set_z_index(0.2).set_opacity(0.3).set_color(
            GREY_N400
        ).set_stroke(YELLOW, width=8, opacity=1)
        highlighterCircleC = circleC.copy()
        highlighterCircleC.set_z_index(0.2).set_opacity(0.3).set_color(
            GREY_N400
        ).set_stroke(YELLOW, width=8, opacity=1)
        self.play(
            FadeIn(highlighterCircleB, highlighterCircleA),
            rate_func=there_and_back,
            run_time=2.5,
        )
        self.play(
            FadeIn(highlighterCircleC),
            rate_func=there_and_back,
            run_time=2.5,
        )
        self.wait(0.5)
        self.play(
            GrowArrow(lengthLabel[0]), GrowArrow(lengthLabel[1]), FadeIn(lengthLabel[2])
        )

        radiusMarkerA = always_redraw(
            lambda: Arrow(
                getCenter(),
                getCenter() + a.get_value() / np.sqrt(2) * (UP + LEFT),
                color=GREY_N800,
                stroke_width=4,
                buff=0,
            )
        )

        tempRadiusLabelA = always_redraw(
            lambda: Text("?", color=RED_N, font_size=42)
            .move_to(radiusMarkerA.get_center())
            .shift((DOWN + LEFT) * 0.25)
        )

        radiusLabelA = always_redraw(
            lambda: nText("x", color=GREY_N800)
            .move_to(radiusMarkerA.get_center())
            .shift((DOWN + LEFT) * 0.25)
        )

        radiusMarkerB = always_redraw(
            lambda: Arrow(
                getCenter(),
                getCenter() + getB() / np.sqrt(2) * (UP + RIGHT),
                color=GREY_N800,
                stroke_width=4,
                buff=0,
            )
        )

        tempRadiusLabelB = always_redraw(
            lambda: Text("?", color=RED_N, font_size=42)
            .move_to(radiusMarkerB.get_center())
            .shift((DOWN + RIGHT) * 0.25)
        )

        radiusLabelB = always_redraw(
            lambda: nText("y", color=GREY_N800)
            .move_to(radiusMarkerB.get_center())
            .shift((DOWN + RIGHT) * 0.25)
        )

        self.play(
            LaggedStart(
                GrowArrow(radiusMarkerA),
                FadeIn(tempRadiusLabelA),
                GrowArrow(radiusMarkerB),
                FadeIn(tempRadiusLabelB),
                lag_ratio=0.5,
            )
        )

        self.play(a.animate.set_value(2.5), run_time=3, rate_func=there_and_back)

        self.wait(2)
        self.play(FadeOut(tempRadiusLabelA, tempRadiusLabelB))
        self.play(
            LaggedStart(
                FadeIn(radiusLabelA, shift=RIGHT * 0.5),
                FadeIn(radiusLabelB, shift=LEFT * 0.5),
                lag_ratio=0.5,
            )
        )

        self.wait(1)
        self.play(a.animate.set_value(L / 2), run_time=3)
        self.play(FadeOut(radiusLabelA, radiusLabelB, radiusMarkerA, radiusMarkerB))

        highlighterSemiCircle = (
            Sector(radius=L / 2, arc_center=getCenter(), angle=PI)
            .set_z_index(0.2)
            .set_opacity(0.3)
            .set_color(GREY_N400)
            .set_stroke(YELLOW, width=8, opacity=1)
        )

        self.play(FadeIn(highlighterSemiCircle), run_time=2.5, rate_func=there_and_back)

        self.wait(5)


class Statements(Scene):
    def construct(self):
        stmt = nMath("Area = ", "\\frac{\\pi\\cdot 12^2}{8}")
        stmt2 = nMath("Area = ", "18\\pi")
        self.play(fadeInTex(stmt), run_time=1.5)
        self.wait(0.5)
        self.play(TransformMatchingTex(stmt, stmt2), run_time=1.5)
        self.wait(2)


class Options(Scene):
    def construct(self):
        options = (
            VGroup(
                MathTex("A) \\ 18\\pi", color=BLACK),
                MathTex("B) \\ 24\\pi", color=BLACK),
                MathTex("C) \\ 12\\pi", color=BLACK),
                MathTex("D) \\ 30\\pi", color=BLACK),
            )
            .arrange(DOWN, aligned_edge=LEFT, center=False, buff=0.5)
            .to_edge(UP)
        )

        self.play(FadeIn(options))
        self.wait(4)

        self.play(
            Create(SurroundingRectangle(options[0], corner_radius=0.1, buff=0.18))
        )
        self.wait(4)
        self.wait(1)
