#!/bin/sh

expect -c "
spawn acc login
expect \"user\"
send $USER\r
expect \"pass\"
send $PASS\r
"