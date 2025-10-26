from manim import *
from utils import *


class Intro(Scene):
    def construct(self):
        addBackground(self)
        r = 1
        r2 = 1.5

        # small mass/charge
        circle = (
            Circle(r, stroke_width=6, fill_opacity=1)
            .set_color_by_gradient([BLUE_N1000, BLUE])
            .shift(LEFT * 2.7 + UP)
        )
        label1 = nMath("M_1", color=WHITE).move_to(circle.get_center())
        label1_ = nMath("-Q_1", color=WHITE).move_to(circle.get_center())
        label1__ = (
            MathTex("\\mathbf{?}", color=WHITE).scale(1.8).move_to(circle.get_center())
        )

        # big mass/charge
        circle2 = (
            Circle(r2, stroke_width=6, fill_opacity=1)
            .set_color_by_gradient([BLUE_N1000, BLUE])
            .shift(1.6 * RIGHT * 2 + UP)
        )
        label2 = nMath("M_2", color=WHITE).move_to(circle2.get_center())
        label2_ = nMath("Q_2", color=WHITE).move_to(circle2.get_center())
        label2__ = (
            MathTex("\\mathbf{?}", color=WHITE).scale(1.8).move_to(circle2.get_center())
        )

        # line of force
        line = DashedLine(
            circle.get_center(),
            circle2.get_center(),
            color=GREY_N200,
            z_index=-1,
            stroke_opacity=0,
        )

        # for attraction force
        arrow_tip1 = ArrowTriangleFilledTip(color=GREY_N200, start_angle=0).move_to(
            line.get_center() + 0.8 * LEFT
        )
        arrow_tip2 = ArrowTriangleFilledTip(color=GREY_N200, start_angle=PI).move_to(
            line.get_center() + RIGHT * 0.2
        )

        force = (
            nMath("F(\\vec{r}) = -", "\\frac{GM_1M_2}{r^3}", "\\vec{r}", color=BLACK)
            .shift(1.8 * DOWN)
            .set_color_by_gradient([GREY_N500, BLACK])
            .set_sheen_direction(RIGHT)
        )

        force2 = (
            nMath("F(\\vec{r}) = -", "\\frac{kQ_1Q_2}{r^3}", "\\vec{r}", color=BLACK)
            .shift(1.8 * DOWN)
            .set_color_by_gradient([GREY_N500, BLACK])
            .set_sheen_direction(RIGHT)
        )

        force2.save_state()

        forceTemp = (
            nMath("F(\\vec{r}) = -", "\\frac{k\\hat{r}}{r^2}", color=BLACK)
            .shift(1.8 * DOWN)
            .set_color_by_gradient([GREY_N500, BLACK])
            .set_sheen_direction(RIGHT)
        )

        force3 = (
            nMath("F(\\vec{r}) = -", "\\frac{\\;???\\;}{r^3}", "\\vec{r}", color=BLACK)
            .shift(1.8 * DOWN)
            .set_color_by_gradient([GREY_N500, BLACK])
            .set_sheen_direction(RIGHT)
        )

        saved_label1 = label1.copy().shift(UP)
        saved_label2 = label2.copy().shift(UP)

        # PROLOGUE

        self.play(
            LaggedStart(
                FadeIn(circle, circle2, scale=0.9),
                FadeIn(label1, label2),
                lag_ratio=0.8,
            ),
        )

        self.wait(1)

        self.add(line)
        self.play(
            line.animate.set_opacity(1),
            FadeIn(arrow_tip1, arrow_tip2),
            run_time=2,
        )
        self.play(Write(force), run_time=2.5)
        self.wait(2)

        # MAIN

        self.play(
            LaggedStart(
                AnimationGroup(
                    circle.animate.set_color_by_gradient([GREEN_NDARK, GREEN_N200]),
                    ReplacementTransform(label1, label1_),
                ),
                AnimationGroup(
                    circle2.animate.set_color_by_gradient([GREEN_NDARK, GREEN_N200]),
                    ReplacementTransform(label2, label2_),
                ),
                lag_ratio=0.3,
            ),
            run_time=2,
        )
        hgl = solidHighlight(self, force2[1][0:5], buff=0.1, animate=0)
        self.play(FadeIn(*hgl))
        self.play(TransformMatchingTex(force, force2), run_time=2)
        self.wait(1)
        self.play(hgl[0].animate.set_opacity(0))
        self.wait(1)

        self.play(Transform(force2, forceTemp), run_time=1.5)
        self.wait(1)

        self.play(Restore(force2), run_time=1.5)

        self.wait(2)

        saved_label2_ = label2_.copy().shift(UP)
        saved_label1_ = label1_.copy().shift(UP)

        self.play(
            circle.animate.set_color_by_gradient([GREY_N800, GREY_N100]),
            circle2.animate.set_color_by_gradient([GREY_N800, GREY_N100]),
            ReplacementTransform(label1_, label1__),
            ReplacementTransform(label2_, label2__),
        )
        self.play(TransformMatchingTex(force2, force3))
        self.wait(1)

        self.play(
            VGroup(
                circle, circle2, label1__, label2__, line, arrow_tip1, arrow_tip2
            ).animate.shift(UP),
            force3.animate.shift(UP * 1.5),
        )

        potentialEnergy3 = (
            nMath("U(\\vec{r}) = -\\frac{???}{r}", color=BLACK)
            .set_color_by_gradient([GREY_N500, BLACK])
            .set_sheen_direction(RIGHT)
            .next_to(force3, DOWN, buff=0.75)
        )
        self.play(fadeInTex(potentialEnergy3))
        self.wait(1)

        self.play(
            LaggedStart(
                FadeOut(force3),
                potentialEnergy3.animate.next_to(force3, 0),
                lag_ratio=0.5,
            )
        )

        potentialEnergy2 = (
            nMath("U(\\vec{r}) = -\\frac{kQ_1Q_2}{r}", color=BLACK)
            .set_color_by_gradient([GREY_N500, BLACK])
            .set_sheen_direction(RIGHT)
            .next_to(potentialEnergy3, 2 * DOWN + RIGHT * 2, buff=0.5)
        )
        pointer2 = CurvedArrow(
            potentialEnergy3.get_right() + 0.3 * RIGHT,
            potentialEnergy2.get_top() + 0.3 * UP,
            color=GREY_N200,
            angle=-PI / 3,
        )

        # saved_label1__ = label1__.copy()
        # saved_label2__ = label2__.copy()

        self.play(
            LaggedStart(
                AnimationGroup(
                    circle.animate.set_color_by_gradient([GREEN_NDARK, GREEN_N200]),
                    circle2.animate.set_color_by_gradient([GREEN_NDARK, GREEN_N200]),
                    ReplacementTransform(label2__, saved_label2_),
                    ReplacementTransform(label1__, saved_label1_),
                ),
                Create(pointer2),
                fadeInTex(potentialEnergy2),
                lag_ratio=0.5,
            )
        )

        potentialEnergy1 = (
            nMath("U(\\vec{r}) = -\\frac{GM_1M_2}{r}", color=BLACK)
            .set_color_by_gradient([GREY_N500, BLACK])
            .set_sheen_direction(RIGHT)
            .next_to(potentialEnergy3, 2 * DOWN + LEFT * 2, buff=0.5)
        )
        pointer1 = CurvedArrow(
            potentialEnergy3.get_left() + 0.3 * LEFT,
            potentialEnergy1.get_top() + 0.3 * UP,
            color=GREY_N200,
            angle=PI / 3,
        )

        self.play(
            LaggedStart(
                AnimationGroup(
                    circle.animate.set_color_by_gradient([BLUE_N1000, BLUE]),
                    circle2.animate.set_color_by_gradient([BLUE_N1000, BLUE]),
                    ReplacementTransform(saved_label2_, saved_label2),
                    ReplacementTransform(saved_label1_, saved_label1),
                ),
                Create(pointer1),
                fadeInTex(potentialEnergy1),
                lag_ratio=0.5,
            )
        )

        self.wait(2)

        # self.play(
        #     LaggedStart(
        #         FadeOut(pointer1, pointer2, potentialEnergy1, potentialEnergy2),
        #         AnimationGroup(
        #             circle.animate.set_color_by_gradient([GREY_N800, GREY_N100]),
        #             circle2.animate.set_color_by_gradient([GREY_N800, GREY_N100]),
        #             ReplacementTransform(saved_label2, saved_label2__),
        #             ReplacementTransform(saved_label1, saved_label1__),
        #         ),
        #         potentialEnergy3.animate.next_to(force3, DOWN, buff=0.75),
        #         FadeIn(force3),
        #         lag_ratio=0.5,
        #     ),
        #     run_time=3,
        # )

        self.wait(10)


