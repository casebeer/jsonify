# Jsonify: A command line utility to pretty print JSON

Pipe JSON in to have it formatted: 

    $ cat tweets.json | jsonify 

Specify JSON keys to extract and print as arguments, using a dot to separate nested keys:

	$ cat tweets.json | jsonify user.screen_name text

Contents of each key will be printed on separate lines using Python's pprint module. If you don't want pprinting (for instance, if your keys' values are simple strings, not JSON objects), pass the --raw flag:

	$ cat tweets.json | jsonify --raw user.screen_name text

Missing keys will be printed as blank lines. You can use this to separate JSON objects with double spaces:

	$ cat tweets.json | jsonify --raw user.screen_name text BLANK_LINE

Omit all key arguments or use a dot to print the whole JSON object:

    $ cat tweets.json | jsonify
    $ cat tweets.json | jsonify .
    $ cat tweets.json | jsonify . BLANK_LINE

JSON objects must be provided one per line.

Simple command line streaming Twitter "client:"

    $ curl 'http://stream.twitter.com/1/statuses/filter.json?track=ipv6,v6day' \
		-u $SCREEN_NAME \
		| jsonify --raw user.screen_name text BLANK_LINE \
		| fold -sw 80

In --raw mode, strings are encoded to utf8 before being printed.
