import requests

URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5-coder:7b"

messages = [
    {"role": "system", "content": "Du bist ein hilfreicher Programmierassistent. Antworte auf Deutsch und gib Code in Markdown-Codeblöcken aus."}
]

print(f"Chat mit {MODEL} gestartet. Mit 'exit' beenden.\n")

while True:
    user_input = input("Du: ").strip()
    if user_input.lower() in ("exit", "quit"):
        break
    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})
    try:
        response = requests.post(
            URL,
            json={"model": MODEL, "messages": messages, "stream": False},
            timeout=300,
        )
        response.raise_for_status()
        answer = response.json()["message"]["content"]
    except Exception as error:
        print(f"Fehler: {error}\n")
        messages.pop()
        continue

    messages.append({"role": "assistant", "content": answer})
    print(f"\nKI: {answer}\n")