from manim import *
from utils import *


class Template(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            axis_config={
                "include_ticks": False,
                "include_numbers": False,
                "color": GRAY_D,
                "font_size": 24,
                "tip_shape": StealthTip,
            },
        )

        rotaxis = Line3D(
            np.array([0, 0, -5]),
            np.array([0, 0, 5]),
            thickness=0.04,
            color=GREY_N200,
        )
        # Define vertices of a triangular pyramid (tetrahedron)
        A = np.array([0, 0, 0])
        B = np.array([4, 3, 0])
        C = np.array([0, 3, 0])
        D = np.array([0, 0, 2])
        E = np.array([4, 3, 2])
        F = np.array([0, 3, 2])

        # Faces (triangles)
        faces = [
            [A, B, C],  # Base
            [D, E, F],
            # [B, C, D],
            [A, B, E, D],
            [A, C, F, D],
            # [C, A, D],
        ]

        # Create polygons for faces
        pyramid_faces = VGroup()
        colors = [RED, BLUE, GREEN, YELLOW]
        for i, face in enumerate(faces):
            tri = Polygon(
                *face,
                fill_opacity=0.5,
                stroke_color=GREY_N400,
                stroke_width=4,
                fill_color=BLUE,
            )
            pyramid_faces.add(tri)

        pyramid_faces.set_flat_stroke(False)

        # Add 3D rotation
        self.set_camera_orientation(
            phi=40 * DEGREES, theta=-50 * DEGREES, zoom=1, focal_distance=10000
        )
        self.add(pyramid_faces, rotaxis)

        self.move_camera(
            phi=0 * DEGREES,
            theta=-90 * DEGREES,
            frame_center=1.5 * RIGHT + 1.5 * UP,
            run_time=4,
            zoom=1.2,
            added_anims=[pyramid_faces[1].animate.set_opacity(0)],
        )

        self.wait(5)


