from aiohttp import web
import asyncio

async def handle_card(request):
    card = await request.json()
    if card["action"] == "reverse_string":
        text = card["payload"]["text"]
        response_card = {
            "type": "response",
            "action": "reverse_string",
            "payload": {"result": text[::-1]}
        }
        return web.json_response(response_card)
    return web.json_response({"error": "unknown action"})

app = web.Application()
app.add_routes([web.post("/card", handle_card)])

if __name__ == "__main__":
    web.run_app(app, port=8002)
