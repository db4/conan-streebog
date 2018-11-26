#include <stdio.h>
#include "gost3411-2012-core.h"

int main(int argc, char *argv[])
{
    ALIGN(16) GOST34112012Context CTX;
    unsigned char digest[64];
    int i;

    GOST34112012Init(&CTX, 512);

    GOST34112012Update(&CTX, "0123456789", 10);
    /* call GOST34112012Update() for each block of data */

    GOST34112012Final(&CTX, &digest[0]);
    /* You now have GOST R 34.11-2012 hash in 'digest' */

    GOST34112012Cleanup(&CTX);

    for (i = 0; i < 64; ++i) {
        printf("%02X", digest[i]);
    }
    printf("\n");

    return 0;
}
