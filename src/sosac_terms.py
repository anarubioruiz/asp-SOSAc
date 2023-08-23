from clorm import ComplexTerm, Predicate, ConstantField, StringField


class ActID(Predicate):
    device = ConstantField
    act = ConstantField

class sosac_device(Predicate):
    id = ConstantField
    klass = ConstantField

class x_is_the_y_of_z(Predicate):
    value = ConstantField
    property = ConstantField
    entity = ConstantField

class x_is_the_interest_of_z(Predicate):
    interest = ConstantField
    entity = ConstantField

class sosakc_observesProperty(Predicate):
    klass = ConstantField
    observable_property = ConstantField

class sosakc_makesObservation(Predicate):
    klass = ConstantField
    observation_klass = ConstantField

class sosakc_actsOnProperty(Predicate):
    klass = ConstantField
    actuatable_property = ConstantField

class sosakc_makesActuation(Predicate):
    klass = ConstantField
    actuation_klass = ConstantField

class sosakc_hasFeatureOfInterest(Predicate):
    class _id(Predicate):
        device_klass = ConstantField
        activity_klass = ConstantField
        class Meta:
            is_tuple = True

    id = _id.Field
    property = ConstantField

# CLINGO TERMS --------------

class Act(Predicate):
    id = ActID.Field

class sosac_featureOfInterest(Predicate):
    id = ConstantField

class sosac_sensor(Predicate):
    id = ConstantField

class sosac_observableProperty(Predicate):
    id = ConstantField

class sosac_observation(Predicate):
    id = ActID.Field

class sosac_actuator(Predicate):
    id = ConstantField

class sosac_actuation(Predicate):
    id = ActID.Field

class sosac_actuatableProperty(Predicate):
    id = ConstantField

class sosac_result(Predicate):
    id = StringField

class sosac_platform(Predicate):
    id = ConstantField

class sosac_isObservedBy(Predicate):
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
    actuation = ActID.Field

class madeByActuator(Predicate):
    actuation = ActID.Field
    actuator = ConstantField

class actsOnProperty(Predicate):
    actuation = ActID.Field
    actuatable_property = ConstantField

class hasFeatureOfInterest(Predicate):
    act = ActID.Field
    feature_of_interest = ConstantField

class isFeatureOfInterestOf(Predicate):
    feature_of_interest = ConstantField
    act = ActID.Field

class isResultOf(Predicate):
    result = StringField
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
