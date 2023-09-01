from fractions import Fraction
total_outcomes = 36  
favorable_outcomes = [
    (1, 5), (2, 4), (4, 2), (5, 1)  
]
probability = Fraction(len(favorable_outcomes), total_outcomes)
print(f"{probability.numerator}/{probability.denominator}")
