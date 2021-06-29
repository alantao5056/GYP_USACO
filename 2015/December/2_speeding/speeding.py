def getMaxSpeeding(speeding, bessie):
  maxSpeeding = 0 # return this
  for i in range(1, 101):
    if speeding[i] < bessie[i]:
      maxSpeeding = max(maxSpeeding, bessie[i] - speeding[i])
  return maxSpeeding

def main(inputFile, outputFile):
  inputFile = open(inputFile, 'r')
  outputFile = open(outputFile, 'w')
  
  N, M = inputFile.readline().strip().split()
  N, M = int(N), int(M)
  
  # initializing speeding
  curSpeedIndex = 1
  speeding = [-1] * 101
  
  for _ in range(N):
    length, speed = inputFile.readline().strip().split()
    length, speed = int(length), int(speed)
    
    # adding array of length and speed
    for i in range(curSpeedIndex, curSpeedIndex + length):
      speeding[i] = speed
    curSpeedIndex += length
  

  # initializing bessie
  curBessieIndex = 1
  bessie = [-1] * 101
  
  for _ in range(M):
    length, speed = inputFile.readline().strip().split()
    length, speed = int(length), int(speed)
    
    # adding array of length and speed
    for i in range(curBessieIndex, curBessieIndex + length):
      bessie[i] = speed
    curBessieIndex += length
  
  inputFile.close()
  
  outputFile.write(str(getMaxSpeeding(speeding, bessie)) + '\n')
  
  outputFile.close()


main('speeding.in', 'speeding.out')