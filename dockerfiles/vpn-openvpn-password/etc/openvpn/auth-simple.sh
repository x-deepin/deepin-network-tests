#!/bin/sh

# username: test
# password: test
if [ x"${username}" = xtest -a x"${password}" = xtest ]; then
  exit 0
else
  exit 1
fi
