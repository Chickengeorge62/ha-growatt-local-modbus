"""Define constants for the Growatt Server component."""
from enum import StrEnum  # Verwende das Standardmodul ab Python 3.11
from homeassistant.const import Platform

# Kommunikationslayer
CONF_LAYER = "communication_layer"
CONF_SERIAL = "serial"
CONF_TCP = "tcp"
CONF_UDP = "udp"
CONF_FRAME = "modbus_frame"

# Serielle Kommunikation
CONF_SERIAL_PORT = "port"
CONF_BAUDRATE = "baudrate"
CONF_STOPBITS = "stopbits"
CONF_PARITY = "parity"
CONF_BYTESIZE = "bytesize"

# Geräteparameter
CONF_DC_STRING = "dc_string"
CONF_AC_PHASES = "ac_phases"
CONF_SERIAL_NUMBER = "serial_number"
CONF_FIRMWARE = "firmware"

# Power-Scan
CONF_POWER_SCAN_INTERVAL = "power_scan_interval"
CONF_POWER_SCAN_ENABLED = "power_scan_enabled"

# Paritätsoptionen
class ParityOptions(StrEnum):
    NONE = "None"
    EVEN = "Even"
    ODD = "Odd"
    MARK = "Mark"
    SPACE = "Space"

# Allgemeine Konstanten
DEFAULT_PLANT_ID = "0"
DEFAULT_NAME = "Growatt Modbus"
DOMAIN = "growatt_local"
PLATFORMS = [Platform.SENSOR]
