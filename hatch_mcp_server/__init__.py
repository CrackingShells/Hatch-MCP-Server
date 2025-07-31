"""
Hatch MCP Server - The wrapper for MCP servers to service Hatch-related applications.

This package provides a class for extending MCP servers with additional functionalities
relevant to the Hatch ecosystem. This includes:

- Citations for Origin Software and MCP server implementations as MCP resources.

"""

__version__ = "0.2.0"

from .hatch_mcp import HatchMCP

__all__ = [
    'HatchMCP'
]