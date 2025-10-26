from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        addBackground(self)

        # Part 0: Create the catenary: Rope, poles and ground
        axes = getAxis([-5, 5], [-15, 20], 8, 7)
        pseudoAxis = getAxis([-0.5, 3], [-1, 20], 5, 5)

        catenary = axes.plot(
            lambda x: np.cosh(x), [-3.5, 3.5], color=NUMBRIK_COLOR, stroke_width=6
        )

        P = catenary.get_start()
        Q = catenary.get_end()
        pole1 = Line(P, P + DOWN * 5.5, color=BLACK, stroke_width=10)
        pole2 = Line(Q, Q + DOWN * 5.5, color=BLACK, stroke_width=10)
        ground = Line(
            pole1.get_end() + LEFT * 1.5,
            pole2.get_end() + RIGHT * 1.5,
            color=GREY,
            stroke_width=12,
        )

        # Part 0: Animation
        self.play(
            LaggedStart(
                Create(ground),
                Create(pole1),
                Create(pole2),
                Create(catenary),
                lag_ratio=0.8,
            )
        )

        self.wait(2)

        # Part 1: Create a piece and fade in axis
        piece = axes.plot(lambda x: np.cosh(x), [2, 2.5], color=BLACK, stroke_width=6)

        # Part1: Animation (I)
        self.play(
            AnimationGroup(FadeIn(piece), FadeOut(pole1, pole2, catenary, ground)),
        )

        self.play(
            piece.animate.scale(2.5).shift(ORIGIN - piece.get_center() + 0.5 * UP),
            FadeIn(pseudoAxis.get_x_axis()),
        )

        # Part 1: create dashed lines on the coord(II)
        pieceStart = piece.get_start()
        pieceEnd = piece.get_end()

        pseudoXAxis = Line(pseudoAxis.get_origin(), pseudoAxis.get_origin() + 2 * RIGHT)
        x = pseudoXAxis.get_projection(pieceStart)
        xPlusDx = pseudoXAxis.get_projection(pieceEnd)

        xLabel = nMath("x").next_to(x, DOWN).scale(0.8)
        xPlusDxLabel = (
            nMath("x+dx")
            .next_to(xLabel, RIGHT)
            .shift(0.04 * UP + RIGHT * 0.4)
            .scale(0.8)
        )

        pseudoYAxis = Line(pseudoAxis.get_origin(), pseudoAxis.get_origin() + 2 * UP)
        y = pseudoYAxis.get_projection(pieceStart)
        yPlusDy = pseudoYAxis.get_projection(pieceEnd)

        yLabel = nMath("y").next_to(y, LEFT).scale(0.8)
        yPlusDyLabel = nMath("y+dy").next_to(yPlusDy, LEFT, buff=0.1).scale(0.8)

        dashedLineX = DashedLine(pieceStart, x, color=GREY_N100)
        dashedLineXPlusDx = DashedLine(pieceEnd, xPlusDx, color=GREY_N100)

        dashedLineY = DashedLine(pieceStart, y, color=GREY_N100)
        dashedLineYPlusDy = DashedLine(pieceEnd, yPlusDy, color=GREY_N100)

        helperLine = Line(pieceStart, pieceStart + 2 * RIGHT, color=GREY_N100)

        slopeAngle = Angle(
            helperLine,
            Line(pieceStart, pieceEnd + 0.3 * DOWN),
            color=GREY_N100,
            radius=0.5,
        )

        angleLabel = (
            nMath("\\theta").next_to(slopeAngle, RIGHT, buff=0.1).shift(UP * 0.1)
        )

        self.play(
            LaggedStart(
                Create(dashedLineX),
                Create(dashedLineXPlusDx),
                lag_ratio=0.5,
            )
        )
        self.play(
            FadeIn(xLabel, shift=UP * 0.5),
            FadeIn(xPlusDxLabel, shift=UP * 0.5),
        )
        self.wait(2)

        # Part 3: FBD

        tension1End = 2.4 * pieceEnd - 1.4 * pieceStart
        tension1 = Arrow(pieceEnd, tension1End, color=RED_N100, buff=0)

        labelTension1 = (
            nMath("T(x+dx)").scale(0.8).next_to(tension1.get_end(), RIGHT, buff=0.2)
        )

        tension1x = Arrow(
            pieceEnd, np.array([tension1End[0], pieceEnd[1], 0]), color=RED_N100, buff=0
        )
        labelTension1x = (
            nMath("T_x(x+dx)").scale(0.8).next_to(tension1x.get_end(), RIGHT, buff=0.2)
        )

        tension1y = Arrow(
            pieceEnd, np.array([pieceEnd[0], tension1End[1], 0]), color=RED_N100, buff=0
        )
        labelTension1y = (
            nMath("T_y(x+dx)")
            .scale(0.8)
            .next_to(tension1y.get_end(), RIGHT, buff=0.4)
            .shift(0.2 * DOWN)
        )

        tension2End = 2.4 * pieceStart - 1.4 * pieceEnd
        tension2 = Arrow(pieceStart, tension2End, color=RED_N100, buff=0)

        labelTension2 = (
            nMath("T(x)")
            .scale(0.8)
            .next_to(tension2.get_end(), LEFT, buff=0.2)
            .shift(0.2 * UP)
        )

        tension2x = Arrow(
            pieceStart,
            np.array([tension2End[0], pieceStart[1], 0]),
            color=RED_N100,
            buff=0,
        )
        labelTension2x = (
            nMath("T_x(x)").scale(0.8).next_to(tension2x.get_end(), LEFT, buff=0.2)
        )

        tension2y = Arrow(
            pieceStart,
            np.array([pieceStart[0], tension2End[1], 0]),
            color=RED_N100,
            buff=0,
        )
        labelTension2y = (
            nMath("T_y(x)")
            .scale(0.8)
            .next_to(tension2y.get_end(), LEFT, buff=0.4)
            .shift(0.2 * UP)
        )

        gravity = Arrow(
            (pieceStart + pieceEnd) / 2 + 0.13 * DOWN,
            (pieceStart + pieceEnd) / 2 + 1.5 * DOWN,
            color=RED_N100,
            buff=0,
        )
        gravityLabel = (
            nMath("mg")
            .scale(0.9)
            .next_to(gravity.get_end(), RIGHT, buff=0.4)
            .shift(0.1 * UP)
        )

        dashedLineXPlusDxTransformed = VGroup(
            DashedLine(pieceEnd, pieceEnd + 1.5 * DOWN, color=GREY_N50),
            DashedLine(xPlusDx + UP, xPlusDx, color=GREY_N50),
        )

        helperLine1 = Line(
            pieceStart, np.array([pieceEnd[0], pieceStart[1], 0]), color=GREY_N100
        )

        helperLabel1 = nMath("dx").scale(0.8).next_to(helperLine1, DOWN, buff=0.2)

        helperLine2 = Line(
            pieceEnd, np.array([pieceEnd[0], pieceStart[1], 0]), color=GREY_N100
        )

        helperLabel2 = nMath("dy").scale(0.8).next_to(helperLine2, RIGHT, buff=0.2)

        lengthDs = nMath("ds").scale(0.8).next_to(piece, LEFT + UP, buff=-0.4)

        # Part 3: Animation
        self.play(
            LaggedStart(
                GrowArrow(tension1),
                FadeIn(labelTension1, shift=0.5 * DOWN),
                lag_ratio=0.7,
            )
        )
        self.wait(1)
        self.play(
            LaggedStart(
                GrowArrow(tension2),
                FadeIn(labelTension2, shift=0.5 * DOWN),
                lag_ratio=0.7,
            )
        )
        self.wait(1)
        self.play(
            LaggedStart(
                GrowArrow(gravity),
                AnimationGroup(
                    FadeOut(dashedLineXPlusDx), FadeIn(dashedLineXPlusDxTransformed)
                ),
                FadeIn(gravityLabel),
                lag_ratio=0.7,
            ),
        )
        self.wait(1)

        self.play(
            Transform(tension1, VGroup(tension1x, tension1y)),
            Transform(labelTension1, VGroup(labelTension1x, labelTension1y)),
        )
        self.play(
            Transform(tension2, VGroup(tension2x, tension2y)),
            Transform(labelTension2, VGroup(labelTension2x, labelTension2y)),
        )

        grp = VGroup(
            piece,
            pseudoAxis.get_x_axis(),
            dashedLineX,
            dashedLineXPlusDxTransformed,
            labelTension1,
            labelTension2,
            xPlusDxLabel,
            xLabel,
            tension1,
            tension2,
            gravity,
            gravityLabel,
        )
        self.play(grp.animate.to_edge(LEFT))

        # part 4: balance force quation

        ## Horizontal components
        forceBalancingXLabel = (
            nMath("\\text{Balancing forces along x:}")
            .shift(UP * 1.5 + 4 * RIGHT)
            .scale(0.8)
        )
        eq1 = (
            nMath("T_x(x) = T_x(x+dx)", color=BLACK)
            .scale(0.9)
            .shift(UP * 0.65 + 4 * RIGHT)
        )

        # Animation:

        self.play(fadeInTex(forceBalancingXLabel))

        hgl = solidHighlight(
            self,
            [labelTension1[0], labelTension2[0]],
            buff=0.2,
            wait_time=0.5,
            unhighlight=False,
        )

        self.play(fadeInTex(eq1))
        self.play(highlight.animate.set_opacity(0) for highlight in hgl)
        self.wait(1)

        # Vertical Components

        forceBalancingYLabel = (
            nMath("\\text{Balancing forces along y:}")
            .shift(DOWN * 0.65 + 4 * RIGHT)
            .scale(0.8)
        )

        eq2 = (
            nMath("T_y(x+dx)", "=", "mg", "+", "T_y(x)", color=BLACK)
            .scale(0.9)
            .shift(DOWN * 1.5 + 4 * RIGHT)
        )

        eq2_ = (
            nMath("T_y(x+dx)", "-", "T_y(x)", "=", "mg", color=BLACK)
            .scale(0.9)
            .shift(DOWN * 1.5 + 4 * RIGHT)
        )

        ## Animation
        self.play(fadeInTex(forceBalancingYLabel))

        hgl = solidHighlight(
            self,
            [labelTension1[1], labelTension2[1], gravityLabel],
            buff=0.2,
            wait_time=0.5,
            unhighlight=False,
        )

        self.play(fadeInTex(eq2))
        self.wait(1)
        self.play(TransformMatchingTex(eq2, eq2_))
        self.play(highlight.animate.set_opacity(0) for highlight in hgl)

        self.wait(10)


