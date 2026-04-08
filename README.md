                      
<br/>
<div align="center">

# Simple Agno AI Chatbot
## An agent ai created using Agno framework

<br/>

## Basic knowledge

<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/8b6ddb9b-9d15-4497-adfc-6e590b4e7931" />

## Thinking
<img width="600" height="285" alt="image" src="https://github.com/user-attachments/assets/cd65ba0c-22bf-4c8d-bd66-6966e6a5deb2" />


 ## Tools used in the Chatbot
 </div>
 
 ### Calculator tool
 - Written as function in python
<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/ed7fb4d3-b007-4030-87b3-d10020a028cf" />

### Stock news tool
- Fetch stock data from the yfinance library in the Agno
![Stock news tool used]()

### Currency value tool
- Fetch current currency value from the user query using an external api
![Currency value tool used]()

### User data json storage
- Storing user data into a json from users who want to open a bank account
![User data stored]()

 ### Built With

- [Agno](https://www.agno.com/)
- [Fast API](https://fastapi.tiangolo.com/)
- [Streamlit UI](https://streamlit.io/)

### Used Model
- Ollama phi4-mini : installed locally and used

 ## Getting Started

Inorder to run the whole application first you need to start the backend server then run the frontend.
 ### Prerequisites

Inorder to run the application you should install the following:
- Python
- UV
- uvicorn

 ### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/nandhana-esbee/Simple_Agno_AI.git
   ```
2. Create a virtual environment and activate
   ```sh
   python -m venv yourvenv
   ```
   To activate in windows cmd:
   ```
   cd yourvenv/Scripts
   ```
   then type:
   ```
   activate
   ```
   Now do twice :
   ```
   cd ..
   ```
   For other platforms read : https://docs.python.org/3/library/venv.html
   
4. Install the requirements
   ```sh
   - cd Simple_Agno_AI
   - uv sync
   ```
5. Enter your env variables inside .env file
   ```sh
    EXCHANGE_API_URL=url
    EXCHANGE_API_KEY=key

   ```
6. Run the fastapi and streamlit in different terminals
    ```sh
    - uvicorn main:app --reload
    - streamlit run app.py
    ```
