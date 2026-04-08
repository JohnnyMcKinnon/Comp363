# Needleman-Wunsch string alignment (Dynamic Programming-DP)

# cost of inserting a gap
gap_penalty = 1

# penalty function for match/mismatch
def penalty(x, y):
    # if characters match, no cost
    if x == y:
        return 0
    # mismatch cost
    else:
        return 2


def make_table(s1, s2):
    m = len(s1)
    n = len(s2)

    # dp table (m+1 x n+1)
    dp = []
    for i in range(m + 1):
        dp.append([0] * (n + 1))

    # base case: align string with empty string (all gaps)
    for i in range(1, m + 1):
        dp[i][0] = i * gap_penalty

    for j in range(1, n + 1):
        dp[0][j] = j * gap_penalty

    # fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # diagonal = match/mismatch
            diag = dp[i-1][j-1] + penalty(s1[i-1], s2[j-1])

            # up = gap in s2
            up = dp[i-1][j] + gap_penalty

            # left = gap in s1
            left = dp[i][j-1] + gap_penalty

            # take best (min cost)
            dp[i][j] = min(diag, up, left)

    return dp


def get_alignment(s1, s2, dp):
    i = len(s1)
    j = len(s2)

    a1 = ""  # aligned version of s1
    a2 = ""  # aligned version of s2

    # traceback from bottom-right of dp table
    while i > 0 or j > 0:

        # compute possible moves safely
        if i > 0 and j > 0:
            diag = dp[i-1][j-1] + penalty(s1[i-1], s2[j-1])
        else:
            diag = float('inf')

        if i > 0:
            up = dp[i-1][j] + gap_penalty
        else:
            up = float('inf')

        if j > 0:
            left = dp[i][j-1] + gap_penalty
        else:
            left = float('inf')

        # choose best move (tie-breaking favors diagonal first)
        if diag <= left and diag <= up:
            # match/mismatch case (diagonal move)
            a1 = s1[i-1] + a1
            a2 = s2[j-1] + a2
            i -= 1
            j -= 1

        elif left <= up:
            # gap in s1 (move left)
            a1 = "-" + a1
            a2 = s2[j-1] + a2
            j -= 1

        else:
            # gap in s2 (move up)
            a1 = s1[i-1] + a1
            a2 = "-" + a2
            i -= 1

    return a1, a2


def stats(a1, a2):
    matches = 0
    mismatches = 0
    gaps = 0

    # compare aligned strings by each character
    for i in range(len(a1)):
        if a1[i] == "-" or a2[i] == "-":
            gaps += 1
        elif a1[i] == a2[i]:
            matches += 1
        else:
            mismatches += 1

    return matches, mismatches, gaps


def run_case(s1, s2):
    dp = make_table(s1, s2)        # build DP table
    a1, a2 = get_alignment(s1, s2, dp)  # reconstruct alignment

    matches, mismatches, gaps = stats(a1, a2)  # compute stats

    # print formatted result
    print(f"{s1} --> |{a1}| matches: {matches} mismatches: {mismatches}")
    print(f"{s2} --> |{a2}| gaps: {gaps}")
    print()


# test cases
tests = [
    ("CRANE", "RAIN"),
    ("CYCLE", "BICYCLE"),
    ("ASTRONOMY", "GASTRONOMY"),
    ("INTENTION", "EXECUTION"),
    ("AGGTAB", "GXTXAYB"),
    ("GATTACA", "GCATGCU"),
    ("DELICIOUS", "RELIGIOUS"),
]

for s1, s2 in tests:
    run_case(s1, s2)