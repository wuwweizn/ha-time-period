"""Time Period Sensor Integration."""
from __future__ import annotations
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "time_period"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the integration via YAML (not used)."""
    return True  # 不支持 YAML 配置，只返回 True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up time period sensor from a config entry."""
    # 你可以在这里初始化你的平台，注册实体等
    # 比如 forward 到 sensor 平台
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")
