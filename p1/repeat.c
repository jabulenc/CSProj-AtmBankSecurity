#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int main(){
char str[20];
FILE *file;

file = fopen("output.txt","r");
fread(str, sizeof(char), 20, file);
fclose(file);
printf("%20s\n", str);
}
