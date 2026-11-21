
class Solution {
    public int minMoves(String[] classroom, int energy) {
        int m = classroom.length;
        int n = classroom[0].length();

        int[][] id = new int[m][n];
        int sr = 0, sc = 0, litter = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char c = classroom[i].charAt(j);

                if (c == 'S') {
                    sr = i;
                    sc = j;
                } else if (c == 'L') {
                    id[i][j] = litter++;
                }
            }
        }

        if (litter == 0) return 0;

        int masks = 1 << litter;
        boolean[][][][] visited = new boolean[m][n][energy + 1][masks];

        int fullMask = masks - 1;

        int[] qr = new int[m * n * (energy + 1) * masks];
        int[] qc = new int[qr.length];
        int[] qe = new int[qr.length];
        int[] qm = new int[qr.length];

        int head = 0, tail = 0;

        qr[tail] = sr;
        qc[tail] = sc;
        qe[tail] = energy;
        qm[tail] = fullMask;
        tail++;

        visited[sr][sc][energy][fullMask] = true;

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        int moves = 0;

        while (head < tail) {
            int size = tail - head;

            while (size-- > 0) {
                int r = qr[head];
                int c = qc[head];
                int e = qe[head];
                int mask = qm[head++];

                if (mask == 0) return moves;

                if (e == 0) continue;

                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                    if (classroom[nr].charAt(nc) == 'X') continue;

                    char cell = classroom[nr].charAt(nc);

                    int ne = e - 1;
                    if (cell == 'R') {
                        ne = energy;
                    }

                    int nmask = mask;

                    if (cell == 'L') {
                        nmask &= ~(1 << id[nr][nc]);
                    }

                    if (!visited[nr][nc][ne][nmask]) {
                        visited[nr][nc][ne][nmask] = true;

                        qr[tail] = nr;
                        qc[tail] = nc;
                        qe[tail] = ne;
                        qm[tail] = nmask;
                        tail++;
                    }
                }
            }

            moves++;
        }

        return -1;
    }
}
