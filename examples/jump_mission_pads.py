#!/usr/bin/env python3

import asyncio
from tello_asyncio import Tello, Vector

async def main():
    drone = Tello()
    try:
        await drone.connect()
        await drone.takeoff()
        await drone.enable_mission_pads()
        await drone.jump(relative_position=Vector(0, 0, 100), speed=25, yaw=45, from_mission_pad=1, to_mission_pad=2)
        await drone.land()
    finally:
        await drone.disconnect()

asyncio.run(main())