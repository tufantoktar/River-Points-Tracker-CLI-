from river_points.calculator import estimate_points, Inputs, ModelParams

def test_zero_days():
    res = estimate_points(Inputs(stake=1000, engagement_per_day=100, days=0))
    assert res.total_points == 0

def test_basic_calc():
    params = ModelParams(stake_apr=0.10, engagement_rate=0.4, multiplier=1.0)
    res = estimate_points(Inputs(stake=1000, engagement_per_day=100, days=10), params)
    # stake: 1000 * 0.10 / 365 * 10 = ~2.7397
    # engagement: 100 * 0.4 * 10 = 400
    assert abs(res.stake_points - 2.7397) < 0.01
    assert abs(res.engagement_points - 400) < 0.01
    assert abs(res.total_points - (res.stake_points + res.engagement_points)) < 0.001

def test_negative_inputs():
    try:
        estimate_points(Inputs(stake=-1, engagement_per_day=0, days=1))
        assert False, "should raise"
    except ValueError:
        pass
