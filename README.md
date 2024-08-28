# Flask Web Chat App

This is a simple real-time web chat application built with Flask and Flask-SocketIO. Users can join chat rooms, send messages, and interact with others instantly through a responsive web interface.

## Demo

Check out the project repository [here](https://github.com/Den-1114/Flask-Chatapp).

## Features

- Real-time messaging using WebSockets and Flask-SocketIO
- Multiple users can join and participate in the chat
- Responsive and dynamic chat interface
- Messages broadcasted to all connected clients in real-time

## Technologies Used

- **Flask**: Micro web framework for Python to build the backend.
- **Flask-SocketIO**: Handles WebSockets for real-time communication.
- **HTML/CSS/JavaScript**: Frontend technologies for the chat interface.
- **jQuery**: Handles client-side events and dynamic content.
- **Bootstrap**: Provides a simple and responsive UI.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine
- `pip` (Python package manager) installed
- Basic understanding of Python, HTML, and JavaScript

### Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/Den-1114/Flask-Chatapp.git
    cd Flask-Chatapp
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```bash
    python app.py
    ```

5. Open your web browser and go to:
    ```
    http://localhost:5000
    ```

## Usage
- Once the server is running, users can open the chat app in their browser. They can enter a chat room, send messages, and see messages from other users in real-time. The messages are broadcasted to everyone connected to the chat room.
Example Code
Here’s an overview of the core Flask app and SocketIO setup:
