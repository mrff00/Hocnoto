import json



def generate_prompt(transcript: str) -> str:
    prompt = f"""
    Act as an expert study-notes assistant. Using the provided YouTube transcript as your **only source**, 
    create concise but comprehensive study notes.
    Do not introduce outside information, assumptions, examples, statistics, or citations;
    if something is missing or unclear, state “Not covered in transcript.” 
    Organize the notes with a descriptive title and one-sentence overview, 
    5–8 bullet executive summary, and structured sections covering key concepts, definitions, transcript examples or processes, 
    and their importance.
    Bold essential terms and include timestamps only when available.
    Finish with a glossary table (Term | Simple definition | Why it matters), 
    5–7 key takeaways, a concise conclusion, common misconceptions, unexplained concepts or gaps, and a practical 
    7-day study plan requiring 15–30 minutes daily. Prioritize conceptual understanding, retention, and exam preparation while 
    compressing lengthy content without losing essential information.
    Here is the transcript:

    {transcript}


"""
    return prompt





