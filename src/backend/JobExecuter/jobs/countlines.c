#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char *argv[]) {
	char filename[1024], output[1024], *token;
	char data[1024], res[10];
	FILE *input, *out;
	int count = 0;

	strcpy (filename, argv[1]);
	strcpy (output, argv[2]);

	input = fopen (filename, "r");
	out = fopen (output, "w");

	fread (data, 1024, 1, input);
	
	token = strtok (data, "\n");
	while (token) {
		count++;
		token = strtok (NULL, "\n");
	}

	fprintf (out, "%d", count);
}
