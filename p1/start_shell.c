/* start_shell.c */

/* This is the foundation for the machine code instructions
 * that we've already put into exploit_1.c for you */

#include <stdio.h>

int main() {
  char *name[2];
  name[0] = "/bin/sh";
  name[1] = NULL;
  execve(name[0], name, NULL);
} 