class CircularMotion(Scene):
    def construct(self):
        addBackground(self)

        axis = (
            getAxis(x_length=7, y_length=7)
            .set_color_by_gradient([GREY_N100, BLACK])
            .set_sheen_direction(RIGHT + UP)
        )

        rad = 2
        theta = ValueTracker(4 * PI / 18)

        circle = Circle(rad, stroke_color=[GREY_N800, GREY_N50], stroke_width=6)

        getRadial = (
            lambda: np.cos(theta.get_value()) * RIGHT + np.sin(theta.get_value()) * UP
        )

        def getPosition():
            return (
                rad * np.cos(theta.get_value()) * RIGHT
                + rad * np.sin(theta.get_value()) * UP
                + axis.get_origin()
            )

        def getPerp():
            return np.sin(theta.get_value()) * LEFT + np.cos(theta.get_value()) * UP

        particle = always_redraw(
            lambda: Dot(getPosition(), radius=0.12, z_index=1).set_color_by_gradient(
                [GREY_N800, GREY_N100]
            )
        )

        position_vector = always_redraw(
            lambda: Arrow(
                axis.get_origin(),
                getPosition(),
                buff=0,
                stroke_width=7,
                tip_length=0.4,
            )
            .set_color_by_gradient([GREEN_N100, GREEN_N200, GREEN_NDARK])
            .set_sheen_direction(getRadial())
        )

        velocity_vector = always_redraw(
            lambda: Arrow(
                getPosition(),
                getPosition() + getPerp() * 2,
                buff=0,
                stroke_width=7,
                tip_length=0.4,
            )
            .set_color_by_gradient(
                [
                    BLUE_D,
                    NUMBRIK_COLOR_DARK,
                ]
            )
            .set_sheen_direction(getPerp())
        )

        def getEqn(*args):
            return (
                nMath(*args)
                .set_sheen_direction(RIGHT)
                .set_color_by_gradient([GREY_N500, BLACK])
                .next_to(RIGHT * 1.5, aligned_edge=LEFT)
            )

        labelPosition = always_redraw(
            lambda: (
                getEqn("\\vec{r}").move_to(
                    (axis.get_origin() + getPosition()) / 2 + getPerp() * 0.4,
                )
            )
        )

        labelVelocity = always_redraw(
            lambda: (
                getEqn("\\vec{v}").move_to(
                    (getPosition() + getPerp() + 0.4 * getRadial())
                )
            )
        )

        # self.add(
        #     axis,
        #     circle,
        #     particle,
        #     position_vector,
        #     velocity_vector,
        #     labelPosition,
        #     labelVelocity,
        # )

        # self.play(theta.animate.set_value(PI / 3), run_time=3)

        # ANIMATIONS

        self.play(
            LaggedStart(
                Create(particle),
                Create(circle),
                Create(axis),
                lag_ratio=0.5,
            ),
            run_time=3,
        )

        self.play(
            theta.animate.set_value(theta.get_value() + 2 * PI),
            rate_func=smoothstep,
            run_time=4,
        )
        self.wait(1)

        self.play(
            LaggedStart(
                GrowArrow(velocity_vector), fadeInTex(labelVelocity), lag_ratio=0.5
            )
        )

        self.wait(1)

        self.play(
            LaggedStart(
                GrowArrow(position_vector), fadeInTex(labelPosition), lag_ratio=0.5
            )
        )
        self.add(labelPosition, labelVelocity)
        self.wait(1)

        self.play(
            theta.animate.set_value(theta.get_value() + 2 * PI - PI / 18),
            rate_func=smoothstep,
            run_time=4,
        )

        self.play(
            VGroup(
                axis,
                circle,
                # velocity_vector,
                # position_vector,
                # labelPosition,
                # labelVelocity,
            ).animate.shift(LEFT * 2.5)
        )

        eq1 = getEqn("\\frac{d\\vec{r}}{dt} =", "\\vec{v}")

        eq2 = getEqn("\\frac{d\\vec{r}}{dt} =", "v", "\\hat{r}_{\\perp}")

        disclaimer = getEqn("\\text{Let }|\\vec{v}| = |\\vec{r}|").next_to(
            eq2, UP, buff=2, aligned_edge=LEFT
        )

        eq3 = getEqn(
            "\\frac{d\\vec{r}}{dt} =",
            "r",
            "\\hat{r}_{\\perp}",
        )

        eq5 = getEqn(
            "\\frac{d\\vec{r}}{dt} =",
            "\\vec{r}_{\\perp}",
        )

        self.play(Write(eq1))
        self.wait(1)

        velocity_extended = always_redraw(
            lambda: DashedLine(
                getPosition(), getPosition() - getPerp(), color=GREY_N200
            )
        )

        position_extended = always_redraw(
            lambda: DashedLine(
                getPosition(), getPosition() + getRadial(), color=GREY_N200
            )
        )

        rtAng = always_redraw(
            lambda: RightAngle(
                velocity_extended, position_extended, color=GREY_N200, length=0.3
            )
        )

        self.play(
            LaggedStart(
                Create(velocity_extended),
                Create(position_extended),
                Create(rtAng),
                lag_ratio=0.3,
            )
        )
        self.wait(1)
        self.play(
            theta.animate.set_value(theta.get_value() + PI / 2),
            rate_func=there_and_back,
            run_time=3,
        )
        self.wait(1)
        self.play(TransformMatchingTex(eq1, eq2))
        solidHighlight(self, [eq2[2], labelPosition], buff=0.1)
        self.play(fadeInTex(disclaimer))
        highlight(self, disclaimer, buff=0.25)
        self.wait(1)
        hgl = solidHighlight(self, eq2[1:], buff=0.1, unhighlight=False)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(1)
        self.play(TransformMatchingTex(eq3, eq5))
        self.wait(1)
        self.play(
            hgl[0].animate.set_opacity(0),
            FadeOut(velocity_extended, position_extended, rtAng),
        )

        self.wait(2)

        self.play(FadeOut(eq5))
        self.play(theta.animate.set_value(theta.get_value() - PI / 6))
        self.wait(2)

        labelT0 = (
            getEqn("T = 0")
            .next_to(particle, RIGHT + DOWN, buff=0.25)
            .shift(LEFT * 0.15)
            .scale(0.8)
        )
        particleShadow = particle.copy().set_color(GREY_N100).set_z_index(0.5)

        self.add(particleShadow)
        self.play(fadeInTex(labelT0))
        self.wait(1)

        thetaCache = theta.get_value()
        arc = always_redraw(
            lambda: Arc(
                rad,
                0,
                theta.get_value() - thetaCache,
                arc_center=axis.get_origin(),
                color=BLACK,
            )
        )
        self.add(arc)

        self.play(theta.animate.set_value(theta.get_value() + 4 * PI / 18))
        self.wait(1)

        labelT1 = (
            getEqn("T = t")
            .next_to(particle, RIGHT + UP, buff=0.25)
            .scale(0.8)
            .shift(LEFT * 0.15)
        )

        self.play(fadeInTex(labelT1))
        self.wait(1)

        lengthEq1 = getEqn(
            "L", "=", "v \\cdot", "t", "=", "r\\cdot", "\\mathbf{\\theta}"
        ).next_to(eq5, 0, aligned_edge=LEFT)

        lengthEq2 = getEqn("\\mathbf{\\theta}", "=", "t").next_to(
            eq5, 0, aligned_edge=LEFT
        )

        self.play(
            TransformFromCopy(arc, lengthEq1[0]),
        )
        self.wait(1)
        self.play(
            FadeIn(lengthEq1[1:4]),
        )
        self.wait(1)

        angle = Angle(axis.get_x_axis(), position_vector, color=GREY_N100, radius=0.7)
        angleLabel = (
            getEqn("\\theta")
            .next_to(angle.get_center(), RIGHT, buff=0.3)
            .shift(UP * 0.1)
        )

        perp = DashedLine(
            getPosition(), axis.x_axis.get_projection(getPosition()), color=GREY_N100
        )

        tempLine = Line(
            axis.get_origin(),
            axis.x_axis.get_projection(getPosition()),
            color=GREY_A,
            z_index=-1,
        )

        self.play(LaggedStart(Create(angle), FadeIn(angleLabel), lag_ratio=0.5))
        self.wait(1)
        self.play(FadeIn(lengthEq1[4:]))
        self.wait(1)
        self.play(TransformMatchingTex(lengthEq1, lengthEq2), run_time=2)
        self.wait(1)

        self.play(FadeOut(labelT0, labelT1))
        self.play(Create(perp))
        self.wait(1)

        eqRes = getEqn(
            "\\vec{r}", "= (", "r\\cos{\\theta}", ", \\ ", "r\\sin{\\theta}", ")"
        ).shift(0.5 * DOWN)

        eqRes2 = getEqn(
            "\\vec{r}", "= (", "r\\cos{t}", ", \\ ", "r\\sin{t}", ")"
        ).shift(0.5 * DOWN)

        eqRes3 = getEqn(
            "\\vec{r}",
            "= ",
            "r\\cos{t}",
            "\\,\\hat{i}",
            "+",
            "r\\sin{t}",
            "\\,\\hat{j}",
        ).next_to(eqRes2, 0, aligned_edge=LEFT)

        self.play(
            LaggedStart(
                lengthEq2.animate.shift(0.5 * UP),
                FadeIn(tempLine),
                FadeIn(eqRes[0:2]),
                AnimationGroup(TransformFromCopy(tempLine, eqRes[2]), run_time=2),
                FadeIn(eqRes[3]),
                AnimationGroup(TransformFromCopy(perp, eqRes[4]), run_time=2),
                FadeIn(eqRes[5:]),
                lag_ratio=0.7,
            )
        )
        self.wait(1)
        self.play(TransformMatchingTex(eqRes, eqRes2))
        self.wait(1)
        self.play(TransformMatchingTex(eqRes2, eqRes3))
        self.wait(1)

        eq5.shift(UP * 0.75)
        self.play(FadeOut(perp, angle, particleShadow, arc, lengthEq2, tempLine))
        self.play(fadeInTex(eq5))
        self.wait(1)

        highlight(self, VGroup(eq5, eqRes3), buff=0.2, unhighlight=False)

        self.wait(10)

        # self.play(
        #     theta.animate.set_value(theta.get_value() + velocity),
        #     run_time=0.5,
        #     rate_func=linear,
        # )

        # theta.add_updater(
        #     lambda _, dt: theta.set_value(theta.get_value() + velocity * dt)
        # )

        # self.play()

        self.wait(10)


