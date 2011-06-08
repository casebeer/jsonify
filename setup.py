from setuptools import setup, find_packages
required_modules = [ 
	"simplejson"
	]

setup(
	name="jsonify",
	version="0.0.1",
	description="",
	author="Christopher H. Casebeer",
	author_email="christopher@chc.name",
	url="",
	entry_points = '''
		[console_scripts]
		jsonify = jsonify:main
	''',
	packages=find_packages(exclude='tests'),
	install_requires=required_modules
	)

