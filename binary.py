from manim import *
from utils import *
import numpy as np
from PIL import Image
from collections import Counter


class Binary(Scene):
    def construct(self):
        # self.binaryDecimalConversion()
        # self.binaryCounter()
        # self.poisonBottle2()
        self.limitsExample()

    def poisonBottle(self):
        wineBottle = ImageMobject("assets/wine_bottle.webp").scale(0.5).to_edge(LEFT)
        bottles = [wineBottle]
        labels = [Text("0").next_to(wineBottle, DOWN)]
        for i in range(7):
            bottles.append(wineBottle.copy().next_to(bottles[i], RIGHT, buff=0.5))
            labels.append(Text(str(i + 1)).next_to(bottles[i + 1], DOWN))

        self.play(FadeIn(*bottles))

        for i in range(8):
            self.play(Write(labels[i]), run_time=0.25)

        self.wait(4)

    def poisonBottle2(self):
        wineBottle = ImageMobject("assets/wine_bottle.webp").scale(0.5)
        bottleLabel = MathTex("(581)_{10}").next_to(wineBottle, DOWN)
        bottleLabel2 = MathTex("(1001000101)_2").next_to(bottleLabel, DOWN)
        circles = VGroup(*[Circle(0.5).copy() for _ in range(10)]).arrange(RIGHT)
        circles.to_edge(UP)
        labels = VGroup(*[Text("P" + str(i)).scale(0.5) for i in range(10)])
        for circle, label in zip(circles, labels):
            label.move_to(circle)

        self.play(Create(circles), Create(labels), run_time=3)
        self.play(FadeIn(wineBottle), Write(bottleLabel), run_time=2)
        self.play(Write(bottleLabel2))

        self.wait(2)

        for i, circle, label in zip(range(10), circles, labels):
            self.play(bottleLabel2[0][i + 1].animate.set_color(GREEN))
            binSeq = "1001000101"

            if binSeq[i] == "1":
                self.play(
                    circle.animate.set_color(GREEN_N100),
                    label.animate.set_color(GREEN_N100),
                )
            self.wait(0.5)
            self.play(bottleLabel2[0][i + 1].animate.set_color(WHITE))

        self.wait(4)

    def binaryCounter(self):
        # Initial binary number
        binary_text = MathTex("0").scale(2)
        decimalText = MathTex("0").next_to(binary_text, UP, buff=0.5)
        self.play(Write(binary_text), Write(decimalText))
        self.wait(0.5)

        # Update binary numbers from 1 to 10
        for i in range(1, 17):
            newText = MathTex(bin(i)[2:]).scale(2)
            newText.move_to(binary_text)
            newDecimalText = MathTex(str(i)).move_to(decimalText)
            self.play(
                Transform(binary_text, newText),
                Transform(decimalText, newDecimalText),
                run_time=0.5,
            )
            self.wait(0.5)

        self.wait(1)

    def limitsExample(self):
        animateTextSeq(
            self,
            [
                MathTex("10 \\implies 1024"),
                MathTex("20 \\implies 1.04 \\times 10^6"),
                MathTex("40 \\implies 1.09 \\times 10^{12}"),
            ],
        )
        self.wait(4)

    def binaryDecimalConversion(self):
        # Title
        title = (
            Text("Binary to Decimal Conversion", color=NUMBRIK_COLOR)
            .scale(0.8)
            .to_edge(UP)
        )
        self.play(Write(title))
        self.wait(1)

        animateTextSeq(
            self,
            [
                MathTex("1011_2 = ?_{10}", color=NUMBRIK_COLOR),
                MathTex(
                    "1 \\times 2^3 + 0 \\times 2^2 + 1 \\times 2^1 + 1 \\times 2^0"
                ),
                MathTex("8 + 0 + 2 + 1 = 11_{10}"),
            ],
            shift_val=DOWN,
        )

        clearScreen(self, 2)

        title2 = Text("Decimal to Binary Conversion").scale(0.8).to_edge(UP)
        self.play(Write(title2))

        self.wait(1)

        animateTextSeq(
            self,
            [
                MathTex("13_{10} = ?_2", color=NUMBRIK_COLOR),
                MathTex("13 \\div 2 = 6, \\text{ remainder } = 1"),
                MathTex("6 \\div 2 = 3, \\text{ remainder } = 0"),
                MathTex("3 \\div 2 = 1, \\text{ remainder } = 1"),
                MathTex("1 \\div 2 = 0, \\text{ remainder } = 1"),
                MathTex("\\Rightarrow 13_{10} = 1101_2"),
            ],
            next_reference=title2,
        )

        self.wait(3)