class TriangularPrism(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            axis_config={
                "include_ticks": False,
                "include_numbers": False,
                "color": GRAY_D,
                "font_size": 24,
                "tip_shape": StealthTip,
            },
        )

        rotaxis = Line3D(
            np.array([0, 0, -3]),
            np.array([0, 0, 3]),
            thickness=0.04,
            color=GREY_N200,
        )
        # Define vertices of a triangular pyramid (tetrahedron)
        A = np.array([0, 0, -1])
        B = np.array([4, 3, -1])
        C = np.array([0, 3, -1])
        D = np.array([0, 0, 1])
        E = np.array([4, 3, 1])
        F = np.array([0, 3, 1])

        # Faces (triangles)
        faces = [
            [A, B, C],  # Base
            [D, E, F],
            [A, B, E, D],
            [A, C, F, D],
            [B, C, F, E],
        ]

        # Create polygons for faces
        prism_faces = VGroup()
        colors = [RED, BLUE, GREEN, YELLOW]

        for i, face in enumerate(faces):
            tri = Polygon(
                *face,
                fill_opacity=0,
                stroke_color=GREY_N400,
                stroke_width=4,
                # fill_color=GREY_N50,
            )
            prism_faces.add(tri)

        prism_faces.set_flat_stroke(False)
        prism_faces.set_stroke([GREY_N200, GREY_N400]).set_sheen_direction(IN)

        self.set_camera_orientation(
            phi=20 * DEGREES, theta=120 * DEGREES, zoom=1, focal_distance=10000
        )
        # self.add(prism_faces, rotaxis)
        self.play(FadeIn(prism_faces), FadeIn(rotaxis))

        waterHeight = ValueTracker(-1)

        def getWater():
            A = np.array([0, 0, -1])
            B = np.array([4, 3, -1])
            C = np.array([0, 3, -1])
            D = np.array([0, 0, waterHeight.get_value()])
            E = np.array([4, 3, waterHeight.get_value()])
            F = np.array([0, 3, waterHeight.get_value()])

            faces = [
                [A, B, C],  # Base
                [D, E, F],
                [A, B, E, D],
                [A, C, F, D],
                [B, C, F, E],
            ]

            # Create polygons for faces
            prism_faces = VGroup()

            for i, face in enumerate(faces):
                tri = Polygon(
                    *face,
                    fill_opacity=0.7,
                    stroke_color=None,
                    stroke_width=0,
                    fill_color=NUMBRIK_COLOR_100,
                )
                prism_faces.add(tri)

            prism_faces.set_flat_stroke(False)

            return prism_faces

        water = always_redraw(getWater)

        # reference
        # self.set_camera_orientation(
        #     phi=60 * DEGREES, theta=-50 * DEGREES, zoom=1, focal_distance=10000
        # )

        # self.add(prism_faces, rotaxis)

        self.move_camera(phi=60 * DEGREES, theta=-30 * DEGREES, run_time=2)

        self.play(
            Rotate(
                prism_faces,
                2 * PI,
                -Line(np.array([0, 0, -5]), np.array([0, 0, 5])).get_unit_vector(),
                ORIGIN,
            ),
            run_time=3,
        )
        self.move_camera(phi=PI / 2)

        self.add(water)
        self.play(waterHeight.animate.set_value(0.25), run_time=3)

        self.move_camera(phi=PI / 3, run_time=2)
        self.wait(1)

        tmpHeight = 0.8
        arrow1 = Arrow(
            (A + C) / 2 + tmpHeight * OUT,
            (A + C) / 2 - 2.5 * perpendicular_unit_vector(A, C, OUT) + tmpHeight * OUT,
            color=GREY_N400,
            buff=0,
        )

        arrow2 = Arrow(
            (A + B) / 2 + tmpHeight * OUT,
            (A + B) / 2 + 2.5 * perpendicular_unit_vector(A, B, OUT) + tmpHeight * OUT,
            color=GREY_N400,
            buff=0,
        )

        arrow3 = Arrow(
            (B + C) / 2 + tmpHeight * OUT,
            (B + C) / 2 + 2.5 * perpendicular_unit_vector(B, C, OUT) + tmpHeight * OUT,
            color=GREY_N400,
            buff=0,
        )

        anti_clockwise_arrow = CurvedArrow(
            ORIGIN + 0.85 / np.sqrt(2) * UP + 0.85 / np.sqrt(2) * LEFT,
            ORIGIN + 0.85 * RIGHT,
            angle=-3 * PI / 4,
            color=RED_N,
            arc_center=ORIGIN,
        )

        self.play(
            LaggedStart(
                GrowArrow(arrow1),
                GrowArrow(arrow2),
                GrowArrow(arrow3),
                Create(anti_clockwise_arrow),
                lag_ratio=0.5,
            )
        )
        self.wait(1)
        self.play(FadeOut(arrow1, arrow2, arrow3, anti_clockwise_arrow))

        waterFace = Polygon(
            np.array([0, 0, 0]),
            np.array([4, 3, 0]),
            np.array([0, 3, 0]),
            fill_opacity=0.85,
            stroke_color=GREY_N400,
            stroke_width=4,
            fill_color=NUMBRIK_COLOR_50,
        )

        self.play(Create(waterFace))
        self.play(water.animate.set_opacity(0), prism_faces.animate.set_opacity(0))
        self.remove(water, prism_faces)
        self.wait(1)

        # # Add 3D rotation

        self.move_camera(
            phi=0 * DEGREES,
            theta=-90 * DEGREES,
            frame_center=1.5 * RIGHT + 2.25 * UP,
            run_time=4,
            zoom=1.2,
        )

        self.wait(5)


