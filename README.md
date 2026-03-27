# About
We're going modular this year! 2025-2026 files for the Utah Students Robotics Electrical Subteam can be found here.

## Folders
### Backplane
* The mainboard used to host and connect most of our other boards
* Uses 8-bit ISA connectors

### MCU/Digital Card
* Hosts the main Raspberry Pi Pico that interfaces with a mini PC and handles digital I/O

### Motor Driver Card
* Quadruple motor drivers capable of independently driving four linear actuators

### Analog Card
* Essentially an I/O expansion board that uses a second Pi Pico to handle exclusively analog signals.

### Power Delivery Board
* Routes 24 volts to the rest of the robot and produces 12v and 5v low-current power for general use.

### Protoboard
* Perfboard with 8-bit ISA edge connectors
* For physically prototyping other board designs

### ~~Realsense Adapter~~
* ~~Adapter for Intel Realsense T265~~

### Libraries
* KiCad symbol and footprint libraries
* Make sure to use relative paths!
  * `${KIPRJMOD}/../Libraries/USR.kicad_sym` for symbols
  * `${KIPRJMOD}/../Libraries/USR.pretty` for footprints

### ~~USB 2 to 3 bridge~~
~~???~
