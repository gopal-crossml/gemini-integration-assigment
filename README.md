# gemini-integration-assigment
Understand basic text generation using a Large Language Model (LLM) and analyze the impact of generation parameters.

## :pushpin: Project Overview
The project consists of **two main experiments**:
1. **Text Generation Experiments**
   - Blog introduction generation
   - Product description generation
   - Short story generation
   - Parameter tuning for creativity vs determinism
2. **Multimodal Generation Experiments**
   - Image + text prompts
   - Interior design suggestions
   - Food recipe generation from images
---
## :hammer_and_wrench: Tech Stack
- **Language:** Python 3.10+
- **LLM:** Google Gemini
- **SDK:** `google-genai`
- **Image Processing:** Pillow (PIL)
---
## :gear: Installation
1. Clone the repository
    ```bash
        git clone https://github.com/gopal-crossml/gemini-integration-assigment.git
        cd gemini-integration-assigment
2. Create and activate a virtual environment (recommended)
    ```bash
        python -m venv venv
        source venv/bin/activate
3. Install dependencies
    ```bash
        pip install google-genai pillow
4. :closed_lock_with_key: API Key Setup
    Replace API-KEY in the code with your Gemini API key:
    python
        client = genai.Client(api_key="YOUR_API_KEY")
5. :arrow_forward: Usage
  :one: Text Generation Experiment
    This script explores how different prompts and parameters affect generated text.
        python Assignment1.py
    Prompts Used:
      -  Technical blog introduction
      -  Product description from bullet points
      -  Short story generation
    Parameters Tuned:
      -  temperature
      -  top_p
      -  max_output_tokens
   :two: Multimodal (Image + Text) Generation
      This script uses images + prompts to generate contextual responses.
          python Assignment2.py
   
   Parameters Tuned:
      -  temperature
      -  top_p
      -  top_k
:test_tube: Learning Outcomes
  -  Understand the impact of temperature on creativity
  -  Compare top_p vs top_k sampling
  -  Learn how Gemini handles multimodal inputs
  -  Build intuition for prompt engineering
