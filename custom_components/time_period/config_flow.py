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
            data_schema=vol.Schema({}),
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get options flow."""
        return TimePeriodOptionsFlowHandler(config_entry)

class TimePeriodOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle config flow options."""

    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        # 这里可扩展时间段配置，目前保持空
        return self.async_create_entry(title="", data={})
