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

        # self.add(piece, helperLine1, helperLine2, helperLabel1, helperLabel2, lengthDs)
        # self.add()

        # self.play(FadeOut(dashedLineXPlusDx), FadeIn(dashedLineXPlusDxTransformed))
        # self.add(gravity, gravityLabel)

        # self.add(tension1, tension2, gravity)

        self.wait(10)


class TensionBreakdown:
    def getScene():
        def createComponents(force, color):
            forceStart = force.get_start()
            forceEnd = force.get_end()

            forceX = Arrow(
                forceStart,
                np.array([forceEnd[0], forceStart[1], 0]),
                color=color,
                buff=0,
            )

            forceY = Arrow(
                forceStart,
                np.array([forceStart[0], forceEnd[1], 0]),
                color=color,
                buff=0,
            )

            return forceX, forceY

        tension = Arrow(ORIGIN, 3 * UP + 2.5 * RIGHT, color=GREY_N800, buff=0)
        tension.move_to(ORIGIN)

        tensionX, tensionY = createComponents(tension, GREY_N800)

        labelTensionX = nMath("T_x(x)").next_to(tensionX, RIGHT, buff=0.2)
        labelTensionY = nMath("T_y(x)").next_to(tensionY, UP, buff=0.2)
        labelTension = nMath("T(x)").next_to(tension, UP + RIGHT, buff=0.2)

        angle = Angle(tensionX, tension, color=GREY_N800, radius=0.8)
        angleLabel = (
            nMath("\\theta").next_to(angle, RIGHT, buff=0.2).scale(1.5).shift(0.2 * UP)
        )

        return VGroup(
            tension,
            tensionX,
            tensionY,
            labelTensionX,
            labelTensionY,
            labelTension,
            angle,
            angleLabel,
        )


class AnalysisEqn1(Scene):
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

        # Part 1: Create a piece and fade in axis (I)
        piece = axes.plot(lambda x: np.cosh(x), [2, 2.5], color=BLACK, stroke_width=6)
        (piece.scale(2.5).shift(ORIGIN - piece.get_center() + 0.5 * UP),)

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

        helperLine1 = Line(
            pieceStart, np.array([pieceEnd[0], pieceStart[1], 0]), color=GREY_N100
        )

        helperLabel1 = nMath("dx").scale(0.8).next_to(helperLine1, DOWN, buff=0.2)

        helperLine2 = Line(
            pieceEnd, np.array([pieceEnd[0], pieceStart[1], 0]), color=GREY_N100
        )

        helperLabel2 = nMath("dy").scale(0.8).next_to(helperLine2, RIGHT, buff=0.2)

        lengthDs = nMath("ds").scale(0.8).next_to(piece, LEFT + UP, buff=-0.4)

        grp = VGroup(
            piece,
            pseudoAxis,
            dashedLineX,
            dashedLineXPlusDx,
            dashedLineY,
            dashedLineYPlusDy,
            xPlusDxLabel,
            xLabel,
            yLabel,
            yPlusDyLabel,
            helperLine1,
            slopeAngle,
            angleLabel,
        ).shift(RIGHT * 4 + 0.5 * UP)

        # self.add(grp)

        eq1 = (
            nMath("T_x(x) = T_x(x+dx)", color=BLACK)
            .scale(0.9)
            .shift(UP * 0.65 + 4 * RIGHT)
        )

        # Main Analysis of Equation 1

        eq1 = nMath("T_x(x) = T_x(x+dx)", color=BLACK)
        eq2 = nMath("T_x(x) = constant = c")

        grpEq = VGroup(eq1, eq2)

        tensionBreakdownScene = (
            TensionBreakdown.getScene().scale(0.8).shift(2.5 * RIGHT)
        )

        self.play(FadeIn(eq1))
        self.wait(1)
        self.play(
            LaggedStart(eq1.animate.shift(1.2 * UP), fadeInTex(eq2), lag_ratio=0.5)
        )
        self.wait(1)
        self.play(grpEq.animate.shift(LEFT * 2.5))
        self.play(FadeIn(tensionBreakdownScene))
        self.wait(1)

        eq3 = (
            nMath("T_y(x) =", "T_x(x)", "\\tan{\\theta}")
            .next_to(eq2, 0)
            .shift(1.2 * DOWN)
        )
        eq4 = nMath("T_y(x) =", "c", "\\frac{dy}{dx}").next_to(eq3, 0)
        eq5 = nMath("T_y(x) =", "c", "y'").next_to(eq3, 0)

        self.play(fadeInTex(eq3))
        self.wait(1)
        self.play(
            LaggedStart(FadeOut(tensionBreakdownScene), FadeIn(grp), lag_ratio=0.7)
        )
        self.wait(1)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(1)
        self.play(TransformMatchingTex(eq4, eq5))
        highlight(self, eq5, buff=0.2, unhighlight=0, color=RED_N100)
        self.wait(10)


