from openai import OpenAI, APITimeoutError, APIConnectionError
from gitroast.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def roast_diff(diff: str) -> str:
    """Diff ko OpenAI bhej ke ek savage roast wapas lao."""
    system_prompt = (
        "Tu ek savage senior developer hai jo code review mein "
        "logon ki band bajata hai. Tujhe ek git diff diya jayega. "
        "Us code ko roast kar — funny, sarcastic, thoda mean, "
        "par actually valid technical points ke saath. "
        "Hinglish mein bol. 3-4 lines se zyada mat kar. "
        "Emoji use kar sakta hai."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Is diff ko roast kar:\n\n{diff}"},
            ],
            temperature=0.9,
        )
        return response.choices[0].message.content
    except (APITimeoutError, APIConnectionError):
        return "⚠️ OpenAI se connect nahi ho paya. Internet check kar aur dobara try kar."
    except Exception as e:
        return f"⚠️ Kuch gadbad ho gayi: {e}"