class ComplexPlane(Scene):
    def construct(self):
        addBackground(self)

        axis = getAxis(x_length=11, y_length=7, x_range=[-5, 5], y_range=[-2, 10])

        rad = ValueTracker(4)
        theta = ValueTracker(4 * PI / 18)

        def getPosition():
            return (
                axis.get_origin()
                + rad.get_value() * np.cos(theta.get_value()) * RIGHT
                + rad.get_value() * np.sin(theta.get_value()) * UP
            )

        def getPerpPosition():
            return (
                axis.get_origin()
                + rad.get_value() * np.sin(theta.get_value()) * LEFT
                + rad.get_value() * np.cos(theta.get_value()) * UP
            )

        z = always_redraw(
            lambda: Arrow(
                axis.get_origin(),
                getPosition(),
                buff=0,
                stroke_width=7,
                tip_length=0.4,
            )
            .set_color_by_gradient([GREEN_N100, GREEN_N200, GREEN_NDARK])
            .set_sheen_direction(getPosition())
        )

        z_perp = always_redraw(
            lambda: Arrow(
                axis.get_origin(),
                getPerpPosition(),
                buff=0,
                stroke_width=7,
                tip_length=0.4,
            )
            .set_color_by_gradient([NUMBRIK_COLOR_50, NUMBRIK_COLOR])
            .set_sheen_direction(getPerpPosition())
        )

        def getEqn(*args):
            return (
                nMath(*args)
                .set_sheen_direction(RIGHT)
                .set_color_by_gradient([GREY_N500, BLACK])
            )

        # Labels and markers
        x_line = Line(
            getPosition(),
            axis.x_axis.get_projection(getPosition()),
            stroke_color=[GREY_N800, GREY_N100],
            sheen_direction=UP,
        )

        y_line = Line(
            z_perp.get_end(),
            axis.y_axis.get_projection(z_perp.get_end()),
            stroke_color=[GREY_N800, GREY_N100],
            sheen_direction=LEFT,
        )

        labelPosition1 = getEqn("z", "=", "x", "+", "i", "y")

        lengthMarkerX1 = (
            BraceBetweenPoints(
                axis.x_axis.get_projection(getPosition()),
                z.get_end(),
            )
            .set_sheen_direction(UP)
            .set_color_by_gradient([GREY_N800, GREY_N100])
        )

        lengthMarkerY1 = (
            BraceBetweenPoints(
                axis.get_origin(),
                axis.x_axis.get_projection(getPosition()),
                color=BLACK,
            )
            .set_sheen_direction(RIGHT)
            .set_color_by_gradient([GREY_N800, GREY_N100])
        )

        labelPosition2 = getEqn("iz", "=", "-", "y", "+", "i", "x").move_to(
            getPerpPosition() + 0.4 * UP + 1.4 * LEFT
        )

        lengthMarkerX2 = (
            BraceBetweenPoints(
                axis.y_axis.get_projection(getPerpPosition()),
                getPerpPosition(),
            )
            .set_sheen_direction(LEFT)
            .set_color_by_gradient([GREY_N800, GREY_N100])
        )

        lengthMarkerY2 = (
            BraceBetweenPoints(
                getPerpPosition(),
                axis.x_axis.get_projection(getPerpPosition()),
            )
            .set_sheen_direction(UP)
            .set_color_by_gradient([GREY_N800, GREY_N100])
        )

        angle1 = Angle(
            axis.x_axis,
            z,
            color=GREY_N400,
            radius=0.8,
        )
        angle2 = Angle(
            axis.y_axis,
            z_perp,
            color=GREY_N400,
            radius=0.8,
        )

        tempLineX = DashedLine(
            axis.get_origin(), axis.get_origin() + 5 * RIGHT, color=GREY_N400
        )
        tempLineY = DashedLine(
            axis.get_origin(), axis.get_origin() + 5 * UP, color=GREY_N400
        )

        angle3 = RightAngle(tempLineX, tempLineY, color=GREY_N400)

        tempGroup = VGroup(tempLineX, tempLineY, angle3)

        # self.add(z, z_perp, axis, labelPosition1, lengthMarkerX1, lengthMarkerY1)
        # self.add(lengthMarkerX2, lengthMarkerY2, labelPosition2)
        # self.add(angle1, angle2, tempLineX, tempLineY, angle3)
        # self.add(x_line, y_line)

        eq1 = getEqn("iz").shift(LEFT * 4)
        eq2 = getEqn("iz", "=", "i", "(", "x", "+", "iy", ")").next_to(
            eq1, 0, aligned_edge=LEFT + DOWN
        )

        eq1.next_to(eq2[0], 0, aligned_edge=LEFT + DOWN)
        eq3 = getEqn(
            "iz",
            "=",
            "i",
            "x",
            "+",
            "i^2",
            "y",
        ).next_to(eq2, 0, aligned_edge=LEFT + DOWN)
        eq4 = getEqn(
            "iz",
            "=",
            "i",
            "x",
            "-",
            "y",
        ).next_to(eq2, 0, aligned_edge=LEFT + DOWN)
        eq5 = getEqn(
            "iz",
            "=",
            "-",
            "y",
            "+",
            "i",
            "x",
        ).next_to(eq2, 0, aligned_edge=LEFT + DOWN)

        # ANIMATION HUB

        self.play(Write(labelPosition1), run_time=2)

        point1 = Dot(getPosition(), color=GREEN_N200)

        self.play(
            LaggedStart(
                labelPosition1.animate.move_to(z.get_end() + 0.4 * UP + 1.2 * RIGHT),
                Create(axis),
                Create(point1),
                lag_ratio=0.5,
            ),
            run_time=3,
        )

        self.play(ReplacementTransform(point1, z), run_time=2)
        self.wait(1)

        self.play(Create(x_line))
        label3 = labelPosition1[5].copy()
        self.play(
            FadeIn(lengthMarkerX1),
            label3.animate.next_to(lengthMarkerX1, RIGHT, buff=0.2),
        )
        label4 = labelPosition1[2].copy()
        self.play(
            FadeIn(lengthMarkerY1),
            label4.animate.next_to(lengthMarkerY1, DOWN, buff=0.2),
            run_time=1.5,
        )

        self.play(fadeInTex(eq1))
        self.wait(1)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(1)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(1)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(1)
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait(1)
        self.play(Transform(eq5, labelPosition2), GrowArrow(z_perp))
        self.play(Create(y_line))

        label1 = labelPosition2[3].copy()
        self.play(
            FadeIn(lengthMarkerX2),
            label1.animate.next_to(lengthMarkerX2, UP, buff=0.2),
        )

        label2 = labelPosition2[6].copy()
        self.play(
            FadeIn(lengthMarkerY2),
            label2.animate.next_to(lengthMarkerY2, LEFT, buff=0.2),
            run_time=1.5,
        )
        self.wait(1)

        tri1 = getTriangularRegion(
            axis.get_origin(), getPosition(), axis.x_axis.get_projection(getPosition())
        )
        tri2 = getTriangularRegion(
            axis.get_origin(),
            getPerpPosition(),
            axis.y_axis.get_projection(getPerpPosition()),
        )
        self.play(FadeIn(tri1, tri2))

        self.play(LaggedStart(Create(angle1), Create(angle2), lag_ratio=0.5))
        self.wait(1)
        self.play(FadeIn(tempGroup))
        self.play(Rotate(tempGroup, theta.get_value(), OUT, axis.get_origin()))
        self.play(
            FadeOut(
                tempLineX,
                tempLineY,
                tri1,
                tri2,
                label1,
                label2,
                label3,
                label4,
                angle1,
                angle2,
                lengthMarkerX1,
                lengthMarkerX2,
                lengthMarkerY1,
                lengthMarkerY2,
                x_line,
                y_line,
            )
        )
        self.wait(1)
        self.add(z, z_perp)
        self.play(
            LaggedStart(
                FadeOut(labelPosition1, eq5, angle3),
                AnimationGroup(
                    theta.animate.set_value(PI / 6), rad.animate.set_value(5)
                ),
                lag_ratio=0.5,
            )
        )

        labelPosition3 = getEqn("z", "=", "e^{ix}").move_to(
            getPosition() + 0.7 * UP + 0.7 * RIGHT
        )

        labelPosition4 = getEqn("z_{\\perp}", "=", "ie^{ix}").move_to(
            getPerpPosition() + 0.7 * UP + 0.8 * LEFT
        )
        self.play(fadeInTex(labelPosition3), fadeInTex(labelPosition4))
        self.wait(4)


