# Testing guide
Here you will find a brief description of the types of tests implemented.

Read the main README (at the root of the repo) for more information about no-SOSA entities used and other considerations.

## Unit tests for SOSA: `test_unit_sosa.py`

These tests have been implemented to test SOSA entities and their relations with other SOSA entities. For example, that _observes_ is the inverse relation of _isObservedBy_:

- _Sensor_ **_observes_** _ObservableProperty_
- _ObservableProperty_ **_isObservedBy_** _Sensor_

Also some Scott concepts have been introduced in order to group some SOSA entities. For instance, _Act_ is an entity type that groups _Actuations_, _Observations_ and _Samplings_, and it is used in the relation _hasFeatureOfInterest_. In this relation, the domain entities are _Acts_ and the range of entities covered are _FeaturesOfInterest_:

- _Act_ **_hasFeatureOfInterest_** _FeatureOfIinterest_

## Scenario tests for SOSA
