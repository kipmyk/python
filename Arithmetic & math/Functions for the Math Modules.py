import math

# Constants
print(f"Pi constant: {math.pi} (Ratio of circle's circumference to diameter)")
print(f"Euler's number: {math.e} (Base of natural logarithms)")
print(f"Tau constant: {math.tau} (2 * pi)")
print(f"Infinity: {math.inf} (Represents positive infinity)")
print(f"NaN: {math.nan} (Not a Number)")

# Power and logarithmic functions
print(f"Square root of 25: {math.sqrt(25)} (Returns the square root)")
print(f"2 to the power of 3: {math.pow(2, 3)} (Raises to a power)")
print(f"e raised to 2: {math.exp(2)} (Exponential function)")
print(f"Natural log of 10: {math.log(10)} (Log base e)")
print(f"Log base 10 of 100: {math.log(100, 10)}")
print(f"Log base 10 of 1000: {math.log10(1000)}")
print(f"Log base 2 of 8: {math.log2(8)}")

# Trigonometric functions
print(f"Sine of π/2: {math.sin(math.pi/2)}")
print(f"Cosine of π: {math.cos(math.pi)}")
print(f"Tangent of π/4: {math.tan(math.pi/4)}")

# Inverse trigonometric functions
print(f"Arcsine of 1: {math.asin(1)} (Returns angle in radians)")
print(f"Arccosine of 1: {math.acos(1)}")
print(f"Arctangent of 1: {math.atan(1)}")

# Angle conversion
print(f"Degrees from pi radians: {math.degrees(math.pi)}")
print(f"Radians from 180 degrees: {math.radians(180)}")

# Hyperbolic functions
print(f"Sinh(1): {math.sinh(1)} (Hyperbolic sine)")
print(f"Cosh(1): {math.cosh(1)} (Hyperbolic cosine)")
print(f"Tanh(1): {math.tanh(1)} (Hyperbolic tangent)")

# Special functions
print(f"Error function erf(1): {math.erf(1)}")
print(f"Complementary error function erfc(1): {math.erfc(1)}")
print(f"Gamma of 5: {math.gamma(5)} (Generalized factorial)")
print(f"Log gamma of 5: {math.lgamma(5)} (Logarithm of gamma)")

# Rounding and remainder
print(f"Ceiling of 4.2: {math.ceil(4.2)} (Rounds up)")
print(f"Floor of 4.8: {math.floor(4.8)} (Rounds down)")
print(f"Truncate 4.8: {math.trunc(4.8)} (Drops decimal)")
print(f"Fmod 7 % 3: {math.fmod(7, 3)} (Remainder, same sign as numerator)")
print(f"Remainder of 7 divided by 3: {math.remainder(7, 3)}")

# Combinatorics
print(f"Factorial of 5: {math.factorial(5)}")
print(f"Combinations of 5 choose 2: {math.comb(5, 2)}")
print(f"Permutations of 5 taken 2: {math.perm(5, 2)}")

# Absolute value and signs
print(f"Absolute value of -4.5: {math.fabs(-4.5)}")
print(f"Copy sign from -2 to 1: {math.copysign(1, -2)}")

# Float checks
print(f"Is 10 finite? {math.isfinite(10)}")
print(f"Is infinity infinite? {math.isinf(math.inf)}")
print(f"Is NaN a NaN? {math.isnan(math.nan)}")
print(f"Is 1.0001 close to 1.0002? {math.isclose(1.0001, 1.0002, rel_tol=1e-3)}")

# Next and precision
print(f"Next float after 1 toward 2: {math.nextafter(1, 2)}")
print(f"ULP of 1.0: {math.ulp(1.0)} (Unit in the Last Place)")