class Exp(Scene):
    def construct(self):
        addBackground(self)

        # Axis
        axis = (
            getAxis(x_range=[-3.5, 4], y_range=[-3, 15], x_length=8)
            .scale(1.2)
            .shift(0.5 * LEFT + 0.25 * DOWN)
            .set_color_by_gradient([GREY_N100, BLACK])
            .set_sheen_direction(RIGHT + UP)
        )

        # Curve
        exp = axis.plot(
            lambda x: np.e**x + 0.5,
            x_range=[-3, 2.6],
            color=BLACK,
            stroke_color=[WHITE, GREEN_N100, GREEN_N200],
            stroke_width=7,
            sheen_direction=UP + RIGHT,
        )

        alpha = ValueTracker(0.597)

        get_alpha = lambda: alpha.get_value()

        def getTangentLine():
            tangent = TangentLine(
                exp,
                length=7,
                alpha=get_alpha(),
                stroke_color=[GREY_N200, GREY_N800],
                stroke_width=6,
            )
            tangent.set_sheen_direction(tangent.get_unit_vector())
            return tangent

        tangent = always_redraw(getTangentLine)

        # get the point of tangency
        getPoc = lambda: exp.point_from_proportion(get_alpha())
        # get coordinates wrt axes
        get_coord = lambda: axis.p2c(exp.point_from_proportion(get_alpha()))

        x_line = always_redraw(
            lambda: DashedLine(
                start=getPoc(),
                end=axis.x_axis.get_projection(getPoc()),
                color=GREY_N100,
            )
        )

        y_line = always_redraw(
            lambda: DashedLine(
                start=getPoc(),
                end=axis.y_axis.get_projection(getPoc()),
                color=GREY_N100,
            )
        )

        # Labels
        graphLabel = (
            nMath("y = e^x", color=GREY_N500)
            .scale(1.1)
            .set_color_by_gradient([GREY_N500, BLACK])
            .set_sheen_direction(RIGHT)
            .next_to(exp.get_start(), UP)
            .shift(0.5 * RIGHT)
        )

        label_slope = always_redraw(
            lambda: nText("slope = " + get_formatted_value(get_coord()[1] - 0.5))
            .set_color_by_gradient([GREY_N500, BLACK])
            .scale(1.1)
            .set_sheen_direction(RIGHT)
            .move_to(tangent.get_midpoint() + RIGHT, aligned_edge=LEFT)
        )

        label_y = always_redraw(
            lambda: nText(get_formatted_value(get_coord()[1] - 0.5))
            .set_color_by_gradient([GREY_N500, BLACK])
            .scale(1.1)
            .set_sheen_direction(RIGHT)
            .next_to(axis.y_axis.get_projection(getPoc()), LEFT)
        )

        label_x = always_redraw(
            lambda: nText(
                get_formatted_value(get_coord()[0]),
            )
            .set_color_by_gradient([GREY_N500, BLACK])
            .scale(1.1)
            .set_sheen_direction(RIGHT)
            .next_to(axis.x_axis.get_projection(getPoc()), DOWN)
        )

        # ANIMATION HUB

        # PART 1:

        self.play(LaggedStart(Create(axis), Create(exp), lag_ratio=0.7), run_time=3)
        self.wait(1)
        self.play(
            LaggedStart(
                Create(x_line),
                Create(y_line),
                Create(tangent),
                FadeIn(label_x),
                FadeIn(label_y),
                FadeIn(label_slope),
                lag_ratio=0.5,
            )
        )

        self.play(alpha.animate.set_value(0.7), run_time=6, rate_func=there_and_back)
        self.wait(1)
        self.play(fadeInTex(graphLabel))
        highlight(self, graphLabel, buff=0.2)

        self.play(alpha.animate.set_value(0.65))
        self.wait(1)

        # PART 2:

        label_slope_new = always_redraw(
            lambda: nMath("\\frac{dy}{dx} =", "e^x")
            .set_color_by_gradient([GREY_N500, BLACK])
            .scale(1.1)
            .set_sheen_direction(RIGHT)
            .move_to(tangent.get_midpoint() + RIGHT, aligned_edge=LEFT)
        )

        label_x_new = always_redraw(
            lambda: nMath("x")
            .set_color_by_gradient([GREY_N500, BLACK])
            .scale(1.1)
            .set_sheen_direction(RIGHT)
            .next_to(axis.x_axis.get_projection(getPoc()), DOWN)
        )

        label_y_new = always_redraw(
            lambda: nMath("e^x")
            .set_color_by_gradient([GREY_N500, BLACK])
            .scale(1.1)
            .set_sheen_direction(RIGHT)
            .next_to(axis.y_axis.get_projection(getPoc()), LEFT)
        )

        self.play(
            LaggedStart(
                ReplacementTransform(label_x, label_x_new),
                ReplacementTransform(label_y, label_y_new),
                lag_ratio=0.4,
            )
        )
        self.wait(1)
        self.play(ReplacementTransform(label_slope, label_slope_new))
        self.wait(1)

        self.wait(10)


