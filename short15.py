from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        themeColor = GREY_N500
        radius = 3
        A = LEFT * radius
        B = RIGHT * radius

        semicircle = ArcBetweenPoints(B, A, angle=PI, color=themeColor)

        # Point C moving on arc from 60 to 10 degrees
        arc_tracker = ValueTracker(120)

        def get_c():
            angle_rad = arc_tracker.get_value() * DEGREES
            return radius * np.array([np.cos(angle_rad), np.sin(angle_rad), 0])

        triangle_arc = always_redraw(
            lambda: Polygon(
                A, B, get_c(), fill_color=YELLOW, fill_opacity=1, color=themeColor
            )
        )

        base = Line(A, B, color=themeColor)

        def getHeight():
            return radius * np.sin(arc_tracker.get_value() * DEGREES)

        base_marker = DoubleArrow(
            B + DOWN * 0.4,
            A + DOWN * 0.4,
            color=themeColor,
            stroke_width=4,
            buff=0,
        ).set_z_index(-20)

        base_label = Text(
            "8", font="Comic Sans MS", font_size=28, color=NUMBRIK_COLOR
        ).next_to(base_marker, 0, buff=0.2)

        base_label_background = BackgroundRectangle(
            base_label, color=WHITE, buff=0.1, fill_opacity=1
        ).set_z_index(-10)

        right_angle = always_redraw(
            lambda: RightAngle(
                Line(get_c(), A),
                Line(get_c(), B),
                length=0.3,
                quadrant=(1, 1),
                color=themeColor,
            )
        )

        def getLocusP3():
            return DashedLine(
                A + UP * getHeight(),
                B + UP * getHeight(),
                color=themeColor,
            )

        def getHeightMarker():
            return DoubleArrow(
                B + 0.5 * RIGHT,
                B + 0.5 * RIGHT + UP * getHeight(),
                color=themeColor,
                stroke_width=4,
                buff=0,
            ).set_z_index(-20)

        def getHeightLabel(label):
            return Text(
                label, font="Comic Sans MS", font_size=28, color=NUMBRIK_COLOR
            ).next_to(getHeightMarker(), 0)

        def getHeightLabelBackground(height_label):
            return BackgroundRectangle(
                height_label, color=WHITE, buff=0.1, fill_opacity=1
            ).set_z_index(-10)

        ## PART 1: Problem Introduction

        self.play(Create(base), Create(triangle_arc))
        self.play(Create(right_angle))
        self.play(FadeIn(base_label, base_label_background), run_time=0.5)
        self.play(GrowArrow(base_marker), run_time=0.5)

        height_label = getHeightLabel("5")
        locus_p3 = getLocusP3()
        height_label_background = getHeightLabelBackground(height_label)
        self.play(
            Create(locus_p3),
            FadeIn(height_label, height_label_background),
            run_time=0.5,
        )

        height_marker = getHeightMarker()
        self.play(GrowArrow(height_marker), run_time=0.5)

        self.wait(4)

        self.play(
            FadeOut(locus_p3, height_label, height_label_background, height_marker)
        )

        self.wait(1)

        label_a = Text(
            "B", font="Comic Sans MS", font_size=28, color=NUMBRIK_COLOR
        ).move_to((get_c() + B) / 2 + 0.3 * UP + 0.1 * RIGHT)

        label_b = Text(
            "A", font="Comic Sans MS", font_size=28, color=NUMBRIK_COLOR
        ).move_to((get_c() + A) / 2 + 0.3 * UP + 0.2 * LEFT)

        self.play(FadeIn(label_a, label_b))

        self.wait(4)

        self.play(FadeOut(label_a, label_b))
        self.play(Create(semicircle))
        self.wait(1)

        self.play(arc_tracker.animate.set_value(90))

        newHeightLabel = getHeightLabel("R = 4")
        newHeightLabelBackground = getHeightLabelBackground(newHeightLabel)
        newLocusP3 = getLocusP3()

        newHeightMarker = getHeightMarker()
        self.play(
            Create(newLocusP3),
            FadeIn(newHeightLabel, newHeightLabelBackground),
        )
        self.play(GrowArrow(newHeightMarker))

        self.wait(4)

        self.play(
            FadeOut(
                newLocusP3, newHeightLabel, newHeightLabelBackground, newHeightMarker
            ),
        )

        self.play(arc_tracker.animate.set_value(120))

        self.play(
            FadeIn(locus_p3, height_label, height_label_background, height_marker)
        )
        highlight(self, height_label, color=RED, buff=0.2, wait_time=3)
        self.wait(1)


class Statements(Scene):
    def construct(self):
        step0 = MathTex(
            "Area",
            "\\ne",
            "\\, 20",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        step_ = MathTex(
            "\\ne",
            color=NUMBRIK_COLOR,
        ).next_to(step0[1], 0)

        step1 = MathTex(
            "Area = \\frac{1}{2}\\cdot8\\cdot5 = 20",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        step2 = MathTex(
            "A^2 + B^2 = 8^2 = 64",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        self.play(FadeIn(step0[0], step0[2], step_))
        clearScreen(self, 1)

        self.play(FadeIn(step1))
        clearScreen(self, 1)

        self.play(FadeIn(step2))
        clearScreen(self, 1)

        step3 = MathTex(
            "\\text{AM-GM Inequality}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        step4 = MathTex(
            "\\frac{A^2 + B^2}{2} \\geq \\sqrt{A^2B^2}",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step3, DOWN, buff=0.5)

        step5 = MathTex(
            "\\Rightarrow \\frac{64}{2} \\geq AB",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step4, DOWN, buff=0.5)

        step6 = MathTex(
            "\\text{Area} = \\frac{AB}{2} \\geq 16 ",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(step5, DOWN, buff=0.5)

        self.play(FadeIn(step3))
        self.wait(1)
        self.play(FadeIn(step4))
        self.wait(1)
        self.play(FadeIn(step5))
        self.wait(1)
        self.play(FadeIn(step6))
        clearScreen(self, 4)

        extra1 = MathTex(
            "Radius = \\frac{8}{2} = 4",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).to_edge(UP)

        extra1_ = MathTex(
            "\\text{Max height} = 4",
            color=NUMBRIK_COLOR,
            tex_template=TexFontTemplates.comic_sans,
        ).next_to(extra1, DOWN, buff=0.5)

        self.play(FadeIn(extra1))
        self.wait(1)
        self.play(FadeIn(extra1_))
        clearScreen(self, 4)
