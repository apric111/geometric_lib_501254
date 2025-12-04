# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Content
The project contains four python files named circle.py, square.py, rectangle.py and triangle.py. 
Each of the files contains two functions: one for finding the area and one for finding the perimeter 
of the shape, which is specified in the file name.
The mathematical library is used in functions to determine the constant value of pi (15 decimal places).

# Description of functions
## Circle
### `area(r)`
The function for finding the area of a circle takes as an argument a single float  value r - the radius of the circle and returns math.pi * r * r (float) - the area of the circle.
Examlple of a call:

- `area(5)` returns 78.53981633974483, since pi * 5 * 5 = 78.53981633974483
- `area(20)` returns 1256.6370614359173, since pi * 20 * 20 = 1256.6370614359173

### `perimeter(r)`
The function for finding the perimeter of a circle takes as an argument a single float  value r - the radius of the circle and returns 2 * math.pi * r (float) - the perimeter of the circle.

Examlple of a call:

- `perimeter(5)` returns 31.41592653589793, since 2 * pi * 5 = 31.41592653589793
- `perimeter(20)` returns 125.66370614359172, since 2 * pi * 20 = 125.66370614359172

## Rectangle
### `area(a, b)`
The function for finding the area of a reactangle takes as an argument two float  vlaues: a and b - the lengths of the sides of the rectangle and returns a * b (float) - the area of the rectangle.

Examlple of a call:

- `area(5, 10)` returns 50, since 5 * 10 = 50
- `area(20, 25)` returns 500, since 20 * 25 = 500

### `perimeter(a, b)`
The function for finding the perimeter of a reactangle takes as an argument two float  vlaues: a and b - the lengths of the sides of the rectangle and returns (a + b) * 2 (float) - the perimeter of the rectangle.

Examlple of a call:

- `perimeter(5, 10)` returns 30, since (5 + 10) * 2 = 30
- `perimeter(20, 25)` returns 90, since(20 + 25) * 2 = 90

## Square
### `area(a)`
The function for finding the area of a square takes as an argument a single float  vlaue a - the length of the side of the square and returns a * a (float) - the area of the square.

Examlple of a call:

- `area(5)` return 25, since 5 * 5 = 25
- `area(20)` returns 400, since 20 * 20 = 400

### `perimeter(a)`
The function for finding the perimeter of a square takes as an argument a single float  vlaue a - the length of the side of the square and returns 4 * a (float) - the perimeter of the square.

Examlple of a call:

- `perimeter(5)` returns 20, since 4 * 5 = 20
- `perimeter(20)` returns 80, since 4 * 20 = 80

## Triangle
### `area(a, h)`
The function for finding the area of a triangle takes as an argument two float  vlaues: a - the length of the side of the trianlge and h - height lowered to the side with length a and returns a * h / 2 (float) - the area of the triangle.

Examlple of a call:

- `area(5, 10)` returns 25, since 5 * 10 / 2 = 25
- `area(20, 25)` returns 250, since 20 * 25 / 2 = 250

### `perimeter(a, b, c)`
The function for finding the perimeter of a triangle takes as an argument three float  vlaues: a, b, c - the lengths of the sides of the triangle and returns a + b + c (float) - the perimeter of the triangle.

Examlple of a call:

- `perimeter(10, 10, 10)` returns 30, since 10 + 10 + 10 = 30
- `perimeter(20, 30, 40)` returns 90, since 20 + 30 + 40 = 90

# History of change
- commit 078b7a2, date - Thu Oct 16 23:26:30 2025:
    Added new file rectangle.py

- commit e6703fb, date - Thu Oct 16 23:27:56 2025:
    Added new file triangle.py
    Fixed mistake in function in ractangle.py
