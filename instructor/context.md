# What is instructor used for?

instructor solves a common frustration: 
LLMs return text, but your code needs structured data.

Say you ask Claude to extract a person's details from text. 

Without instructor, you get a string back—maybe JSON, maybe not—and you have to parse it, hope the format is right, handle failures, etc.

Instructor lets you define a Pydantic model (like Person with name, age, occupation fields), pass it to the LLM call, and get back a validated Python object directly. 

If the LLM's response doesn't match the schema, instructor automatically retries with the validation errors included in the prompt.

It's essentially "type-safe LLM outputs" in a small, clean package.

## Why it matters practically:

The moment you build anything real with LLMs—agents, data extraction pipelines, structured RAG—you need reliable structured output. Instructor is one of the most popular solutions, and understanding how it works gives you transferable knowledge.