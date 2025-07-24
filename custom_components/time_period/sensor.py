"""Sensor platform for Time Period Sensor."""
from datetime import datetime, timedelta
import asyncio
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import EntityCategory

TIME_PERIODS = [
    (0, 5, "深夜"),
    (5, 7, "清晨"),
    (7, 11, "上午"),
    (11, 13, "中午"),
    (13, 17, "下午"),
    (17, 19, "傍晚"),
    (19, 23, "晚上"),
    (23, 24, "午夜"),
]

def get_time_period():
    hour = datetime.now().hour
    for start, end, label in TIME_PERIODS:
        if start <= hour < end:
            return label
    return "未知"

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up sensor entity from config entry."""
    async_add_entities([TimePeriodSensor()], True)

class TimePeriodSensor(SensorEntity):
    """Sensor that reports current time period."""

    _attr_name = "当前时间段"
    _attr_icon = "mdi:clock-time-eight-outline"
    _attr_entity_category = EntityCategory.DIAGNOSTIC
    _attr_unique_id = "time_period_sensor"
    _attr_should_poll = True  # 启用轮询自动更新

    def __init__(self):
        self._state = get_time_period()

    @property
    def native_value(self):
        return self._state

    async def async_update(self):
        self._state = get_time_period()