class TorqueBalance(ThreeDScene):
    def construct(self):
        rotaxis = Line3D(
            np.array([0, 0, -5]),
            np.array([0, 0, 5]),
            thickness=0.04,
            color=GREY_N200,
        )

        waterFace = Polygon(
            np.array([0, 0, 0]),
            np.array([4, 3, 0]),
            np.array([0, 3, 0]),
            fill_opacity=0.85,
            stroke_color=GREY_N400,
            stroke_width=4,
            fill_color=NUMBRIK_COLOR_50,
        )

        self.set_camera_orientation(focal_distance=1000)
        self.add(waterFace, rotaxis)

        # Add 3D rotation

        self.move_camera(
            phi=0 * DEGREES,
            theta=-90 * DEGREES,
            frame_center=1.5 * RIGHT + 2.25 * UP,
            run_time=1,
            zoom=1.2,
        )
        self.wait(1)

        # Define vertices of a triangular pyramid (tetrahedron)
        A = np.array([0, 0, 0])
        B = np.array([4, 3, 0])
        C = np.array([0, 3, 0])

        arrow1 = Arrow(
            (A + C) / 2,
            (A + C) / 2 - 1.5 * perpendicular_unit_vector(A, C, OUT),
            color=GREY_N400,
            buff=0,
        )

        arrow2 = Arrow(
            (A + B) / 2,
            (A + B) / 2 + 1.5 * perpendicular_unit_vector(A, B, OUT),
            color=GREY_N400,
            buff=0,
        )

        arrow3 = Arrow(
            (B + C) / 2,
            (B + C) / 2 + 1.5 * perpendicular_unit_vector(B, C, OUT),
            color=GREY_N400,
            buff=0,
        )

        forceLabel1 = (
            nMath("F_{a} = a")
            .next_to(arrow1, arrow1.get_unit_vector(), buff=0.2)
            .scale(0.8)
        )

        forceLabel2 = (
            nMath("F_{c} = c")
            .next_to(arrow2, arrow2.get_unit_vector(), buff=0.2)
            .scale(0.8)
        )

        forceLabel3 = (
            nMath("F_{b} = b")
            .next_to(arrow3, arrow3.get_unit_vector(), buff=0.2)
            .scale(0.8)
        )

        refLine = DashedLine(
            (B + C) / 2,
            (B + C) / 2 - 3.5 * perpendicular_unit_vector(B, C, OUT),
            color=GREY_N500,
            dash_length=0.2,
            dashed_ratio=0.8,
            buff=0,
        )

        lengthMarker1 = BraceBetweenPoints(A, (A + C) / 2, color=GREY_N800, buff=0.1)
        lengthMarker2 = BraceBetweenPoints(A, (A + B) / 2, color=GREY_N800, buff=0.1)
        lengthMarker3 = BraceBetweenPoints(
            A, refLine.get_projection(A), color=GREY_N800, buff=0.1
        ).shift(UP)

        lengthLabel1 = (
            nMath("\\frac{a}{2}", color=BLACK)
            .next_to(lengthMarker1, RIGHT, buff=0.1)
            .scale(0.85)
        )
        lengthLabel2 = (
            nMath("\\frac{c}{2}", color=BLACK)
            .next_to(lengthMarker2, DOWN + RIGHT, buff=-0.5)
            .shift(LEFT * 0.45)
            .scale(0.85)
        )
        lengthLabel3 = (
            nMath("\\frac{b}{2}", color=BLACK)
            .next_to(lengthMarker3, DOWN, buff=0.1)
            .scale(0.85)
        )

        self.play(
            LaggedStart(
                GrowArrow(arrow1),
                fadeInTex(forceLabel1),
                GrowArrow(arrow2),
                fadeInTex(forceLabel2),
                GrowArrow(arrow3),
                fadeInTex(forceLabel3),
                lag_ratio=0.5,
            )
        )
        self.wait(1)

        clockwise_arrow = CurvedArrow(
            ORIGIN + 0.85 * RIGHT,
            ORIGIN + 0.85 / np.sqrt(2) * UP + 0.85 / np.sqrt(2) * LEFT,
            color=RED_N,
            arc_center=ORIGIN,
            angle=3 * PI / 4,
        )

        hgl = solidHighlight(
            self,
            forceLabel1,
            buff=0.2,
            animate=False,
        )
        self.play(FadeIn(*hgl))
        self.play(
            LaggedStart(
                Write(lengthMarker1),
                fadeInTex(lengthLabel1),
                lag_ratio=0.5,
            )
        )
        self.wait(1)
        self.play(FadeOut(lengthMarker1, lengthLabel1))
        self.play(Create(clockwise_arrow))
        self.wait(1)
        self.play(FadeOut(clockwise_arrow), hgl[0].animate.set_opacity(0))
        self.wait(1)

        hgl = solidHighlight(
            self,
            forceLabel3,
            buff=0.2,
            animate=False,
        )
        self.play(FadeIn(*hgl))
        self.play(
            LaggedStart(
                Create(refLine),
                Write(lengthMarker3),
                fadeInTex(lengthLabel3),
                lag_ratio=0.5,
            )
        )
        self.wait(1)
        self.play(FadeOut(lengthMarker3, lengthLabel3, refLine))
        self.play(Create(clockwise_arrow))
        self.wait(1)
        self.play(FadeOut(clockwise_arrow), hgl[0].animate.set_opacity(0))
        self.wait(1)

        hgl = solidHighlight(
            self,
            forceLabel2,
            buff=0.2,
            animate=False,
        )
        self.play(FadeIn(*hgl))
        self.play(
            LaggedStart(
                Write(lengthMarker2),
                fadeInTex(lengthLabel2),
                lag_ratio=0.5,
            )
        )
        self.wait(1)
        self.play(FadeOut(lengthMarker2, lengthLabel2))

        anti_clockwise_arrow = CurvedArrow(
            ORIGIN + 0.85 / np.sqrt(2) * UP + 0.85 / np.sqrt(2) * LEFT,
            ORIGIN + 0.85 * RIGHT,
            angle=-3 * PI / 4,
            color=RED_N,
            arc_center=ORIGIN,
        )

        self.play(Create(anti_clockwise_arrow))
        self.wait(1)
        self.play(FadeOut(anti_clockwise_arrow), hgl[0].animate.set_opacity(0))
        self.wait(5)


