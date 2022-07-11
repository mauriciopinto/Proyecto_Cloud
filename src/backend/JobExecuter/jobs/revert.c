#include <string.h>
#include <stdio.h>

int main (int argc, char *argv[]) {
	int n;
	char filename[1024], output[1024], string[1024], reverse[1024];
	FILE *input, *out;
	
	strcpy (filename, argv[1]);
	strcpy (output, argv[2]);

	input = fopen (filename, "r");
	out = fopen (output, "w");

	n = fread (string, 1, 1024, input);
	
	for (int i = 0; i < n; ++i) {
		reverse[i] = string[n - (i + 1)];
	}
	
	fwrite (reverse, n, 1, out);
}
