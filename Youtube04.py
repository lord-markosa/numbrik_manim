from manim import *
from utils import *
import random
import math

W = 6
H = 3


class Statement(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        rect = Rectangle(width=W, height=H, color=BLACK)
        rect.move_to(ORIGIN)
        self.play(Create(rect))

        # mark a point P
        P = ORIGIN + 0.15 * W * RIGHT + 0.1 * H * DOWN
        label_P = Text("O", font_size=24, color=BLACK).next_to(P, UP, buff=0.2)
        vertices = rect.get_vertices()

        # Draw lines from point to each vertex
        connectors = [Line(v, P, color=BLACK) for v in vertices]

        self.play(FadeIn(label_P))
        self.play(*[FadeIn(line) for line in connectors])
        self.wait(1)

        PA = connectors[0]
        PB = connectors[1]
        PC = connectors[2]
        PD = connectors[3]

        label_PA = Text(
            "6", font_size=30, color=NUMBRIK_COLOR, font="Comic Sans MS"
        ).next_to(PA, LEFT + UP, buff=-0.9)

        self.play(PA.animate.set_color(NUMBRIK_COLOR), Write(label_PA))
        self.play(PA.animate.set_color(BLACK))

        label_PD = Text(
            "5", font_size=30, color=NUMBRIK_COLOR, font="Comic Sans MS"
        ).next_to(PD, RIGHT + 0.5 * UP, buff=-1)

        self.play(PD.animate.set_color(NUMBRIK_COLOR), Write(label_PD))
        self.play(PD.animate.set_color(BLACK))

        label_PC = Text(
            "8", font_size=30, color=NUMBRIK_COLOR, font="Comic Sans MS"
        ).next_to(PC, LEFT + 0.35 * UP, buff=-1.6)

        self.play(PC.animate.set_color(NUMBRIK_COLOR), Write(label_PC))
        self.play(PC.animate.set_color(BLACK))

        label_PB = Text(
            "x", font_size=30, color=NUMBRIK_COLOR, font="Comic Sans MS"
        ).next_to(PB, RIGHT + 0.5 * UP, buff=-1.7)

        self.play(PB.animate.set_color(NUMBRIK_COLOR), Write(label_PB))
        self.play(PB.animate.set_color(BLACK))

        self.wait(1)
        self.play(
            Create(
                SurroundingRectangle(
                    label_PB, corner_radius=0.15, buff=0.2, color=RED_N100
                )
            )
        )

        self.wait(4)


class Solve(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Create a rectangle
        rect = Rectangle(width=W, height=H, color=BLACK)
        rect.move_to(ORIGIN)
        self.play(Create(rect))

        # mark a point P
        P = ORIGIN + 0.15 * W * LEFT + 0.1 * H * DOWN
        label_P = Text("O", font_size=24, color=BLACK).next_to(
            P, 0.25 * RIGHT + UP, buff=0.2
        )
        vertices = rect.get_vertices()

        A = vertices[0]
        B = vertices[1]
        C = vertices[2]
        D = vertices[3]

        label_A = Text("A", font_size=24, color=BLACK).next_to(A, RIGHT + UP, buff=0.1)
        label_B = Text("B", font_size=24, color=BLACK).next_to(B, LEFT + UP, buff=0.1)
        label_C = Text("C", font_size=24, color=BLACK).next_to(C, LEFT + DOWN, buff=0.1)
        label_D = Text("D", font_size=24, color=BLACK).next_to(
            D, RIGHT + DOWN, buff=0.1
        )

        self.play(FadeIn(label_A, label_B, label_C, label_D))

        # Draw lines from point to each vertex
        connectors = [Line(v, P, color=BLACK) for v in vertices]
        self.play(*[FadeIn(line) for line in connectors])
        self.play(FadeIn(label_P))
        self.wait(1)

        # Drop perpendiculars to each side
        # Use line projection formula
        sides = [Line(vertices[i], vertices[(i + 1) % 4], color=BLUE) for i in range(4)]
        projections = []

        for side in sides:
            proj = side.get_projection(P)
            perp = DashedLine(P, proj, color=NUMBRIK_COLOR)

            projections.append(perp)

        self.play(*[Create(p) for p in projections])
        self.wait(1)

        OW = projections[0]
        OX = projections[1]
        OY = projections[2]
        OZ = projections[3]

        # highlight each small rectangle
        rectangles = [
            Polygon(
                P,
                OW.get_end(),
                A,
                OZ.get_end(),
                fill_color=YELLOW,
                fill_opacity=1,
                stroke_width=0,
            ),
            Polygon(
                P,
                OW.get_end(),
                B,
                OX.get_end(),
                fill_color=YELLOW,
                fill_opacity=1,
                stroke_width=0,
            ),
            Polygon(
                P,
                OX.get_end(),
                C,
                OY.get_end(),
                fill_color=YELLOW,
                fill_opacity=1,
                stroke_width=0,
            ),
            Polygon(
                P,
                OY.get_end(),
                D,
                OZ.get_end(),
                fill_color=YELLOW,
                fill_opacity=1,
                stroke_width=0,
            ),
        ]

        for i in range(4):
            rectangles[i].z_index = -10
            self.play(FadeIn(rectangles[i]), run_time=0.3)
            self.play(FadeOut(rectangles[i]), run_time=0.3)

        self.wait(1)

        # create labels for the perpendicular
        label_w = Text(
            "w", font_size=24, font="Comic Sans MS", color=NUMBRIK_COLOR
        ).next_to(OW, LEFT, buff=0.1)
        label_x = Text(
            "x", font_size=24, font="Comic Sans MS", color=NUMBRIK_COLOR
        ).next_to(OX, UP, buff=0.1)
        label_y = Text(
            "y", font_size=24, font="Comic Sans MS", color=NUMBRIK_COLOR
        ).next_to(OY, LEFT, buff=0.1)
        label_z = Text(
            "z", font_size=24, font="Comic Sans MS", color=NUMBRIK_COLOR
        ).next_to(OZ, UP, buff=0.1)

        self.play(FadeIn(label_w, label_x, label_y, label_z))
        self.wait(1)

        # final solution
        triangle = Polygon(
            P, OY.get_end(), D, fill_color=YELLOW, fill_opacity=1, stroke_width=0
        )
        self.play(FadeIn(triangle))
        self.wait(1)
        self.play(FadeOut(triangle))
        self.wait(1)

        triangle2 = Polygon(
            P, OZ.get_end(), A, fill_color=YELLOW, fill_opacity=1, stroke_width=0
        )

        triangle2.z_index = -10
        self.play(FadeIn(triangle2))
        self.wait(1)
        self.play(FadeOut(triangle2))

        triangle3 = Polygon(
            P, OX.get_end(), B, fill_color=YELLOW, fill_opacity=1, stroke_width=0
        )

        triangle3.z_index = -10
        self.play(FadeIn(triangle3))
        self.wait(1)
        self.play(FadeOut(triangle3))

        triangle4 = Polygon(
            P,
            OY.get_end(),
            C,
            fill_color=YELLOW,
            fill_opacity=1,
            stroke_width=0,
        )

        triangle4.z_index = -10
        self.play(FadeIn(triangle4))
        self.wait(1)
        self.play(FadeOut(triangle4))

        self.wait(4)


class Solution(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        step1 = (
            MathTex(
                "OD^2 = y^2 + z^2",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .to_edge(UP)
        )

        step2 = (
            MathTex(
                "OA^2 = z^2 + w^2",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step1, DOWN, buff=0.35)
        )

        step3 = (
            MathTex(
                "OB^2 = x^2 + w^2",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step2, DOWN, buff=0.35)
        )

        step4 = (
            MathTex(
                "OC^2 = y^2 + x^2",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step3, DOWN, buff=0.35)
        )

        self.play(FadeIn(step1))
        self.wait(1)
        self.play(FadeIn(step2))
        self.wait(1)
        self.play(FadeIn(step3))
        self.wait(1)
        self.play(FadeIn(step4))
        self.wait(1)

        highlight1 = SurroundingRectangle(step1, corner_radius=0.15, buff=0.2)
        highlight2 = SurroundingRectangle(step2, corner_radius=0.15, buff=0.2)
        highlight3 = SurroundingRectangle(step3, corner_radius=0.15, buff=0.2)
        highlight4 = SurroundingRectangle(step4, corner_radius=0.15, buff=0.2)

        step5 = (
            MathTex(
                "OB^2 + OD^2 = x^2 + y^2 + z^2 + w^2",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step4, DOWN, buff=0.5)
        )

        step6 = (
            MathTex(
                "OA^2 + OC^2 = x^2 + y^2 + z^2 + w^2",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step5, DOWN, buff=0.25)
        )

        step_final = (
            MathTex(
                "\\Rightarrow OA^2 + OC^2 = OB^2 + OD^2",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step6, DOWN, buff=0.5)
        )

        highlight5 = SurroundingRectangle(step_final, corner_radius=0.15, buff=0.2)

        self.play(Create(highlight1), Create(highlight3))
        self.play(Write(step5))
        self.play(FadeOut(highlight1, highlight3))
        self.wait(1)

        self.play(Create(highlight2), Create(highlight4))
        self.play(Write(step6))
        self.play(FadeOut(highlight2, highlight4))
        self.wait(1)

        self.play(Write(step_final))
        self.play(Create(highlight5))

        clearScreen(self, 1)

        self.play(FadeIn(step_final.to_edge(UP)))
        self.wait(1)

        step7 = (
            MathTex(
                "x^2 + 5^2 = 6^2 + 8^2",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step_final, DOWN, buff=0.5)
        )

        step8 = (
            MathTex(
                "x^2 = 75",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step7, DOWN, buff=0.25)
        )

        step9 = (
            MathTex(
                "x = 5\\sqrt{3}",
                color=NUMBRIK_COLOR,
                tex_template=TexFontTemplates.comic_sans,
            )
            .scale(0.7)
            .next_to(step8, DOWN, buff=0.25)
        )

        self.play(FadeIn(step7))
        self.wait(1)
        self.play(FadeIn(step8))
        self.wait(1)
        self.play(FadeIn(step9))
        self.play(
            step9.animate.scale(1.3).shift(DOWN * 0.2),
        )
        self.play(
            Create(
                BackgroundRectangle(
                    step9,
                    buff=0.1,
                    corner_radius=0.1,
                    color=YELLOW,
                ).set_z_index(-10)
            )
        )
        self.wait(1)

        self.wait(4)
