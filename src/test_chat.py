import asyncio
from chat_client import Message, ChatClient

async def main():
    # Create a chat client
    client = ChatClient()
    
    # Create a test message
    messages = [
        Message("system", "You are a helpful AI assistant."),
        Message("user", "Say hello and introduce yourself briefly.")
    ]
    
    try:
        # Send the message and get response
        response = await client.chat(messages)
        print("AI Response:", response)
    except Exception as e:
        print(f"Error: {str(e)}")

# Run the test
if __name__ == "__main__":
    asyncio.run(main())
