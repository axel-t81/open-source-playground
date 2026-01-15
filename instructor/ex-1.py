#!/usr/bin/env python3

# "How does instructor force structured output?"

# Step 1: Use it (30 mins)

import instructor
from anthropic import Anthropic
from pydantic import BaseModel

client = instructor.from_anthropic(Anthropic())

class Person(BaseModel):
    name: str
    age: int
    occupation: str

person = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Extract: John is a 32 year old carpenter"}],
    response_model=Person,
)

print(person)