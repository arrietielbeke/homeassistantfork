import asyncio
import logging
import time

_LOGGER = logging.getLogger(__name__)

DOMAIN = "nozzlecontrol"

NOZZLENUMBER = "nozzlenumber"
DFNOZZLENUMBER = "1"

TIMERTIME = "timetorun"


async def async_setup(hass, config):
    async def handletimer(call):
        _LOGGER.info("Call is made to handleTimer blah blah")

        nozzle_number = call.data.get(NOZZLENUMBER, DFNOZZLENUMBER)
        timer_time = call.data.get(TIMERTIME, 3)

        epcocht = time.time()
        datetime = time.ctime(epcocht)

        hass.states.async_set("person.arrie", "teststate")

        await timer(timer_time)

        _LOGGER.info(datetime)
        _LOGGER.info(nozzle_number)

    hass.services.async_register(DOMAIN, "handletimer", handletimer)

    async def timer(time_in_m: int):
        time_in_seconds = time_in_m * 60

        _LOGGER.info(time_in_seconds)

        while time_in_seconds != 0:
            await asyncio.sleep(1)
            time_in_seconds -= 1
            _LOGGER.info(time_in_seconds)

    return True
