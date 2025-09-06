"""Growatt server PV inverter sensor integration."""
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import (
    CONF_LAYER,
    CONF_SERIAL,
    CONF_SERIAL_PORT,
    CONF_BAUDRATE,
    CONF_BYTESIZE,
    CONF_PARITY,
    CONF_STOPBITS,
    CONF_TCP,
    CONF_UDP,
    CONF_IP_ADDRESS,
    CONF_PORT,
    CONF_TYPE,
)
from .API.const import DeviceTypes
from .API.growatt import GrowattDevice, GrowattSerial, GrowattNetwork

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Growatt integration from a config entry."""
    try:
        if entry.data[CONF_LAYER] == CONF_SERIAL:
            device_layer = GrowattSerial(
                entry.data[CONF_SERIAL_PORT],
                entry.data[CONF_BAUDRATE],
                entry.data[CONF_STOPBITS],
                entry.data[CONF_PARITY],
                entry.data[CONF_BYTESIZE],
            )
        elif entry.data[CONF_LAYER] in (CONF_TCP, CONF_UDP):
            device_layer = GrowattNetwork(
                entry.data[CONF_LAYER],
                entry.data[CONF_IP_ADDRESS],
                entry.data[CONF_PORT],
            )
        else:
            _LOGGER.error(f"Unsupported communication layer: {entry.data[CONF_LAYER]}")
            return False

        device = GrowattDevice(
            device_layer,
            DeviceTypes(entry.data[CONF_TYPE]),
            entry.data[CONF_ADDRESS],
        )

        await device.connect()
        # Weitere Initialisierung hier...

        return True

    except Exception as err:
        _LOGGER.error(f"Error setting up Growatt integration: {err}")
        return False