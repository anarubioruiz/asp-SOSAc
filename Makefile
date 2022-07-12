test-unit:
	pytest-3 test/test_unit.py

test-scenario:
	pytest-3 test/test_scenario.py

test-all:
	pytest-3 test/

run:
	clingo src/*.lp 0