class Exp2(Scene):
    def construct(self):
        addBackground(self)

        # Axis
        axis = (
            getAxis(x_range=[-3.5, 4], y_range=[-3, 15], x_length=8)
            .scale(1.2)
            .shift(0.5 * LEFT + 0.25 * DOWN)
            .set_color_by_gradient([BLUE_N1000, BLUE_N_LIGHT])
            .set_sheen_direction(RIGHT + UP)
        )

        # Curve
        exp = axis.plot(
            lambda x: np.e**x + 0.5,
            x_range=[-3, 2.6],
            color=BLACK,
            stroke_color=[WHITE, GREEN_N100, GREEN_N200],
            stroke_width=7,
            sheen_direction=UP + RIGHT,
            z_index=-0.5,
        )

        exp2 = axis.plot(
            lambda x: np.e ** (2 * x) + 0.5,
            x_range=[-3, 1.3],
            color=BLACK,
            stroke_color=[WHITE, GREEN_N100, GREEN_N200],
            stroke_width=7,
            sheen_direction=UP + RIGHT,
            z_index=-0.5,
        )

        alpha = ValueTracker(0.65)

        ## FOR DEBUGGING
        # alpha.set_value(0.749)

        get_alpha = lambda: alpha.get_value()

        def getTangentLine():
            tangent = TangentLine(
                exp,
                length=7,
                alpha=get_alpha(),
                stroke_color=[GREY_N200, GREY_N800],
                stroke_width=6,
            )
            tangent.set_sheen_direction(tangent.get_unit_vector())
            return tangent

        tangent = always_redraw(getTangentLine)

        # get the point of tangency
        getPoc = lambda: exp.point_from_proportion(get_alpha())
        # get coordinates wrt axes
        get_coord = lambda: axis.p2c(exp.point_from_proportion(get_alpha()))

        particle = always_redraw(
            lambda: Dot(getPoc(), radius=0.08, z_index=1).set_color_by_gradient(
                [NUMBRIK_COLOR_50, NUMBRIK_COLOR_DARK]
            )
        )

        x_line = always_redraw(
            lambda: DashedLine(
                start=getPoc(),
                end=axis.x_axis.get_projection(getPoc()),
                color=GREY_N100,
            )
        )

        y_line = always_redraw(
            lambda: DashedLine(
                start=getPoc(),
                end=axis.y_axis.get_projection(getPoc()),
                color=GREY_N100,
            )
        )

        # Labels
        graphLabel = (
            nMath("y = e^", "x", color=GREY_N500)
            .set_color_by_gradient([GREY_N500, BLACK])
            .scale(1.1)
            .set_sheen_direction(RIGHT)
            .next_to(exp.get_start(), UP)
            .shift(0.5 * RIGHT)
        )
        graphLabelNew = (
            nMath("y = e^", "{2x}", color=GREY_N500)
            .set_color_by_gradient([GREY_N500, BLACK])
            .scale(1.1)
            .set_sheen_direction(RIGHT)
            .next_to(exp.get_start(), UP)
            .shift(0.5 * RIGHT)
        )

        label_slope = always_redraw(
            lambda: nText("slope = " + get_formatted_value(get_coord()[1] - 0.5))
            .set_color_by_gradient([GREY_N500, BLACK])
            .scale(1.1)
            .set_sheen_direction(RIGHT)
            .move_to(tangent.get_midpoint() + RIGHT, aligned_edge=LEFT)
        )

        label_y = always_redraw(
            lambda: nText(get_formatted_value(get_coord()[1] - 0.5))
            .set_color_by_gradient([GREY_N500, BLACK])
            .scale(1.1)
            .set_sheen_direction(RIGHT)
            .next_to(axis.y_axis.get_projection(getPoc()), LEFT)
        )

        label_x = always_redraw(
            lambda: nText(
                get_formatted_value(get_coord()[0]),
            )
            .set_color_by_gradient([GREY_N500, BLACK])
            .scale(1.1)
            .set_sheen_direction(RIGHT)
            .next_to(axis.x_axis.get_projection(getPoc()), DOWN)
        )

        label_x_new = always_redraw(
            lambda: nMath("x")
            .set_color_by_gradient([GREY_N500, BLACK])
            .scale(1.1)
            .set_sheen_direction(RIGHT)
            .next_to(axis.x_axis.get_projection(getPoc()), DOWN)
        )

        # ANIMATION HUB

        self.add(
            axis,
            exp,
            particle,
            tangent,
            x_line,
            y_line,
            graphLabel,
            label_x,
            label_y,
            label_slope,
        )

        self.wait(1)

        hgl2 = highlight(self, graphLabelNew, buff=0.2, unhighlight=False)
        self.play(TransformMatchingTex(graphLabel, graphLabelNew), run_time=2)

        self.play(
            Transform(exp, exp2),
            alpha.animate.set_value(0.735),
            FadeOut(label_slope, *hgl2),
            run_time=3,
        )
        label_slope_new2 = (
            nText("slope = 2 x " + get_formatted_value(get_coord()[1] - 0.5))
            .set_color_by_gradient([GREY_N500, BLACK])
            .scale(1.1)
            .set_sheen_direction(RIGHT)
            .move_to(tangent.get_midpoint() + RIGHT, aligned_edge=LEFT)
        )

        label_slope_new3 = (
            nMath("\\frac{dy}{dx} = 2e^{2x}")
            .set_color_by_gradient([GREY_N500, BLACK])
            .set_sheen_direction(RIGHT)
            .move_to(tangent.get_midpoint() + RIGHT, aligned_edge=LEFT)
        )

        self.play(fadeInTex(label_slope_new2))
        self.wait(1)
        self.play(ReplacementTransform(label_slope_new2, label_slope_new3))
        self.remove(label_slope_new2)

        # self.play(
        #     FadeIn(label_slope_new2),
        # )
        # self.remove(label_slope)
        # self.play(alpha.animate.set_value(0.749), run_time=4)

        # grp = VGroup(axis, exp, graphLabel)

        # self.play(ReplacementTransform(label_slope, label_slope_new))
        # self.remove(label_slope)

        # self.wait(2)

        # self.play(
        #     FadeOut(label_slope),
        #     LaggedStart(grp.animate.shift(LEFT * 1.5), lag_ratio=0.5),
        # )

        # self.play(
        #     ReplacementTransform(label_x, label_x_new),
        #     ReplacementTransform(label_y, label_y_new),
        # )
        # self.remove(label_x, label_y)
        # self.play(alpha.animate.set_value(0.65), run_time=4)

        self.wait(10)


