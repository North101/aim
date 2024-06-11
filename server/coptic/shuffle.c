#include <stdio.h>
#include <stdint.h>
#include <string.h>

/*
reads in the file generated by coptic
*/

uint8_t tables[32][8];
uint8_t seats[8][8][4];

void swap_rows(uint8_t row[8][4], uint8_t b, uint8_t c) {
    uint8_t temp[4];
    for (uint8_t s = 0; s < 4; s++) {
      tables[row[b][s]][b]--;
      tables[row[c][s]][b]++;
      tables[row[b][s]][c]++;
      tables[row[c][s]][c]--;
    }
    memcpy(temp, row[b], 4);
    memcpy(row[b], row[c], 4);
    memcpy(row[c], temp, 4);
}

void count_tables() {
  uint8_t p;
  for (uint8_t h = 0; h < 8; h++) {
    for (uint8_t t = 0; t < 8; t++) {
      for (uint8_t s = 0; s < 4; s++) {
        p = seats[h][t][s];
        tables[p][t]++;
      }
    }
  }
}

int score_seats() {
  /*
   check no player is on any one table too often
   3-visits are right out - so huge penalty of 1000 for every 3+ visit
   no player should have too many 2-visits. So a penalty of n-squared for the count of 2-visits
  */
  int score = 0;
  for (uint8_t p = 0; p < 32; p++) {
    uint8_t twos = 0;
    for (uint8_t t = 0; t < 8; t++) {
      if (tables[p][t] > 2) {
        score += tables[p][t] * 10000;
      } else if (tables[p][t] == 2) {
        twos++;
      }
    }
    score += twos * twos;
  }
  return score;
}

int main(int argc, char *argv[]) {
  char *filename;
  if(argc > 1) {
      filename = argv[1];
  } else {
      filename = "coptic.coptic/default.txt";
  }

  FILE *file = fopen(filename, "r");
  if (file == NULL) {
      printf("Could not open file\n");
      return 1;
  }

  uint8_t seats[8][8][4];
  char line[256];
  while (fgets(line, sizeof(line), file)) {
      if (strstr(line, "SEATING BY ROUND, BY TABLE") != NULL) {
          for (int i = 0; i < 8; i++) {
              for (int j = 0; j < 8; j++) {
                  fscanf(file, "%hhu,%hhu,%hhu,%hhu, ;", &seats[i][j][0], &seats[i][j][1], &seats[i][j][2], &seats[i][j][3]);
              }
          }
          break;
      }
  }
 
  fclose(file);

  for (uint8_t h = 0; h < 8; h++) {
    for (uint8_t t = 0; t < 8; t++) {
      for (uint8_t s = 0; s < 4; s++) {
        uint8_t p = seats[h][t][s];
        tables[p][t]++;
      }
    }
  }

  printf("\n\n initial tables\n\n");
  // Print the results
  for (int i = 0; i < 32; i++) {
      for (int j = 0; j < 8; j++) {
          printf("%u, ", tables[i][j]);
      }
      printf("\n");
  }

  int score = score_seats();
  int score2;
  int last_score = score + 1;
  printf("initial score: %d", score);

  while (score < last_score) {
    last_score = score;
    printf("\n");
    for (int h  = 0; h < 8; h++) {
      // shuffle tables within each hanchan to reduce players visiting the same table twice
      for (int t = 0; t < 8; t++) {
        for (int t2 = t + 1; t2 < 8; t2++) {
          swap_rows(seats[h], t, t2);
          score2 = score_seats();
          if (score2 < score) {
            printf("%d, ", score2);
            score = score2;
          } else {
            // no improvement, so swap back
            swap_rows(seats[h], t, t2);
          }
        }
      }
    }
  }

  printf("\n\nSEATING BY ROUND, BY TABLE\n\n");
  for (int h = 0; h < 8; h++) {
      for (int t = 0; t < 8; t++) {
          printf("%4u, %4u, %4u, %4u, ; ", seats[h][t][0], seats[h][t][1], seats[h][t][2], seats[h][t][3]);
      }
      printf("\n");
  }

  printf("\n\nTABLE COUNT BY PLAYER\n\n");
  // Print the results
  for (int i = 0; i < 32; i++) {
      for (int j = 0; j < 8; j++) {
          printf("%u, ", tables[i][j]);
      }
      printf("\n");
  }
  printf("\n\nFINAL SCORE: %5d\n\n", score);
  return 0;
} 