from openai import OpenAI, APITimeoutError, APIConnectionError

from devask.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY, timeout=60.0)

MODEL = "text-embedding-3-small"
BATCH_SIZE = 100


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Text ki list ko vectors mein badlo (batch mein)."""
    vectors = []

    for i in range(0, len(texts), BATCH_SIZE):
        batch = texts[i:i + BATCH_SIZE]
        response = client.embeddings.create(model=MODEL, input=batch)
        vectors.extend([item.embedding for item in response.data])

    return vectors


def embed_query(text: str) -> list[float]:
    """Ek single sawaal ko vector banao."""
    response = client.embeddings.create(model=MODEL, input=[text])
    return response.data[0].embedding