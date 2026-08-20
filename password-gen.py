#!/usr/bin/env python3
import secrets,string
print(''.join(secrets.choice(string.ascii_letters+string.digits) for _ in range(16)))
