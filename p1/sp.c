/* sp.c */

/* print value of stack pointer (esp) */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

unsigned long get_sp(void) {
  __asm__("movl %esp,%eax");
}
int main() {
  printf("0x%lx\n", get_sp());
}
