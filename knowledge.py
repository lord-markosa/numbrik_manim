from manim import *
from utils import *


def getText(text, color=WHITE):
    return Text(text, font_size=34, font="Times New Roman", color=color)


class CollatzConjecture(Scene):
    def collatz_sequence(self, n):
        sequence = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            sequence.append(n)
        return sequence

    def getNode(self, str, color, radius=0.5):
        node = Circle(radius, color).move_to(LEFT * 2)
        label = getText(str).move_to(node.get_center())
        return VGroup(node, label)

    def displayNode(self, node):
        self.play(Create(node[0]), Write(node[1]))

    def construct(self):
        # Node display
        node_n = self.getNode("N", BLUE, 0.75).move_to(TITLE_TEXT_POSITION + UP)

        node_odd = self.getNode("3N+1", GREEN, 0.75).next_to(
            node_n, 2 * DOWN + 0.5 * LEFT, buff=1
        )

        node_even = self.getNode("N/2", ORANGE, 0.75).next_to(
            node_n, 2 * DOWN + 0.5 * RIGHT, buff=1
        )

        arrow_odd = Arrow(start=node_n, end=node_odd, buff=0.1, stroke_width=3)
        arrow_even = Arrow(start=node_n, end=node_even, buff=0.1, stroke_width=3)

        cond_odd = getText("Odd").next_to(node_n, LEFT + DOWN, buff=0.5)
        cond_even = getText("Even").next_to(node_n, RIGHT + DOWN, buff=0.5)

        self.displayNode(node_n)
        self.play(GrowArrow(arrow_odd), Write(cond_odd))
        self.displayNode(node_odd)
        self.play(GrowArrow(arrow_even), Write(cond_even))
        self.displayNode(node_even)
        self.wait(2)

        # clearScreen(self)

        # Pick number 11 and compute sequence
        # number = 37
        # sequence = self.collatz_sequence(number)

        # numText = getText("Let N = 13").scale(1.5).shift(UP)
        # self.play(Write(numText))

        # numText2 = getText("B")
        # self.play(Transform(numText, numText2))
        # n1 = self.getNode("F1", BLUE, 0.5)
        # n2 = self.getNode("F2", BLUE, 0.5)
        # n3 = self.getNode("F3", BLUE, 0.5)
        # arrow1 = Arrow(n1, n2, buff=0.1, stroke_width=3)
        # arrow2 = Arrow(n2, n3, buff=0.1, stroke_width=3)
        # formula1 = getText("3N+1", GREEN)
        # formula2 = getText("N/2", ORANGE)

        # for i, num in enumerate(sequence):
        #     if i == 0:
        #         n1 = self.getNode(str(num), BLUE, 0.5).move_to(
        #             TITLE_TEXT_POSITION + 2 * UP
        #         )
        #         self.displayNode(n1)
        #         continue

        #     if i % 2 == 1:
        #         # reset logic
        #         if i > 2:
        #             self.play(
        #                 LaggedStart(
        #                     FadeOut(n1, n2, arrow1, arrow2, formula1, formula2),
        #                     n3.animate.move_to(TITLE_TEXT_POSITION + 2 * UP),
        #                     lag_ratio=0.2,
        #                 ),
        #                 run_time=0.75,
        #             )
        #             n1 = n3

        #         n2 = self.getNode(str(num), GREEN, 0.5).move_to(TITLE_TEXT_POSITION)
        #         arrow1 = Arrow(n1, n2, buff=0.1, stroke_width=3)
        #         formula1 = getText("3N+1" if (sequence[i - 1] & 1) else "N/2").next_to(
        #             arrow1, RIGHT, buff=0.5
        #         )
        #         self.play(Write(formula1), GrowArrow(arrow1), run_time=0.5)
        #         self.displayNode(n2)

        #     else:
        #         n3 = self.getNode(str(num), ORANGE, 0.5).move_to(
        #             TITLE_TEXT_POSITION + 2 * DOWN
        #         )

        #         arrow2 = Arrow(n2, n3, buff=0.1, stroke_width=3)
        #         formula2 = getText("3N+1" if (sequence[i - 1] & 1) else "N/2").next_to(
        #             arrow2, RIGHT, buff=0.5
        #         )
        #         self.play(Write(formula2), GrowArrow(arrow2), run_time=0.5)
        #         self.displayNode(n3)

        self.wait(2)
