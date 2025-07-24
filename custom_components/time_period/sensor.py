from datetime import datetime
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

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([TimePeriodSensor()], True)

async def async_setup_entry(hass, config_entry, async_add_entities):
    async_add_entities([TimePeriodSensor()], True)

class TimePeriodSensor(SensorEntity):
    def __init__(self):
        self._attr_name = "当前时间段"
        self._attr_icon = "mdi:clock-time-eight-outline"
        self._attr_entity_category = EntityCategory.DIAGNOSTIC

    @property
    def unique_id(self):
        return "time_period_sensor"

    @property
    def state(self):
        return get_time_period()

    async def async_update(self):
        # 每次更新状态
        self._attr_native_value = get_time_period()
