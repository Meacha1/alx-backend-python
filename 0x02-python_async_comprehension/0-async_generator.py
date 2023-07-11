#!/usr/bin/env python3
"""
Module for Async Generator
"""

import asyncio
import random


async def async_generator() -> float:
    """
    Coroutine that generates and yields random numbers
    between 0 and 10 asynchronously.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
