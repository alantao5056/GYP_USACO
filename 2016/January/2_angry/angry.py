# public variables
hays = []
N=0;


def getMaxHaybales():
  global hays, N;

  maxExplosionCount = 0
  for h in hays:
    # h is the first explosion
    alreadyExploded = set([h])
    needToExplode = [(h, 1,)] # queue

    # start while recursive
    while needToExplode:
      # need to explode is not empty
      curHay = needToExplode.pop()

      # explosion chain reaction
      for explodeHay in hays:
        if (explodeHay not in alreadyExploded) and ((explodeHay > curHay[0] and explodeHay <= curHay[0] + curHay[1]) or (explodeHay < curHay[0] and explodeHay >= curHay[0] - curHay[1])):
          # will explode
          needToExplode.append((explodeHay, curHay[1] + 1,))
          alreadyExploded.add(explodeHay)
    maxExplosionCount = max(maxExplosionCount, len(alreadyExploded))
  return maxExplosionCount

def main(inputFile: str, outputFile: str):
  global hays, N
  angryInput = open(inputFile, 'r')
  angryOutput = open(outputFile, 'w')

  N = int(angryInput.readline().strip())
  for _ in range(N):
    hays.append(int(angryInput.readline().strip()))
  
  hays.sort()

  angryInput.close()

  angryOutput.write(f'{getMaxHaybales()}\n')

  angryOutput.close()

main('angry.in', 'angry.out')