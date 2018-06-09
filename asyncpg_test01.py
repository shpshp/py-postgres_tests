#!/usr/bin/python3

import asyncio
import asyncpg

async def run():
    conn = await asyncpg.connect(user='user', password='1', database='testdb', host='localhost')
    values = await conn.fetch('''SELECT * FROM Products''')
    await conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
