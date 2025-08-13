from manim import *


# Constants

TITLE_TEXT_POSITION = ORIGIN + UP
NUMBRIK_COLOR_50 = ManimColor("#8bb1ff")
NUMBRIK_COLOR = ManimColor("#1e66f7")
GREEN_N200 = ManimColor("#49B618")
GREEN_N100 = ManimColor("#9dfc70")
RED_N = ManimColor("#FF0000")
RED_N50 = ManimColor("#ff8c8c")
RED_N100 = ManimColor("#ff4f4f")
RED_N900 = ManimColor("#ba000071")
BLUE_N1000 = ManimColor("#000131")
YELLOW_N40 = ManimColor("#f0f682")
YELLOW_N50 = ManimColor("#f8ff6f")
GREY_N400 = ManimColor("#5E5E5E")
GREY_N500 = ManimColor("#474747")
GREY_N800 = ManimColor("#3C3C3C")


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
    self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)


def solidHighlight(self, part, buff=0.05, wait_time=1):
    # Accept a single part or a list of parts
    if not isinstance(part, (list, tuple)):
        parts = [part]
    else:
        parts = part

    highlights = [
        BackgroundRectangle(
            p, buff=buff, corner_radius=0.12, color=YELLOW, fill_opacity=1, z_index=-10
        )
        for p in parts
    ]

    self.play(FadeIn(highlight) for highlight in highlights)
    self.wait(wait_time)
    self.play(highlight.animate.set_opacity(0) for highlight in highlights)
    self.wait(1)


def highlight(self, parts, buff=0.1, wait_time=1, color=YELLOW, unhighlight=True):
    # Accept a single part or a list of parts
    if not isinstance(parts, (list, tuple)):
        parts = [parts]
    highlights = [
        SurroundingRectangle(part, corner_radius=0.1, buff=buff, color=color)
        for part in parts
    ]
    self.play(Create(highlight) for highlight in highlights)
    if wait_time != 0:
        self.wait(wait_time)

    if unhighlight:
        self.play(FadeOut(VGroup(*highlights)))


def nText(str):
    return Text(str, font_size=32, font="Comic Sans MS", color=NUMBRIK_COLOR)


def nMath(*args):
    return MathTex(
        *args,
        color=NUMBRIK_COLOR,
        tex_template=TexFontTemplates.comic_sans,
    )


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


def getTriangularRegion(A, B, C, color=YELLOW):
    triangleABC_area = Polygon(A, B, C, color=color, fill_opacity=1, stroke_width=0)
    triangleABC_area.z_index = -10
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


def fadeInText(text):
    return LaggedStart(*[FadeIn(char) for char in text], lag_ratio=0.05)


def fadeInTex(text):
    return LaggedStart(
        *[FadeIn(char) for line in text for char in line], lag_ratio=0.05
    )