class TorqueStatements(Scene):
    def construct(self):
        eq1 = nMath("T_{anti-clockwise} =", "a\\cdot \\frac{a}{2}")
        eq2 = nMath(
            "T_{anti-clockwise} =", "a\\cdot \\frac{a}{2}", "+", "b\\cdot \\frac{b}{2}"
        )

        self.play(fadeInTex(eq1))
        self.wait(1)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(1)
        self.play(eq2.animate.shift(UP))

        eq3 = nMath("T_{clockwise}", "=", "c\\cdot \\frac{c}{2}").next_to(
            eq2, DOWN, buff=0.7
        )
        eq4 = nMath(
            "a\\cdot \\frac{a}{2}",
            "+",
            "b\\cdot \\frac{b}{2}",
            "=",
            "c\\cdot \\frac{c}{2}",
        )

        eqFinal = nMath("a^2 + b^2 = c^2", color=BLACK)

        self.play(fadeInTex(eq3))
        self.wait(1)
        self.play(
            LaggedStart(
                FadeOut(eq2[0], eq3[0]),
                AnimationGroup(
                    ReplacementTransform(eq2[1], eq4[0]),
                    ReplacementTransform(eq2[2], eq4[1]),
                    ReplacementTransform(eq2[3], eq4[2]),
                    ReplacementTransform(eq3[1], eq4[3]),
                    ReplacementTransform(eq3[2], eq4[4]),
                ),
                lag_ratio=0.5,
            )
        )
        self.wait(1)
        self.play(FadeOut(eq4, shift=UP), FadeIn(eqFinal, shift=UP))
        highlight(self, eqFinal, buff=0.2, unhighlight=False)

        self.wait(10)


class Intro(Scene):
    def construct(self):
        mathSet = Ellipse(3, 2, fill_opacity=1).set_color_by_gradient(
            [VIOLET_N1000, NUMBRIK_COLOR_200]
        )
        physicsSet = Ellipse(3, 2, fill_opacity=1).set_color_by_gradient(
            [GREEN_NDARK, GREEN_N100]
        )

        VGroup(mathSet, physicsSet).arrange(RIGHT, buff=2)

        titleMath = nMath("Maths", color=WHITE).move_to(mathSet.get_center())
        titlePhysics = nMath("Physics", color=WHITE).move_to(physicsSet.get_center())

        arrow1 = CurvedArrow(
            mathSet.get_top() + 0.3 * UP + RIGHT * 0.75,
            physicsSet.get_top() + 0.3 * UP + LEFT * 0.75,
            angle=-2 * PI / 3,
            stroke_color=[GREY_N400, GREY_N500],
            stroke_width=8,
            tip_length=0.5,
            sheen_direction=RIGHT,
        )

        arrow2 = CurvedArrow(
            physicsSet.get_bottom() + 0.3 * DOWN + LEFT * 0.75,
            mathSet.get_bottom() + 0.3 * DOWN + RIGHT * 0.75,
            angle=-2 * PI / 3,
            stroke_color=[GREY_N400, GREY_N500],
            stroke_width=8,
            tip_length=0.5,
            sheen_direction=RIGHT,
        )

        text1 = getCurvedText(
            "used in",
            arrow1.radius + 0.2,
            arrow1.get_arc_center(),
            angle=45,
            size=44,
            invert=False,
        )

        text2 = getCurvedText(
            "inspires",
            arrow2.radius + 0.6,
            arrow2.get_arc_center(),
            angle=45,
            size=44,
            invert=True,
        )

        text2[3].shift(DOWN * 0.2)

        # self.add(
        #     mathSet, physicsSet, titleMath, titlePhysics, arrow1, arrow2, text1, text2
        # )

        self.play(
            FadeIn(mathSet, shift=2 * LEFT),
            FadeIn(physicsSet, shift=2 * RIGHT),
            run_time=1.5,
        )

        self.play(
            LaggedStart(fadeInTex(titleMath), fadeInTex(titlePhysics), lag_ratio=0.5)
        )
        self.wait(1)
        self.play(LaggedStart(Create(arrow1), Write(text1), lag_ratio=0.5))
        self.wait(1)
        self.play(LaggedStart(Create(arrow2), Write(text2), lag_ratio=0.5))

        self.wait(2)

        self.play(
            Swap(VGroup(mathSet, titleMath), VGroup(physicsSet, titlePhysics)),
            run_time=2,
        )

        self.wait(10)


