from pydantic import BaseModel, Field


class Subtopic(BaseModel):
    heading: str
    points: list[str] = Field(default_factory=list)


class Topic(BaseModel):
    heading: str
    explanation: str
    subtopics: list[Subtopic] = Field(default_factory=list)


class KeyConcept(BaseModel):
    term: str
    definition: str


class Example(BaseModel):
    description: str
    related_topic: str = ""


class Notes(BaseModel):
    title: str
    overview: str
    topics: list[Topic]
    key_concepts: list[KeyConcept] = Field(default_factory=list)
    examples: list[Example] = Field(default_factory=list)
    summary_bullets: list[str]
    conclusion: str