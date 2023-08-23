# SOSA<sup>c</sup>-Reasoner

## What can you find in this repo?
This repository contains the implementation of the ASP engine for generating SOSA<sup>c</sup> knowledge. It comprises the following:

- The `src/` directory, housing the source code. In this directory, you can find
a) the ASP program `sosac_engine.lp`, containing the rules for basic inferences about the SOSA<sup>c</sup> restrictions and annotations;
b) the ASP program `engine.lp`, containing rules for generating the SOSA<sup>c</sup> knowledge from a scenario's specification;
c) the Python programs `sosac_clingo.py` and `sosac_terms.py`, setting up the Clingo ORM Clorm for this project;
d) the ASP program `graphs.lp`, used for generating graphs that represent the calculated solution with Clingraph;
e) the Python program `eval_performance.py`, for running a performance evaluation based on configurable parameters; and
f) the `kb/` directory, containing knowledge about how devices work.

- The `scenarios/` directory, with deployment descriptions used for validating the engine. Each scenario consists of a `.lp` file:
a) `actuator.lp` and `sensor.lp` scenarios, composed of a single room and a single device (useful for easily understanding the generated knowledge for a device);
b) the `sampler.lp` scenario, which has one device of each type deployed in three different rooms (allows seeing one example of every device type modelled in the available knowledge);
c) the `casas.lp` scenario, a realistic scenario derived from one of the datasets from the Center for Advanced Studies in Adaptive Systems (CASAS); and
d) the `temp_sensors.lp` scenario, featuring two different types of temperature
sensors, demonstrating that the default feature of interest can be changed.

- The `examples/` directory, showcasing a simple example of how generated SOSA<sup>c</sup> knowledge can be used for commonsense reasoning.

- The `docs/` directory, containing the `evaluation.csv` dataset that includes the results of a large-scale performance evaluation.

In the root directory, the `Makefile` includes the rules for running the engine, the examples, and so forth.

## Try it yourself
You need to install the following Python libraries and deb packages:

```bash
$ pip install clingo
$ pip install clorm
$ pip install clingraph
$ sudo apt install graphviz
$ sudo apt install gringo
```

Other option is to use the Dockerfile provided in this repo. To do so, you need to install Docker and build the image:

```bash
$ docker build -t sosac-reasoner .
```

Then, you can run with the image any of the commands described below in the README by executing:

```bash
$ make docker-run CMD="<command>"
```

### Generate SOSA<sup>c</sup> knowledge for a scenario
To execute the SOSA<sup>c</sup>-Reasoner for any of the use cases you can find at `scenarios/` (sensor, actuator, sampler, casas), execute `make <scenario_name>.lp`. This command will create:

1. a file `scenarios/<scenario_name>.output.lp` with the ASP atoms forming the SOSA<sup>c</sup> instance of the use case, and
2. a file `scenarios/<scenario_name>.graph.pdf` with a graph representing the generated knowledge.

The command `make <scenario_name>.output.lp` only generates the knowledge file.

### Run the commonsense example
To run the commonsense example included in the `examples/` directory, execute:

```bash
$ make run-example
```
### Evaluate the performance
You can conduct your own performance evaluation with, for example, 10 different scenarios, the first one of size 1 and the following ones of an increasing size of 100, with 5 iterations for each. To do so, execute:

```bash
$ make run-eval SIZE_FROM=1 SIZE_OFFSET=100 NUM_CASES=10 ITERATIONS=5
```
The data obtained in an evaluation performed by the repo owners can be found at the `docs/` directory by default, in this case with the name `from1-offset100-10cases5times-evaluation.csv`

### Test the engine
To run the unit tests, install Pytest:

```bash
$ pip install pytest
```

Then, execute:

```bash
$ make test-unit
```
