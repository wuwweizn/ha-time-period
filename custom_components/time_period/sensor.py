"""Sensor platform for Time Period Sensor."""
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import EntityCategory
from homeassistant.util import dt as dt_util
from homeassistant.helpers.event import async_track_time_interval

TIME_PERIODS = [
    (0, 5, "深夜"),
    (5, 8, "清晨"),
    (8, 12, "上午"),
    (12, 14, "中午"),
    (14, 17, "下午"),
    (17, 19, "傍晚"),
    (19, 22, "晚上"),
    (22, 24, "午夜"),
]

def get_time_period():
    """返回当前时间段标签（使用 HA 时区）"""
    now = dt_util.now()
    hour = now.hour
    for start, end, label in TIME_PERIODS:
        if start <= hour < end:
            return label
    return "未知"

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up sensor entity from config entry."""
    sensor = TimePeriodSensor()
    async_add_entities([sensor], True)

    # 每1分钟刷新一次
    async def refresh_time_period(now):
        sensor.update_state()
        sensor.async_write_ha_state()

    async_track_time_interval(hass, refresh_time_period, timedelta(minutes=1))

class TimePeriodSensor(SensorEntity):
    """Sensor that reports current time period."""

    _attr_name = "当前时间段"
    _attr_icon = "mdi:clock-time-eight-outline"
    _attr_entity_category = EntityCategory.DIAGNOSTIC
    _attr_unique_id = "time_period_sensor"
    _attr_should_poll = False  # 不依赖轮询

    def __init__(self):
        self._state = get_time_period()

    @property
    def native_value(self):
        return self._state

    def update_state(self):
        """手动更新传感器状态"""
        self._state = get_time_period()
