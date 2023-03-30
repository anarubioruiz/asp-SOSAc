clean:
	$(RM) scenarios/*.output.lp
	$(RM) scenarios/*.graph
	$(RM) -r .pytest_cache

test-unit:
	pytest-3 test/test_unit_sosa.py test/test_unit_kb.py

run-example:
	clingo src/engine.lp src/sosac_engine.lp src/kb/*.lp examples/commonsense.lp -c time=night -c remove_device=sb01

%.lp:
	$(MAKE) $*.output $*.graphs

%.output:
	clingo src/engine.lp src/sosac_engine.lp src/kb/*.lp scenarios/$*.lp 0 -V0 --out-atomf=%s. | head -n 1 > scenarios/$*.output.lp

%.graphs:
	clingo src/graphs.lp scenarios/$*.output.lp 0 --outf=2 | clingraph --out=render --type=digraph --dir scenarios/ --name-format='$*.graph'

SIZE_FROM=1
SIZE_OFFSET=100
NUM_CASES=10
OUTPUT_FILE=evaluation.csv
ITERATIONS=5

run-eval:
	python3 src/eval_performance.py ${SIZE_FROM} ${SIZE_OFFSET} ${NUM_CASES} ${ITERATIONS} ${OUTPUT_FILE}