class ExpStatements(Scene):
    def construct(self):
        addBackground(self)

        def getEqn(*args):
            return (
                nMath(*args)
                .scale(1.2)
                .set_sheen_direction(RIGHT)
                .set_color_by_gradient([GREY_N500, BLACK])
            )

        eq1 = getEqn("\\frac{d}{dx}", "(e^", "x", ")", "=", "e^x")
        eq2 = getEqn("\\frac{d}{dx}", "(e^", "{kx}", ")", "=", "\\; ?")
        eq3 = getEqn(
            "\\frac{d}{dx}",
            "(e^",
            "{kx}",
            ")",
            "=",
            "\\frac{d(e^{kx})}{d(kx)}",
        )
        eq3_ = getEqn(
            "\\frac{d}{dx}",
            "(e^",
            "{kx}",
            ")",
            "=",
            "e^{kx}",
        )
        eq4 = getEqn(
            "\\frac{d}{dx}",
            "(e^",
            "{kx}",
            ")",
            "=",
            "e^{kx}",
            "\\cdot \\frac{d(kx)}{dx}",
        )
        eq5 = getEqn(
            "\\frac{d}{dx}",
            "(e^",
            "{kx}",
            ")",
            "=",
            "e^{kx}",
            "\\cdot k",
        )
        eq7 = getEqn(
            "\\frac{d}{dx}",
            "(e^",
            "{kx}",
            ")",
            "=",
            "k",
            "e^{kx}",
        )
        eq8 = getEqn(
            "\\frac{d}{dx}",
            "(e^",
            "{ix}",
            ")",
            "=",
            "k",
            "e^{kx}",
        )
        eq9 = getEqn(
            "\\frac{d}{dx}",
            "(e^",
            "{ix}",
            ")",
            "=",
            "i",
            "e^{ix}",
        )
        self.add(eq1)
        self.wait(1)
        self.play(TransformMatchingTex(eq1, eq2), run_time=2)
        self.wait(1)

        self.play(TransformMatchingTex(eq2, eq3), run_time=2)
        self.play(TransformMatchingTex(eq3, eq3_), run_time=2)
        self.play(TransformMatchingTex(eq3_, eq4), run_time=2)
        self.wait(1)
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait(1)
        self.play(TransformMatchingTex(eq5, eq7))
        self.wait(4)
        hgl = solidHighlight(self, eq7[2], buff=0.2, unhighlight=False)
        self.play(TransformMatchingTex(eq7, eq8), run_time=2)
        self.play(FadeOut(*hgl))
        self.play(TransformMatchingTex(eq8, eq9), run_time=2)
        self.wait(10)


