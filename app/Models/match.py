from pydantic import field_validator, model_validator, BaseModel


class Match(BaseModel):
    match_id: int
    home_score: int
    away_score: int
    yellow_cards: int
    stadium: str
    home_team: str
    away_team: str

    @field_validator('home_score', 'away_score')
    @classmethod
    def validate_score(cls, value, info):
        if value < 0:
            raise ValueError(f'{info.field_name} cannot be negative')
        return value

    @model_validator(mode='after')
    def validate_teams(self):
        if self.home_team == self.away_team:
            raise ValueError('home team and away team are equal')
        return self
