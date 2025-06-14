Supported font:
'Arial', 'Bahnschrift', 'Book Antiqua',
'Bookman Old Style', 'Bradley Hand ITC', 'Calibri', 'Cambria', 'Cambria
Math', 'Candara', 'Cascadia Code', 'Cascadia Mono', 'Century', 'Century
Gothic', 'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Courier
New', 'Cursive', 'Dubai', 'Ebrima', 'Fantasy', 'Franklin Gothic',
'Freestyle Script', 'French Script MT', 'Gabriola', 'Gadugi',
'Garamond', 'Georgia', 'Impact', 'Ink Free', 'Javanese Text', 'Juice
ITC', 'Kristen ITC', 'Leelawadee', 'Leelawadee UI', 'Lucida Console',
'Lucida Handwriting', 'Lucida Sans Unicode', 'MS Gothic', 'MS PGothic',
'MS Reference Sans Serif', 'MS UI Gothic', 'MV Boli', 'Malgun Gothic',
'MesloLGL Nerd Font', 'MesloLGL Nerd Font Mono', 'MesloLGL Nerd Font
Propo', 'MesloLGLDZ Nerd Font', 'MesloLGLDZ Nerd Font Mono',
'MesloLGLDZ Nerd Font Propo', 'MesloLGM Nerd Font', 'MesloLGM Nerd Font
Mono', 'MesloLGM Nerd Font Propo', 'MesloLGMDZ Nerd Font', 'MesloLGMDZ
Nerd Font Mono', 'MesloLGMDZ Nerd Font Propo', 'MesloLGS Nerd Font',
'MesloLGS Nerd Font Mono', 'MesloLGS Nerd Font Propo', 'MesloLGSDZ Nerd
Font', 'MesloLGSDZ Nerd Font Mono', 'MesloLGSDZ Nerd Font Propo',
'Microsoft Himalaya', 'Microsoft JhengHei', 'Microsoft JhengHei UI',
'Microsoft New Tai Lue', 'Microsoft PhagsPa', 'Microsoft Sans Serif',
'Microsoft Tai Le', 'Microsoft Uighur', 'Microsoft YaHei', 'Microsoft
YaHei UI', 'Microsoft Yi Baiti', 'MingLiU-ExtB', 'MingLiU_HKSCS-ExtB',
'Mistral', 'Mongolian Baiti', 'Monospace', 'Monotype Corsiva', 'Myanmar
Text', 'NSimSun', 'Nirmala UI', 'PMingLiU-ExtB', 'Palatino Linotype',
'Papyrus', 'Pristina', 'Sans', 'Sans Serif Collection', 'Sans-Serif',
'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Emoji', 'Segoe UI
Historic', 'Segoe UI Symbol', 'Segoe UI Variable Display', 'Segoe UI
Variable Small', 'Segoe UI Variable Text', 'Serif', 'SimSun',
'SimSun-ExtB', 'SimSun-ExtG', 'Sitka Banner', 'Sitka Display', 'Sitka
Heading', 'Sitka Small', 'Sitka Subheading', 'Sitka Text', 'Sylfaen',
'System-ui', 'Tahoma', 'Tempus Sans ITC', 'Times New Roman', 'Trebuchet
MS', 'Verdana', 'Yu Gothic', 'Yu Gothic UI'

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
