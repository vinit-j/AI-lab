from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure of the Bayesian Network
model = BayesianNetwork([('Flu', 'Cough')])

# Define conditional probability distributions (CPDs)
cpd_flu = TabularCPD(variable='Flu', variable_card=2, values=[[0.95], [0.05]])
cpd_cough = TabularCPD(variable='Cough', variable_card=2, 
                       values=[[0.7, 0.1], [0.3, 0.9]],
                       evidence=['Flu'], evidence_card=[2])

# Add CPDs to the model
model.add_cpds(cpd_flu, cpd_cough)

# Check if the model is valid
assert model.check_model()

# Perform exact inference
inference = VariableElimination(model)

# Calculate the probability of having the flu given coughing
probability = inference.query(variables=['Flu'], evidence={'Cough': 1})
print(probability)
