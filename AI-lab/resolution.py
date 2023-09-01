class PropositionalResolution:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def resolve(self, clause1, clause2):
        resolved_clause = []

        for literal in clause1:
            if -literal not in clause2:
                resolved_clause.append(literal)

        return resolved_clause

    def resolution(self, query):
        self.kb.append(query)
        while True:
            new_clauses = []
            n = len(self.kb)

            for i in range(n):
                for j in range(i + 1, n):
                    clause1 = self.kb[i]
                    clause2 = self.kb[j]
                    resolvents = self.resolve(clause1, clause2)

                    if not resolvents:
                        return True  # An empty clause was derived, so the query is true (contradiction found)

                    new_clauses.extend(resolvents)

            if all(new_clause in self.kb for new_clause in new_clauses):
                return False  # No new clauses were added, and the query is false (no contradiction found)

            self.kb.extend(new_clauses)

if __name__ == "__main__":
    # Example usage:
    kb = [[-1, 2], [1, -2], [-1, -2], [2], [-2]]
    query = [1]

    resolver = PropositionalResolution(kb)
    result = resolver.resolution(query)

    if result:
        print("The query is valid (true).")
    else:
        print("The query is invalid (false).")
