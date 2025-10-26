## Long division

```py
self.play(
            Write(
                MathTex(
                    r"\begin{array}{r}2x^3-7x^2+37x-184\phantom{)}\\x+5{\overline{\smash{\big)}\,2x^4 + 3x^3 + 2x^2 + x + 1\phantom{)}}}\\\underline{-~\phantom{(}(2x^4+10x^3) \ \ \ \ \ \ \ \ \ \ \ \ \ \phantom{-b)}}\\-7x^3+2x^2\ \ \ \ \ \ \ \ \ \ \ \phantom{)}\\ \underline{-~\phantom{()}(-7x^3-35x^2) \ \ \ \ \ \ \ \ \ \ }\\ 37x^2+x \ \ \ \ \ \phantom{)}\\ \underline{-~\phantom{()}(37x^2+185x)} \\ -184x+1\phantom{)} \\ \underline{-~\phantom{()}(-184x-920)} \\ 921\phantom{)}\end{array}",
                )
            ),
            run_time=6,
        )
```

## Curved arrow arcs

```py
centerMarker = CurvedArrow(
    O + LEFT * 2.5 + UP * 2.5,
    O + UP * 0.2,
    color=RED_N,
    angle=-PI / 3,  # Negative angle for opposite curvature
)
```

## Highlight a polygon

```py
tempPolygon = Polygon(proj2, arc_center, B, color=RED_N100, stroke_width=7)

```

## Question statement group

```py
question = (
    VGroup(
        MathTex(
            "\\alpha, \\beta \\text{ are the roots of }",
            "x^2 - 6x + 10 = 0",
            color=BLACK,
        ),
        MathTex(
            "\\text{Find }",
            "\\frac{a_{10} + 10b_8}{a_9}",
            "\\text{ where } a_n = \\alpha^{n} - \\beta^{n}",
            color=BLACK,
        ),
    )
    .arrange(DOWN)
    .to_edge(UP)
)
```

## Options

```py
 options = (
    VGroup(
        MathTex("A) \\ what??", color=BLACK),
        MathTex("B) \\ what??", color=BLACK),
        MathTex("C) \\ what??", color=BLACK),
        MathTex("D) \\ what??", color=BLACK),
    )
    .arrange(DOWN, aligned_edge=LEFT, center=False, buff=0.5)
    .to_edge(UP)
 )

self.play(FadeIn(options))
self.wait(4)

self.play(Create(SurroundingRectangle(options[0], corner_radius=0.18, buff=0.1)))
self.wait(4)
```

## 2 column Options

```py
    options = (
        VGroup(
            VGroup(
                MathTex("A) \\ 6", color=BLACK),
                MathTex("C) \\ 12", color=BLACK),
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
            VGroup(
                MathTex("B) \\ 6\\sqrt{3}", color=BLACK),
                MathTex("D) \\ 12\\sqrt{3}", color=BLACK),
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT),
        )
        .arrange(RIGHT, buff=2)
        .to_edge(UP)
    )

    self.play(FadeIn(options))
    self.wait(5)

    self.wait(1)
    self.play(
        Create(SurroundingRectangle(options[0][1], corner_radius=0.1, buff=0.1))
    )
    self.wait(4)
```

## AXIS

```py
def getAxis(x_range=[-5, 5, 1], y_range=[-5, 5, 1], x_length=6, y_length=6):
    return Axes(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        tips=True,
        axis_config={
            "include_ticks": False,
            "include_numbers": False,
            "color": GRAY_D,
            "font_size": 24,
            "tip_shape": StealthTip,
        },
    )
```

## Highlight

```py
    SurroundingRectangle(part, corner_radius=0.1, buff=0.1, wait_time=1, color=YELLOW)
```

```
 eqn = MathTex(
            "\\mathbf{a^2 + b^2 = c^2}",
            color=BLACK,
            tex_template=TexFontTemplates.comic_sans,
        ).scale(3)
```

## Gradient colors

```py
    square_a = (
        Square(
            a,
            fill_opacity=1,
        )
        .set_color_by_gradient([GREEN_N100, WHITE])
        .set_stroke(BLACK)
        .move_to(Line(B, C).get_center(), aligned_edge=RIGHT)
        .set_sheen_direction(UP+RIGHT)
    )
```

## Properties of line

line.get_angle() ==> slope angle
TangentLine(curve, length, alpha)
Example:
```py
TangentLine(
    exp,
    length=6,
    alpha=get_alpha(),
    stroke_color=[GREY_N200, GREY_N800],
    stroke_width=6,
)
```

## Properties of axis

axes.c2p(X, Y) => takes a point(X, Y) wrt axes and produces an outside point (POINT)
axes.p2c(POINT) => takes an outside point (POINT) and produces the coordinates (X, Y)
axes.x_axis.get_projection(POINT) => gives the POINT (outside) on x-axis
curve.point_from_proportion(alpha) alpha is used with TangentLine(x)