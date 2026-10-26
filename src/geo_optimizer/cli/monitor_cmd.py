"""CLI command: geo monitor."""

from __future__ import annotations

import sys
from pathlib import Path

import click

from geo_optimizer.cli.formatters import format_monitor_json, format_monitor_text
from geo_optimizer.core.monitor import normalize_monitor_domain, run_passive_monitor
from geo_optimizer.models.config import DEFAULT_HISTORY_RETENTION_DAYS
from geo_optimizer.models.project_config import load_config
from geo_optimizer.utils.validators import validate_public_url


@click.command(name="monitor")
@click.option("--domain", required=True, help="Domain to monitor in passive AI-visibility mode")
@click.option(
    "--format",
    "output_format",
    type=click.Choice(["text", "json"]),
    default="text",
    show_default=True,
    help="Output format",
)
@click.option("--output", "output_file", default=None, help="Output file path (optional)")
@click.option("--cache", is_flag=True, help="Use local HTTP cache for the audit step")
@click.option("--config", "config_file", default=None, help="Path to .geo-optimizer.yml config file")
@click.option(
    "--save-history/--no-save-history",
    default=True,
    show_default=True,
    help="Persist the homepage audit in the local tracking database",
)
@click.option(
    "--retention-days",
    default=DEFAULT_HISTORY_RETENTION_DAYS,
    show_default=True,
    type=int,
    help="Retention window for local snapshots",
)
@click.option("--history-db", default=None, hidden=True, help="Override local tracking DB path")
def monitor(domain, output_format, output_file, cache, config_file, save_history, retention_days, history_db):
    """Run passive AI visibility monitoring for a domain."""
    normalized = normalize_monitor_domain(domain)
    safe, reason = validate_public_url(normalized)
    if not safe:
        click.echo(f"\n❌ Unsafe domain: {reason}", err=True)
        sys.exit(1)

    config_path = Path(config_file) if config_file else None
    project_config = load_config(config_path)
    history_path = Path(history_db) if history_db else None

    result = run_passive_monitor(
        normalized,
        use_cache=cache,
        project_config=project_config,
        save_history=save_history,
        retention_days=retention_days,
        history_db=history_path,
    )
    output = format_monitor_json(result) if output_format == "json" else format_monitor_text(result)

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(output)
        click.echo(f"✅ Report written to: {output_file}")
        return

    click.echo(output)
