# Decisions

## Why Python instead of JavaScript for the backend?

For this project, Python is the main language for Artificial Intelligence, and python has a great foundation within most of Large Language Model (LLM) libraries. Whereas JavaScript, for an alternative,
would let me use one language everywhere. The downside is that I
have to learn two languages, Python and TypeScript, for the frontend.

## Why fastapi instead of flask or django in this project?

for an LLM / AI full stack web, i choose FASTAPI for the framework on my backend because it is arranged with an async-first design, that lets the server handle slow LLM responses and RAG pipelines without freezing . It uses Python type hints and Pydantic to validate complex JSON payloads automatically, good for AI agents and thanks to it, for me FASTAPI beats Flask and Django in terms for a better framework on AI / LLM powered web backends

## Why a monorepo?

## Why a .env file for configuration?

## Why wrap the library’s exceptions in TranscriptUnavailable?

## Why do the tests use a fake API instead of the real YouTube?

## Why is the real-call test marked live and skipped by default?

## What is the IP-blocking problem, what did you do about it now, and what are your options for deployment (proxies, a Whisper fallback, ## paste-your-own-transcript option)?
