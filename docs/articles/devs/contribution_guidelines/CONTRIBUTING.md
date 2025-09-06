# Contributing to Hatch-MCP-Server

Thank you for your interest in contributing to Hatch-MCP-Server! This comprehensive guide covers everything you need to know about our development workflow, contribution standards, and MCP-specific requirements.

This article is about:

- Complete development workflow and contribution process
- Commit message standards and automated versioning
- MCP compatibility requirements and testing
- Code standards and best practices
- Release process and maintenance considerations

## Commit Message Format

We use [Conventional Commits](https://www.conventionalcommits.org/) for automated versioning and changelog generation.

### Format

```plaintext
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

- **feat**: New features (triggers minor version bump)
- **fix**: Bug fixes (triggers patch version bump)
- **docs**: Documentation changes
- **refactor**: Code refactoring without functional changes
- **test**: Adding or updating tests
- **chore**: Maintenance tasks, dependency updates
- **ci**: Changes to CI/CD configuration
- **perf**: Performance improvements
- **style**: Code style changes (formatting, etc.)

### Examples

```bash
# Good commit messages
feat: add support for new MCP protocol version
fix: resolve server initialization timeout
docs: update MCP server wrapper documentation
refactor: simplify server lifecycle management
test: add integration tests for MCP protocol
chore: update dependencies to latest versions

# Breaking changes (use sparingly until v1.0.0)
feat!: change MCP server interface
fix!: remove deprecated wrapper methods

# With scope
feat(server): add new MCP server capabilities
fix(wrapper): resolve connection handling issue
docs(api): update server wrapper documentation
```

### Using Commitizen

For guided commit messages, use commitizen:

```bash
# Install dependencies first
npm install

# Use commitizen for guided commits
npm run commit
# or
npx cz
```

This will prompt you through creating a properly formatted commit message.

## Development Workflow

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/Hatch-MCP-Server.git
cd Hatch-MCP-Server
```

### 2. Set Up Development Environment

```bash
# Install Python dependencies
pip install -e .

# Install Node.js dependencies for semantic-release
npm install
```

### 3. Create Feature Branch

```bash
git checkout -b feat/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 4. Make Changes

- Write code following existing patterns
- Add tests for new functionality
- Update documentation as needed
- Follow PEP 8 style guidelines
- Ensure MCP protocol compatibility

### 5. Test Your Changes

```bash
# Run basic import test
python -c "import hatch_mcp_server; print('Package imports successfully')"

# Test MCP server functionality when available
```

### 6. Commit Changes

```bash
# Use commitizen for guided commits
npm run commit

# Or commit manually with conventional format
git commit -m "feat: add your feature description"
```

### 7. Push and Create Pull Request

```bash
git push origin feat/your-feature-name
```

Then create a pull request on GitHub.

## Pull Request Guidelines

### Title Format

Use conventional commit format for PR titles:

- `feat: add new MCP server functionality`
- `fix: resolve server wrapper issue`
- `docs: update installation guide`

### Description

Include in your PR description:

- **What**: Brief description of changes
- **Why**: Reason for the changes
- **How**: Implementation approach (if complex)
- **Testing**: How you tested the changes
- **MCP Compatibility**: Any MCP protocol considerations
- **Breaking Changes**: Any breaking changes (if applicable)

### Checklist

- [ ] Code follows existing style and patterns
- [ ] Tests added for new functionality
- [ ] Documentation updated (if needed)
- [ ] Commit messages follow conventional format
- [ ] All tests pass
- [ ] MCP protocol compatibility maintained
- [ ] No breaking changes (unless intentional and documented)

#### MCP-Specific Checklist

- [ ] FastMCP compatibility maintained
- [ ] Citation resources follow URI standards
- [ ] No breaking changes to citation schemes
- [ ] Documentation updated for MCP-specific features
- [ ] Examples work with real MCP clients (if available)

## Development Environment Setup

### Prerequisites

```bash
# Required dependencies
pip install mcp>=1.6.0

# Development dependencies (when test suite is available)
pip install pytest pytest-cov black flake8
```

### Local Development

```bash
# Clone and install in development mode
git clone https://github.com/CrackingShells/Hatch-MCP-Server.git
cd Hatch-MCP-Server
pip install -e .

# Install Node.js dependencies for semantic-release
npm install

# Verify installation
python -c "import hatch_mcp_server; print('Installation successful')"
```

## MCP Compatibility Requirements

### Core MCP Principles

When contributing to HatchMCP, ensure changes maintain:

1. **MCP Protocol Compliance**: All resources must follow MCP resource specifications
2. **FastMCP Compatibility**: Changes must work with current and future FastMCP versions
3. **Resource Standards**: Citation resources must use standardized URI schemes
4. **Client Compatibility**: Resources must be accessible by standard MCP clients

### Testing MCP Functionality

```python
# Test citation resource registration
def test_citation_resources():
    server = HatchMCP("test", 
                      origin_citation="test origin",
                      mcp_citation="test mcp")
    
    # Verify resources are registered (implementation depends on available test utilities)
    # Expected resources:
    # - citation://origin/test
    # - citation://mcp/test  
    # - name://{module_path}
```

### MCP Client Testing

```python
# Example integration test with MCP client (when test framework is available)
async def test_with_mcp_client():
    server = HatchMCP("integration_test")
    
    # Start server in test mode
    # Connect MCP client
    # Request citation resources
    # Verify correct responses
```

## Code Standards

### Python Standards

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for public functions and classes
- Keep functions focused and small
- Use meaningful variable and function names

### MCP Server Considerations

- Maintain compatibility with MCP protocol specifications
- Follow MCP server best practices
- Ensure proper error handling for MCP operations
- Document any MCP-specific functionality

### Documentation

- Update relevant documentation for changes
- Use clear, concise language
- Include code examples where helpful
- Keep README.md up to date

### Type Hints

All public interfaces must include type hints:

```python
from typing import Optional
from mcp.server.fastmcp import FastMCP

def new_method(self, param: str, optional_param: Optional[int] = None) -> str:
    """Example of proper type hinting."""
    return f"Result: {param}"
```

### Documentation Standards

All public methods require docstrings:

```python
def public_method(self, param: str) -> str:
    """Brief description of the method.
    
    Args:
        param: Description of parameter
        
    Returns:
        str: Description of return value
        
    Raises:
        RuntimeError: When this error occurs
    """
```

### Citation Resource Standards

When adding new citation resource types:

```python
# Follow this pattern for new citation resources
@self.server.resource(
    uri=f"citation://{scheme}/{self.name}",
    name=f"{Scheme} Citation",
    description=f"Citation information for {scheme}",
    mime_type="text/plain"
)
def get_citation() -> str:
    return self._citation_data
```

## Testing

### Running Tests

```bash
# Basic import test
python -c "import hatch_mcp_server; print('Package imports successfully')"

# Run unit tests (when available)
pytest tests/

# Test with real FastMCP server
python examples/test_server.py

# Verify citation resources work
python -c "
from hatch_mcp_server import HatchMCP
server = HatchMCP('test', origin_citation='test')
print('Citation system working')
"
```

### Writing Tests

- Add tests for new features
- Test edge cases and error conditions
- Test MCP protocol interactions
- Use descriptive test names
- Follow existing test patterns

### Documentation Updates

Update relevant documentation for any changes:

- **API changes**: Update [APIReference.md](../../users/APIReference.md)
- **New features**: Update [GettingStarted.md](../../users/GettingStarted.md)
- **Citation changes**: Update [CitationSystem.md](../../users/CitationSystem.md)
- **Architecture changes**: Update [Overview.md](../architecture/Overview.md)

## Release Process

Releases are fully automated using semantic-release:

1. **Commits are analyzed** for conventional commit format
2. **Version is calculated** based on commit types
3. **Changelog is generated** from commit messages
4. **Version files are updated** (pyproject.toml, CHANGELOG.md)
5. **Changes are committed** back to repository using GitHub App
6. **GitHub release is created** with release notes and tags

### Version Impact

- `feat:` commits → Minor version (0.2.0 → 0.3.0)
- `fix:` commits → Patch version (0.2.0 → 0.2.1)
- `feat!:` or `BREAKING CHANGE:` → Major version (0.2.0 → 1.0.0)
- Other types → No release

## Advanced Development Tasks

### Adding New Citation Types

```python
# Example: Adding support for license citations
def _register_license_citation(self):
    if hasattr(self, '_license_citation') and self._license_citation:
        @self.server.resource(
            uri=f"citation://license/{self.name}",
            name="License Citation",
            description="License information for the implementation",
            mime_type="text/plain"
        )
        def get_license_citation() -> str:
            return self._license_citation
```

### Extending Module Detection

```python
# Example: Supporting alternative module detection
def _detect_module_name(self):
    """Enhanced module detection with fallbacks."""
    try:
        # Current implementation
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        if module and module.__file__:
            return module.__file__[1:]
    except Exception:
        pass
    
    # Fallback mechanisms
    # ... additional detection logic
    
    raise RuntimeError("Unable to determine module name")
```

### Testing New Features

```python
# Integration test template
def test_new_feature():
    # Setup
    server = HatchMCP("test_server", 
                      origin_citation="test",
                      mcp_citation="test")
    
    # Test new functionality
    result = server.new_method("test_param")
    
    # Verify results
    assert result == expected_result
    
    # Verify MCP compatibility
    # (Check that citation resources still work)
```

## Release Considerations

### Version Compatibility

- **MCP Protocol**: Maintain compatibility with MCP protocol versions
- **FastMCP**: Support current and recent FastMCP versions  
- **Python**: Support Python 3.12+ as specified in pyproject.toml

### Breaking Changes

Before introducing breaking changes:

1. **Document impact**: Clearly describe what breaks
2. **Provide migration path**: Show how to update existing code
3. **Consider deprecation**: Add deprecation warnings before removal
4. **Update examples**: Ensure all documentation examples work

### Testing Before Release

```bash
# Comprehensive pre-release testing
python -c "import hatch_mcp_server; print('Import OK')"

# Test with various FastMCP configurations
python test_scripts/test_new_server.py
python test_scripts/test_wrapped_server.py

# Verify documentation examples work
python -c "exec(open('docs/articles/users/GettingStarted.md').read())"

# Test installation from source
pip install .
python -c "from hatch_mcp_server import HatchMCP; print('Install OK')"
```

## Debugging and Troubleshooting

### Common Issues

1. **Module detection failures**: Check execution context and call stack
2. **FastMCP incompatibility**: Verify MCP package version
3. **Citation resource conflicts**: Check for URI naming conflicts
4. **Logging issues**: Verify logger configuration

### Debug Mode

```python
import logging
logging.getLogger("hatch_mcp_server.HatchMCP").setLevel(logging.DEBUG)

server = HatchMCP("debug_server")
# Debug output will show module detection and resource registration
```

## Getting Help

- **Issues**: Report bugs or request features via GitHub Issues
- **Discussions**: Ask questions in GitHub Discussions
- **Documentation**: Check existing documentation for guidance
- **Code**: Look at existing code for patterns and examples
- **MCP Compatibility**: Check FastMCP documentation and examples
- **Code Review**: Maintainers will review PRs for MCP compliance

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow GitHub's community guidelines

## Maintenance Notes

### Dependencies

- **MCP**: Core dependency - monitor for breaking changes
- **FastMCP**: Wrapper target - ensure compatibility with updates
- **Python stdlib**: Only uses `inspect`, `logging`, `typing` - minimal risk

### Long-term Considerations

- **Citation standards**: May need updates as scientific citation practices evolve
- **MCP protocol**: May need updates as MCP protocol evolves
- **FastMCP API**: May need adapter pattern if FastMCP API changes significantly

Thank you for contributing to Hatch-MCP-Server! 🚀

This comprehensive contribution guide ensures that changes maintain the core value of scientific attribution while preserving MCP compatibility and ease of use.
