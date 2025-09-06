# Hatch-MCP-Server

A wrapper around FastMCP servers that adds automatic citation capabilities for scientific transparency and attribution in MCP (Model Context Protocol) applications.

## What is HatchMCP?

HatchMCP enhances FastMCP servers by automatically exposing citation information as standardized MCP resources. This enables proper attribution for both original research/algorithms and MCP server implementations, which is critical for attribution in scientific computing and autonomous agent systems.

**Key Features:**

- 🔬 **Scientific Attribution**: Automatic citation resource registration
- 🔄 **FastMCP Compatibility**: Works with existing FastMCP servers
- 📋 **Standardized URIs**: Uses `citation://origin/` and `citation://mcp/` schemes
- 🪶 **Lightweight**: Minimal overhead, zero configuration required

## Quick Start

### Installation

```bash
# Install directly from the repository
pip install git+https://github.com/CrackingShells/Hatch-MCP-Server.git

# Or install local copy
git clone https://github.com/CrackingShells/Hatch-MCP-Server.git
cd Hatch-MCP-Server
pip install .
```

### Basic Usage

```python
from hatch_mcp_server import HatchMCP

# Create an MCP server with citation capabilities
hatch_mcp = HatchMCP(
    name="MyServer",
    origin_citation="Smith, J. 'Original Algorithm', Nature, 2024",
    mcp_citation="Your Name, 'MCP Implementation', GitHub, 2024"
)

# Add tools using FastMCP decorator syntax
@hatch_mcp.server.tool()
def process_data(data: str) -> str:
    """Process data using the wrapped algorithm."""
    hatch_mcp.logger.info(f"Processing: {data}")
    return f"Processed: {data}"

# Run the server
if __name__ == "__main__":
    hatch_mcp.server.run()
```

### Existing FastMCP Server

Assuming you have an existing FastMCP server (`mcp_server.py`)

```python
from mcp.server.fastmcp import FastMCP

existing_server = FastMCP("my_existing_server")

@existing_server.tool()
def existing_function(data: str) -> str:
    return f"Existing: {data}"
```

You can wrap it with HatchMCP:

```python
from mcp.server.fastmcp import FastMCP
from hatch_mcp_server import HatchMCP

from mcp_server import existing_server

# Wrap with HatchMCP for citation capabilities
hatch_mcp = HatchMCP(
    name="my_existing_server",
    fast_mcp=existing_server,
    origin_citation="Original work citation",
    mcp_citation="MCP implementation citation"
)

# Run the server
if __name__ == "__main__":
    hatch_mcp.server.run()
```

The server automatically exposes citation information through:

- `citation://origin/MyServer` - Original algorithm citation
- `citation://mcp/MyServer` - MCP implementation citation

## Documentation

📚 **[Complete Documentation](docs/articles/index.md)** - Full documentation table of contents and navigation guide

### Quick Start Guides

- **[Getting Started](docs/articles/users/GettingStarted.md)** - Installation, setup, and first steps
- **[API Reference](docs/articles/users/APIReference.md)** - Complete API documentation
- **[Citation System](docs/articles/users/CitationSystem.md)** - Understanding scientific attribution features
- **[Examples](docs/articles/users/Examples.md)** - Practical usage patterns and code samples

### Developer Resources

- **[Contributing Guide](docs/articles/devs/contribution_guidelines/Contributing.md)** - Complete development workflow and MCP-specific requirements
- **[Architecture Overview](docs/articles/devs/architecture/Overview.md)** - Design principles and implementation details

### I Want To

- **🚀 Get started quickly** → [Installation & Quick Start](docs/articles/users/GettingStarted.md#installation)
- **🔄 Wrap existing FastMCP servers** → [Basic Usage](docs/articles/users/GettingStarted.md#Wrapping-Existing-FastMCP-Servers)
- **📖 Learn about citations** → [Citation System Guide](docs/articles/users/CitationSystem.md)
- **🔍 Look up specific APIs** → [API Reference](docs/articles/users/APIReference.md)
- **💡 See examples** → [Examples & Patterns](docs/articles/users/Examples.md)
- **🛠️ Contribute code** → [Contributing Guide](docs/articles/devs/contribution_guidelines/Contributing.md)
- **🏗️ Understand design** → [Architecture Overview](docs/articles/devs/architecture/Overview.md)
- **📋 Browse all docs** → [Documentation Table of Contents](docs/articles/index.md)

## Why Use HatchMCP?

### Scientific Transparency

```python
# Citation information is automatically available to MCP clients
# citation://origin/ServerName -> "Smith, J. 'Algorithm X', Nature, 2024"
# citation://mcp/ServerName -> "Your Name, 'MCP Implementation', 2024"
```

### Zero Configuration

```python
# Just wrap your server - citation resources are registered automatically
hatch_mcp = HatchMCP("server_name", origin_citation="...", mcp_citation="...")
# Use hatch_mcp.server exactly like FastMCP
```

### FastMCP Compatibility

```python
# Wrap existing FastMCP servers without changes
existing_server = FastMCP("my_server")
wrapped = HatchMCP("my_server", fast_mcp=existing_server, ...)
```

## Contributing

We welcome contributions! Please see our comprehensive [Contributing Guide](docs/articles/devs/contribution_guidelines/Contributing.md) for detailed guidelines covering development workflow, MCP compatibility requirements, and coding standards.

### Overview

1. **Fork and clone** the repository
2. **Install dependencies**: `pip install -e .` and `npm install`
3. **Create a feature branch**: `git checkout -b feat/your-feature`
4. **Make changes** and add tests
5. **Use conventional commits**: `npm run commit` for guided commits
6. **Create a pull request**

For complete details on commit formats, testing requirements, and MCP-specific development guidelines, see the [Contributing Guide](docs/articles/devs/contribution_guidelines/Contributing.md).

## Requirements

- **Python**: 3.12+
- **Dependencies**: `mcp>=1.6.0`
- **Compatibility**: FastMCP servers and MCP clients

## License

AGPL v3: see [LICENSE](./LICENSE)

---

**Part of the [Cracking Shells Ecosystem](https://github.com/CrackingShells)**: [Hatch!](https://github.com/CrackingShells/Hatch) - A package management system for scientific MCP servers.
