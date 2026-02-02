#!/usr/bin/env python3

# "How does instructor force structured output?"

# Step 1: Use it (30 mins)

import instructor
from openai import OpenAI
from pydantic import BaseModel

# Point OpenAI client at Ollama's local server
client = instructor.from_openai(
    OpenAI(base_url="http://localhost:11434/v1", api_key="ollama"),
    mode=instructor.Mode.JSON
)

class Person(BaseModel):
    name: str
    age: int
    occupation: str
    location: str

person = client.chat.completions.create(
    model="llama3.2",
    messages=[{"role": "user", 
    "content": "Extract: Max was about to start his new job as a software engineer in New York City. He is 28 years old and has a bachelor's degree in computer science."}],
    response_model=Person,
)

print(person)