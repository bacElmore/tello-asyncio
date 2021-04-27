#!/usr/bin/env python3

import asyncio
from tello_asyncio import Tello

async def main():
    drone = Tello()
    try:
        await drone.connect()
        await drone.takeoff()
        await drone.move_up(50)
        await drone.move_down(50)
        await drone.move_left(50)
        await drone.move_right(50)
        await drone.move_forward(50)
        await drone.move_back(50)
        await drone.land()
    finally:
        await drone.disconnect()

asyncio.run(main())