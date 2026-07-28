import numpy as np
from openai import OpenAI, APITimeoutError, APIConnectionError

from devask.config import OPENAI_API_KEY
from devask import embedder

client = OpenAI(api_key=OPENAI_API_KEY, timeout=60.0)

TOP_K = 5


def search(question: str, index: dict) -> list[dict]:
    """Sawaal se sabse milte-julte chunks dhoondo."""
    q_vector = np.array(embedder.embed_query(question), dtype=np.float32)
    vectors = index["vectors"]

    # cosine similarity = normalized dot product
    q_norm = q_vector / np.linalg.norm(q_vector)
    v_norms = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)
    scores = v_norms @ q_norm

    top_indices = np.argsort(scores)[-TOP_K:][::-1]

    results = []
    for i in top_indices:
        chunk = index["chunks"][i]
        results.append({
            "path": chunk["path"],
            "content": chunk["content"],
            "score": float(scores[i]),
        })

    return results


def answer(question: str, chunks: list[dict]) -> str:
    """Retrieved chunks ke basis pe answer banao."""
    context = "\n\n---\n\n".join(
        f"File: {c['path']}\n\n{c['content']}" for c in chunks
    )

    system_prompt = (
        "You are a helpful assistant that answers questions about a codebase. "
        "Answer ONLY based on the provided code context. "
        "If the context doesn't contain the answer, say so honestly. "
        "Reference specific file names when relevant. Be concise."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Code context:\n\n{context}\n\nQuestion: {question}"},
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content
    except (APITimeoutError, APIConnectionError):
        return "OpenAI se connect nahi ho paya. Internet check kar."
    except Exception as e:
        return f"Kuch gadbad: {e}"