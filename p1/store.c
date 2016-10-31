#include <stdio.h>
#include <string.h>

int main(){
	char str[20];
	FILE *output;
	scanf("%20s", str);
	
	output = fopen("./output.txt","w");
	fwrite(str, 20, 1, output);
	fclose(output);
	return 0;
}
