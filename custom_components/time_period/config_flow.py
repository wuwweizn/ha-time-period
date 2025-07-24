"""Config flow for Time Period Sensor integration."""
import voluptuous as vol
from homeassistant import config_entries

DOMAIN = "time_period"

class TimePeriodConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Time Period Sensor."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Time Period Sensor", data={})

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )
