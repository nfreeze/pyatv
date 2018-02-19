"""Functional tests for Airplay."""

import asyncio

from aiohttp import ClientSession
from aiohttp.test_utils import (AioHTTPTestCase, unittest_run_loop)

from pyatv.airplay import player
from tests.airplay.fake_airplay_device import (
    FakeAirPlayDevice, AirPlayUseCases)


STREAM = 'http://airplaystream'
START_POSITION = 0.8


class AirPlayPlayerTest(AioHTTPTestCase):

    def setUp(self):
        AioHTTPTestCase.setUp(self)

        # This is a hack that overrides asyncio.sleep to avoid making the test
        # slow. It also counts number of calls, since this is quite important
        # to the general function.
        player.asyncio.sleep = self.fake_asyncio_sleep
        self.no_of_sleeps = 0

    @asyncio.coroutine
    def get_application(self, loop=None):
        self.fake_device = FakeAirPlayDevice(self.loop, self)
        self.usecase = AirPlayUseCases(self.fake_device)
        return self.fake_device

    @asyncio.coroutine
    def fake_asyncio_sleep(self, time, loop):
        self.no_of_sleeps += 1

    @unittest_run_loop
    def test_play_video(self):
        self.usecase.airplay_playback_idle()
        self.usecase.airplay_playback_playing()
        self.usecase.airplay_playback_idle()

        session = ClientSession(loop=self.loop)
        aplay = player.AirPlayPlayer(
            self.loop, session, '127.0.0.1', port=self.server.port)
        yield from aplay.play_url(STREAM, position=START_POSITION)

        self.assertEqual(self.fake_device.last_airplay_url, STREAM)
        self.assertEqual(self.fake_device.last_airplay_start, START_POSITION)
        self.assertEqual(self.no_of_sleeps, 2)  # playback + idle = 3

        session.close()
