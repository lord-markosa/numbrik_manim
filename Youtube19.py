from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        addBackground(self)

        eqn1 = nMath("x+y+z", "=", "1").shift(UP)
        eqn2 = nMath("x^2+y^2+z^2", "=", "29")
        eqn3 = nMath("xyz = -24").shift(DOWN)

        self.play(fadeInTex(eqn1))
        self.play(fadeInTex(eqn2))
        self.play(fadeInTex(eqn3))
        self.wait(4)

        def observe(shouldWait=False):
            self.play(
                eqn1.animate.shift(DOWN).scale(1.1),
                eqn2.animate.shift(DOWN).scale(0.9).set_color(NUMBRIK_COLOR_50),
                eqn3.animate.shift(DOWN).scale(0.9).set_color(NUMBRIK_COLOR40),
            )
            if shouldWait:
                self.wait(1)

            self.play(
                eqn1.animate.shift(UP).scale(0.9 / 1.1).set_color(NUMBRIK_COLOR_50),
                eqn2.animate.shift(UP).scale(1.1 / 0.9).set_color(NUMBRIK_COLOR),
                eqn3.animate.shift(UP).scale(0.9 / 0.9).set_color(NUMBRIK_COLOR_50),
            )
            if shouldWait:
                self.wait(1)

            self.play(
                eqn1.animate.shift(UP).scale(0.9 / 0.9).set_color(NUMBRIK_COLOR_50),
                eqn2.animate.shift(UP).scale(0.9 / 1.1).set_color(NUMBRIK_COLOR_50),
                eqn3.animate.shift(UP).scale(1.1 / 0.9).set_color(NUMBRIK_COLOR),
            )
            if shouldWait:
                self.wait(1)

            self.play(
                eqn1.animate.shift(DOWN).scale(1 / 0.9).set_color(NUMBRIK_COLOR),
                eqn2.animate.shift(DOWN).scale(1 / 0.9).set_color(NUMBRIK_COLOR),
                eqn3.animate.shift(DOWN).scale(1 / 1.1).set_color(NUMBRIK_COLOR),
            )
            self.wait(1)

        observe(True)

        self.play(eqn1.animate.shift(UP))

        eqn2_ = nMath(
            "(", "x+y+z", ")^2", "- (", "x^2 + y^2 + z^2", ") = ", "1^2", "-", "29"
        ).shift(UP)

        self.play(
            TransformFromCopy(eqn1[0], eqn2_[1]),
            TransformFromCopy(eqn1[2], eqn2_[6]),
            Write(eqn2_[0]),
            Write(eqn2_[2]),
        )
        self.play(Write(eqn2_[3]), Write(eqn2_[5]), Write(eqn2_[7]))

        self.play(
            ReplacementTransform(eqn2[0], eqn2_[4]),
            ReplacementTransform(eqn2[2], eqn2_[8]),
            FadeOut(eqn2[1]),
        )
        self.wait(1)

        eqn2 = nMath("2(xy + yz + zx) = -28")
        self.play(fadeInTex(eqn2))
        self.wait(1)
        self.play(Transform(eqn2, nMath("xy+yz+zx = -14")))
        self.wait(1)
        self.play(LaggedStart(FadeOut(eqn2_), eqn1.animate.shift(DOWN), lag_ratio=0.6))
        self.wait(1)

        observe()

        label1 = Tex(
            "Sum of roots",
            tex_template=TexFontTemplates.comic_sans,
            color=BLACK,
            font_size=40,
        ).next_to(eqn1, LEFT + UP, buff=1)
        arrow1 = Arrow(
            label1.get_corner(DOWN + RIGHT), eqn1.get_corner(UP + LEFT), color=GREY_N400
        )
        self.play(
            LaggedStart(
                Create(
                    SurroundingRectangle(
                        eqn1, corner_radius=0.1, buff=0.15, color=GREEN_N100
                    )
                ),
                fadeInTex(label1),
                GrowArrow(arrow1),
                lag_ratio=0.6,
            )
        )
        self.wait(1)

        label2 = Tex(
            "Sum of product\\\\ of roots taken\\\\ two at a time",
            tex_template=TexFontTemplates.comic_sans,
            color=BLACK,
            font_size=40,
        ).next_to(eqn2, RIGHT, buff=1.4)

        arrow2 = Arrow(
            label2.get_edge_center(LEFT), eqn2.get_edge_center(RIGHT), color=GREY_N400
        )
        self.play(
            LaggedStart(
                Create(
                    SurroundingRectangle(
                        eqn2, corner_radius=0.1, buff=0.15, color=YELLOW
                    )
                ),
                fadeInTex(label2),
                GrowArrow(arrow2),
                lag_ratio=0.6,
            )
        )
        self.wait(1)

        label3 = Tex(
            "Product of roots",
            tex_template=TexFontTemplates.comic_sans,
            color=BLACK,
            font_size=40,
        ).next_to(eqn3, LEFT + DOWN, buff=1)

        arrow3 = Arrow(
            label3.get_corner(UP + RIGHT), eqn3.get_corner(DOWN + LEFT), color=GREY_N400
        )
        self.play(
            LaggedStart(
                Create(
                    SurroundingRectangle(
                        eqn3, corner_radius=0.1, buff=0.15, color=RED_N50
                    )
                ),
                fadeInTex(label3),
                GrowArrow(arrow3),
                lag_ratio=0.6,
            )
        )

        clearScreen(self, 4)

        eqn = nMath("w^3 - w^2 -14w + 24 = 0").set_color(BLACK)
        step1 = nMath("1^3 - 1^2 - 14 \\cdot 1 + 24 \\ne 0").shift(0.5 * DOWN)
        step1_ = nMath("2^3 - 2^2 - 14 \\cdot 2 + 24 = 0").shift(0.5 * DOWN)
        step2 = nMath("(w-2)(w^2 + w -12) = 0").shift(UP)
        step3 = nMath("(w-2)(w-3)(w+4) = 0")
        step4 = nMath("w = 2, 3, -4").shift(DOWN)

        self.play(fadeInTex(eqn))
        self.wait(2)
        self.play(
            LaggedStart(eqn.animate.shift(0.5 * UP), fadeInTex(step1), lag_ratio=0.8)
        )
        self.wait(1)
        self.play(FadeOut(step1))
        self.play(fadeInTex(step1_))
        self.wait(1)
        self.play(FadeOut(step1_), eqn.animate.shift(1.5 * UP))
        self.play(fadeInTex(step2))
        self.wait(1)

        self.play(fadeInTex(step3))
        self.wait(1)

        self.play(fadeInTex(step4))
        self.wait(1)

        self.play(
            Create(
                SurroundingRectangle(
                    step4, corner_radius=0.1, buff=0.15, color=RED_N100
                )
            )
        )

        clearScreen(self, 4)

        final = nMath("(x, y, z) = Permutation(2, 3, -4)").set_color(BLACK)
        self.play(fadeInTex(final))
        self.play(
            Create(
                SurroundingRectangle(final, corner_radius=0.15, buff=0.25, color=YELLOW)
            )
        )

        self.wait(10)


class Thumbnail(Scene):
    def construct(self):
        eqn1 = MathTex(
            "\\mathbf{x+y+z",
            "=",
            "1}",
            color=BLACK,
            tex_template=TexFontTemplates.droid_sans,
        ).shift(UP)
        eqn2 = MathTex(
            "\\mathbf{x^2+y^2+z^2",
            "=",
            "29}",
            color=BLACK,
            tex_template=TexFontTemplates.droid_sans,
        )
        eqn3 = MathTex(
            "\\mathbf{xyz = -24}", color=BLACK, tex_template=TexFontTemplates.droid_sans
        ).shift(DOWN)

        self.add(VGroup(eqn1, eqn2, eqn3).scale(2))

        self.wait(10)
