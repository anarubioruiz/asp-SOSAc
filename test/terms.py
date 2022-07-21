from clorm import ComplexTerm, Predicate, ConstantField, IntegerField

class Sensor(Predicate):
    id = ConstantField

class ObservableProperty(Predicate):
    id = ConstantField

class Observation(Predicate):
    id = ConstantField

class isObservedBy(Predicate):
    observable_property = ConstantField
    sensor = ConstantField

class observes(Predicate):
    sensor = ConstantField
    observable_property = ConstantField

class makesObservation(Predicate):
    sensor = ConstantField
    observation = ConstantField

class madeBySensor(Predicate):
    observation = ConstantField
    sensor = ConstantField

    # ---------------------

class Actuator(Predicate):
    id = ConstantField

class Actuation(Predicate):
    id = ConstantField

class ActuatableProperty(Predicate):
    id = ConstantField

class makesActuation(Predicate):
    actuator = ConstantField
    actuation = ConstantField

class isActedOnBy(Predicate):
    actuable_property = ConstantField
    actuator = ConstantField

class madeByActuator(Predicate):
    actuation = ConstantField
    actuator = ConstantField

# class actsOnProperty(Predicate):
#     actuator = ConstantField
#     actuable_property = ConstantField




    # ---------------------

class hasFeatureOfInterest(Predicate):
    entity = ConstantField
    feature_of_interest = ConstantField
