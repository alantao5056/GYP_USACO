def main(inputFile: str, outputFile: str):
  promoteInput = open(inputFile, 'r')
  promoteOutput = open(outputFile, 'w')

  # getting input

  bronzeBefore, bronzeAfter = promoteInput.readline().strip().split()
  bronzeBefore, bronzeAfter = int(bronzeBefore), int(bronzeAfter)

  silverBefore, silverAfter = promoteInput.readline().strip().split()
  silverBefore, silverAfter = int(silverBefore), int(silverAfter)

  goldBefore, goldAfter = promoteInput.readline().strip().split()
  goldBefore, goldAfter = int(goldBefore), int(goldAfter)

  plantiumBefore, plantiumAfter = promoteInput.readline().strip().split()
  plantiumBefore, plantiumAfter = int(plantiumBefore), int(plantiumAfter)

  promoteInput.close()

  # writing

  goldToPlantium = plantiumAfter - plantiumBefore
  silverToGold = goldAfter - goldBefore + goldToPlantium
  bronzeToSilver = silverAfter - silverBefore + silverToGold

  promoteOutput.write(str(bronzeToSilver) + '\n')
  promoteOutput.write(str(silverToGold) + '\n')
  promoteOutput.write(str(goldToPlantium) + '\n')

main("promote.in", "promote.out")