class StillWater(Scene):
    def construct(self):
        container = Rectangle(
            height=3,
            width=5,
            stroke_color=BLACK,
        )

        height = ValueTracker(0)

        ground = Line(
            container.get_corner(DL) + LEFT * 1.5,
            container.get_corner(DR) + RIGHT * 1.5,
            color=GREY_N400,
            stroke_width=10,
        )

        water = always_redraw(
            lambda: Rectangle(
                height=height.get_value(),
                width=5,
                color=BLUE,
                stroke_color=WHITE,
                fill_opacity=1,
                z_index=-0.1,
            ).next_to(container, 0, aligned_edge=DOWN)
        )

        # self.add(container, water, arrow1, arrow2, ground, labelmg, labelN)
        self.add(water)
        self.play(
            LaggedStart(
                Create(container),
                Create(ground),
                height.animate.set_value(2),
                lag_ratio=0.5,
            )
        )
        self.wait(1)
        arrow1 = Arrow(
            water.get_center(), water.get_center() + 2.5 * DOWN, color=GREY_N800, buff=0
        )
        arrow2 = Arrow(
            container.get_bottom(),
            container.get_bottom() + 2.8 * UP,
            color=GREY_N400,
            stroke_width=8,
            buff=0,
            z_index=-0.05,
        )

        labelmg = nMath("mg").next_to(arrow1, DOWN, buff=0.4)
        labelN = nMath("N").next_to(arrow2, UP, buff=0.6)

        water2 = water.copy()

        self.play(LaggedStart(GrowArrow(arrow1), Write(labelmg), lag_ratio=0.5))
        self.play(LaggedStart(GrowArrow(arrow2), Write(labelN), lag_ratio=0.5))
        self.wait(1)
        self.add(water2)
        self.remove(water)

        shift_scene_up(self, 2 * LEFT)

        force_net = nMath("\\vec{F}_{net} = 0").shift(RIGHT * 4).shift(UP * 0.5)
        torque_net = nMath("\\vec{T}_{net} = 0").shift(RIGHT * 4).shift(DOWN * 0.5)

        self.play(fadeInTex(force_net))
        self.play(fadeInTex(torque_net))

        self.wait(10)


def getCurvedText(text, radius=2, arc_center=ORIGIN, angle=60, size=50, invert=False):
    # Create a circular arc path
    arc = Arc(
        radius=radius,
        arc_center=arc_center,
        angle=(1 if invert else -1) * angle * DEGREES,
        start_angle=(270 - angle / 2 if invert else 90 + angle / 2) * DEGREES,
    )  # semicircle

    # Create individual characters
    chars = [
        Text(c, color=GREY_N800, font="Bradley Hand", font_size=size) for c in text
    ]

    # Number of positions along the arc
    n = len(chars)

    grp = VGroup()

    # Distribute characters along the arc
    for i, char in enumerate(chars):
        t = i / (n - 1)  # parameter from 0 to 1
        point = arc.point_from_proportion(t)  # position on arc
        tangent = TangentLine(arc, t).get_unit_vector()  # tangent vector

        # Move char to point
        char.move_to(point, aligned_edge=DOWN)

        # Rotate char to align with tangent
        angle = angle_of_vector(tangent)
        char.rotate(angle)  # adjust to face along curve

        grp.add(char)

    return grp


