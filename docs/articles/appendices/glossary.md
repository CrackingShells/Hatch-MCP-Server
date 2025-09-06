# Glossary

This glossary defines key terms used throughout the Hatch-MCP-Server documentation and codebase.

## A

**Attribution**: The practice of giving credit to original authors, researchers, or implementers of tools and algorithms.

## C

**Citation**: A reference to the source of information, research, or implementation, following academic or software attribution standards.

**Citation Resource**: An MCP resource that provides citation information accessible via standardized URIs.

**Citation URI**: A standardized URI scheme (`citation://`) used to access citation information through MCP resources.

**Composition Pattern**: A design pattern where HatchMCP contains a FastMCP instance rather than inheriting from it.

## F

**FastMCP**: The underlying MCP server framework that HatchMCP wraps to add citation capabilities.

## H

**HatchMCP**: The main wrapper class that enhances FastMCP servers with automatic citation resource registration.

## M

**MCP (Model Context Protocol)**: A protocol that enables language models to securely access external tools and data sources through standardized interfaces.

**MCP Client**: Software that connects to MCP servers to access tools and resources.

**MCP Resource**: A piece of data or content made available through an MCP server, accessible via URI.

**MCP Server**: Software that provides tools, resources, and capabilities accessible through the MCP protocol.

**MCP Tool**: A function or capability provided by an MCP server that can be called by MCP clients.

**Module Detection**: The automatic process by which HatchMCP determines the calling module's file path for URI generation.

## O

**Origin Citation**: Citation information for the original research, algorithm, or tool being wrapped by an MCP server.

## R

**Resource Registration**: The process of making resources available through an MCP server's resource system.

## S

**Scientific Attribution**: The practice of properly crediting scientific work, research, and implementations to maintain transparency and enable reproducibility.

**Stack Inspection**: The technique used by HatchMCP to automatically detect the calling module using Python's `inspect.stack()` function.

## U

**URI Scheme**: A standardized format for identifying and accessing resources, such as `citation://origin/` or `name://`.

## W

**Wrapper Pattern**: A design approach where one class (HatchMCP) encapsulates and enhances another class (FastMCP) without inheritance.
