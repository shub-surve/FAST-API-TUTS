import time
import asyncio
import aiohttp

async def make_req(session, req_n):
    url = "https://httpbin.org/get"
    print(f"making request {req_n}")
    async with session.get(url) as resp:
        if resp.status == 200:
            await resp.text()

async def main():
    req_count = 10
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *[make_req(session, i) for i in range(req_count)]  
        )

loop = asyncio.get_event_loop()
start = time.time()
loop.run_until_complete(main())
end = time.time()

print("time elapsed: ", end - start)

