from manim import *


# Multiline text with Tex and comma separated list.
class LaggedFadeMultiline(Scene):
    def construct(self):
        text = Tex(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "\\\\ Phasellus in lacus tristique, \\\\interdum turpis sit amet, bibendum felis.",
            "Suspendisse mattis arcu quis leo tempus condimentum. Sed luctus turpis mauris,",
            color=BLACK,
            font_size = 80
        )

        self.play(
            LaggedStart(
                *[FadeIn(char) for line in text for char in line], lag_ratio=0.05
            ),
        )
        self.wait(1)
        self.play(FadeOut(text))
