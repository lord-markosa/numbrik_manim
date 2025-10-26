from manim import *
from utils import *


class Solve(Scene):
    def construct(self):
        addBackground(self)

        d = ValueTracker(3)
        b = 1.5
        k = 4

        axes = Axes(
            x_range=[-d.get_value(), d.get_value()],
            y_range=[-b, k],
            x_length=2 * d.get_value(),
            y_length=k + b,
            tips=True,
            axis_config={
                "include_ticks": False,
                "include_numbers": False,
                "color": GRAY_D,
                "font_size": 24,
                "tip_shape": StealthTip,
            },
        )

        def getCoeff():
            return k / d.get_value() ** 2

        parabola = always_redraw(
            lambda: axes.plot(
                lambda x: getCoeff() * x**2,
                x_range=[-d.get_value(), d.get_value()],
                color=NUMBRIK_COLOR,
            )
        )

        pole1 = always_redraw(
            lambda: Line(
                axes.c2p(d.get_value(), getCoeff() * d.get_value() ** 2),
                axes.c2p(d.get_value(), -b),
                color=BLACK,
                stroke_width=10,
            )
        )

        pole2 = always_redraw(
            lambda: Line(
                axes.c2p(-d.get_value(), getCoeff() * d.get_value() ** 2),
                axes.c2p(-d.get_value(), -b),
                color=BLACK,
                stroke_width=10,
            )
        )

        ground = Line(
            axes.c2p(-d.get_value() - 1, -b),
            axes.c2p(d.get_value() + 1, -b),
            stroke_width=12,
            color=GREY_B,
        )

        def get_bottomLengthMarker():
            val = lengthMarkerV2(pole2.get_end(), pole1.get_end(), "?", DOWN * 0.6)
            if np.linalg.norm(pole2.get_end() - pole1.get_end()) < 1:
                return VGroup()
            return VGroup(val[0], val[1])

        to_find = always_redraw(lambda: get_bottomLengthMarker())

        to_find_label = Text("?", color=RED_N, font_size=56).next_to(
            (pole2.get_end() + pole1.get_end()) / 2 + 0.6 * DOWN, 0
        )

        labelHighlighter = solidHighlight(self, to_find_label, buff=0.2, animate=False)

        self.add(
            parabola,
            pole1,
            pole2,
            ground,
            to_find,
            to_find_label,
        )

        # things to animate

        heightLeveler = DashedLine(
            pole2.get_start(), pole1.get_start() + 0.8 * RIGHT, color=GREY_N400
        )

        lengthPole = lengthMarkerV2(
            pole1.get_end(), pole1.get_start(), "100", RIGHT * 0.6
        )

        bottomHeight = DoubleArrow(
            axes.c2p(0, 0), axes.c2p(0, -b), color=GREY_N400, buff=0
        )

        bottomHeightLabel = nMath("20").next_to(bottomHeight, LEFT, buff=0.2)

        bottomHeightLeveler = DashedLine(
            axes.c2p(0, 0),
            axes.c2p(-d.get_value(), 0) + LEFT * 0.8,
            color=GREY_N400,
        )

        rem_heightMarker = lengthMarkerV2(
            pole2.get_start(), axes.c2p(-d.get_value(), 0), "80", LEFT * 0.6
        )

        rope_length = nMath("\\text{Rope Length: } 160").to_edge(UP)

        self.play(fadeInTex(rope_length))
        self.wait(1)

        #     lengthPole,
        #     heightLeveler,
        self.play(
            Create(heightLeveler),
            GrowArrow(lengthPole[0]),
            GrowArrow(lengthPole[1]),
            FadeIn(lengthPole[2], scale=1.1),
        )
        self.wait(1)

        #     bottomHeight,
        self.play(GrowArrow(bottomHeight), FadeIn(bottomHeightLabel))
        self.wait(1)

        self.play(to_find_label.animate.scale(1.1), FadeIn(labelHighlighter[0]))
        self.wait(4)

        #     bottomHeightLeveler,
        self.play(
            Create(bottomHeightLeveler),
            GrowArrow(rem_heightMarker[0]),
            GrowArrow(rem_heightMarker[1]),
            FadeIn(rem_heightMarker[2], scale=1.1),
        )
        #     rem_heightMarker,

        self.wait(2)

        self.play(
            d.animate.set_value(0.2),
            Transform(
                to_find_label,
                Text("0", color=RED_N, font_size=56).next_to(
                    (pole2.get_end() + pole1.get_end()) / 2 + 0.6 * DOWN, 0
                ),
            ),
            run_time=3,
        )
        self.wait(2)
