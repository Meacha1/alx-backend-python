#!/usr/bin/env python3
"""
Basic asynchronous syntax
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive)
    and eventually returns it.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
