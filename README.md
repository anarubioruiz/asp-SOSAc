# SOSA<sub>c</sub> ASP engine

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
You need to install the following Python libraries and deb packages:

```bash
$ pip install clingo
$ pip install clorm
$ pip install clingraph
$ sudo apt-get install graphviz
```

### Generate SOSA<sub>c</sub> knowledge for a scenario
To start the knowledge generation process for any of the use cases addressed in the paper (*minimal*, *sampler* or *casas*), execute:
`make <scenario>.out`. This command will create 1) a file scenarios/output.lp with the ASP atoms conforming the SOSA<sub>c</sub> instance of the usecase, and 2) a file scenarios/graph_output.pdf with a grap representing the knowledge generated. The command `make <scenario>.lp` only generates the knowledge file.

### Run the commonsense example
To run the commonsense example addressed in the paper, run:

```bash
make run-example
```
### Evaluate the performance
You can conduct your own performance evaluation with:

```bash
make run-eval
```

### Test the engine

```bash
make test-unit
```
