# Auto-Reply AI Chatbot

This project automates the process of interacting with a chat application. It is designed to analyze chat history and generate humorous responses using OpenAI's GPT-3.5-turbo model. The virtual assistant, named **Naruto**, is a character that roasts people in a funny way based on the chat history.

---

## Features

- **Automated Chat Interaction**  
  Uses `pyautogui` to perform mouse and keyboard operations, interacting with the chat application without manual intervention.

- **Chat History Analysis**  
  Copies chat history from the chat application and analyzes it to determine if the last message was sent by a specific user.

- **Humorous Response Generation**  
  Integrates with OpenAI's GPT-3.5-turbo model to generate funny, roast-style responses based on the analyzed chat history.

- **Clipboard Operations**  
  Utilizes `pyperclip` to copy and paste text, facilitating the retrieval and insertion of chat messages.

---

## Workflow

1. **Initialization and Setup**  
   - Click on the Chrome icon to open the chat application.  
   - Wait for a brief period to ensure the application is open and ready for interaction.

2. **Chat History Retrieval**  
   - Periodically select and copy chat history by dragging the mouse over the chat area and using the copy shortcut.  
   - Retrieve the copied text from the clipboard.

3. **Message Analysis**  
   - Analyze the copied chat history to check if the last message is from a specific user.  
   - If the last message is from the target user, send the chat history to OpenAI's GPT-3.5-turbo to generate a humorous response.  
   - Copy the generated response to the clipboard.

4. **Send Response**  
   - Click on the chat input area and paste the generated response.  
   - Press 'Enter' to send the response.

---

## Libraries Used

- **`pyautogui`**: For automating mouse and keyboard interactions.  
- **`time`**: For adding delays between operations.  
- **`pyperclip`**: For clipboard operations.  
- **`openai`**: For interacting with OpenAI's GPT-3.5-turbo model.

---

## How to Use

1. Install the required libraries:
   ```bash
   pip install pyautogui pyperclip openai


## How to Run
1. Clone the repository (if you haven't already):
   ```bash
   git clone https://github.com/Rumsha703/Python-Mastery.git