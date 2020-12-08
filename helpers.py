import csv
import os

def getParsedNormalizedData(fileName):
    fields, players, data = parseData(fileName)
    playerScores = scorePlayers(data)
    normalizedData = normalizeData(data)
    numpyData = convertToNumpy(normalizedData)
    return fields, players, numpyData, playerScores


# Takes in a file name and returns a dictionary of player names to list of stats
def parseData(fileName):
    if os.path.exists(fileName):
        try:
            f = open(fileName, 'r')
        except:
            print("Could not open/read file", fileName)
            sys.exit()
        with f:
            reader = csv.reader(f)
            fields = []
            players = {}
            data = []
            i = 0
            for row in reader:
                if i == 0:
                    fields = row[3:]
                else:
                    players[row[0]] = i
                    data.append([float(i) for i in row[3:]])
                i += 1
            return fields, players, data
    else:
        return [], {}

def scorePlayers(data):
    scores = []
    for d in data:
        # singles, doubles, triples, home runs
        score = d[4] + (2*d[5]) + (3*d[6]) + (4*d[7])
        # runs, runs batted in, walks, hit by pitch
        score += d[3] + d[8] + d[11] + d[15]
        # stolen bases - caught stealing
        score += (2*d[9]) - d[10]
        scores.append(score)
    maxScore = 0
    for score in scores:
        maxScore = max(maxScore, score)
    return [x / maxScore for x in scores]

# Takes dictionary of (playerName -> list of stats) and finds max and mins of
# each stat for normalization purposes and returns a dictionary of
# (playerName -> list of normalized stats ranged (0, 1.0))
def normalizeData(data):
    # Gettin maxmins
    maxmins = []
    for pValue in list(data)[0]:
        maxmins.append([pValue, pValue])
    for values in data:
        for i in range(0, len(values)):
            maxmins[i][0] = min(maxmins[i][0], values[i])
            maxmins[i][1] = max(maxmins[i][1], values[i])

    dataNormalized = []
    for values in data:
        newValues = []
        for i in range(0, len(values)):
            newValues.append((values[i] - maxmins[i][0]) / (maxmins[i][1] - maxmins[i][0]))
        dataNormalized.append(newValues)
    return dataNormalized

# Takes in normalized data with (playerName -> data) and returns playerNamesList
# and 2d numpy array of the data
def convertToNumpy(data):
    import numpy as np
    playerData = []
    for d in data:
        playerData.append(d)
    return np.array(playerData)
