import asyncio
from tikv_client.asynchronous.transaction import Client

async def main():
    client = Client("127.0.0.1:2379")

    txn = await client.begin()
    await txn.put(b"k1", b"v1")
    await txn.put(b"k2", b"v2")
    await txn.put(b"k3", b"v3")
    await txn.put(b"k4", b"v4")
    await txn.put(b"k5", b"v5")
    await txn.commit()

    txn2 = await client.begin()
    print(await txn2.get(b"k3"))
    print(await txn2.batch_get([b"k1", b"k4"]))
    print(await txn2.scan(b"k1", limit=10, include_start=False))

event_loop = asyncio.get_event_loop()
asyncio.get_event_loop().run_until_complete(main())