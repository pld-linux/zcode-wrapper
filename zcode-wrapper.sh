#!/bin/sh

if [ -f /usr/share/games/zcode/`basename $0`.z5 ]; then
        GAME=/usr/share/games/zcode/`basename $0`.z5
elif [ -f /usr/share/games/zcode/`basename $0`.z8 ]; then
        GAME=/usr/share/games/zcode/`basename $0`.z8
else
        echo "This game does not exist."
        exit
fi

if [ "$DISPLAY" ] && [ -x /usr/bin/zoom ]; then
	/usr/bin/zoom $GAME
elif [ -x /usr/bin/frotz ]; then
	/usr/bin/frotz $GAME
else
	echo "You don't have working interpreter for zcode files"
fi
