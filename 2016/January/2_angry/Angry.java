import java.util.Set;
import java.util.StringTokenizer;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Angry {
  static int N;
  static int[] hays;

  static class Hay {
    int h, radius;
    Hay(int h, int radius) {
      this.h = h;
      this.radius = radius;
    }
  }

  static int getMaxHaybale() {
    int maxExplosionCount = 0;
    for (int i = 0; i < N; i++) {
      // h is the first explosion
      Set<Integer> alreadyExploded = new HashSet<>();
      alreadyExploded.add(hays[i]);
      Queue<Hay> needToExplode = new LinkedList<>();
      needToExplode.add(new Hay(hays[i], 1));

      // start while recursive
      while (!needToExplode.isEmpty()) {
        // need to explode is not empty
        Hay curHay = needToExplode.poll();

        // explosion chain reaction
        for (int explodeHay : hays) {
          if ((!alreadyExploded.contains(explodeHay)) && ((explodeHay > curHay.h && explodeHay <= curHay.h + curHay.radius) || (explodeHay < curHay.h && explodeHay >= curHay.h - curHay.radius))) {
            // will explode
            needToExplode.add(new Hay(explodeHay, curHay.radius + 1));
            alreadyExploded.add(explodeHay);
          }
        }
      }
      maxExplosionCount = Math.max(maxExplosionCount, alreadyExploded.size());
    }
    return maxExplosionCount;
  }

  public static void main(String[] args) throws IOException{
    String in = new String(Files.readAllBytes(Paths.get("angry.in")));
    PrintWriter pw = new PrintWriter(new FileWriter("angry.out"));
    StringTokenizer st = new StringTokenizer(in);

    N = Integer.parseInt(st.nextToken());
    hays = new int[N];

    for (int i = 0; i < N; i++) {
      hays[i] = Integer.parseInt(st.nextToken());
    }

    Arrays.sort(hays);

    pw.println(getMaxHaybale());
    pw.close();
  }
}