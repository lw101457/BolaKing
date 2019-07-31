from typing import Optional

from pydantic import BaseModel


class Betting(BaseModel):
    id :int
    betting_sceen_id : int
    betting_time : str
    betting_money : int
    betting_result : str