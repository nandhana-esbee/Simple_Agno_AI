from fastapi import FastAPI
from agent import agent

app = FastAPI()

@app.post("/chat")
async def chat(query: str):
    response = agent.run(query)
    return {"response": response.content}