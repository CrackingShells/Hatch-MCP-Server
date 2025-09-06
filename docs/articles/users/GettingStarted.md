# Getting Started with Hatch-MCP-Server

This article is about:

- Understanding what HatchMCP is and why you need it
- Installing and setting up the wrapper in your MCP server
- Creating your first MCP server with citation capabilities
- Testing your implementation

## What is HatchMCP?

HatchMCP is a wrapper around FastMCP servers that adds automatic citation capabilities to MCP (Model Context Protocol) servers. It enables scientific transparency and attribution by automatically exposing citation information as MCP resources.

### Key Features

- **Citation Resources**: Automatically exposes citation information for both original tools/algorithms and MCP server implementations
- **FastMCP Integration**: Seamlessly wraps FastMCP servers without changing your existing code
- **Scientific Attribution**: Supports proper attribution in scientific computing and autonomous agent contexts
- **Automatic URI Generation**: Creates standardized citation URIs based on your server name

## Installation

Install directly from the repository:

```bash
pip install git+https://github.com/CrackingShells/Hatch-MCP-Server.git
```

Or install a local copy:

```bash
git clone https://github.com/CrackingShells/Hatch-MCP-Server.git
cd Hatch-MCP-Server
pip install .
```

## Quick Start

### Basic Usage

Here's how to create an MCP server with citation capabilities:

```python
from hatch_mcp_server import HatchMCP

# Initialize with citations
hatch_mcp = HatchMCP(
    name="my_server",
    origin_citation="Smith, J. et al. 'Original Algorithm', Journal of Science, 2024",
    mcp_citation="Your Name, 'MCP Server Implementation', GitHub, 2024"
)

# Add tools using the FastMCP decorator syntax
@hatch_mcp.server.tool()
def my_function(param: str) -> str:
    """Your tool function.
    
    Args:
        param: Input parameter
        
    Returns:
        str: Processed result
    """
    hatch_mcp.logger.info(f"Function called with: {param}")
    return f"Processed: {param}"

# Run the server
if __name__ == "__main__":
    hatch_mcp.server.run()
```

### Wrapping Existing FastMCP Servers

If you already have a FastMCP server, you can wrap it:

```python
from mcp.server.fastmcp import FastMCP
from hatch_mcp_server import HatchMCP

# Your existing FastMCP server
existing_server = FastMCP("my_existing_server")

@existing_server.tool()
def existing_function(data: str) -> str:
    return f"Existing: {data}"

# Wrap with HatchMCP
hatch_mcp = HatchMCP(
    name="my_existing_server",
    fast_mcp=existing_server,
    origin_citation="Original work citation",
    mcp_citation="MCP implementation citation"
)

if __name__ == "__main__":
    hatch_mcp.server.run()
```

## What Happens Automatically

When you create a HatchMCP instance, it automatically:

1. **Registers citation resources** using standard URI schemes:
   - `citation://origin/{server_name}` - Information about original tools/algorithms
   - `citation://mcp/{server_name}` - Information about the MCP server implementation
   - `name://{module_file}` - Server name for URI resolution

2. **Configures logging** with a dedicated logger for your server

3. **Preserves all FastMCP functionality** - use `hatch_mcp.server` just like a FastMCP instance

## Testing Your Server

Test that your server works correctly:

```python
# Test basic functionality
if __name__ == "__main__":
    # Basic import test
    from hatch_mcp_server import HatchMCP
    
    # Create test instance
    test_server = HatchMCP("test", 
                          origin_citation="Test citation",
                          mcp_citation="Test MCP citation")
    
    # Check that citation resources are available
    print(f"Server name: {test_server.name}")
    print("Citation resources registered automatically")
    
    # Your tool testing here
    print("Server ready to run!")
```

## Next Steps

- **API Reference**: See [APIReference.md](./APIReference.md) for complete API documentation
- **Citation System**: Learn more about citation capabilities in [CitationSystem.md](./CitationSystem.md)
- **Examples**: Check out practical examples in [Examples.md](./Examples.md)

## Common Patterns

### Server Entry Point

Create a dedicated entry point file for your Hatch package:

```python
# hatch_mcp_server_entry.py
from hatch_mcp_server import HatchMCP
from my_server import mcp  # Your FastMCP server

hatch_mcp = HatchMCP(
    name="MyToolServer",
    fast_mcp=mcp,
    origin_citation="Smith, J. 'Original Algorithm', 2024",
    mcp_citation="Your Name, 'MCP Implementation', 2024"
)

if __name__ == "__main__":
    hatch_mcp.server.run()
```

### Logging

Use the built-in logger for consistent logging:

```python
@hatch_mcp.server.tool()
def my_tool(data: str) -> str:
    hatch_mcp.logger.info(f"Processing: {data}")
    
    try:
        result = process_data(data)
        hatch_mcp.logger.info(f"Success: {result}")
        return result
    except Exception as e:
        hatch_mcp.logger.error(f"Error processing {data}: {e}")
        raise
```

You're now ready to create MCP servers with proper citation capabilities!
