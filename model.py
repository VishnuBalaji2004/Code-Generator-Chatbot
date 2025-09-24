from langchain_groq import ChatGroq

def create_chat_gorq():
    """
    Function to initialize chat gorq
    Returns:
        ChatGroq
    """
    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2
        )