class Conclusion(Scene):
    def construct(self):
        addBackground(self)

        axis = getAxis(x_length=11, y_length=7, x_range=[-5, 5], y_range=[-2, 10])

        rad = 5
        theta = PI / 6

        def getPosition():
            return (
                axis.get_origin()
                + rad * np.cos(theta) * RIGHT
                + rad * np.sin(theta) * UP
            )

        def getPerpPosition():
            return (
                axis.get_origin()
                + rad * np.sin(theta) * LEFT
                + rad * np.cos(theta) * UP
            )

        z = (
            Arrow(
                axis.get_origin(),
                getPosition(),
                buff=0,
                stroke_width=7,
                tip_length=0.4,
            )
            .set_color_by_gradient([GREEN_N100, GREEN_N200, GREEN_NDARK])
            .set_sheen_direction(getPosition())
        )

        z_perp = (
            Arrow(
                axis.get_origin(),
                getPerpPosition(),
                buff=0,
                stroke_width=7,
                tip_length=0.4,
            )
            .set_color_by_gradient([NUMBRIK_COLOR_50, NUMBRIK_COLOR])
            .set_sheen_direction(getPerpPosition())
        )

        def getEqn(*args):
            return (
                nMath(*args)
                .set_sheen_direction(RIGHT)
                .set_color_by_gradient([GREY_N500, BLACK])
            )

        # ANIMATION HUB

        labelPosition3 = getEqn("z", "=", "e^{ix}").move_to(
            getPosition() + 0.7 * UP + 0.7 * RIGHT
        )

        labelPosition4 = getEqn("z_{\\perp}", "=", "ie^{ix}").move_to(
            getPerpPosition() + 0.7 * UP + 0.8 * LEFT
        )

        grp = VGroup(z, z_perp, axis, labelPosition3, labelPosition4)
        # grp.shift(3 * LEFT).scale(0.8)
        # self.add(grp)

        axis2 = (
            getAxis(x_length=7, y_length=7)
            .set_color_by_gradient([GREY_N100, GREY_N500])
            .set_sheen_direction(RIGHT + UP)
        )

        rad = 2.5

        circle = Circle(rad, stroke_color=[GREY_N800, GREY_N50], stroke_width=6)

        def getPosition2():
            return (
                axis2.get_origin()
                + rad * np.cos(theta) * RIGHT
                + rad * np.sin(theta) * UP
            )

        def getPerpPosition2():
            return (
                axis2.get_origin()
                + rad * np.sin(theta) * LEFT
                + rad * np.cos(theta) * UP
            )

        position_vector = (
            Arrow(
                axis2.get_origin(),
                getPosition2(),
                buff=0,
                stroke_width=7,
                tip_length=0.4,
            )
            .set_color_by_gradient([GREEN_N100, GREEN_N200, GREEN_NDARK])
            .set_sheen_direction(getPosition2())
        )

        velocity_vector = (
            Arrow(
                getPosition2(),
                getPosition2() + getPerpPosition2(),
                buff=0,
                stroke_width=7,
                tip_length=0.4,
            )
            .set_color_by_gradient([NUMBRIK_COLOR_50, NUMBRIK_COLOR])
            .set_sheen_direction(getPerpPosition2())
        )

        self.add(grp)
        self.wait(1)

        self.play(
            Transform(axis, axis2),
            Transform(z, position_vector),
            Transform(z_perp, velocity_vector),
            Create(circle),
            labelPosition3.animate.move_to(
                (axis2.get_origin() + getPosition2()) / 2 + 0.2 * getPerpPosition2(),
            ).shift(LEFT * 0.4),
            labelPosition4.animate.next_to(velocity_vector, RIGHT, buff=-0.1),
            run_time=3,
        )
        self.wait(1)
        grp.add(circle)
        self.play(grp.animate.shift(2.5 * LEFT))

        eq5 = (
            getEqn(
                "\\frac{de^{ix}}{dx} =",
                "ie^{ix}",
            ).move_to(RIGHT * 2.5, aligned_edge=LEFT)
            # .shift(0.75 * UP)
        )

        self.play(fadeInTex(eq5))
        self.wait(2)
        self.play(
            LaggedStart(FadeOut(grp), eq5.animate.move_to(ORIGIN + UP), lag_ratio=0.5),
            run_time=3,
        )
        self.wait(1)

        eq6 = (
            getEqn(
                "\\frac{de^{ix}}{dx} =",
                "ie^{ix}",
                "\\iff",
                "\\frac{d\\vec{z}}{dx} =",
                "\\vec{z}_{\\perp}",
            ).next_to(eq5, 0)
            # .shift(0.75 * UP)
        )

        eqRes3 = (
            getEqn(
                "\\vec{z}",
                "= ",
                "(",
                "\\cos{x}",
                ",\\;",
                "\\sin{x}",
                ")",
            )
            .next_to(eq6, DOWN, buff=0.5)
            .shift(0.5 * DOWN)
        )

        eqRes4 = getEqn(
            "e^{ix}",
            "= ",
            "(",
            "\\cos{x}",
            ",\\;",
            "\\sin{x}",
            ")",
        ).next_to(eqRes3, 0, aligned_edge=DOWN)

        eqRes5 = getEqn(
            "e^{ix}",
            "= ",
            "\\cos{x}",
            "+ i",
            "\\sin{x}",
        ).next_to(eqRes3, 0, aligned_edge=UP)

        self.play(TransformMatchingTex(eq5, eq6), run_time=2)
        self.wait(1)
        self.play(fadeInTex(eqRes3))
        self.wait(1)
        self.play(TransformMatchingTex(eqRes3, eqRes4), run_time=2)
        self.wait(1)
        self.play(TransformMatchingTex(eqRes4, eqRes5), run_time=2)
        self.wait(2)

        self.play(
            LaggedStart(
                FadeOut(eq6), eqRes5.animate.move_to(ORIGIN).scale(1.2), lag_ratio=0.5
            )
        )
        highlight(
            self,
            eqRes5,
            buff=0.25,
            corner_radius=0.2,
            unhighlight=False,
        )

        self.wait()


