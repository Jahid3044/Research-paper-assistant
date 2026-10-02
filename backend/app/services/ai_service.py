from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_summary(paper_text):

    prompt = f"""
Analyze the following academic research paper.

Return:

1. Problem Statement
2. Research Objective
3. Methodology
4. Dataset
5. Preprocessing
6. Models
7. Evaluation Metrics
8. Main Results
9. Contributions
10. Limitations
11. Future Work

IMPORTANT:
Only use information available in the paper.
Do not invent values.

PAPER:

{paper_text}
"""

    response = client.responses.create(
        model=os.getenv(
            "OPENAI_CHAT_MODEL",
            "gpt-5"
        ),
        input=prompt
    )

    return response.output_text

def generate_research_gaps(paper_text):

    prompt = f"""
Analyze this research paper and identify potential research gaps.

Separate your answer into:

A. Explicit limitations stated by the authors

B. Potential methodological gaps

C. Dataset-related gaps

D. Possible future research directions

IMPORTANT:

Do not claim that an inferred gap was explicitly
stated by the authors.

Only make reasonable research-oriented observations.

PAPER:

{paper_text}
"""

    response = client.responses.create(
        model=os.getenv(
            "OPENAI_CHAT_MODEL",
            "gpt-5"
        ),
        input=prompt
    )

    return response.output_text

def answer_question(question, contexts):

    context_text = "\n\n".join(
        f"[Page {item['page_number']}]\n{item['content']}"
        for item in contexts
    )

    prompt = f"""
You are a research paper assistant.

Answer the question using ONLY the provided
paper excerpts.

Question:
{question}

Paper excerpts:
{context_text}

Rules:

1. Do not invent information.
2. If evidence is insufficient, say so.
3. Include page references.
4. Keep the answer concise.
"""

    response = client.responses.create(
        model=os.getenv(
            "OPENAI_CHAT_MODEL",
            "gpt-5"
        ),
        input=prompt
    )

    return response.output_text