class MassCalculation(Scene):
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

        # Part 1: Create a piece and fade in axis (I)
        piece = axes.plot(lambda x: np.cosh(x), [2, 2.5], color=BLACK, stroke_width=6)
        (piece.scale(2.5).shift(ORIGIN - piece.get_center() + 0.5 * UP),)

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

        helperLine1 = Line(
            pieceStart, np.array([pieceEnd[0], pieceStart[1], 0]), color=GREY_N100
        )

        helperLabel1 = nMath("dx").scale(0.8).next_to(helperLine1, DOWN, buff=0.2)

        helperLine2 = Line(
            pieceEnd, np.array([pieceEnd[0], pieceStart[1], 0]), color=GREY_N100
        )

        helperLabel2 = nMath("dy").scale(0.8).next_to(helperLine2, RIGHT, buff=0.2)

        lengthDs = (
            nMath("ds")
            .scale(0.8)
            .next_to(piece, LEFT + UP, buff=-0.35)
            .shift(0.2 * DOWN)
        )

        grp = VGroup(
            piece,
            pseudoAxis,
            dashedLineX,
            dashedLineXPlusDx,
            dashedLineY,
            dashedLineYPlusDy,
            xPlusDxLabel,
            xLabel,
            yLabel,
            yPlusDyLabel,
            helperLine1,
            helperLine2,
            helperLabel1,
            helperLabel2,
            lengthDs,
        ).scale(1.1)

        eq1 = nMath(
            "ds",
            "=",
            "\\sqrt{dx^2+dy^2}",
        ).shift(RIGHT * 3.5)

        eq2 = nMath(
            "ds",
            "=",
            "dx",
            "\\sqrt{1+",
            "\\frac{dy}{dx}^2",
            "}",
        ).shift(RIGHT * 3.5 + 0.5 * DOWN)

        eq2_ = nMath(
            "ds",
            "=",
            "dx",
            "\\sqrt{1+",
            "y'^2",
            "}",
        ).shift(RIGHT * 3.5 + 0.25 * DOWN)

        self.play(FadeIn(grp))
        self.wait(1)
        self.play(grp.animate.shift(LEFT * 2.5))
        self.wait(1)

        self.play(fadeInTex(eq1))
        self.wait(1)
        self.play(LaggedStart(eq1.animate.shift(UP), fadeInTex(eq2), lag_ratio=0.7))
        self.wait(1)
        self.play(TransformMatchingTex(eq2, eq2_))
        self.wait(1)
        self.play(FadeOut(eq1, shift=UP), eq2_.animate.shift(UP * 1.5))
        self.wait(1)

        eq3 = nMath("\\mu = \\text{Linear density}").next_to(eq2_, DOWN, buff=0.65)

        eq4 = nMath(
            "m = \\mu\\cdot dx",
            "\\sqrt{1+y'^2}",
        ).next_to(eq3, DOWN, buff=0.5)

        self.play(FadeIn(eq3))
        self.wait(1)
        self.play(FadeIn(eq4))
        highlight(self, eq4, 0.2, 0, RED, 0)
        self.wait(10)


