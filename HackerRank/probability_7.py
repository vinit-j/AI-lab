from fractions import Fraction

# Define the production and defect rates for each plant
production_A = 500
defect_rate_A = 0.005
production_B = 1000
defect_rate_B = 0.008
production_C = 2000
defect_rate_C = 0.010

# Calculate the overall probability of selecting a defective pipe
total_production = production_A + production_B + production_C
overall_defect_rate = (production_A * defect_rate_A + production_B * defect_rate_B + production_C * defect_rate_C) / total_production

# Calculate the probability that a defective pipe came from plant A using Bayes' theorem
probability_defect_from_A = (production_A * defect_rate_A) / (total_production * overall_defect_rate)

# Convert the probability to an irreducible fraction
probability_fraction = Fraction(probability_defect_from_A).limit_denominator()

# Print the result in the required format
print(f"{probability_fraction.numerator}/{probability_fraction.denominator}")
