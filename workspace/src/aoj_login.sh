#!/bin/sh

expect -c "
spawn oj login https://atcoder.jp
expect \"Username\"
send $USER\r
expect \"Password\"
send $PASS\r
"