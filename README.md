# SOSA<sub>c</sub> ASP engine
To Do: Description

### Related publication
*Not published yet*

## What can you find in this repo?
This repository has the implementation of the ASP engine for generating SOSA<sub>c</sub> knowledge. It is composed of the following:

- The `src/` directory with the source code. In this directory, you can find: a) the ASP program `sosac_engine.lp` with the rules for basic inferences about the SOSA<sub>c</sub> restrictions and annotations; b) the ASP program `engine.lp` with rules for generating the SOSA<sub>c</sub> knowledge from the specification of a scenario; c) Python programs `sosac_clingo.py` and `sosac_terms.py` with the setup of the [Clingo ORM Clorm](https://github.com/potassco/clorm) for this project; d) the ASP program `graphs.lp` used for generting graphs that represent the solution calculated, with [Clingraph](https://github.com/potassco/clingraph); e) the Python program `eval_performance.py` for running a performance evaluation according to some configurable parameters; and f) the directory `kb/` with knowledge about how devices work.
- The `scenarios/` directory with the deployment descriptions used for validating the engine. Each scenario is composed of a `.lp`, and you can find four: a) the `minimal.lp` scenario composed by a single room and a single device (usefull to see easily the generated knowledge for a device); b) the `sampler.lp` scenario, with one device of each type deployed in three different rooms (allows to see one example of every device type modelled in the available knowledge); c) the `casas.lp` scenario, that is a realistic scenario extracted from one of the datasets of the Center for Advanced Studies in Adaptive Systems (CASAS); and d) the `temp_sensors.lp` scenario with two different types of temperature sensors that shows that the default feature of interest can be changed.
- The `examples` directory, with a simple example of how the generate SOSA<sub>c</sub> knowledge can be used for commonsense reasoning.
- The `docs/` directory with a `evaluation.csv` dataset that contains the results of a large performance evaluation.

In the root directory, the Makefile has the rules for running the engine, the examples, and so on.

## Try it yourself
To Do: setup/installation

```
$ pip install clingo
$ pip install clorm
$ pip install clingraph
$ sudo apt-get install graphviz
```

### Generate SOSA<sub>c</sub> knowledge for a scenario
To Do: scenarios execution - `make <scenario>.output`, `make <scenario.graphs>` and `make <scenario>.lp`

### Run the commonsense example
To Do: commonsense example execution - `make run-example`

### Evaluate the performance
To Do: run the performance evaluation - `make run-eval`

### Test the engine
To Do: testing - `make test-unit`
