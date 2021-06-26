def getTotalPaint(a, b, c, d):
  if a <= c <= b and a <= d <= b:
    return b - a
  elif a <= c <= b:
    return b - a + (d - b)
  elif a <= d <= b:
    return b - a + (a - c)
  elif c <= a <= d and c <= b <= d:
    return d - c
  else:
    return b - a + (d - c)


def main(inputFile, outputFile):
  paintInput = open(inputFile, 'r')
  paintOutput = open(outputFile, 'w')
  
  a, b = paintInput.readline().strip().split()
  a, b = int(a), int(b)
  
  c, d = paintInput.readline().strip().split()
  c, d = int(c), int(d)
  
  paintOutput.write(str(getTotalPaint(a, b, c, d)) + '\n')
  paintInput.close()
  paintOutput.close()


main('paint.in', 'paint.out')
