import os
from google import genai
from google.genai import types


STOP_TOKEN = "STOP123"
MODEL_ID = "gemini-2.5-flash"  


SYSTEM_INSTRUCTION = """
You are a debate partner role-playing as a hardline right-wing / ultra-conservative commentator.

GOAL:
- Debate the user on the chosen topic.
- Be persuasive, combative-but-civil, and rhetorically sharp.
- Use common conservative argument frames (limited government, traditional values,
  national sovereignty, law-and-order, fiscal restraint, skepticism of institutions).

STYLE:
- Keep responses punchy (aim 6–14 sentences), with 2–5 bullet points when helpful.
- Ask one pointed question back each turn to keep the debate moving.
- If the user makes multiple claims, pick the 1–2 most central claims to attack.

SAFETY / BOUNDARIES (must follow strictly):
- Do NOT use slurs or dehumanizing language.
- Do NOT advocate violence or “removal” of any protected group.
- Do NOT praise or support extremist organizations or ideologies.
- If the user asks for hate/violence or extremist propaganda, refuse and pivot to a policy-only discussion.
- You may criticize ideas, policies, and institutions, but not attack protected groups.
"""

def main() -> None:
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    topic = input("What topic do you want to debate? ").strip()
    if not topic:
        print("No topic entered. Exiting.")
        return

   
    chat = client.chats.create(
        model=MODEL_ID,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.8,
            max_output_tokens=1600,
            safety_settings=[
                # Keep hate/harassment safer. You can adjust, but don't disable safety.
                types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_ONLY_HIGH"),
                types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_ONLY_HIGH"),
                types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_ONLY_HIGH"),
            ],
        ),
    )

    
    opening_prompt = (
        f"Debate topic: {topic}\n"
        "Start with a strong opening statement from your hardline right-wing perspective, "
        "then ask me one pointed question."
    )
    resp = chat.send_message(opening_prompt)
    print("\nAI:", resp.text, "\n")

    while True:
        user_msg = input(f"You (type {STOP_TOKEN} to quit): ").strip()
        if user_msg == STOP_TOKEN:
            print("Conversation ended.")
            break
        if not user_msg:
            continue

        resp = chat.send_message(user_msg)
        print("\nAI:", resp.text, "\n")


if __name__ == "__main__":
    main()
