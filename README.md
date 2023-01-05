# Python gyakorlás

##### Informatika képzési terület a felsőoktatásban

|          megnevezés          | végzettség |   idő   |
|-----------------------------------|-------|---------|
| Programtervező informatikus FOKSZ |       | 4 félév |
| Mérnökinformatikus FOKSZ          |       | 4 félév |
| Gazdaságinformatikus FOKSZ        |       | 4 félév |
| Üzemmérnök-informatikus szak      | BProf | 6 félév |
| Programtervező informatikus szak  | BSc   | 6 félév |
| Mérnökinformatikus szak           | BSc   | 7 félév |
| Gazdaságinformatikus szak         | BSc   | 7 félév |
| Programtervező informatikus szak  | MSc   | 4 félév |
| Mérnökinformatikus szak           | MSc   | 4 félév |
| Gazdaságinformatikus szak         | MSc   | 4 félév |
| Autonómrendszer-informatikus szak | MSc   | 4 félév |
| Orvosi biotechnológia szak        | MSc   | 4 félév |

rövidítések:
- FOKSZ: felsőoktatási szakképzés (felsőfokú szakképzettség)
- BSc: bachelor of science (alapfokozat)
- BProf: bachelor of profession (alapfokozat)
- MSc: master of science (mesterfokozat)

Forrás: [felvi.hu - szakleírások - informatika képzési terület ](https://www.felvi.hu/felveteli/szakok_kepzesek/szakleirasok/!Szakleirasok/index.php/szakterulet/4) (2023.01.04.)

##### Oktatási anyagok, magyarázatok és feladatok:

* [BME - InfoPy - BProf ProgAlap](https://infopy.eet.bme.hu/)
* [Python3 cheatsheet](https://infopy.eet.bme.hu/konyvpuska/python3-puska.pdf)
* [Common Gotchas](https://docs.python-guide.org/writing/gotchas/)

##### Specifikáció, leggyakrabban használt csomagok és ajánlások:

* [The Python Standard Library](https://docs.python.org/3/library)
* [PEP 20 – The Zen of Python](https://peps.python.org/pep-0020/)  
  `import this`
* [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
* [NumPy](https://numpy.org/doc/stable/reference/index.html)
* [SymPy](https://docs.sympy.org/latest/reference/index.html)

##### Fájlok és csomagok

A fájl első sorába shebang-et helyezhetünk el:
`#!/usr/bin/env python3`

Beállíthatjuk a futtatási jogot, majd futtatjuk a kódot:
```bash
$ chmod u+x mycode.py
$ ./mycode.py
```

Csomagok telepítése:
`$ pip install matplotlib`

Importálás:
```python
from sys import argv as args
import matplotlib.pyplot as plt
```

