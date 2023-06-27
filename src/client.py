import asyncio

async def send_message(message):
    reader, writer = await asyncio.open_connection('localhost', 8888)
    print(f"Send: {message!r}")
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    response = data.decode()
    print(f"Received {response!r}")

    print("Close the connection")
    writer.close()
    await writer.wait_closed()

asyncio.run(send_message("Hello, server!"))
