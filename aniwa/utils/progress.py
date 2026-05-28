# aniwa/utils/progress.py
from contextlib import contextmanager
from time import perf_counter
from typing import Optional, Iterator
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.console import Console
from rich.status import Status
from aniwa.config_loader import get_config

console = Console()

class ProgressTracker:
    """Central progress tracking for profiling operations"""
    
    def __init__(self, verbose: bool = None):
        self.verbose = verbose if verbose is not None else get_config().verbose
        self.timings = {}
    
    @contextmanager
    def stage(self, name: str, total_steps: Optional[int] = None):
        """Context manager for profiling stages with timing"""
        start = perf_counter()
        
        if self.verbose:
            if total_steps:
                with Progress(
                    SpinnerColumn(),
                    TextColumn(f"[bold blue]{name}..."),
                    BarColumn(),
                    TimeElapsedColumn(),
                    console=console,
                    transient=True
                ) as progress:
                    task = progress.add_task("", total=total_steps)
                    yield lambda advance=1: progress.advance(task, advance)
            else:
                with Status(f"[bold blue]{name}...", console=console):
                    yield None
        else:
            yield None
        
        elapsed = perf_counter() - start
        self.timings[name] = elapsed
        
        if self.verbose:
            console.print(f"[dim]✓ {name} completed in {elapsed:.2f}s[/dim]")
    
    def show_timing_summary(self):
        """Display all timing information if verbose"""
        if self.verbose and self.timings:
            console.print("\n[bold cyan]Timing Summary:[/bold cyan]")
            for stage, duration in self.timings.items():
                console.print(f"  {stage}: {duration:.2f}s")