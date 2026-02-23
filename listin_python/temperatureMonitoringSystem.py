# Temperature Monitoring System

temps = list(map(float, input("Enter daily temperatures separated by space: ").split()))

if temps:
    hottest = max(temps)
    coldest = min(temps)

    extreme_days = len([t for t in temps if t > 40])

    for i in range(len(temps)):
        if temps[i] > 45:
            temps[i] = "Heat Alert"

    print("Hottest Day Temperature:", hottest)
    print("Coldest Day Temperature:", coldest)
    print("Extreme Days (>40°C):", extreme_days)
    print("Updated Temperature List:", temps)
else:
    print("No temperature data provided.")
    
    #output
    """ Enter daily temperatures separated by space: 35 42 46 39 41 50
Hottest Day Temperature: 50.0
Coldest Day Temperature: 35.0
Extreme Days (>40°C): 4
Updated Temperature List: [35.0, 42.0, 'Heat Alert', 39.0, 41.0, 'Heat Alert']"""