class PixelZoom(MovingCameraScene):
    def construct(self):
        self.pixelateFirst()

    def pixelateLater(self):
        # Load image from local storage
        image_path = "assets/complex_colors.webp"

        pureImg = ImageMobject(image_path)
        self.play(FadeIn(pureImg))

        # Zoom into ORIGIN
        self.play(self.camera.frame.animate.scale(0.1).move_to(ORIGIN), run_time=2)
        self.wait(2)

        # Zoom out back to the full image
        self.play(self.camera.frame.animate.scale(10), run_time=2)
        self.wait(2)

        pixImg = ImageMobject(pixelate_image(image_path, 10))

        self.play(Transform(pureImg, pixImg), run_time=2)
        self.wait(1)

        # Zoom into ORIGIN
        self.play(self.camera.frame.animate.scale(0.1).move_to(ORIGIN), run_time=2)
        self.wait(2)

        # Zoom out back to the full image
        self.play(self.camera.frame.animate.scale(10), run_time=2)
        self.wait(4)

    def pixelateFirst(self):
        # Load image from local storage
        image_path = "assets/BO.jpg"

        pureImg = ImageMobject(image_path).scale(0.25)

        pixImg1 = ImageMobject(pixelate_image(image_path, 120)).scale(0.25)
        pixImg2 = ImageMobject(pixelate_image(image_path, 80)).scale(0.25)

        self.play(FadeIn(pixImg1))
        self.wait(2)
        self.play(FadeIn(pixImg2))
        self.wait(2)
        self.play(FadeIn(pureImg))
        self.wait(2)


def pixelate_image(image_path, pixel_size=20):
    # Load the image
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixels = np.array(image)
    height, width, _ = pixels.shape

    # Create an output image
    output_pixels = np.zeros_like(pixels)

    for i in range(0, height, pixel_size):
        for j in range(0, width, pixel_size):
            # Extract block of pixels
            block = pixels[
                i : min(i + pixel_size, height), j : min(j + pixel_size, width)
            ]

            # Flatten the block and count occurrences of colors
            flat_block = block.reshape(-1, 3)
            most_common_color = Counter(map(tuple, flat_block)).most_common(1)[0][0]

            # Assign the most common color to the block in output image
            output_pixels[
                i : min(i + pixel_size, height), j : min(j + pixel_size, width)
            ] = most_common_color

    # Convert back to image and save
    # output_image = Image.fromarray(output_pixels)
    return output_pixels


class SoundConversion(Scene):
    def construct(self):
        x_range = [-140, 140]
        plane = (
            Axes(
                x_range,
                x_length=10,
                y_range=[-10, 10],
                y_length=7,
            )
            .add_coordinates(None)
            .shift(LEFT)
        )

        controlledRandom = []
        for i in range(10):
            controlledRandom.append(2 * np.random.rand())

        getControlledRandom = lambda x: controlledRandom[
            int(np.absolute(np.floor(x) % 10))
        ]

        def waveFunc(x):
            val = (
                np.sin(x / 2)
                + 2 * np.sin(x / 5)
                + 4 * np.sin(x / 7)
                + 2 * np.sin(x / 3)
                + 2 * getControlledRandom(x) * np.sin(x / 2)
            )

            return val

        wave = plane.plot(waveFunc, x_range).set_color(NUMBRIK_COLOR)

        # Create a stack of squares
        squares = VGroup(*[Square(side_length=0.5).set_color(WHITE) for _ in range(12)])
        squares.arrange(DOWN, buff=0.1).next_to(plane, RIGHT, buff=1)

        # Add labels to the squares
        labels = VGroup(*[Text(str(i)).scale(0.5) for i in range(12)])
        for square, label in zip(squares, labels):
            label.move_to(square)

        # Group squares and labels together
        stack = VGroup(squares, labels)

        # self.play(Create(plane))
        # self.play(Create(x_axis))
        self.play(Create(wave), run_time=10)
        # self.play(FadeIn(stack))

        # # Project the segment onto one of the boxes
        # d = 0.5

        # for i in range(10):
        #     x_0 = x_range[1] * np.random.rand()
        #     x_end = x_range[1] + 30

        #     # Highlight the segment of the wave from x=x_0 to x=x_0+d
        #     x1 = x_0
        #     x2 = x_0 + d
        #     y1 = waveFunc(x1)
        #     y2 = waveFunc(x2)
        #     segment = plane.plot(waveFunc, x_range=[x1, x2], color=YELLOW)
        #     self.play(Create(segment), run_time=2)
        #     projection_line1 = DashedLine(
        #         start=plane.c2p(x1, y1),
        #         end=plane.c2p(x_end, y1),
        #         color=YELLOW,
        #     )
        #     projection_line2 = DashedLine(
        #         start=plane.c2p(x2, y2),
        #         end=plane.c2p(x_end, y2),
        #         color=YELLOW,
        #     )

        #     y_avg = (y1 + y2) / 2
        #     N = int((y_avg + 10) / (20 / 12))

        #     self.play(Create(projection_line1), run_time=1)
        #     self.play(Create(projection_line2), run_time=1)
        #     self.play(
        #         squares[11 - N].animate.set_color(GREEN_N100),
        #         labels[11 - N].animate.set_color(GREEN_N100),
        #     )
        #     self.wait(2)
        #     self.play(
        #         FadeOut(segment, projection_line1, projection_line2),
        #         squares[11 - N].animate.set_color(WHITE),
        #         labels[11 - N].animate.set_color(WHITE),
        #     )

        self.wait(2)
