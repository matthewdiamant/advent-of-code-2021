#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#define INPUTLENGTH 2000

void get_input(int *input) {
  FILE *fp = fopen("./input.txt", "r");

  char *line = NULL;
  size_t len = 0;

  for (int i = 0; getline(&line, &len, fp) != -1; i += 1) {
    input[i] = atoi(line);
  }

  fclose(fp);
}

int solve(int *input, int n) {
  int count = 0;
  for (int i = n; i < INPUTLENGTH; i += 1) {
    if (input[i] > input[i - n]) {
      count += 1;
    }
  }
  return count;
}

int main() {
  int input[INPUTLENGTH];
  get_input(input);

  assert(solve(input, 1) == 1832);
  assert(solve(input, 3) == 1858);

  return 0;
}
