test-unit:
	pytest-3 test/test_unit_sosa.py test/test_unit_kb.py

run:
	clingo src/* src/kb/* 0

gen_graphs:
	clingo src/graphs.lp 0 --outf=2 | clingraph --out=render --type=digraph --dir graphs
