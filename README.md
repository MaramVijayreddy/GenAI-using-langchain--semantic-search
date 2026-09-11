# GenAI using LangChain

This repository contains my hands-on learning and implementation of **Generative AI concepts using LangChain**.

The project is being developed step by step as I learn and implement different LangChain components, LLMs, chat models, embedding models, prompt templates, and GenAI applications.

> **Note:** This repository is a work in progress. The README will be updated as new concepts and implementations are added.

---

## 📌 Current Implementations

### 1. LLMs

Implemented basic usage of Large Language Models with LangChain.

**File:**

```text
LLMs/
└── google.py
```

---

### 2. Chat Models

Implemented chat-model based interactions using different model providers.

**Files:**

```text
CHATMODELs/
├── googlemodel.py
└── OpenSource/
    ├── hf_locally.py
    └── hf_with_api.py
```

These implementations explore working with:

* Google chat models
* Open-source Hugging Face models
* Hugging Face models through API
* Local Hugging Face model usage

---

### 3. Embedding Models

Implemented embedding generation and similarity-related functionality.

**Files:**

```text
EmbbedModels/
├── hf_using_api.py
└── similarity.py
```

Current work includes:

* Generating embeddings using Hugging Face
* Working with embedding vectors
* Understanding similarity between text representations

---

### 4. Prompt Templates

Implemented LangChain's `PromptTemplate` for creating reusable and dynamic prompts.

The current prompt template accepts runtime inputs such as:

* Research paper input
* Explanation style
* Explanation length

Example:

```python
template = PromptTemplate(
    template="...",
    input_variables=[
        "paper_input",
        "style_input",
        "length_input"
    ],
    validate_template=True
)
```

The prompt structure remains fixed, while the actual values are supplied dynamically at runtime.

---

## 🔬 Research Tool

A simple **Streamlit-based Research Tool** has been implemented using LangChain and Hugging Face.

### Current technology stack

* Python
* LangChain
* Streamlit
* Hugging Face
* `ChatHuggingFace`
* `HuggingFaceEndpoint`
* `PromptTemplate`
* `python-dotenv`

The application allows the user to select the explanation style and length and then sends the dynamically generated prompt to the language model.

### Model

The current implementation uses:

```text
openai/gpt-oss-120b
```

through the Hugging Face endpoint.

### Basic flow

```text
User Input
    ↓
Streamlit UI
    ↓
PromptTemplate
    ↓
Dynamic Prompt
    ↓
Hugging Face Chat Model
    ↓
Generated Response
    ↓
Streamlit UI
```

---

## 📂 Project Structure

```text
GenAI-using-langchain--semantic-search/
│
├── CHATMODELs/
│   ├── OpenSource/
│   │   ├── hf_locally.py
│   │   └── hf_with_api.py
│   │
│   └── googlemodel.py
│
├── EmbbedModels/
│   ├── hf_using_api.py
│   └── similarity.py
│
├── LLMs/
│   └── google.py
│
├── promptgenerator.py
├── main.py
├── template.json
├── requirements.txt
├── test.py
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/MaramVijayreddy/GenAI-using-langchain--semantic-search.git
```

Move into the project directory:

```bash
cd GenAI-using-langchain--semantic-search
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project directory and add the required API credentials.

Example:

```env
HUGGINGFACEHUB_API_TOKEN=your_api_token
```

> Never commit API keys or other sensitive credentials to GitHub.

---

## ▶️ Run the Research Tool

Start the Streamlit application using:

```bash
streamlit run main.py
```

The application will open in your browser.

---

## 🛠️ Technologies Used

| Technology    | Purpose                          |
| ------------- | -------------------------------- |
| Python        | Programming language             |
| LangChain     | GenAI application framework      |
| Hugging Face  | LLM and embedding models         |
| Google Models | LLM / Chat Model experimentation |
| Streamlit     | User interface                   |
| python-dotenv | Environment variable management  |

---

## 📈 Project Status

**Status: 🚧 Work in Progress**

This repository represents my ongoing learning journey with **Generative AI and LangChain**.

I will continue adding new implementations as I learn and build them.
The documentation will be updated along with the project.