class Windmill(Scene):
    def construct(self):
        # Pole
        pole = Rectangle(width=0.2, height=3, color=GREY, fill_opacity=1).shift(
            DOWN * 1.5
        )

        # Hub
        hub = Circle(radius=0.2, color=BLACK, fill_opacity=1, z_index=0.1)

        # Blades (simple rectangles)
        blade1 = Rectangle(width=0.3, height=2, color=BLUE, fill_opacity=1).next_to(
            hub, UP, buff=0
        )
        blade1.shift(UP * 0.5)  # move upward more so hub is at base
        bladeHolder = Line(
            blade1.get_corner(UR),
            blade1.get_corner(UR)
            + 1.3 * (blade1.get_corner(DR) - blade1.get_corner(UR)),
            color=GREY_N200,
        )

        # Group and rotate to create other blades
        blades = VGroup(blade1, bladeHolder)
        for k in [1, 2, 3]:
            blades.add(
                blade1.copy().rotate(k * PI / 2, about_point=ORIGIN),
                bladeHolder.copy().rotate(k * PI / 2, about_point=ORIGIN),
            )

        # Combine hub and blades
        rotor = VGroup(hub, blades)

        ground = Line(
            pole.get_corner(DL) + LEFT * 3,
            pole.get_corner(DR) + RIGHT * 3,
            color=GREY_N400,
            stroke_width=10,
        )

        # Add everything
        self.add(pole, rotor, ground)

        # Animate rotation of blades
        self.play(
            Rotate(
                rotor, angle=2 * PI, about_point=ORIGIN, run_time=6, rate_func=linear
            )
        )
        self.wait()


class DoorScene(ThreeDScene):
    def construct(self):
        # Set camera

        self.set_camera_orientation(
            phi=60 * DEGREES,
            theta=-30 * DEGREES,
            # gamma=PI / 2,
            zoom=1.5,
            focal_distance=1000,
        )

        axes = ThreeDAxes(
            axis_config={
                "include_ticks": False,
                "include_numbers": False,
                "color": GRAY_D,
                "font_size": 24,
                "color": VIOLET_N100,
                "tip_shape": StealthTip,
            },
        )

        # Door parameters
        door_width = 2
        door_height = 4
        door_thickness = 0.05

        # Create door as a 3D cube (flattened)
        door = Cube(
            side_length=1,
            fill_opacity=0.8,
            fill_color=LIGHT_BROWN,
            stroke_width=0,
        )

        # hinge = Line(ORIGIN, OUT * 6, color=BLACK)

        hinge = Cylinder(
            radius=0.015, height=door_height, direction=OUT, fill_opacity=1, color=GREY
        )

        door.stretch_to_fit_width(door_thickness)
        door.stretch_to_fit_height(door_width)
        door.stretch_to_fit_depth(door_height)
        # Place hinge at origin (left edge)
        hinge.move_to(ORIGIN).shift(UP * 0.95)

        helperLine1 = DashedLine(
            UP,
            UP + LEFT * 2,
            color=BLACK,
        )
        helperLine1.set_opacity(0)
        force_arrow = Arrow(
            DOWN * 0.75 + LEFT * 2,
            DOWN * 0.75,
            buff=0,
            # door.get_
            # door.get_edge_center(DOWN) + 5 * door.get_,
            color=BLACK,
            stroke_width=6,
        )

        door = VGroup(door, force_arrow, helperLine1)

        door.rotate(
            angle=90 * DEGREES,
            axis=OUT,
            about_point=UP,
        )

        # Add hinge (cylinder at left edge)
        # hinge = Cylinder(
        #     radius=0.05, height=door_height, direction=OUT, fill_opacity=1, color=GREY
        # )

        # Force arrow (applied at far edge of door)

        # Add all objects
        self.add(hinge, door, force_arrow, axes)

        # Rotate the door about hinge
        self.play(
            Rotate(
                door,
                angle=60 * DEGREES,
                axis=OUT,
                about_point=UP,
            ),
            run_time=3,
        )

        self.move_camera(
            phi=0 * DEGREES,
            theta=-90 * DEGREES,
            frame_center=UP,
            run_time=4,
            zoom=1.2,
        )

        braces = BraceBetweenPoints(
            helperLine1.get_end(), force_arrow.get_start(), color=BLACK
        )

        self.play(
            Rotate(
                door,
                angle=PI / 2,
                axis=OUT,
                about_point=UP,
            ),
            run_time=4,
            rate_func=there_and_back,
        )

        forceLabel = nMath("F").next_to(force_arrow, RIGHT + UP, buff=-0.5)
        distanceLabel = nMath("r").move_to(
            braces.get_center() + DOWN * 0.3 + RIGHT * 0.5
        )

        self.play(FadeIn(forceLabel))
        helperLine1.set_opacity(1)
        self.play(Create(helperLine1))
        self.play(
            LaggedStart(
                Write(braces),
                FadeIn(distanceLabel),
                lag_ratio=0.5,
            )
        )

        anti_clockwise_arrow = CurvedArrow(
            ORIGIN + UP + 0.85 * RIGHT,
            ORIGIN + UP + 0.85 / np.sqrt(2) * UP + 0.85 / np.sqrt(2) * LEFT,
            color=RED_N,
            arc_center=ORIGIN,
        )

        torqueLabel = nMath("T_{anti-clock} = r\\times F").shift(2 * UP + 3 * LEFT)

        self.play(Create(anti_clockwise_arrow))
        self.play(fadeInTex(torqueLabel))

        self.wait(12)


