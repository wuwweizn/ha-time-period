"""Config flow for Time Period Sensor integration."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

DOMAIN = "time_period"

class TimePeriodConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Time Period Sensor."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Time Period Sensor", data={})

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),  # 暂时无选项
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Return the options flow handler."""
        return TimePeriodOptionsFlowHandler(config_entry)


class TimePeriodOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow."""

    def __init__(self, config_entry: config_entries.ConfigEntry):
        # 不再手动设置 self.config_entry，以避免弃用警告
        pass

    async def async_step_init(self, user_input=None):
        """Handle the options step."""
        # 这里可以扩展配置选项，目前保持为空
        return self.async_create_entry(title="", data={})
