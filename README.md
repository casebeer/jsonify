# Jsonify: A command line utility to pretty print JSON

Pipe JSON in to have it formatted: 

    $ cat tweets.json | jsonify 

Specify JSON keys to extract and print as arguments, using a dot to separate nested keys:

	$ cat tweets.json | jsonify user.screen_name text

Contents of each key will be printed on separate lines using Python's pprint module. If you don't want pprinting (for instance, if your keys' values are simple strings, not JSON objects), pass the --raw flag:

	$ cat tweets.json | jsonify --raw user.screen_name text

Missing keys will be printed as blank lines. You can use this to separate JSON objects with double spaces:

	$ cat tweets.json | jsonify --raw user.screen_name text BLANK_LINE

Pass the -f flag to make jsonfiy behave like tail -f and continue tailing the end of a file that's being updated:

    $ curl 'http://stream.twitter.com/1/statuses/filter.json?track=ipv6,v6day' \
		-u $SCREEN_NAME \
		| jsonify -f --raw user.screen_name text BLANK_LINE 

Omit all key arguments or use a dot to print the whole JSON object:

    $ cat tweets.json | jsonify
    $ cat tweets.json | jsonify .
    $ cat tweets.json | jsonify . BLANK_LINE

JSON objects must be provided one per line.

If the object provided is a list, each child object will be treated as a separate object:

    $ echo '[{"id":1},{"id":2},{"id":3}]'\
    	| jsonify -r id
    1
    2
    3

Simple command line streaming Twitter "client:"

    $ curl 'http://stream.twitter.com/1/statuses/filter.json?track=ipv6,v6day' \
    	-u $SCREEN_NAME \
    	| jsonify -f --raw user.screen_name text BLANK_LINE \
    	| fold -sw 80

In --raw mode, strings are encoded to utf8 before being printed.

