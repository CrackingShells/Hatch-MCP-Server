# API Reference

This article is about:

- Complete `HatchMCP` class documentation
- Constructor parameters and their usage
- Available attributes and methods
- Citation resource URIs and access patterns

## HatchMCP Class

The main wrapper class that adds citation capabilities to FastMCP servers.

### Constructor

```python
HatchMCP(name: str, 
         fast_mcp: Optional[FastMCP] = None,
         origin_citation: Optional[str] = None, 
         mcp_citation: Optional[str] = None)
```

#### Parameters

**`name`** (str, required)

- The name of your MCP server
- Used in citation URI generation
- Should be descriptive and unique
- Example: `"ArithmeticTools"`, `"DataAnalyzer"`

**`fast_mcp`** (Optional[FastMCP], default: None)

- An existing FastMCP server instance to wrap
- If `None`, creates a new FastMCP instance internally
- Use this when you have an existing server to wrap

**`origin_citation`** (Optional[str], default: None)

- Citation information for the original tools, algorithms, or research
- Should follow standard academic citation formats
- If `None`, defaults to `"No origin citation provided."`
- Example: `"Smith, J. et al. 'Algorithm X', Nature, 2024"`

**`mcp_citation`** (Optional[str], default: None)

- Citation information for the MCP server implementation
- Should credit the developer(s) of the MCP server wrapper
- If `None`, defaults to `"No MCP citation provided."`
- Example: `"Your Name, 'MCP Server Implementation', GitHub, 2024"`

**Example Usage**:

```python
# Basic usage with new FastMCP server
server = HatchMCP(
    name="MyServer",
    origin_citation="Original research citation",
    mcp_citation="My implementation citation"
)

# Wrapping existing FastMCP server
existing_mcp = FastMCP("existing")
wrapped_server = HatchMCP(
    name="existing",
    fast_mcp=existing_mcp,
    origin_citation="Research citation",
    mcp_citation="Implementation citation"
)
```

### Attributes

**`server`** (FastMCP)

- The underlying FastMCP server instance
- Use this to register tools, resources, and other MCP capabilities
- Provides access to all FastMCP functionality

**`name`** (str)

- The server name passed during initialization
- Read-only after initialization

**`logger`** (logging.Logger)

- Dedicated logger instance for the server
- Logger name: `"hatch_mcp_server.HatchMCP"`
- Use for consistent logging across your server

**`module_name`** (str)

- The filename of the calling module (auto-detected)
- Used in URI generation for citation resources
- Determined automatically using stack inspection

**Example Usage**:

```python
# Register tools using the server attribute
@hatch_mcp.server.tool()
def my_tool(param: str) -> str:
    return f"Processed: {param}"

# Use the logger
hatch_mcp.logger.info("Server starting up")

# Access server name
print(f"Running server: {hatch_mcp.name}")
```

### Automatic Citation Resources

HatchMCP automatically registers three MCP resources when initialized:

#### Server Name Resource

**URI**: `name://{module_file}`

- **Name**: "Server Name"
- **Description**: "The name of this MCP server for use in other resource URIs"
- **MIME Type**: `text/plain`
- **Returns**: The server name string

#### Origin Citation Resource

**URI**: `citation://origin/{server_name}`

- **Name**: "Origin Citation"
- **Description**: "Citation information for the original tools/algorithms"
- **MIME Type**: `text/plain`
- **Returns**: The origin citation string

#### MCP Implementation Citation Resource

**URI**: `citation://mcp/{server_name}`

- **Name**: "MCP Implementation Citation"
- **Description**: "Citation information for the MCP server implementation"
- **MIME Type**: `text/plain`
- **Returns**: The MCP implementation citation string

### Citation URI Examples

For a server named `"ArithmeticTools"`:

```python
# Accessing citation resources (conceptual - actual access depends on MCP client)
origin_citation = client.read_resource("citation://origin/ArithmeticTools")
mcp_citation = client.read_resource("citation://mcp/ArithmeticTools")
server_name = client.read_resource("name://path/to/server.py")
```

## FastMCP Integration

Since HatchMCP wraps FastMCP, all FastMCP functionality is available through the `server` attribute:

### Tool Registration

```python
@hatch_mcp.server.tool()
def example_tool(param: str) -> str:
    """Tool with type hints and documentation."""
    return f"Result: {param}"
```

### Resource Registration

```python
@hatch_mcp.server.resource(
    uri="custom://my-resource",
    name="My Custom Resource",
    description="A custom resource",
    mime_type="text/plain"
)
def get_custom_resource() -> str:
    return "Custom resource content"
```

### Prompt Registration

```python
@hatch_mcp.server.prompt(
    name="my_prompt",
    description="A custom prompt"
)
def get_prompt() -> str:
    return "Custom prompt content"
```

### Server Execution

```python
# Run the server (blocks until stopped)
if __name__ == "__main__":
    hatch_mcp.server.run()
```

## Error Handling

HatchMCP includes basic error handling:

### Initialization Errors

```python
try:
    server = HatchMCP("my_server")
except RuntimeError as e:
    # Raised if module name detection fails
    print(f"Failed to initialize server: {e}")
```

### Common Issues

1. **Module detection failure**: Ensure HatchMCP is initialized from a proper Python module file
2. **FastMCP compatibility**: Ensure you're using a compatible version of the `mcp` package
3. **Logging conflicts**: The logger uses the name `"hatch_mcp_server.HatchMCP"`

## Type Hints

HatchMCP is fully typed for better IDE support:

```python
from typing import Optional
from mcp.server.fastmcp import FastMCP
from hatch_mcp_server import HatchMCP

# All parameters are properly typed
server: HatchMCP = HatchMCP(
    name="TypedServer",
    fast_mcp=None,  # Optional[FastMCP]
    origin_citation="Citation",  # Optional[str]
    mcp_citation="MCP Citation"  # Optional[str]
)
```

## Advanced Usage

### Custom Logging Configuration

```python
import logging

# Configure before creating HatchMCP instance
logging.getLogger("hatch_mcp_server.HatchMCP").setLevel(logging.DEBUG)

server = HatchMCP("MyServer")
server.logger.debug("Debug message will be shown")
```

### Accessing Citation Information Programmatically

```python
# Access stored citation information
print(f"Origin: {server._origin_citation}")
print(f"MCP: {server._mcp_citation}")
print(f"Module: {server.module_name}")
```

Note: These are private attributes and should generally not be accessed directly in production code.
