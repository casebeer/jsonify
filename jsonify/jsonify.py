try:
	import simplejson as json
except ImportError: 
	import json
import sys
import time
import pprint
from optparse import OptionParser

def tail_f(in_f, fun):
	while True:
		#where = in_f.tell()
		line = in_f.readline()
		if not line:
			time.sleep(1)
			#in_f.seek(where)
		else:
			fun(line)
def make_printer(keys, pretty=True, do_print=pprint.pprint):
	if not pretty and do_print == pprint.pprint:
		# only override the with normal_print if do_print not explicitly set
		def normal_print(s):
			print unicode(s).encode('utf8')
		do_print = normal_print
	def printer(line):
		try:
			data = json.loads(line.strip())
		except Exception,e:
			print "<UNABLE TO DECODE JSON>"
			return
		outputs = []
		for components in keys:
			obj = data
			if len(components) == 2 \
				and components[0] == "" \
				and components[1] == "":
				# single dot, print whole object
				pass
			else:
				for key in components:
					if obj != None and key in obj:
						obj = obj[key]
					else:
						obj = None
						break
			outputs.append(obj)
		if len(keys) == 0:
			do_print(data)
		else:
			for obj in outputs:
				if obj == None:
					# blank line for missing keys
					print
				else:
					do_print(obj)
	return printer

def main():	
	usage = """usage: %prog [options] [keys]

Specify JSON keys to extract and print as arguments. Separate 
nested key levels with dots. 

Use a single dot or pass no arguments to print the whole JSON 
object.

JSON objects must be one per line."""
	parser = OptionParser(usage=usage)
	parser.add_option("-r", "--raw", dest="pretty", action="store_false", default=True, help="print raw values of key, skipping the pretty printer")
	options, args = parser.parse_args()

	try: 
		tail_f(sys.stdin, make_printer([arg.split(".") for arg in args], pretty=options.pretty))
	except KeyboardInterrupt:
		return 0

if __name__ == '__main__':
	main()
