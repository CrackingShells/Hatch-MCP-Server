# Architecture Overview

This article is about:

- The wrapper pattern used by HatchMCP
- FastMCP integration design
- Automatic resource registration mechanism
- Module detection and URI generation

## Design Principles

HatchMCP follows these core principles:

1. **Minimal Wrapper Pattern**: Enhance without changing the core FastMCP experience
2. **Automatic Citation**: Register citation resources transparently
3. **Scientific Attribution**: Standardize citation information exposure
4. **Backward Compatibility**: Work with existing FastMCP servers seamlessly

## High-Level Architecture

```plaintext
┌─────────────────────────────────────────────────────────────┐
│                        HatchMCP                             │
├─────────────────────────────────────────────────────────────┤
│ Citation Resources    │ Logger Setup    │ Module Detection  │
│ - origin://           │ - Named logger  │ - Stack inspection│
│ - mcp://              │ - Consistent    │ - Auto file path  │
│ - name://             │   formatting    │ - URI generation  │
├─────────────────────────────────────────────────────────────┤
│                      FastMCP Server                         │
│              (tools, resources, prompts)                    │
└─────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. Wrapper Class Design

**File**: `hatch_mcp_server/hatch_mcp.py`

The `HatchMCP` class implements a composition pattern:

```python
class HatchMCP():
    def __init__(self, name, fast_mcp=None, origin_citation=None, mcp_citation=None):
        # Create or wrap FastMCP instance
        self.server = fast_mcp or FastMCP(name, log_level="WARNING")
        
        # Store metadata
        self.name = name
        self._origin_citation = origin_citation or "No origin citation provided."
        self._mcp_citation = mcp_citation or "No MCP citation provided."
        
        # Auto-register citation resources
        self._register_citation_resources()
```

**Design rationale:**

- **Composition over inheritance**: Avoids tight coupling with FastMCP implementation details
- **Optional wrapping**: Can create new servers or wrap existing ones
- **Transparent access**: `hatch_mcp.server` provides full FastMCP functionality

### 2. Module Detection Mechanism

**Purpose**: Automatically determine the calling module for URI generation.

**Implementation**:

```python
# Determine the filename of the calling module for citation URIs
try:
    frame = inspect.stack()[1]  # Get caller's frame
    module = inspect.getmodule(frame[0])
    if module and module.__file__:
        self.module_name = module.__file__[1:]  # Remove leading slash
        self.logger.info(f"Module name for citation URIs: {self.module_name}")
except Exception:
    raise RuntimeError("Unable to determine module name for citation URIs.")
```

**Design rationale:**

- **Automatic detection**: No manual configuration required
- **URI consistency**: Provides consistent naming for citation resources
- **Error handling**: Fails fast if detection fails

### 3. Citation Resource Registration

**Implementation pattern**:

```python
@self.server.resource(
    uri=f"citation://origin/{name}",
    name="Origin Citation",
    description="Citation information for the original tools/algorithms",
    mime_type="text/plain"
)
def get_origin_citation() -> str:
    return self._origin_citation
```

**Design rationale:**

- **Standard URI schemes**: `citation://origin/`, `citation://mcp/`, `name://`
- **Automatic registration**: Happens during initialization
- **Closure pattern**: Citation data captured in closure scope
- **Standard MIME types**: Plain text for simplicity

### 4. Logging Integration

**Logger setup**:

```python
self.logger = logging.getLogger("hatch_mcp_server.HatchMCP")
```

**Design rationale:**

- **Namespaced logging**: Separate from FastMCP and user code
- **Consistent naming**: All HatchMCP instances use same logger namespace
- **Standard Python logging**: Integrates with existing logging configurations

## Data Flow

### Initialization Sequence

1. **Parameter validation**: Check required parameters
2. **FastMCP setup**: Create new or wrap existing server
3. **Module detection**: Inspect call stack for module information
4. **Citation storage**: Store citation strings
5. **Resource registration**: Register three citation resources automatically
6. **Logger configuration**: Set up dedicated logger

