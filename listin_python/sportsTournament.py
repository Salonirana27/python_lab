# Sports Tournament Points Table

points = list(map(int, input("Enter team points separated by space: ").split()))

# Replace negative points with 0
points = [p if p >= 0 else 0 for p in points]

points.sort(reverse=True)

if len(points) >= 2:
    winner = points[0]
    runner_up = points[1]
else:
    winner = runner_up = None

print("Leaderboard:", points)
print("Winner Points:", winner)
print("Runner-up Points:", runner_up)

#output
"""Enter team points separated by space: 45 60 -10 55 70
Leaderboard: [70, 60, 55, 45, 0]
Winner Points: 70
Runner-up Points: 60"""