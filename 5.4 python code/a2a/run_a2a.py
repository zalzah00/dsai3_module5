import aiohttp
import asyncio

async def send_card(agent_url, card):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{agent_url}/card", json=card) as resp:
            return await resp.json()

async def main():
    # Step 1: Send a reverse_string task to Beta
    card_to_beta = {
        "type": "task",
        "action": "reverse_string",
        "payload": {"text": "hello world"}
    }
    beta_response = await send_card("http://localhost:8002", card_to_beta)
    print("Beta Response:", beta_response)

    # Step 2: Send a count_words task to Alpha
    card_to_alpha = {
        "type": "task",
        "action": "count_words",
        "payload": {"text": "hello world from Beta"}
    }
    alpha_response = await send_card("http://localhost:8001", card_to_alpha)
    print("Alpha Response:", alpha_response)

asyncio.run(main())
