
all: clean

clean:
	find . -name '*.pyc' | xargs rm -f
	rm -rf build

deploy-prod:
	fab -i ~/Documents/victorpantoja.pem prod deploy

setup:
	@echo "Installing dependencies..."
	@pip install -r requirements-dev.txt

start:
	PYTHONPATH=`pwd`:`pwd`/portfolio python portfolio/server.py ${PORT}

test: clean
	echo "Running tests..."
	PYTHONPATH=`pwd` \
		nosetests -s --verbose --with-coverage --cover-package=portfolio tests/*

runner_minify:
	@echo "Minifing CSS and JS ..."
    @cd minify && python minify_runner.py --settings=settings.conf
