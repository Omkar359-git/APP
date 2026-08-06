# Program to find the Longest Common Subsequence (LCS)
# using Dynamic Programming (Tabulation)

def longest_common_subsequence(seq1, seq2):
    length1 = len(seq1)
    length2 = len(seq2)

    # Create DP table initialized with 0
    dp = [[0 for col in range(length2 + 1)] for row in range(length1 + 1)]

    # Fill the DP table
    for row in range(1, length1 + 1):
        for col in range(1, length2 + 1):
            if seq1[row - 1] == seq2[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    # Reconstruct the LCS
    row = length1
    col = length2
    lcs = ""

    while row > 0 and col > 0:
        if seq1[row - 1] == seq2[col - 1]:
            lcs = seq1[row - 1] + lcs
            row -= 1
            col -= 1
        elif dp[row - 1][col] > dp[row][col - 1]:
            row -= 1
        else:
            col -= 1

    return lcs, dp[length1][length2]


# Main Program
sequence1 = input("Enter the first sequence: ")
sequence2 = input("Enter the second sequence: ")

lcs, length = longest_common_subsequence(sequence1, sequence2)

print("\nLongest Common Subsequence:", lcs)
print("Length of LCS:", length)