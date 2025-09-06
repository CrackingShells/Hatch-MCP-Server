# Citation System Guide

This article is about:

- Understanding the scientific importance of citation in MCP servers
- How HatchMCP implements automatic citation capabilities
- URI schemes for accessing citation information
- Best practices for providing attribution

## Why Citations Matter

In scientific computing and autonomous agent systems, proper attribution is critical for:

- **Transparency**: Users can trace the origin of tools and algorithms
- **Reproducibility**: Researchers can locate original implementations and methods
- **Credit**: Original authors receive proper recognition for their work
- **Trust**: Clear attribution builds confidence in automated systems
- **Legal compliance**: Proper licensing and copyright attribution

HatchMCP addresses this by automatically exposing citation information as standardized MCP resources.

## How Citation Resources Work

When you create a HatchMCP instance, it automatically registers three types of resources:

### 1. Origin Citation Resource

**Purpose**: Credits the original research, algorithm, or tool being wrapped.

**URI Pattern**: `citation://origin/{server_name}`

**When to use**: Always provide when your MCP server implements or wraps existing algorithms, research, or tools.

```python
hatch_mcp = HatchMCP(
    name="LinearRegression",
    origin_citation="Legendre, A.M. 'Nouvelles méthodes pour la détermination des orbites des comètes', 1805"
)
```

### 2. MCP Implementation Citation Resource

**Purpose**: Credits the developer(s) who created the MCP server wrapper.

**URI Pattern**: `citation://mcp/{server_name}`

**When to use**: Always provide to credit your MCP server implementation work.

```python
hatch_mcp = HatchMCP(
    name="LinearRegression",
    mcp_citation="Smith, J. 'Linear Regression MCP Server', GitHub, 2024"
)
```

### 3. Server Name Resource

**Purpose**: Provides the server name for URI resolution in client applications.

**URI Pattern**: `name://{module_file_path}`

**When to use**: Automatically created - no action needed.

## Citation Format Guidelines

### Academic Citations

For research papers and academic work:

```python
# Format: Author(s), "Title", Journal/Conference, Year
origin_citation="Smith, J. et al. 'Deep Learning for X', Nature, 2024"

# Include DOI when available
origin_citation="Smith, J. 'Algorithm X', Nature, 2024, DOI: 10.1038/nature12345"
```

### Software Citations

For software libraries and tools:

```python
# Format: Author/Organization, "Software Name", Version, Year, URL
origin_citation="NumPy Developers, 'NumPy', v1.24, 2024, https://numpy.org"

# For specific algorithms in libraries
origin_citation="Scikit-learn Team, 'Random Forest Implementation', scikit-learn v1.3, 2024"
```

### MCP Implementation Citations

For your MCP server implementation:

```python
# Personal implementation
mcp_citation="Your Name, 'MCP Server for X', GitHub, 2024"

# With repository URL
mcp_citation="Your Name, 'MCP Server for X', 2024, https://github.com/user/repo"

# Team implementation
mcp_citation="Team Name, 'X Analysis MCP Server', Organization, 2024"
```

## Practical Examples

### Scientific Computing Server

```python
from hatch_mcp_server import HatchMCP
import numpy as np

hatch_mcp = HatchMCP(
    name="StatisticalAnalysis",
    origin_citation="Multiple sources: NumPy (Harris et al., Nature 2020), SciPy (Virtanen et al., Nature Methods 2020)",
    mcp_citation="Lab Name, 'Statistical Analysis MCP Server', University, 2024"
)

@hatch_mcp.server.tool()
def compute_correlation(data1: list, data2: list) -> float:
    """Compute Pearson correlation coefficient."""
    return float(np.corrcoef(data1, data2)[0, 1])
```

### Algorithm Implementation Server

```python
hatch_mcp = HatchMCP(
    name="KMeansClustering",
    origin_citation="MacQueen, J. 'Some methods for classification and analysis of multivariate observations', 1967",
    mcp_citation="Your Name, 'K-Means MCP Implementation', GitHub, 2024"
)

@hatch_mcp.server.tool()
def kmeans_cluster(data: list, k: int) -> dict:
    """Perform K-means clustering."""
    # Implementation here
    pass
```

