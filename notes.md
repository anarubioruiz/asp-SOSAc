## Prioridades, elección de acciones por defecto
https://community.home-assistant.io/t/prioritize-one-automation-over-another-with-same-trigger/408032/2



Me gustaría diferencias en una transición sobre cuándo afecta al estado de su localización (a su localización con transitividad) o al estado de su contenedor (a su localización sin transitividad).

A su contenedor:

propertyValueOf(kitchen, location, fridge)
propertyValueOf(fridge, location, door_sensor1)

transitionTrigger(1, door_sensor, true).
transitionChange(1, container, open).

--> la nevera está open, no la cocina

A su localización:

propertyValueOf(kitchen, location, lamp1)
propertyValueOf(lamp1, location, smart_bulb1)

transitionTrigger(1, smart_bulb, on).
transitionChange(1, location, lit).

 --> La lámpara está iluminada, pero la cocina también


__________________________________________________________




transition(2).
transitionTrigger(2, blind_motor, up).
transitionCondition(2, context, daylighted).
transitionChange(2, location, lit).

instancia de transición:

transitionTrigger(2, blind_motor1, up).
transitionCondition(2, context, daylighted).
transitionChange(2, kitchen, lit).

#
