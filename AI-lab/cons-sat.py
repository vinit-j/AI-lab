class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.assignment = {}

    def is_complete(self):
        return len(self.assignment) == len(self.variables)

    def is_consistent(self, variable, value):
        for constraint in self.constraints.get(variable, []):
            if constraint(self.assignment, variable, value) is False:
                return False
        return True

    def backtrack(self):
        if self.is_complete():
            return self.assignment

        unassigned_variables = [var for var in self.variables if var not in self.assignment]
        first_unassigned = unassigned_variables[0]

        for value in self.domains[first_unassigned]:
            if self.is_consistent(first_unassigned, value):
                self.assignment[first_unassigned] = value
                result = self.backtrack()
                if result:
                    return result
                del self.assignment[first_unassigned]

        return None

def main():
    # Define variables, domains, and constraints for a simple CSP
    variables = ['A', 'B', 'C']
    domains = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}
    
    def constraint1(assignment, var, value):
        # Constraint: A and B cannot have the same value
        return assignment.get('A', value) != value
    
    def constraint2(assignment, var, value):
        # Constraint: B and C cannot have the same value
        return assignment.get('B', value) != value
    
    constraints = {'A': [constraint1], 'B': [constraint1, constraint2], 'C': [constraint2]}

    # Create a CSP instance
    csp = CSP(variables, domains, constraints)

    # Solve the CSP using backtracking
    solution = csp.backtrack()

    if solution:
        print("Solution found:")
        print(solution)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