### Runtime Operation

```plaintext
User calls hatch_mcp.server.tool() 
    ↓
Calls FastMCP.tool() decorator
    ↓
Tool registered in FastMCP server
    ↓
Citation resources remain available alongside tools
```

### Resource Access

```plaintext
MCP Client requests citation://origin/ServerName
    ↓
FastMCP router matches URI to registered resource
    ↓
Citation closure function returns stored citation string
    ↓
Response sent to client
```

## Key Design Decisions

### 1. Composition Pattern

**Decision**: Use composition instead of inheritance.

**Rationale**:

- Avoids breaking changes when FastMCP updates
- Allows wrapping existing FastMCP instances

**Trade-offs**:

- Requires `.server` attribute access
- Slightly more verbose than inheritance

### 2. Automatic Resource Registration

**Decision**: Register citation resources automatically during initialization.

**Rationale**:

- Zero configuration required from users
- Consistent citation resource availability
- Prevents forgetting to register citation information

**Trade-offs**:

- Less flexibility for custom citation schemes
- Potential URI conflicts (mitigated by standard schemes)

### 3. Stack Inspection for Module Detection

**Decision**: Use `inspect.stack()` to determine calling module.

**Rationale**:

- Automatic detection without user configuration
- Consistent URI generation
- Works with standard Python module patterns

**Trade-offs**:

- Relies on Python internals
- Can fail in unusual execution contexts
- Adds complexity for edge cases

### 4. Minimal API Surface

**Decision**: Expose only essential attributes and methods.

**Rationale**:

- Reduces maintenance burden
- Focuses on core citation functionality
- Easier to maintain backward compatibility

**Trade-offs**:

- Less customization options
- May need extension for advanced use cases

## Extension Points

### Custom Citation Schemes

While not currently supported, the architecture allows for future extension:

```python
# Potential future extension
def register_custom_citation(self, scheme: str, citation: str):
    @self.server.resource(
        uri=f"{scheme}://{self.name}",
        name=f"Custom {scheme}",
        description=f"Custom citation scheme: {scheme}",
        mime_type="text/plain"
    )
    def get_custom_citation() -> str:
        return citation
```

### Advanced Module Detection

For unusual execution contexts:

```python
# Potential override mechanism
def set_module_name(self, module_name: str):
    """Override automatic module detection."""
    self.module_name = module_name
    # Re-register name resource with new module name
```

## Performance Considerations

### Initialization Overhead

- **Stack inspection**: Minimal one-time cost during initialization
- **Resource registration**: Three additional resources per server
- **Memory usage**: Negligible - only stores citation strings

### Runtime Overhead

- **Zero runtime cost**: No performance impact on tool execution
- **Citation access**: Standard FastMCP resource access performance
- **Logging**: Standard Python logging performance

## Error Handling Strategy

### Initialization Errors

1. **Module detection failure**: Raise `RuntimeError` with clear message
2. **FastMCP creation failure**: Let FastMCP errors propagate
3. **Citation parameter validation**: Accept any string, use defaults for None

### Runtime Errors

- **Citation resource access**: Standard FastMCP error handling
- **Logging errors**: Python logging framework handles gracefully

## Testing Strategy

### Unit Testing Approach

```python
def test_hatch_mcp_initialization():
    server = HatchMCP("test", origin_citation="test origin")
    assert server.name == "test"
    assert server._origin_citation == "test origin"
    assert isinstance(server.server, FastMCP)

def test_citation_resource_registration():
    server = HatchMCP("test")
    # Verify resources are registered (implementation depends on FastMCP testing utilities)
```

### Integration Testing

- Test with real FastMCP servers
- Verify citation URI resolution
- Test wrapping existing servers

This architecture provides a clean, minimal wrapper that enhances FastMCP with citation capabilities while maintaining full compatibility and ease of use.
