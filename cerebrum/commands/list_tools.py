from cerebrum.manager.tool import ToolManager
from cerebrum.config.config_manager import config
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED

def list_tools():
    console = Console()
    
    with console.status("[bold green]Fetching tools from AgentHub..."):
        tool_manager = ToolManager(config.get_agent_hub_url())
        tools = tool_manager.list_available_tools()
    
    if not tools:
        console.print(Panel("[bold yellow]No tools found in AgentHub", title="Tool List"))
        return
    
    # Create a table with row separators and rounded borders
    table = Table(
        title="Available Tools in AgentHub",
        box=ROUNDED,
        show_header=True,
        header_style="bold white on blue",
        show_lines=True,  # This adds horizontal lines between rows
    )
    
    # Add columns to the table with adjusted widths
    table.add_column("Name", style="cyan bold", no_wrap=True)
    table.add_column("Description", style="green", width=40, overflow="fold")
    table.add_column("Author", style="blue", no_wrap=True)
    table.add_column("Latest Version", style="magenta", no_wrap=True)
    
    # Add rows to the table
    for tool in tools:
        name = tool.get("name", "Unknown")
        description = tool.get("description", "No description available")
        author = tool.get("author", "Unknown")
        version = tool.get("version", "N/A")
        
        table.add_row(name, description, author, version)
    
    # Print the table
    console.print("\n")  # Add some space before the table
    console.print(table)
    
    # Print summary
    summary = Text()
    summary.append(f"\nTotal tools available: ", style="bold")
    summary.append(f"{len(tools)}", style="bold green")
    console.print(summary)
    console.print("\n")  # Add some space after the summary

if __name__ == "__main__":
    list_tools()