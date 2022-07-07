test-unit:
	pytest-3 test/test_unit.py

run:
	clingo src/*.lp 0
