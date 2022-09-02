from clorm import ComplexTerm, Predicate, ConstantField, StringField


class ActID(Predicate):
    device = ConstantField
    act = ConstantField

class Device(Predicate):
    id = ConstantField
    klass = ConstantField

class locatedAt(Predicate):
    entity = ConstantField
    location = ConstantField

# CLINGO TERMS --------------

class Act(Predicate):
    id = ActID.Field

class FeatureOfInterest(Predicate):
    id = ConstantField

class Sensor(Predicate):
    id = ConstantField

class ObservableProperty(Predicate):
    id = ConstantField

class Observation(Predicate):
    id = ActID.Field

class Actuator(Predicate):
    id = ConstantField

class Actuation(Predicate):
    id = ActID.Field

class ActuatableProperty(Predicate):
    id = ConstantField

class Result(Predicate):
    id = ConstantField

class Platform(Predicate):
    id = ConstantField

class isObservedBy(Predicate):
    observable_property = ConstantField
    sensor = ConstantField

class observes(Predicate):
    sensor = ConstantField
    observable_property = ConstantField

class makesObservation(Predicate):
    sensor = ConstantField
    observation = ActID.Field

class madeBySensor(Predicate):
    observation = ActID.Field
    sensor = ConstantField

class observedProperty(Predicate):
    observation = ActID.Field
    observable_property = ConstantField

class makesActuation(Predicate):
    actuator = ConstantField
    actuation = ActID.Field

class isActedOnBy(Predicate):
    actuatable_property = ConstantField
    actuator = ConstantField

class madeByActuator(Predicate):
    actuation = ActID.Field
    actuator = ConstantField

class actsOnProperty(Predicate):
    actuator = ConstantField
    actuatable_property = ConstantField

class hasFeatureOfInterest(Predicate):
    act = ActID.Field
    feature_of_interest = ConstantField

class isFeatureOfInterestOf(Predicate):
    feature_of_interest = ConstantField
    act = ActID.Field

class isResultOf(Predicate):
    result = ConstantField
    act = ActID.Field

class hasResult(Predicate):
    act = ActID.Field
    result = StringField

class hasSimpleResult(Predicate):
    act = ActID.Field
    result = StringField

class hosts(Predicate):
    platform = ConstantField
    hosted = ConstantField

class isHostedBy(Predicate):
    hosted = ConstantField
    platform = ConstantField

class hasProperty(Predicate):
    feature_of_interest = ConstantField
    property = ConstantField
