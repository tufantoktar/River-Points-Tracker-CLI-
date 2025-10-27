from dataclasses import dataclass

@dataclass
class ModelParams:
    stake_apr: float = 0.10           # 10% APR as a default guess
    engagement_rate: float = 0.4      # 0.4 points per engagement unit
    multiplier: float = 1.0           # staking/boost multiplier applied at the end

@dataclass
class Inputs:
    stake: float               # USD (or point base units)
    engagement_per_day: float  # e.g., summed interactions score per day
    days: int

@dataclass
class Result:
    stake_points: float
    engagement_points: float
    total_points: float

def estimate_points(inputs: Inputs, params: ModelParams = ModelParams()) -> Result:
    if inputs.days < 0:
        raise ValueError("days must be >= 0")
    if inputs.stake < 0 or inputs.engagement_per_day < 0:
        raise ValueError("stake and engagement_per_day must be >= 0")

    daily_stake_rate = params.stake_apr / 365.0
    stake_points = inputs.stake * daily_stake_rate * inputs.days
    engagement_points = inputs.engagement_per_day * params.engagement_rate * inputs.days
    total = (stake_points + engagement_points) * params.multiplier
    return Result(stake_points=stake_points, engagement_points=engagement_points, total_points=total)