class AnalysisEqn2(Scene):
    def construct(self):
        addBackground(self)

        eq1 = nMath("T_y(x+dx) - T_y(x)", "=", "mg", color=BLACK).shift(2.6 * UP)

        eq2 = nMath(
            "T_y(x+dx) - T_y(x)", "=", "\\mu g \\sqrt{1+y'^2}", "\\, dx"
        ).next_to(eq1, DOWN, buff=0.65)

        eq3 = nMath(
            "\\frac{T_y(x+dx) - T_y(x)}{dx}",
            "=",
            "\\mu g \\sqrt{1+y'^2}",
        ).next_to(eq2, DOWN, buff=0.65)

        eq4 = nMath(
            "\\frac{dT_y(x)}{dx}",
            "=",
            "\\mu g \\sqrt{1+y'^2}",
        ).next_to(eq2, DOWN, buff=0.65)

        eq5_ = nMath(
            "\\frac{d(cy')}{dx}",
            "=",
            "\\mu g \\sqrt{1+y'^2}",
        ).next_to(eq4, DOWN, buff=0.5)

        eq5 = nMath(
            "c",
            "\\frac{dy'}{dx}",
            "=",
            "\\mu g \\sqrt{1+y'^2}",
        ).next_to(eq4, DOWN, buff=0.5)

        eq6 = nMath(
            "c",
            "y''",
            "=",
            "\\mu g ",
            "\\sqrt{1+y'^2}",
        ).next_to(eq5, 0)

        eq7 = nMath(
            "y''",
            "=",
            "k",
            "\\sqrt{1+y'^2}",
        ).next_to(eq6, 0)

        self.play(fadeInTex(eq1))
        self.wait(1)
        self.play(fadeInTex(eq2))
        self.wait(1)
        self.play(fadeInTex(eq3))
        self.wait(1)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(1)
        self.play(fadeInTex(eq5_))
        self.wait(1)
        self.play(TransformMatchingTex(eq5_, eq5))
        self.wait(1)
        self.play(TransformMatchingTex(eq5, eq6))
        self.wait(1)
        self.play(TransformMatchingTex(eq6, eq7))
        hgl = solidHighlight(self, eq7, buff=0.2, corner_radius=0.16, animate=False)
        self.play(eq7.animate.set_color(BLACK), FadeIn(*hgl))
        self.wait(10)


class SolveDEPart1(Scene):
    def construct(self):
        addBackground(self)

        eq0 = nMath(
            "y''",
            "=",
            "k",
            "\\sqrt{1+y'^2}",
            color=BLACK,
        ).shift(2.8 * UP)

        eq1 = nMath(
            "\\frac{y''}{\\sqrt{1+y'^2}}",
            "=",
            "k",
        ).next_to(eq0, DOWN, buff=0.5)

        eq1_ = nMath(
            "\\int",
            "\\frac{y''}{\\sqrt{1+y'^2}}",
            "\\,dx",
            "=",
            "\\int",
            "k",
            "\\,dx",
        ).next_to(eq0, DOWN, buff=0.5)

        eq2 = nMath(
            "\\text{Let } y' = \\tan{u} \\Rightarrow y'' = \\sec^2{u} \\frac{du}{dx}"
        ).next_to(eq1, DOWN, buff=0.5)

        eq3 = nMath(
            "\\int",
            "\\frac{\\sec^2{u}}{\\sqrt{1+\\tan^2{u}}}",
            "\\,du",
            "=",
            "\\int k \\, dx",
        ).next_to(eq2, DOWN, buff=0.5)

        # grp = VGroup(eq3, reason)

        # self.add(eq1_, eq0, eq2, eq3)
        self.play(fadeInTex(eq0))
        self.wait(1)
        self.play(fadeInTex(eq1))
        self.wait(1)
        self.play(TransformMatchingTex(eq1, eq1_))
        self.wait(1)
        self.play(fadeInTex(eq2))
        self.wait(1)
        self.play(fadeInTex(eq3))
        self.wait(1)
        self.play(eq3.animate.shift(LEFT * 2))
        reason = nMath("\\quad \\because \\sec^2{u} = 1+\\tan^2{u}").next_to(
            eq3, RIGHT, buff=0.75
        )
        self.play(fadeInTex(reason))
        self.wait(1)
        eq3_ = nMath(
            "\\int",
            "\\sec{u}",
            "\\, du",
            "=",
            "\\int k \\, dx",
        ).next_to(eq3, 0, buff=0.5)
        self.play(TransformMatchingTex(eq3, eq3_))
        self.wait(1)
        self.play(FadeOut(reason), eq3_.animate.next_to(eq2, DOWN, buff=0.5))
        self.wait(10)


