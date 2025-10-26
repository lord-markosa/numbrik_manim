from manim import *


# Constants

TITLE_TEXT_POSITION = ORIGIN + UP
NUMBRIK_COLOR30 = ManimColor("#c5d7ff")
NUMBRIK_COLOR40 = ManimColor("#aabbfc")
NUMBRIK_COLOR_50 = ManimColor("#8bb1ff")
NUMBRIK_COLOR_100 = ManimColor("#6196ff")
NUMBRIK_COLOR_200 = ManimColor("#3075ff")
NUMBRIK_COLOR = ManimColor("#1e66f7")
NUMBRIK_COLOR_DARK = ManimColor("#004ce5")

GREEN_NDARK = ManimColor("#174900")
GREEN_N1000 = ManimColor("#298100")
GREEN_N200 = ManimColor("#4ECD14")
GREEN_N100 = ManimColor("#9dfc70")
GREEN_N50 = ManimColor("#b5ff92")
GREEN_N10 = ManimColor("#e1ffd3")

RED_N = ManimColor("#FF0000")
RED_N50 = ManimColor("#ff8c8c")
RED_N100 = ManimColor("#ff4f4f")
RED_N500 = ManimColor("#e00f0f")
RED_N900 = ManimColor("#ba000071")
BLUE_N1000 = ManimColor("#000131")
YELLOW_N40 = ManimColor("#fffd80")
YELLOW_N50 = ManimColor("#f8ff6f")
GREY_N50 = ManimColor("#C7C7C7")
GREY_N100 = ManimColor("#AAAAAA")
GREY_N200 = ManimColor("#949393")
GREY_N300 = ManimColor("#828282")
GREY_N400 = ManimColor("#5E5E5E")
GREY_N500 = ManimColor("#474747")
GREY_N800 = ManimColor("#3C3C3C")
VIOLET_N1000 = ManimColor("#29116f")
VIOLET_N100 = ManimColor("#684dba")
VIOLET_N50 = ManimColor("#9b7aff")
BLUE_N_LIGHT = ManimColor("#615DA0")
BLUE_N1000 = ManimColor("#040043")

ORANGE_N50 = ManimColor("#FFB378")
ORANGE_N100 = ManimColor("#FFA260")
ORANGE_N400 = ManimColor("#FF7F23")

backgroundImage = ImageMobject("assets/canvas.png")


# Utility Functions


def displayTitle(self, title):
    # Title
    title = Text(title, color=NUMBRIK_COLOR).scale(1.2).move_to(TITLE_TEXT_POSITION)
    self.play(Write(title))
    self.wait(0.5)
    self.play(FadeOut(title), run_time=0.5)
    self.wait(1)


def animateTextSeq(
    self,
    lines,
    shift_val=0,
    next_reference=0,
    wait_time=1,
    iterative_callback=None,
    line_buffer=0.5,
    next_buff=0.75,
    run_time=1.5,
):
    if len(lines) > 5:
        lines[0].move_to(TITLE_TEXT_POSITION + 2 * UP)
    elif len(lines) >= 3:
        lines[0].move_to(TITLE_TEXT_POSITION + UP)
    else:
        lines[0].move_to(TITLE_TEXT_POSITION)

    lines[0].shift(shift_val)

    if next_reference != 0:
        lines[0].next_to(next_reference, DOWN, buff=next_buff)

    for i, line in enumerate(lines):
        if i > 0:
            line.next_to(lines[i - 1], DOWN, buff=line_buffer)
        self.play(Write(line), run_time=run_time)
        self.wait(wait_time)
        iterative_callback(lines[i]) if iterative_callback is not None else None

    return lines


def clearScreen(self, wait_time=4):
    self.wait(wait_time)
    # Only fade out mobjects that are not the background image
    self.play(
        *[FadeOut(mob) for mob in self.mobjects if mob is not backgroundImage],
        run_time=1.5,
    )
    self.wait(1)


def solidHighlight(
    self,
    part,
    buff=0.05,
    corner_radius=0.12,
    wait_time=1,
    color=YELLOW,
    animate=True,
    unhighlight=True,
):
    # Accept a single part or a list of parts
    if not isinstance(part, (list, tuple)):
        parts = [part]
    else:
        parts = part

    highlights = [
        BackgroundRectangle(
            p,
            buff=buff,
            corner_radius=corner_radius,
            color=color,
            fill_opacity=1,
            z_index=-10,
        )
        for p in parts
    ]

    if animate:
        self.play(FadeIn(highlight) for highlight in highlights)
        self.wait(wait_time)
        if unhighlight:
            self.play(highlight.animate.set_opacity(0) for highlight in highlights)
            self.wait(1)

    return highlights


