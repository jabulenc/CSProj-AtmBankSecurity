/* stack.c */

/* This program has a buffer overflow vulnerability. */
/* Our task is to exploit this vulnerability, not by
 * modifying this code, but by providing a cleverly
 * constructed input. */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define BSIZE 100000

int bof(char *str)
{
  char buffer[20];
  strcpy(buffer, str);

  return 1;
}


int main(int argc, char **argv)
{
  const char *happy = ":)";
  char str[BSIZE];
  FILE *badfile;
  char *badfname = "badfile";

  badfile = fopen(badfname, "r");
  fread(str, sizeof(char), BSIZE, badfile);
  bof(str);

  printf("Returned Properly %s\n", happy);
  return 1;
}