class SolveDEPart2(Scene):
    def construct(self):
        addBackground(self)

        eq0 = nMath(
            "\\int",
            "\\sec{u}",
            "\\, du",
            "=",
            "\\int k \\, dx",
        ).to_edge(UP)

        eq1 = nMath(
            "\\ln{(\\sec{u} +\\tan{u})}",
            "=",
            " kx +c",
        ).next_to(eq0, DOWN, buff=0.5)

        eq2 = nMath(
            "\\sec{u} +\\tan{u}",
            "=",
            "e^{kx +c}",
        ).next_to(eq1, DOWN, buff=0.5)

        eq3 = nMath(
            "\\sec{u} + \\tan{u}",
            "=",
            "Ae^{kx}",
        ).next_to(eq1, DOWN, buff=0.5)

        reason = nMath(
            "\\sec^2{u} - \\tan^2{u}",
            "=",
            "1",
        ).next_to(eq3, DOWN, buff=0.5)

        eq4_ = nMath(
            "(\\sec{u} + \\tan{u})",
            "(",
            "\\sec{u} - \\tan{u}",
            ")",
            "=",
            "1",
        ).next_to(eq3, DOWN, buff=0.65)

        eq4 = nMath(
            "\\sec{u} - \\tan{u}",
            "=",
            "\\frac{1}{Ae^{kx}}",
        ).next_to(eq3, DOWN, buff=0.5)

        eq5 = nMath(
            "\\sec{u} - \\tan{u}",
            "=",
            "Be^{-kx}",
        ).next_to(eq3, DOWN, buff=0.65)

        # self.add(eq0, eq1, eq2, eq4, reason)
        # self.play(Transform(eq2, eq3))
        # self.play(Transform(eq4[2], eq5[2]))

        eq6 = nMath("\\tan{u}", "= \\frac{Ae^{kx} - Be^{-kx}}{2}").next_to(
            eq5, DOWN, buff=0.75
        )
        eq7 = nMath("y'", "= \\frac{Ae^{kx} - Be^{-kx}}{2}").next_to(
            eq5, DOWN, buff=0.75
        )

        self.play(fadeInTex(eq0))
        self.wait(1)
        self.play(fadeInTex(eq1))
        self.wait(1)
        self.play(fadeInTex(eq2))
        self.wait(1)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(1)

        self.play(fadeInTex(reason))
        self.wait(1)
        self.play(TransformMatchingTex(reason, eq4_))
        self.wait(1)
        self.play(TransformMatchingTex(eq4_, eq4))
        self.wait(1)
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait(1)
        self.play(fadeInTex(eq6))
        self.wait(1)
        self.play(TransformMatchingTex(eq6, eq7))

        self.wait(10)


class SolveDEPart3(Scene):
    def construct(self):
        addBackground(self)

        eq6 = nMath("y'", "= \\frac{Ae^{kx} - Be^{-kx}}{2}").shift(2 * UP)

        eq7 = nMath(
            "\\int y' \\, dx", "= \\int \\frac{Ae^{kx} - Be^{-kx}}{2} \\, dx"
        ).next_to(eq6, DOWN, buff=0.65)

        eq8 = nMath("y", "= \\frac{Ae^{kx} + Be^{-kx}}{2k} + C").next_to(
            eq7, DOWN, buff=0.65
        )
        eq8_ = nMath("y", "= \\frac{Ae^{kx} + Be^{-kx}}{2} + C").next_to(
            eq7, DOWN, buff=0.65
        )

        self.play(fadeInTex(eq6))
        self.wait(1)
        self.play(fadeInTex(eq7))
        self.wait(1)
        self.play(fadeInTex(eq8))
        self.wait(1)
        self.play(TransformMatchingTex(eq8, eq8_))
        self.wait(2)
        self.play(
            LaggedStart(FadeOut(eq6, eq7), eq8_.animate.move_to(ORIGIN), lag_ratio=0.7)
        )
        hgl = solidHighlight(self, eq8_, buff=0.2, corner_radius=0.16, animate=False)
        self.play(eq8_.animate.set_color(BLACK), FadeIn(*hgl))
        self.wait(10)


