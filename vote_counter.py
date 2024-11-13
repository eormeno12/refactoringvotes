import csv
from collections import defaultdict


# Extracción de métodos y eliminar código innecesario (ej: city)
def process_vote_row(row):
    try:
        candidate = row[1]
        votes = int(row[2])
    except (IndexError, ValueError):
        votes = 0
    return candidate, votes

# Extracción de métodos, renombrar variables y eliminar código duplicado
def count_votes(file_path, results=None):
    if results is None:
        results = defaultdict(int)
    
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)

        for row in reader:
            candidate, votes = process_vote_row(row)
            results[candidate] += votes

    return results

# Extracción de métodos y elminar código duplicado
def display_results(results):
    for candidate, total_votes in results.items():
        print(f"{candidate}: {total_votes} votes")

# Extracción de métodos y simplificación de condicionales
def determine_winner(results):
    max_votes = max(results.values(), default=0)
    winners = [candidate for candidate, votes in results.items() if votes == max_votes]
    
    return winners

# Extracción de métodos
def display_winner(winners):
    if len(winners) == 0:
        print("No winner")
    elif len(winners) > 1:
        print(f"winners are: {', '.join(winners)}")
    else:
        print(f"winner is {winners[0]}")

# Extracción de clases
class VoteCounter:
    def __init__(self, file_path):
        self.results = count_votes(file_path)
        self.winner = determine_winner(self.results)

    def display_results(self):
        display_results(self.results)

    def display_winner(self):
        display_winner(self.winner)

# Example usage
if __name__ == '__main__':
    vote_counter = VoteCounter('votes.csv')
    vote_counter.display_results()
    vote_counter.display_winner()
    
