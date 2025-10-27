import json
import click
from rich.console import Console
from rich.table import Table
from .calculator import estimate_points, Inputs, ModelParams

console = Console()

@click.group()
def main():
    """River Points Tracker CLI"""

@main.command()
@click.option("--stake", type=float, required=True, help="Stake amount (e.g., USD)")
@click.option("--engagement", "engagement_per_day", type=float, required=True, help="Daily engagement score")
@click.option("--days", type=int, required=True, help="Number of days")
@click.option("--stake-apr", type=float, default=0.10, show_default=True, help="Annual percentage rate used for stake points")
@click.option("--engagement-rate", type=float, default=0.4, show_default=True, help="Points per engagement unit")
@click.option("--multiplier", type=float, default=1.0, show_default=True, help="End multiplier applied to total points")
@click.option("--json", "as_json", is_flag=True, help="Output JSON")
def calc(stake, engagement_per_day, days, stake_apr, engagement_rate, multiplier, as_json):
    """Estimate points from inputs."""
    res = estimate_points(
        Inputs(stake=stake, engagement_per_day=engagement_per_day, days=days),
        ModelParams(stake_apr=stake_apr, engagement_rate=engagement_rate, multiplier=multiplier),
    )
    if as_json:
        console.print(json.dumps({
            "stake_points": res.stake_points,
            "engagement_points": res.engagement_points,
            "total_points": res.total_points
        }, indent=2))
        return

    table = Table(title="River Points Estimate")
    table.add_column("Metric")
    table.add_column("Value", justify="right")
    table.add_row("Stake Points", f"{res.stake_points:,.2f}")
    table.add_row("Engagement Points", f"{res.engagement_points:,.2f}")
    table.add_row("Total Points", f"{res.total_points:,.2f}")
    console.print(table)