class Final(Scene):
    def construct(self):
        # Part 0: Create the catenary: Rope, poles and ground
        axes = getAxis([-5, 5], [-15, 20], 8, 7)

        catenary = axes.plot(
            lambda x: np.cosh(x), [-3.5, 3.5], color=NUMBRIK_COLOR, stroke_width=6
        )

        P = catenary.get_start()
        Q = catenary.get_end()
        pole1 = Line(P, P + DOWN * 5.5, color=BLACK, stroke_width=10)
        pole2 = Line(Q, Q + DOWN * 5.5, color=BLACK, stroke_width=10)
        ground = Line(
            pole1.get_end() + LEFT * 1.5,
            pole2.get_end() + RIGHT * 1.5,
            color=GREY,
            stroke_width=12,
        )

        # Part 0: Animation
        self.play(
            LaggedStart(
                Create(ground),
                Create(pole1),
                Create(pole2),
                Create(catenary),
                lag_ratio=0.8,
            ),
            run_time=2,
        )

        self.play(Create(axes))

        grp = VGroup(pole1, pole2, axes, catenary, ground)
        self.play(grp.animate.scale(0.7).to_edge(UP))

        catenary1 = nMath("y", "= A\\frac{e^{kx} + e^{-kx}}{2}", "+ C").next_to(
            grp, DOWN, buff=0.7
        )
        self.play(fadeInTex(catenary1))
        solidHighlight(self, catenary1, buff=0.2, corner_radius=0.18, unhighlight=0)
        self.wait(10)