def highlight(
    self,
    parts,
    buff=0.1,
    wait_time=1,
    color=YELLOW,
    unhighlight=True,
    animate=True,
    corner_radius=0.1,
    run_time=1.5,
):
    # Accept a single part or a list of parts
    if not isinstance(parts, (list, tuple)):
        parts = [parts]
    highlights = [
        SurroundingRectangle(part, corner_radius=corner_radius, buff=buff, color=color)
        for part in parts
    ]

    if animate:
        self.play(Create(highlight, run_time=run_time) for highlight in highlights)
        if wait_time != 0:
            self.wait(wait_time)

        if unhighlight:
            self.play(FadeOut(VGroup(*highlights)))

    return highlights


def nText(
    str, font_size=32, color=NUMBRIK_COLOR, gradient_color=None, sheen_direction=RIGHT
):
    txt = Text(str, font_size=font_size, font="Comic Sans MS", color=color)
    if gradient_color is not None:
        txt.set_color_by_gradient(*gradient_color).set_sheen_direction(sheen_direction)
    return txt


def nMath(*args, color=NUMBRIK_COLOR, gradient_color=None, sheen_direction=RIGHT):
    math_tex = MathTex(
        *args,
        color=color,
        tex_template=TexFontTemplates.comic_sans,
    )
    if gradient_color is not None:
        math_tex.set_color_by_gradient(gradient_color).set_sheen_direction(
            sheen_direction
        )
    return math_tex


def createLineMarks(line, mark_length=0.2, gap=0.08, themeColor=GREY_N500):
    # Get start and end points of the line
    start, end = line.get_start(), line.get_end()
    center = (start + end) / 2
    direction = end - start
    direction = direction / np.linalg.norm(direction)

    # Perpendicular direction in 2D
    perp = np.array([-direction[1], direction[0], 0])
    perp = perp / np.linalg.norm(perp)

    # Offset for the two marks
    offset = direction * gap / 2

    # Compute positions for the two marks
    mark1_center = center + offset
    mark2_center = center - offset

    # Create the two marks
    mark1 = Line(
        mark1_center - perp * mark_length / 2,
        mark1_center + perp * mark_length / 2,
        color=themeColor,
        stroke_width=4,
    )
    mark2 = Line(
        mark2_center - perp * mark_length / 2,
        mark2_center + perp * mark_length / 2,
        color=themeColor,
        stroke_width=4,
    )

    return VGroup(mark1, mark2)


def getTriangularRegion(
    A,
    B,
    C,
    color=YELLOW,
):
    triangleABC_area = Polygon(
        A, B, C, color=color, fill_opacity=1, stroke_width=0, z_index=-10
    )
    return triangleABC_area


def lengthMarker(P1, P2, label, scale=1, buff=0):
    length_marker = DoubleArrow(
        P1,
        P2,
        color=GREY_N400,
        stroke_width=4,
        buff=buff,
        tip_length=DEFAULT_ARROW_TIP_LENGTH * scale,
    ).set_z_index(-20)

    length_label = nMath(label).next_to(length_marker, 0).scale(scale)

    length_label_background = BackgroundRectangle(
        length_label, color=WHITE, buff=0.1, fill_opacity=1
    ).set_z_index(-10)

    return length_marker, length_label, length_label_background


def lengthMarkerV2(P1, P2, label, shift=0.5 * DOWN, scale=1, buff=0):
    length_label = nMath(label).move_to((P1 + P2) / 2).scale(scale).shift(shift)

    # Normalize the shift vector
    shift_dir = shift / np.linalg.norm(shift) if np.linalg.norm(shift) != 0 else DOWN

    # Perpendicular direction to shift_dir in 2D
    perp_dir = np.array([-shift_dir[1], shift_dir[0], 0])

    # Arrow 1: from label edge in shift direction to P2+shift
    print(perp_dir)
    length_marker1 = Arrow(
        length_label.get_edge_center(perp_dir) + 0.2 * perp_dir,
        P2 + shift,
        color=GREY_N400,
        stroke_width=4,
        buff=buff,
        tip_length=DEFAULT_ARROW_TIP_LENGTH * scale,
    )

    # Arrow 2: from label edge in -shift direction to P1+shift
    length_marker2 = Arrow(
        length_label.get_edge_center(-perp_dir) - 0.2 * perp_dir,
        P1 + shift,
        color=GREY_N400,
        stroke_width=4,
        buff=buff,
        tip_length=DEFAULT_ARROW_TIP_LENGTH * scale,
    )

    return VGroup(length_marker1, length_marker2, length_label)