class Thumbnail(Scene):
    def construct(self):
        addBackground(self)

        axis = (
            getAxis(x_length=20, y_length=10, x_range=[-5, 8], y_range=[-7, 10])
            .set_color_by_gradient([GREY_N100, BLACK])
            .set_sheen_direction(RIGHT + UP)
            .shift(RIGHT * 3.4 + 0.7 * DOWN)
        )

        rad = 2.4
        theta = PI / 12
        circle = Circle(rad, stroke_color=[GREY_N800, GREY_N50], stroke_width=8).shift(
            3.7 * RIGHT + 0.8 * DOWN
        )

        getRadial = lambda: np.cos(theta) * RIGHT + np.sin(theta) * UP

        exp = axis.plot(
            lambda x: np.e**x,
            x_range=[-8, 5],
            color=GREEN_N200,
            stroke_color=[GREEN_N200, GREEN_NDARK],
        )

        position = (
            rad * np.cos(theta) * RIGHT + rad * np.sin(theta) * UP + circle.get_center()
        )

        perpDir = np.sin(theta) * LEFT + np.cos(theta) * UP

        particle = Dot(position, radius=0.15, z_index=1).set_color_by_gradient(
            [BLACK, GREY_N50]
        )

        position_vector = (
            Arrow(
                circle.get_center(),
                position,
                buff=0,
                stroke_width=10,
                tip_length=0.5,
            )
            .set_color_by_gradient([GREEN_N100, GREEN_N200, GREEN_NDARK])
            .set_sheen_direction(getRadial())
        )

        velocity_vector = (
            Arrow(
                position,
                position + perpDir * 3,
                buff=0,
                stroke_width=10,
                tip_length=0.5,
            )
            .set_color_by_gradient(
                [
                    BLUE_C,
                    NUMBRIK_COLOR_DARK,
                ]
            )
            .set_sheen_direction(perpDir)
        )

        def getEqn(*args):
            return (
                nMath(*args)
                .set_sheen_direction(RIGHT)
                .set_color_by_gradient([GREY_N200, BLACK])
                .scale(1.2)
            )

        labelPosition = getEqn("\\vec{r}").move_to(
            (circle.get_center() + position) / 2 + perpDir * 0.4,
        )

        labelVelocity = getEqn("\\vec{v}").move_to(
            (position + perpDir + 0.4 * getRadial())
        )

        equation = (
            MathTex(
                "e^{\\emph{i}\\,\\theta} = cos(\\theta) + \\emph{i}\\, sin(\\theta)",
                color=BLACK,
                substrings_to_isolate="x",
                tex_template=TexFontTemplates.fourier_utopia,
            ).scale(2.5)
            # .to_corner(UL)
            # .shift(0.8 * DOWN + 0.25 * RIGHT)
        )
        equation[0][2].set_color(NUMBRIK_COLOR_DARK)
        equation[0][8].set_color(NUMBRIK_COLOR_DARK)
        equation[0][16].set_color(NUMBRIK_COLOR_DARK)
        # equation[0][1].set_color(GREEN_N1000)
        # equation[0][11].set_color(GREEN_N1000)
        # equation.set_color_by_tex("\\theta", NUMBRIK_COLOR)
        # hgl = solidHighlight(self, equation, buff=0.5, color=GREEN_N100, animate=False)
        # hgl[0].set_opacity(0.5)
        self.add(equation)
        # self.add(index_labels(equation[0]))

        self.add(
            # circle,
            # position_vector,
            # velocity_vector,
            # exp,
            # particle,
            # labelPosition,
            # labelVelocity,
        )

        self.wait(2)
