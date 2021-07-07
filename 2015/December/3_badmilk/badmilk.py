class Event:
  def __init__(self, id, milk, time):
    self.id = id
    self.milk = milk
    self.time = time

def getCures(N, M, events, sick, sickSet):
  commonDrank = []
  # get all common drank
  for i in range(1, M + 1):
    clearList = [False] * N
    # check if everyone sick drank this
    flag = False
    for e in events:
      if not clearList[e.id - 1]:
        if sickSet[e.id]:
          # e is sick
          if e.milk == i:
            # e drank this milk
            if sick[e.id] <= e.time:
              # sick before drank
              flag = True
              break
            else:
              clearList[e.id - 1] = True
        else:
          clearList[e.id - 1] = True

    if not flag and all(clearList):
      # found common drank
      commonDrank.append(i)
  
  # for cycle commonDrank keep track of count
  maxCount = 0 # return this
  visited = [False] * (N + 1)
  for c in commonDrank:
    count = 0
    for e in events:
      if e.milk == c and not visited[e.id]:
        visited[e.id] = True
        count += 1
    maxCount = max(maxCount, count)
  return maxCount

def main(inputFile, outputFile):
  badmilkInput = open(inputFile, 'r')
  badmilkOutput = open(outputFile, 'w')

  N, M, D, S = badmilkInput.readline().strip().split()
  N, M, D, S = int(N), int(M), int(D), int(S)

  events = [None] * (D + N)
  sick = [-1] * (N + 1)
  sickSet = [False] * (N + 1)

  for i in range(D):
    id, milk, time = badmilkInput.readline().strip().split()
    id, milk, time = int(id), int(milk), int(time)
    events[i] = Event(id, milk, time)
  # generate fake events
  for i in range(D, D + N):
    events[i] = Event(i - D + 1, -1, -1)

  for i in range(1, S + 1):
    id, time = badmilkInput.readline().strip().split()
    id, time = int(id), int(time)
    sickSet[id] = True
    sick[id] = time

  badmilkInput.close()

  badmilkOutput.write(str(getCures(N, M, events, sick, sickSet)) + '\n')
  badmilkOutput.close()


main('badmilk.in', 'badmilk.out')