def lengthMarkerV3(
    P1,
    P2,
    label,
    shift=0.5 * DOWN,
    scale=1,
    buff=0,
    centerDist=0.3,
    tip_length=DEFAULT_ARROW_TIP_LENGTH,
    color=GREY_N400,
    labelColor=NUMBRIK_COLOR,
):
    length_label = (
        nMath(label, color=labelColor).move_to((P1 + P2) / 2).scale(scale).shift(shift)
    )

    # Normalize the shift vector
    shift_dir = shift / np.linalg.norm(shift) if np.linalg.norm(shift) != 0 else DOWN

    # Perpendicular direction to shift_dir in 2D
    perp_dir = np.array([-shift_dir[1], shift_dir[0], 0])

    # Arrow 1: from label edge in shift direction to P2+shift
    length_marker1 = Arrow(
        length_label.get_center() + centerDist * perp_dir,
        P2 + shift,
        color=color,
        stroke_width=4,
        buff=buff,
        tip_length=tip_length,
    )

    # Arrow 2: from label edge in -shift direction to P1+shift
    length_marker2 = Arrow(
        length_label.get_center() - centerDist * perp_dir,
        P1 + shift,
        color=color,
        stroke_width=4,
        buff=buff,
        tip_length=tip_length,
    )

    return VGroup(length_marker1, length_marker2, length_label)


def radiusMarker(P1, P2, label, scale=1, buff=0):
    length_marker = Arrow(
        P1,
        P2,
        color=GREY_N400,
        stroke_width=4,
        buff=buff,
        tip_length=DEFAULT_ARROW_TIP_LENGTH * scale,
    ).set_z_index(-20)

    length_label = nMath(label).next_to(length_marker, 0).scale(scale)

    length_label_background = BackgroundRectangle(
        length_label, color=WHITE, buff=0.1, fill_opacity=1
    ).set_z_index(-10)

    return length_marker, length_label, length_label_background


def fadeInText(text):
    return LaggedStart(*[FadeIn(char) for char in text], lag_ratio=0.05)


def fadeInTex(text):
    return LaggedStart(
        *[FadeIn(char) for line in text for char in line], lag_ratio=0.05
    )


def addBackground(self):
    backgroundImage.scale_to_fit_height(config.frame_height)
    backgroundImage.scale_to_fit_width(config.frame_width)
    backgroundImage.z_index = -1000
    self.add(backgroundImage)


def getAxis(
    x_range=[-5, 5, 1], y_range=[-5, 5, 1], x_length=6, y_length=6, color=GREY_D
):
    return Axes(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        tips=True,
        axis_config={
            "include_ticks": False,
            "include_numbers": False,
            "color": color,
            "font_size": 24,
            "tip_shape": StealthTip,
        },
    )


def getRightAngle(A, B, C, color=GREY_N500, length=0.5, stroke_width=4):
    return RightAngle(
        Line(B, A), Line(B, C), length=length, color=color, stroke_width=stroke_width
    )


def getAngle(A, B, C, color=BLACK, radius=0.5):
    return Angle(Line(B, A), Line(B, C), radius=radius, color=color)


def get_formatted_value(value):
    if abs(value - round(value)) < 1e-6:
        return f"{int(round(value))}"
    else:
        return f"{value:.2f}"


def shift_scene_up(self, shift_val=UP):
    self.play(mob.animate.shift(shift_val) for mob in self.mobjects)


def perpendicular_unit_vector(point1, point2, vector):
    """
    Calculate the unit vector perpendicular to the line joining point1 and point2
    and another given vector using the cross product.

    Args:
        point1 (array-like): Coordinates of the first point [x1, y1, z1].
        point2 (array-like): Coordinates of the second point [x2, y2, z2].
        vector (array-like): The other vector [vx, vy, vz].

    Returns:
        np.ndarray: The unit vector perpendicular to both the line vector and the given vector.
    """
    # Convert inputs to numpy arrays
    p1 = np.array(point1, dtype=float)
    p2 = np.array(point2, dtype=float)
    v = np.array(vector, dtype=float)

    # Compute the line vector
    line_vec = p2 - p1

    # Compute the cross product
    cross_prod = np.cross(line_vec, v)

    # Handle the case where the cross product is zero
    norm = np.linalg.norm(cross_prod)
    if norm == 0:
        raise ValueError(
            "The vectors are parallel or one is zero, cross product is zero."
        )

    # Normalize to get unit vector
    unit_vector = cross_prod / norm

    return unit_vector


def getRegion(*pts, color=YELLOW, gradient_color=None, sheen_direction):
    region = Polygon(*pts, color=color, fill_opacity=1, stroke_width=0, z_index=-10)

    if gradient_color is not None:
        region.set_color_by_gradient(gradient_color).set_sheen_direction(
            sheen_direction
        )
    return region


def createMidPointMarks(line):
    return VGroup(
        createLineMarks(
            Line(line.get_start(), line.get_center()), themeColor=NUMBRIK_COLOR
        ),
        createLineMarks(
            Line(line.get_center(), line.get_end()), themeColor=NUMBRIK_COLOR
        ),
    )


def createParallelArrows(direction, start, end, length, num, color):
    dx = 1 / num * (end - start)

    return VGroup(
        *[
            Arrow(
                start + dx * i,
                start + direction * length + dx * i,
                color=color,
                buff=0,
                stroke_width=6,
            )
            for i in range(num + 1)
        ]
    )


def getPointer(A, B=ORIGIN, color=RED_N100):
    return Arrow(A, B, color=color, buff=0)
