# About
We're going modular this year! 2025-2026 files for the Utah Students Robotics Electrical Subteam can be found here.

## Folders
### Backplane
* The mainboard used to host and connect most of our other boards
* Uses 8-bit ISA connectors

### MCU Card
* Hosts our two Raspberry Pi Pico W's

### Motor Driver Card (TBA)

### Analog Card (TBA)

### Power Delivery Board (TBA)

### Protoboard
* Perfboard with 8-bit ISA edge connectors
* For physically prototyping other board designs

### Realsense Adapter
* Adapter for Intel Realsense T265

### Libraries
* KiCad symbol and footprint libraries
* Make sure to use relative paths!
  * `${KIPRJMOD}/../Libraries/USR.kicad_sym` for symbols
  * `${KIPRJMOD}/../Libraries/USR.pretty` for footprints

### USB 2 to 3 bridge
???