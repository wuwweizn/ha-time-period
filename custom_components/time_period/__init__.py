"""Time Period Sensor integration."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up integration via YAML (not used)."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up integration from UI config flow."""
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload integration."""
    return await hass.config_entries.async_unload_platforms(entry, ["sensor"])