class Statements(Scene):
    def construct(self):
        eq1 = nMath("U", "= \\int", "(dm)", "gy")
        eq2 = nMath("U", "= \\int", "\\mu", "gy", "\\sqrt{1+y'^2}dx")
        eq3 = nMath("y(x)\\text{ that minimizes U}").shift(DOWN * 0.8)
        self.play(fadeInTex(eq1))
        self.wait(1)
        self.play(TransformMatchingTex(eq1, eq2))
        self.play(eq2.animate.shift(0.5 * UP), fadeInTex(eq3))
        self.wait(10)


class Intro2(Scene):
    def construct(self):
        # Part 0: Create the catenary: Rope, poles and ground
        axes = getAxis([-5, 5], [-25, 5], 7, 7).shift(DOWN)

        catenary = axes.plot(
            lambda x: -np.cosh(x), [-3.5, 3.5], color=RED, stroke_width=10
        )

        P = catenary.get_start()
        Q = catenary.get_end()
        ground = Line(
            P + LEFT * 0.5,
            Q + RIGHT * 0.5,
            color=GREY,
            stroke_width=12,
        )

        gravity = Arrow(
            UP, 2 * DOWN, tip_length=2, stroke_width=10, color=NUMBRIK_COLOR
        )
        label_grav = nMath("g").next_to(gravity, RIGHT, buff=0.2).scale(1.2)
        # self.add(gravity, label_grav)

        title = (
            nMath('\\text{"Catenary Arch"}').scale(1.4).to_edge(UP).shift(0.5 * DOWN)
        )

        # Part 0: Animation
        self.play(
            LaggedStart(
                Create(ground),
                Create(catenary),
                lag_ratio=0.8,
            )
        )
        self.play(LaggedStart(GrowArrow(gravity), FadeIn(label_grav), lag_ratio=0.7))
        self.play(fadeInTex(title))
        self.wait(10)
