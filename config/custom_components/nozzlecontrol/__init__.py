import asyncio
import logging
import time
import datetime

_LOGGER = logging.getLogger(__name__)

DOMAIN = "nozzlecontrol"

NOZZLEID = "nozzleid"
DFNOZZLENUMBER = "1"


async def async_setup(hass, config):
    async def handletimer(call):
        _LOGGER.info("Call is made to handleTimer blah blah")

        nozzle_number = call.data.get(NOZZLEID, DFNOZZLENUMBER)
        timer_time = hass.states.get("input_number.testnumber")

        hass.states.async_set("person.arrie", "teststate")

        await timer(int(float(timer_time.state)))

    hass.services.async_register(DOMAIN, "handletimer", handletimer)

    async def timer(time_in_m: int):
        time_in_seconds = time_in_m * 60

        _LOGGER.info(time_in_seconds)

        while time_in_seconds != 0:
            await asyncio.sleep(1)
            time_in_seconds -= 1
            _LOGGER.info(time_in_seconds)

            time_to_timestamp = datetime.timedelta(seconds=time_in_seconds)

            hass.states.async_set("input_datetime.countdown", time_to_timestamp)

    return True
