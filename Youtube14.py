from manim import *
from utils import *


class SymmetricPolynomialSolver(Scene):
    def construct(self):
        # Step 1: Display original equation
        eq1 = nMath(
            "2", "x^4", "-", "x^3", "-11", "x^2", "-", "x", "+", "2", "= 0"
        ).to_edge(UP)
        self.play(FadeIn(eq1, shift=UP))
        self.wait(1)

        # Step 2: Point out symmetry
        self.play(
            eq1.animate.set_color_by_tex_to_color_map(
                {"2": RED_N, "-": GREEN, "-11": PURPLE_E, "x^2": NUMBRIK_COLOR}
            )
        )
        self.wait(1)

        coefficients = (
            nMath("2", "\\quad", "-1", "\\quad", "-11", "\\quad", "-1", "\\quad", 2)
            .next_to(eq1, DOWN, buff=1.5)
            .set_color_by_tex_to_color_map({"2": RED_N, "-": GREEN, "-11": PURPLE_E})
        )

        self.play(
            TransformFromCopy(eq1[0], coefficients[0]),
            TransformFromCopy(eq1[2], coefficients[2]),
            TransformFromCopy(eq1[4], coefficients[4]),
            TransformFromCopy(eq1[6], coefficients[6]),
            TransformFromCopy(eq1[9], coefficients[8]),
        )

        self.wait(1)

        arrow1 = CurvedArrow(
            coefficients[0].get_bottom() + 0.2 * DOWN,
            coefficients[8].get_bottom() + 0.2 * DOWN,
            color=GREY_N400,
        )
        arrow2 = CurvedArrow(
            coefficients[6].get_top() + 0.2 * UP,
            coefficients[2].get_top() + 0.2 * UP + 0.2 * RIGHT,
            color=GREY_N400,
        )

        self.play(Create(arrow1))
        self.play(Create(arrow2))

        self.wait(1)

        self.play(
            eq1.animate.set_color(NUMBRIK_COLOR), FadeOut(arrow1, arrow2, coefficients)
        )

        self.wait(1)

        eq15 = nMath("2x^4", "+2", "-x^3", "-x", "-11x^2", "= 0").next_to(eq1, 0)

        self.play(
            ReplacementTransform(eq1[0:2], eq15[0]),
            ReplacementTransform(eq1[8:10], eq15[1]),
            ReplacementTransform(eq1[2:4], eq15[2]),
            ReplacementTransform(eq1[6:8], eq15[3]),
            ReplacementTransform(eq1[4:6], eq15[4]),
            ReplacementTransform(eq1[10], eq15[5]),
        )

        self.wait(1)

        # Step 3: Divide equation by x^2
        eq2 = nMath("\\frac{2x^4 + 2 - x^3 - x - 11x^2}{x^2} = 0").next_to(
            eq15, DOWN, buff=0.5
        )
        self.play(FadeIn(eq2))
        self.wait(1)

        # Step 3: Divide equation by x^2
        eq3 = nMath(
            "2\\left(x^2 + \\frac{1}{x^2}\\right) - \\left(x + \\frac{1}{x}\\right) - 11 = 0"
        ).next_to(eq2, DOWN, buff=0.5)
        self.play(FadeIn(eq3))
        self.wait(1)

        self.play(FadeOut(eq1, eq15, eq2))
        self.play(eq3.animate.to_edge(UP))
        self.wait(1)

        # Step 4: Rewrite with x + 1/x = y
        sub = nMath("x + \\frac{1}{x} = y").next_to(eq3, DOWN, buff=0.5)
        self.play(FadeIn(sub, shift=UP))
        self.wait(1)

        identity = nMath(
            "\\Rightarrow x^2 + \\frac{1}{x^2}", "+ 2", "=", "y^2"
        ).next_to(sub, DOWN, buff=0.5)
        self.play(FadeIn(identity))
        self.wait(1)

        identity2 = nMath(
            "\\Rightarrow x^2 + \\frac{1}{x^2}", "=", "y^2", "-2"
        ).next_to(identity, 0)

        self.play(
            ReplacementTransform(identity[0], identity2[0]),
            ReplacementTransform(identity[2], identity2[1]),
            ReplacementTransform(identity[3], identity2[2]),
            ReplacementTransform(identity[1], identity2[3]),
        )
        self.wait(1)

        # # Step 5: Final substituted quadratic
        quad = nMath("2(y^2 - 2) - y - 11 = 0").next_to(sub, DOWN, buff=0.75)
        self.play(
            Transform(eq3, quad),
            sub.animate.to_edge(UP),
            identity.animate.next_to(sub, 0),
        )
        self.wait(1)

        quad2 = nMath("2y^2 - y - 15 = 0").next_to(quad, DOWN, buff=0.5)
        self.play(FadeIn(quad2))
        self.wait(1)

        self.play(
            FadeOut(sub, identity2, eq3),
            quad2.animate.to_edge(UP),
        )

        quad3 = nMath("(2y+5)(y-3) = 0").next_to(quad2, DOWN, buff=0.5)
        self.play(FadeIn(quad3))

        # Step 6: Solve the quadratic
        roots = nMath("y = 3", "\\quad \\text{or} \\quad y = -\\frac{5}{2}").next_to(
            quad3, DOWN, buff=0.5
        )
        self.play(FadeIn(roots))
        self.wait(2)

        clearScreen(self, 2)

        # Step 7: Replace y with x + 1/x
        case1 = nMath("\\text{Case I: } y = 3").to_edge(UP)
        back1 = nMath("x + \\frac{1}{x} = 3").next_to(case1, DOWN, buff=0.5)
        quad1 = nMath("x^2 - 3x + 1 = 0").next_to(back1, DOWN, buff=0.5)
        ans1 = nMath("x = \\frac{3 \\pm \\sqrt{5}}{2}").next_to(quad1, DOWN, buff=0.5)
        self.play(FadeIn(case1, shift=UP))
        self.wait(1)
        self.play(Write(back1))
        self.wait(1)
        self.play(FadeIn(quad1))
        self.wait(1)
        self.play(FadeIn(ans1))
        self.wait(2)

        clearScreen(self, 2)

        case2 = nMath("\\text{Case II: } y = -\\frac{5}{2}").to_edge(UP)
        back2 = nMath("x + \\frac{1}{x} = -\\frac{5}{2}").next_to(
            case2, DOWN, buff=0.75
        )
        quad2 = nMath("2x^2 + 5x + 2 = 0").next_to(back2, DOWN, buff=0.5)
        quad23 = nMath("(2x+1)(x+2) = 0").next_to(quad2, DOWN, buff=0.5)
        ans2 = nMath(
            "\\quad x = -\\frac{1}{2} \\quad or \\quad x = -2",
        ).next_to(quad23, DOWN, buff=0.5)
        self.play(FadeIn(case2, shift=UP))
        self.wait(1)
        self.play(Write(back2))
        self.wait(1)
        self.play(FadeIn(quad2))
        self.wait(1)
        self.play(FadeIn(quad23))
        self.wait(1)
        self.play(FadeIn(ans2))
        self.wait(2)
        clearScreen(self, 2)

        # # Step 9: Show all 4 roots
        final_roots = nMath(
            "x = \\frac{3 \\pm \\sqrt{5}}{2},",
            "\\quad x = -\\frac{1}{2},",
            "\\quad x = -2",
        ).to_edge(UP)
        self.play(FadeIn(final_roots, shift=UP))
        highlight(self, final_roots, buff=0.2, wait_time=4)