class Prologue(Scene):
    def construct(self):
        prologue1 = MathTex(
            "\\text{Mathematics is the branch of theoretical physics}",
            tex_template=TexFontTemplates.droid_serif,
            color=GREY_N800,
        ).shift(UP)
        prologue2 = MathTex(
            "\\text{where the experiments are cheap}",
            tex_template=TexFontTemplates.droid_serif,
            color=GREY_N800,
        ).next_to(prologue1, DOWN, buff=0.3)

        prologueBy = nMath("\\text{- V. Arnold}", color=NUMBRIK_COLOR).next_to(
            prologue2, DOWN, buff=0.7
        )
        self.play(
            LaggedStart(
                LaggedStart(fadeInTex(prologue1), fadeInTex(prologue2), lag_ratio=0.6),
                AnimationGroup(Write(prologueBy), run_time=2),
                lag_ratio=0.8,
            )
        )

        clearScreen(self, 4)


class LawOfDifficulty(Scene):
    def construct(self):
        law = MathTex(
            "\\text{Law of conservation of Difficulty}",
            tex_template=TexFontTemplates.droid_serif,
            color=GREY_N800,
        ).shift(1 * UP)

        self.play(fadeInTex(law))

        text1 = nMath("\\text{Algebraic Manipulation}").next_to(law, DOWN, buff=1)
        text2 = nMath("\\text{Relevant Physical System}").next_to(text1, 0)
        hgl = highlight(self, text2, buff=0.25, color=RED_N100, animate=False)
        self.play(LaggedStart(Write(text1), Create(*hgl), lag_ratio=0.5))
        self.wait(1)
        self.play(FadeOut(text1, shift=UP), FadeIn(text2, shift=UP))

        self.wait(10)


class Pressure(Scene):
    def construct(self):
        eqn = nMath("F_{side} =", "Pressure", "\\cdot", "Area")
        eqn2 = nMath(
            "F_{side} =", "Pressure", "\\cdot", "L_{side}", "\\cdot", "H_{side}"
        )
        eqn3 = nMath(
            "F_{side} =", "Pressure", "\\cdot", "H_{side}", "\\cdot", "L_{side}"
        )
        eqn4 = nMath("F_{side} =", "k", "\\cdot", "L_{side}")
        eqn5 = nMath("F_{side} =", "1", "\\cdot", "L_{side}")
        eqn6 = nMath("F_{side} =", "L_{side}")

        self.play(fadeInTex(eqn))
        self.play(TransformMatchingTex(eqn, eqn2), run_time=1.5)
        self.play(TransformMatchingTex(eqn2, eqn3), run_time=1.5)
        self.play(TransformMatchingTex(eqn3, eqn4), run_time=1.5)
        self.play(TransformMatchingTex(eqn4, eqn5), run_time=1.5)
        self.play(TransformMatchingTex(eqn5, eqn6), run_time=1.5)
        self.wait(5)