### Data Processing Server

```python
hatch_mcp = HatchMCP(
    name="DataPreprocessor",
    origin_citation="Pandas Development Team, 'pandas: powerful Python data analysis toolkit', 2024",
    mcp_citation="Data Team, 'Data Preprocessing MCP Server', Company, 2024"
)
```

## Accessing Citation Information

### From MCP Clients

Citation resources can be accessed like any other MCP resource:

```python
# Conceptual client usage (actual syntax depends on MCP client library)
client = MCPClient()

# Get origin citation
origin = client.read_resource("citation://origin/StatisticalAnalysis")
print(f"Origin: {origin}")

# Get implementation citation  
impl = client.read_resource("citation://mcp/StatisticalAnalysis")
print(f"Implementation: {impl}")
```

### Programmatic Access

```python
# Direct access to citation information
server = HatchMCP("MyServer", 
                  origin_citation="Original work",
                  mcp_citation="My implementation")

# Access via private attributes (not recommended for production)
print(f"Origin: {server._origin_citation}")
print(f"MCP: {server._mcp_citation}")
```

## Best Practices

### 1. Always Provide Both Citations

```python
# Good: Both citations provided
hatch_mcp = HatchMCP(
    name="MyServer",
    origin_citation="Original algorithm citation",
    mcp_citation="My MCP implementation citation"
)

# Avoid: Missing citations
hatch_mcp = HatchMCP(name="MyServer")  # Uses default "No citation provided"
```

### 2. Be Specific and Complete

```python
# Good: Specific and complete
origin_citation="Pedregosa et al. 'Scikit-learn: Machine Learning in Python', JMLR 12, 2011"

# Avoid: Vague or incomplete
origin_citation="scikit-learn"
```

### 3. Update Citations When Dependencies Change

```python
# When updating algorithms or dependencies, update citations
hatch_mcp = HatchMCP(
    name="MLServer",
    origin_citation="scikit-learn 1.3 (Pedregosa et al. 2011), numpy 1.24 (Harris et al. 2020)",
    mcp_citation="Updated implementation by Your Name, 2024"
)
```

### 4. Use Consistent Citation Formats

Establish a format within your project and stick to it:

```python
# Consistent academic format
origin_citation="Author, A. 'Title', Journal Vol(Issue), Year, pp. X-Y"

# Consistent software format  
origin_citation="Project Team, 'Software Name v1.0', Year, URL"
```

## Citation in Multi-Tool Servers

For servers that implement multiple algorithms:

```python
hatch_mcp = HatchMCP(
    name="MathToolbox",
    origin_citation="Multiple: NumPy (Harris et al. 2020), SciPy (Virtanen et al. 2020), scikit-learn (Pedregosa et al. 2011)",
    mcp_citation="Math Team, 'Mathematical Tools MCP Server', Organization, 2024"
)

@hatch_mcp.server.tool()
def linear_algebra_operation(matrix: list) -> list:
    """Performs linear algebra operation using NumPy."""
    # Document specific algorithm source if needed
    hatch_mcp.logger.info("Using NumPy linear algebra routines")
    # Implementation
    pass

@hatch_mcp.server.tool()  
def statistical_test(data: list) -> dict:
    """Performs statistical test using SciPy."""
    hatch_mcp.logger.info("Using SciPy statistical functions")
    # Implementation
    pass
```

## Troubleshooting Citation Issues

### Citation Not Appearing

1. **Check server initialization**: Ensure HatchMCP was created successfully
2. **Verify resource registration**: Citation resources are registered automatically
3. **Check client compatibility**: Ensure your MCP client can access resources

### URI Resolution Problems

1. **Check server name**: Ensure it matches between URI and server initialization
2. **Module detection**: Verify the module file path is detected correctly
3. **Case sensitivity**: URIs are case-sensitive

### Citation Format Issues

1. **Special characters**: Ensure citations don't contain characters that break URI schemes
2. **Length limits**: Very long citations might be truncated by some clients
3. **Encoding**: Use UTF-8 compatible characters in citations

The citation system ensures that your MCP servers maintain proper scientific attribution and transparency, building trust in autonomous systems that rely on your tools.
