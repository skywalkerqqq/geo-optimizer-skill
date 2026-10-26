"""CLI command: geo logs."""

from __future__ import annotations

import json
from dataclasses import asdict

import click

from geo_optimizer.core.log_analyzer import analyze_log_file


@click.command(name="logs")
@click.option("--file", "log_file", required=True, type=click.Path(exists=True), help="Path to server access log")
@click.option(
    "--format",
    "output_format",
    type=click.Choice(["text", "json"]),
    default="text",
    show_default=True,
    help="Output format",
)
def logs(log_file: str, output_format: str) -> None:
    """Analyze server logs for AI crawler activity."""
    result = analyze_log_file(log_file)

    if output_format == "json":
        click.echo(json.dumps(asdict(result), indent=2))
    else:
        _print_text(result)


def _print_text(result) -> None:
    """Format log analysis as human-readable text."""
    click.echo("")
    click.echo("🤖 " * 15)
    click.echo("  AI CRAWLER REPORT")
    click.echo("🤖 " * 15)
    click.echo(f"\n  File: {result.log_file}")
    click.echo(f"  Lines: {result.total_lines:,} | AI requests: {result.ai_requests:,}")
    if result.date_range_start:
        click.echo(f"  Period: {result.date_range_start} → {result.date_range_end}")

    if result.bots:
        click.echo(f"\n  {'Bot':<25} {'Visits':>8} {'Pages':>8}")
        click.echo(f"  {'─' * 25} {'─' * 8} {'─' * 8}")
        for bot in result.bots:
            click.echo(f"  {bot.bot_name:<25} {bot.visits:>8,} {bot.unique_pages:>8}")

    if result.top_pages:
        click.echo("\n  📄 Top crawled pages:")
        for i, page in enumerate(result.top_pages[:10], 1):
            bots_str = ", ".join(page.bots[:3])
            click.echo(f"  {i:>3}. {page.path} ({page.total_visits} visits — {bots_str})")

    if not result.bots:
        click.echo("\n  No AI crawler activity found in this log file.")
