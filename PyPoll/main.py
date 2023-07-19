import csv

results = csv.reader(open('PyPoll/Resources/election_data.csv'))
header = next(results)

votes = 0
greatest = 0
vote0 = 1
vote1 = 1
vote2 = 1 
candidates = []

for row in results:
    votes += 1

    if row[2] not in candidates:
        candidates.append(row[2])
    elif row[2] == candidates[0]:
        vote0 += 1
        if vote0 > greatest:
            greatest = vote0
            winner = candidates[0]
    elif row[2] == candidates[1]:
        vote1 += 1
        if vote1 > greatest:
            greatest = vote1
            winner = candidates[1]
    elif row[2] == candidates[2]:
        vote2 += 1
        if vote2 > greatest:
            greatest = vote2
            winner = candidates[2]

def percent(count):
    percent = round(count/votes*100, 3)

    return percent

returns = (f'''
        Election Results
        ------------------------
        Total Votes: {votes}
        ------------------------
        {candidates[0]}: {percent(vote0)}% ({vote0})
        {candidates[1]}: {percent(vote1)}% ({vote1})
        {candidates[2]}: {percent(vote2)}%  ({vote2})
        ------------------------
        Winner: {winner}
        ------------------------
        ''')

print(returns)

with open("PyPoll/Analysis/budget_analysis.txt", 'w') as file:
    file.write(returns)