
all:

clean:
	rm -rf jsonify.egg-info build dist
	find . -type f -name *.pyc | xargs rm -f
