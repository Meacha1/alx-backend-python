#!/usr/bin/env python3
"""
Concurrent coroutines
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds
        for each wait_random call.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for task in tasks:
        delay = await task
        delays.append(delay)

    return sorted(delays)
