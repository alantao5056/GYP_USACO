class Segment:
  def __init__(self, length, speed):
    self.length = length
    self.speed = speed


def getMaxSpeeding(speedLimit, bessie):
  maxSpeeding = 0
  curSpeedIndex = 0
  curBessieIndex = 0

  while curSpeedIndex < len(speedLimit) and curBessieIndex < len(bessie):
    curSpeeding = speedLimit[curSpeedIndex]
    curBessie = bessie[curBessieIndex]
    if curBessie.length < curSpeeding.length:
      # update maxSpeeding
      maxSpeeding = max(maxSpeeding, curBessie.speed - curSpeeding.speed)
      # cut off segment and subtract length
      curSpeeding.length -= curBessie.length
      curBessieIndex += 1
    elif curBessie.length > curSpeeding.length:
      # update maxSpeeding
      maxSpeeding = max(maxSpeeding, curBessie.speed - curSpeeding.speed)
      # cut off segment and subtract length
      curBessie.length -= curSpeeding.length
      curSpeedIndex += 1
    else:
      # equivilent
      # update maxSpeeding
      maxSpeeding = max(maxSpeeding, curBessie.speed - curSpeeding.speed)
      # cur off both segments
      curSpeedIndex += 1
      curBessieIndex += 1
  return maxSpeeding


def main(inputFile, outputFile):
  speedingInput = open(inputFile, 'r')
  speedingOutput = open(outputFile, 'w')

  N, M = speedingInput.readline().strip().split()
  N, M = int(N), int(M)

  speedLimit = [None] * N
  bessie = [None] * M

  for i in range(N):
    length, speed = speedingInput.readline().strip().split()
    length, speed = int(length), int(speed)
    speedLimit[i] = Segment(length, speed)


  for i in range(M):
    length, speed = speedingInput.readline().strip().split()
    length, speed = int(length), int(speed)
    bessie[i] = Segment(length, speed)

  speedingInput.close()

  speedingOutput.write(str(getMaxSpeeding(speedLimit, bessie)) + '\n')
  speedingOutput.close()


main('speeding.in', 'speeding.out')