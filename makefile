install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py
	
lint:
	pylint --disable=R, C factorial.py
	
test:
	python -m pytest -vv --cov=factorial test_factorial.py
	
all: install lint test 
