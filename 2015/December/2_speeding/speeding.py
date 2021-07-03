def getMaxSpeeding(speeding, bessie):
  maxSpeeding = 0 # return this
  for i in range(1, 101):
    if speeding[i] < bessie[i]:
      maxSpeeding = max(maxSpeeding, bessie[i] - speeding[i])
  return maxSpeeding

def main(inputFile, outputFile):
  speedingInput = open(inputFile, 'r')
  speedingOutput = open(outputFile, 'w')

  N, M = speedingInput.readline().strip().split()
  N, M = int(N), int(M)

  # initializing speeding
  curSpeedIndex = 1
  speeding = [-1] * 101

  for _ in range(N):
    length, speed = speedingInput.readline().strip().split()
    length, speed = int(length), int(speed)

    # adding array of length and speed
    for i in range(curSpeedIndex, curSpeedIndex + length):
      speeding[i] = speed
    curSpeedIndex += length


  # initializing bessie
  curBessieIndex = 1
  bessie = [-1] * 101

  for _ in range(M):
    length, speed = speedingInput.readline().strip().split()
    length, speed = int(length), int(speed)

    # adding array of length and speed
    for i in range(curBessieIndex, curBessieIndex + length):
      bessie[i] = speed
    curBessieIndex += length

  speedingInput.close()

  speedingOutput.write(str(getMaxSpeeding(speeding, bessie)) + '\n')

  speedingOutput.close()


main('speeding.in', 'speeding.out')