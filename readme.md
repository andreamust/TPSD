# Tonal Pitch Step Distance (TPSD)

In this repository, we propose a Python3 implementation of the Tonal Pitch Space Distance as described
in ([De Haas et al., 2008](https://ismir2008.ismir.net/papers/ISMIR2008_252.pdf))
and ([De Haas et al., 2013](https://link.springer.com/article/10.1007/s13735-013-0036-6))

The content of this repository is in no way attributable to the authors of the above-mentioned papers.

## Usage

The implementation of the Tonal Pitch Step Distance (TPSD) has been split into two main modules that implement the *TPS*
and the *TPSD*, respectively.

All chords and keys are expressed in the Harte notation (as described
in [Harte et al., 2005](https://ismir2005.ismir.net/proceedings/1080.pdf)). For this, we reuse
the [chord-labels library](https://github.com/bzamecnik/chord-labels).

For running all the scripts Python 3.10 is required.

### TPS

TPS implements the Tonal Pitch Space (TPS), as described
in ([Lerdahl F., 2005](https://oxford.universitypressscholarship.com/view/10.1093/acprof:oso/9780195178296.001.0001/acprof-9780195178296))
.

TPS takes in input a chord and a key:

```python
from src.tps import Tps

chord = Tps(chord='C', key='C:maj')
```

Some methods were implemented to compute the different TPS levels, both individually and piled together in the same
list:

```python
from src.tps import Tps

chord = Tps(chord='C', key='C:maj')

diatonic_level = chord.diatonic_level()
triadic_level = chord.triadic_level()
fifth_level = chord.fifth_level()
root_level = chord.root_level()

all_levels = chord.get_levels()
```

Moreover, a method for visualising the extracted levels has been implemented:

```python
chord.show_table()
```

Which plots a table having this shape:\
<img width="328" alt="Screenshot 2022-03-24 at 14 59 01" src="https://user-images.githubusercontent.com/44606182/159932696-c7b6c078-a3e1-4b9b-928c-8ff8f3df9e9c.png">

### TPSD

TPDS provides some methods for comparing different chords. It takes as input two chords and their keys and returns
different distance metrics as implemented in the original TPSD:

```python
from src.tpsd import Tpsd

tpsd = Tpsd(chord_a='C', key_a='C:maj', chord_b='E', key_b='E:maj')

circle_of_fifth_rule = tpsd.circle_fifth_rule()
chord_distance_rule = tpsd.chord_distance_rule()

tpsd_distance = tpsd.distance()
```

Moreover, a method for visualising the TPSD distance has been implemented:

```python
tpsd.plot()
```

Which returns a table representing the two chords stacked, where the non-overlapping tones are highlighted in red:\
<img width="336" alt="Screenshot 2022-03-24 at 14 58 42" src="https://user-images.githubusercontent.com/44606182/159932610-fd22a54a-752b-4076-b2d4-028349553ad3.png">

## Testing

Two different unit tests have been implemented containing all the examples provided in the TPDS papers,
i.e. ([De Haas et al., 2008](https://ismir2008.ismir.net/papers/ISMIR2008_252.pdf))
and ([De Haas et al., 2013](https://link.springer.com/article/10.1007/s13735-013-0036-6))

---

# License

MIT License

Copyright (c) 2022 Andrea Poltronieri, Jacopo de Berardinis

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
