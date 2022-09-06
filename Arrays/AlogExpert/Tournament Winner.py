# HashMap Approach | O(N) and O(K)
def tournamentWinner(competitions, results):
    # Write your code here.
    winner = ""
    dict = {winner: 0}
    for i in range(len(competitions)):

        team = competitions[i][1] if results[i] == 0 else competitions[i][0]

        if team in dict:
            dict[team] += 3
        else:
            dict[team] = 3
        if dict[team] > dict[winner]:
            winner = team

    return winner


def findMax(dictionary):
    return max(dictionary, key=dictionary.get)