class Final(Scene):
    def construct(self):
        addBackground(self)

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
            )
        )
        self.wait(1)

        self.play(Create(axes))
        self.wait(1)

        eq8 = nMath("y", "= \\frac{Ae^{kx} + Be^{-kx}}{2}", "+ C").shift(RIGHT * 4)
        bc1 = nMath("y'(0) = 0").next_to(eq8, 0).shift(0.5 * DOWN)

        grp = VGroup(pole1, pole2, axes, catenary, ground)
        self.play(grp.animate.scale(0.8).shift(3 * LEFT))

        dot1 = Dot(axes.c2p(0, 1), color=RED_N100)
        pointer1 = Arrow(axes.c2p(2, 12), axes.c2p(0, 1), buff=0.4, color=GREY_N400)

        dot2 = Dot(catenary.get_start(), color=RED_N100)
        pointer2 = Arrow(
            axes.c2p(-1.5, 28), catenary.get_start(), buff=0.4, color=GREY_N400
        )

        dot3 = Dot(catenary.get_end(), color=RED_N100)
        pointer3 = Arrow(
            axes.c2p(5.5, 28), catenary.get_end(), buff=0.4, color=GREY_N400
        )

        self.play(fadeInTex(eq8))
        self.wait(1)
        self.play(Create(dot1), GrowArrow(pointer1))
        self.play(LaggedStart(eq8.animate.shift(UP), fadeInTex(bc1), lag_ratio=0.7))
        result1 = (
            nMath("\\Rightarrow A = B").next_to(bc1, DOWN, buff=0.5).shift(LEFT * 0.1)
        )
        self.wait(1)
        self.play(fadeInTex(result1), FadeOut(pointer1, dot1))
        self.wait(1)

        final1 = (
            nMath("y", "= A\\frac{e^{kx} + e^{-kx}}{2}", "+ C")
            .next_to(eq8, 0)
            .shift(0.75 * DOWN)
        )
        final2 = nMath("y", "= A\\cosh{(kx)}", "+ C").next_to(final1, 0)
        self.play(
            LaggedStart(
                FadeOut(bc1, result1), TransformMatchingTex(eq8, final1), lag_ratio=0.7
            )
        )

        self.wait(1)
        self.play(TransformMatchingTex(final1, final2))
        self.wait(1)
        self.play(
            FadeIn(dot2, dot3, dot1),
            GrowArrow(pointer1),
            GrowArrow(pointer2),
            GrowArrow(pointer3),
        )
        self.wait(1)
        self.play(FadeOut(dot1, dot2, dot3, pointer1, pointer2, pointer3))
        self.wait(1)

        hgl = solidHighlight(self, final2, buff=0.2, corner_radius=0.16, animate=False)
        self.play(final2.animate.set_color(BLACK), FadeIn(*hgl))

        self.wait(10)


class Intro(Scene):
    def construct(self):
        addBackground(self)

        prologue = MathTex(
            '\\text{"If knowledge is power, then curiosity is the muscle"}',
            tex_template=TexFontTemplates.droid_serif,
            color=BLACK,
        ).shift(UP * 0.5)
        prologueBy = nMath("\\text{- Danielle LaPorte}", color=NUMBRIK_COLOR).shift(
            DOWN * 0.5
        )
        self.play(
            LaggedStart(
                fadeInTex(prologue),
                AnimationGroup(Write(prologueBy), run_time=2.5),
                lag_ratio=0.7,
            )
        )

        clearScreen(self, 4)


class Intro2(Scene):
    def construct(self):
        addBackground(self)

        # Part 0: Create the catenary: Rope, poles and ground
        axes = getAxis([-5, 5], [-15, 20], 7, 6).shift(DOWN)

        catenary = axes.plot(
            lambda x: np.cosh(x), [-3.5, 3.5], color=NUMBRIK_COLOR, stroke_width=6
        )

        P = catenary.get_start()
        Q = catenary.get_end()
        pole1 = Line(P, P + DOWN * 4.5, color=BLACK, stroke_width=10)
        pole2 = Line(Q, Q + DOWN * 4.5, color=BLACK, stroke_width=10)
        ground = Line(
            pole1.get_end() + LEFT * 1.5,
            pole2.get_end() + RIGHT * 1.5,
            color=GREY,
            stroke_width=12,
        )

        lr = (np.cosh(3.5) - 1) / 3.5**2

        parabola = axes.plot(
            lambda x: lr * x**2 + 1, [-4, 4], color=RED_N100, stroke_width=5
        )

        circle = Circle.from_three_points(
            P, Q, axes.c2p(0, 1), stroke_width=5, color=RED_N100
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

        title = nMath("Catenary", color=BLACK).scale(1.2).shift(1.4 * DOWN)

        self.wait(1)
        self.play(Create(parabola))
        self.play(Uncreate(parabola))
        self.play(Create(circle))
        self.play(Uncreate(circle))
        self.play(VGroup(ground, pole1, pole2, catenary).animate.shift(UP).scale(1.2))
        self.play(fadeInTex(title))
        solidHighlight(self, title, buff=0.25, corner_radius=0.3, unhighlight=False)
        self.wait(10)
