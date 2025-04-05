from pydantic import BaseModel


class Word(BaseModel):
    id: int
    direction: int
    pos: list[int]
    text: str | None = None


class Towers(BaseModel):
    done_towers: list[dict]
    score: float
    tower: list[Word]