class PressureExplainer(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            axis_config={
                "include_ticks": False,
                "include_numbers": False,
                "color": GRAY_D,
                "font_size": 24,
                "tip_shape": StealthTip,
            },
        )

        rotaxis = Line3D(
            np.array([0, 0, -3]),
            np.array([0, 0, 3]),
            thickness=0.04,
            color=GREY_N200,
        )
        # Define vertices of a triangular pyramid (tetrahedron)
        A = np.array([0, 0, -1])
        B = np.array([4, 3, -1])
        C = np.array([0, 3, -1])
        D = np.array([0, 0, 1])
        E = np.array([4, 3, 1])
        F = np.array([0, 3, 1])

        # Faces (triangles)
        faces = [
            [A, B, C],  # Base
            [D, E, F],
            [A, B, E, D],
            [A, C, F, D],
            [B, C, F, E],
        ]

        # Create polygons for faces
        prism_faces = VGroup()

        for i, face in enumerate(faces):
            tri = Polygon(
                *face,
                fill_opacity=0,
                stroke_color=GREY_N400,
                stroke_width=4,
                # fill_color=GREY_N50,
            )
            prism_faces.add(tri)

        prism_faces.set_flat_stroke(False)
        prism_faces.set_stroke([GREY_N200, GREY_N400]).set_sheen_direction(IN)

        self.set_camera_orientation(
            phi=20 * DEGREES, theta=120 * DEGREES, zoom=1, focal_distance=10000
        )
        # self.add(prism_faces, rotaxis)
        self.add(prism_faces, rotaxis)
        # self.play(FadeIn(prism_faces), FadeIn(rotaxis))

        waterHeight = ValueTracker(0.25)

        def getWater():
            A = np.array([0, 0, -1])
            B = np.array([4, 3, -1])
            C = np.array([0, 3, -1])
            D = np.array([0, 0, waterHeight.get_value()])
            E = np.array([4, 3, waterHeight.get_value()])
            F = np.array([0, 3, waterHeight.get_value()])

            faces = [
                [A, B, C],  # Base
                [D, E, F],
                [A, B, E, D],
                [A, C, F, D],
                [B, C, F, E],
            ]

            # Create polygons for faces
            prism_faces = VGroup()

            for i, face in enumerate(faces):
                tri = Polygon(
                    *face,
                    fill_opacity=0.7,
                    stroke_color=None,
                    stroke_width=0,
                    fill_color=NUMBRIK_COLOR_100,
                )
                prism_faces.add(tri)

            prism_faces.set_flat_stroke(False)

            return prism_faces

        water = always_redraw(getWater)

        # reference
        # self.set_camera_orientation(
        #     phi=60 * DEGREES, theta=-50 * DEGREES, zoom=1, focal_distance=10000
        # )

        # self.add(prism_faces, rotaxis)

        self.set_camera_orientation(phi=60 * DEGREES, theta=-30 * DEGREES, run_time=2)

        # self.play(
        #     Rotate(
        #         prism_faces,
        #         2 * PI,
        #         -Line(np.array([0, 0, -5]), np.array([0, 0, 5])).get_unit_vector(),
        #         ORIGIN,
        #     ),
        #     run_time=3,
        # )
        # self.move_camera(phi=PI / 2)

        self.add(water)

        # self.move_camera(phi=PI / 3, run_time=2)
        # self.wait(1)

        tmpHeight = 0.8
        arrow1 = Arrow(
            (A + C) / 2 + tmpHeight * OUT,
            (A + C) / 2 - 2 * perpendicular_unit_vector(A, C, OUT) + tmpHeight * OUT,
            color=GREY_N400,
            buff=0,
        )

        arrow2 = Arrow(
            (A + B) / 2 + tmpHeight * OUT,
            (A + B) / 2 + 2 * perpendicular_unit_vector(A, B, OUT) + tmpHeight * OUT,
            color=GREY_N400,
            buff=0,
        )

        arrow3 = Arrow(
            (B + C) / 2 + tmpHeight * OUT,
            (B + C) / 2 + 2 * perpendicular_unit_vector(B, C, OUT) + tmpHeight * OUT,
            color=GREY_N400,
            buff=0,
        )

        waterFace = Polygon(
            np.array([0, 0, -0.2]),
            np.array([4, 3, -0.2]),
            np.array([0, 3, -0.2]),
            fill_opacity=0.85,
            stroke_color=GREY_N400,
            stroke_width=4,
            fill_color=NUMBRIK_COLOR_50,
        )

        lengthLabel1 = (
            nMath("F_{side}", color=BLACK)
            .next_to(arrow2, DOWN + RIGHT, buff=0.1)
            .scale(0.85)
            .rotate(np.arctan(3 / 4))
        )

        self.play(
            LaggedStart(
                Create(waterFace),
                GrowArrow(arrow1),
                GrowArrow(arrow2),
                GrowArrow(arrow3),
                FadeIn(lengthLabel1),
                lag_ratio=0.5,
            )
        )

        self.wait(1)
        # self.play(FadeOut(arrow1, arrow2, arrow3, anti_clockwise_arrow))

        # self.play(water.animate.set_opacity(0), prism_faces.animate.set_opacity(0))
        # self.remove(water, prism_faces)
        # self.wait(1)

        # # # Add 3D rotation

        # self.move_camera(
        #     phi=0 * DEGREES,
        #     theta=-90 * DEGREES,
        #     frame_center=1.5 * RIGHT + 2.25 * UP,
        #     run_time=4,
        #     zoom=1.2,
        # )

        self.wait(5)
