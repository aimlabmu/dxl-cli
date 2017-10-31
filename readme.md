# dxl-cli

A simple command line wrapper to test dynamixel ax-12 motor without using Roboplus program.

## Dependency

This python class only relies on [`pyax12` library](https://github.com/jeremiedecock/pyax12) which can be installed as follows

```sh
pip install --pre pyax12
```

## Usage

You can call information below anytime by calling `MotorManager.help()`.

```python
# List of methods available.
====== Connection ======
# --- Import
from dxlcli import MotorManager

# --- Instantiate class
m = MotorManager(p="/dev/ttyUSB0", baudRate=1000000, scanLimit=20, defaultSpeed=90)
# *** USE COMXX on Windows ***

# --- Terminate connection
m.terminateConnection()

# --- Get connected motor ids
m.getConnectIds()

====== ID settings ======
# --- Set new id to specified motor id
m.setNewIdOf(self, motor_id, new_id):

====== Printing Information ======
# --- All available baudrates
m.printAvailableBaudrates()

# --- Motor status table
m.printControlTable(motor_id)

====== Position Control ======
# --- Get
m.getPositionOf(motor_id)
m.getPositionAll()

# --- Set
m.setPositionOf(self, motor_id, pos=512, speed=90)
m.setPositionAll(self, pos=512, speed=90)

====== Baudrate Control ======
# --- Get
m.getBaudrateOf(motor_id)
m.getBaudrateAll()

# --- Set
m.setBaudrateOf(motor_id, baudId=1)
m.setBaudrateAll(baudId=1)
```