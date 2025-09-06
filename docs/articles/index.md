# Documentation Table of Contents

Welcome to the Hatch-MCP-Server documentation. This page provides navigation to all available documentation for users, developers, and maintainers.

## For Users

### Getting Started

- **[Getting Started](./users/GettingStarted.md)** - Installation, quick start, and basic usage patterns
- **[API Reference](./users/APIReference.md)** - Complete documentation of the HatchMCP class and methods
- **[Citation System Guide](./users/CitationSystem.md)** - Understanding and implementing scientific attribution
- **[Examples](./users/Examples.md)** - Practical examples and usage patterns

### Quick Links

- [Installation instructions](./users/GettingStarted.md#installation)
- [Basic usage example](./users/GettingStarted.md#quick-start)
- [Citation URI schemes](./users/CitationSystem.md#how-citation-resources-work)
- [Constructor parameters](./users/APIReference.md#constructor)

## For Developers

### Architecture and Design

- **[Architecture Overview](./devs/architecture/Overview.md)** - Design principles, components, and patterns
- **[Contributing Guide](./devs/contribution_guidelines/Contributing.md)** - Development workflow and MCP compatibility requirements

### Development Resources

- [Design principles](./devs/architecture/Overview.md#design-principles)
- [Wrapper pattern explanation](./devs/architecture/Overview.md#core-components)
- [MCP compatibility requirements](./devs/contribution_guidelines/Contributing.md#mcp-compatibility-requirements)
- [Testing guidelines](./devs/contribution_guidelines/Contributing.md#testing)

## Reference Materials

### Appendices

- **[Glossary](./appendices/glossary.md)** - Definitions of key terms and concepts

### Maintenance Information

- [Dependencies and compatibility](./appendices/glossary.md#dependencies)
- [Troubleshooting guide](./appendices/glossary.md#troubleshooting-guide)
- [Release process](./appendices/glossary.md#release-process)

## External Resources

### Related Projects

- [FastMCP Documentation](https://github.com/punkpeye/fastmcp) - The underlying MCP server framework
- [MCP Protocol Specification](https://modelcontextprotocol.io/) - Official MCP protocol documentation
- [Hatch Ecosystem](https://github.com/CrackingShells/Hatch) - The broader Hatch package management system

### Community

- [GitHub Repository](https://github.com/CrackingShells/Hatch-MCP-Server) - Source code and issue tracking
- [Contributing Guide](./devs/contribution_guidelines/Contributing.md) - Complete development guidelines and workflow
- [License](../LICENSE) - AGPL v3 license information

## Navigation Tips

### Finding Information Quickly

**I want to...**

- **Use HatchMCP in my project** → Start with [Getting Started](./users/GettingStarted.md)
- **Understand citation features** → Read [Citation System Guide](./users/CitationSystem.md)
- **Look up API details** → Check [API Reference](./users/APIReference.md)
- **Contribute to the project** → See [Contributing Guide](./devs/contribution_guidelines/Contributing.md)
- **Understand the architecture** → Read [Architecture Overview](./devs/architecture/Overview.md)
- **Find definitions** → Use [Glossary](./appendices/glossary.md)

### Documentation Organization

```plaintext
docs/
├── articles/
│   ├── users/              # End-user documentation
│   │   ├── GettingStarted.md
│   │   ├── APIReference.md
│   │   ├── CitationSystem.md
│   │   └── Examples.md
│   ├── devs/               # Developer documentation
│   │   ├── architecture/
│   │   │   └── Overview.md
│   │   └── contribution_guidelines/
│   │       └── Contributing.md
│   └── appendices/         # Reference materials
│       └── glossary.md
└── table_of_contents.md    # This file
```

### Documentation Conventions

- **Prerequisites**: Clearly stated at the beginning of each article
- **Code examples**: Always tested and functional
- **Cross-references**: Links to related documentation sections
- **Audience indicators**: User vs. developer content clearly marked

## Recent Updates

- **Initial documentation release** - Complete user and developer documentation suite
- **Citation system guide** - Comprehensive guide to scientific attribution features
- **Architecture overview** - Technical documentation for contributors

## Feedback and Improvements

Found an issue with the documentation? Have suggestions for improvement?

- **Errors or unclear content**: [Open an issue](https://github.com/CrackingShells/Hatch-MCP-Server/issues)
- **Contributing documentation**: See [Contributing Guide](./devs/contribution_guidelines/Contributing.md#documentation-updates)

---

*This documentation follows the [Cracking Shells organization documentation standards](https://github.com/CrackingShells/.github/blob/main/instructions/documentation.instructions.md).*
