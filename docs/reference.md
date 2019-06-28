# Core

## Enum `SpinDirections`

This enum class models the allowed spinning directions for a rotor.

A rotor can spin `CLOCKWISE`, meaning that is moving to *move forward* along its direction, or `COUNTER_CLOCKWISE`, meaning that is moving *backward* along its direction.

## Class Frame

This class models a generic reference frame. A reference frame is a three-dimensional space, which can be used to model the position of an object.

Properties:
x, y, z


# Motion

## Base Motion

### Description

time, position

A generic model of motion is characterized by the *time* and the *position* of the object.

Specialized models can be further extended.