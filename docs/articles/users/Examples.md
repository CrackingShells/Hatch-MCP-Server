# Examples

This article is about:

- Real-world usage patterns for HatchMCP
- Complete working examples for different scenarios
- Integration patterns with existing FastMCP servers
- Best practices demonstrated through code

## Basic Examples

### Simple MCP Server with Citations

```python
from hatch_mcp_server import HatchMCP

# Create a basic server with proper citations
hatch_mcp = HatchMCP(
    name="TextProcessor",
    origin_citation="Standard string processing algorithms",
    mcp_citation="Example Team, 'Text Processing MCP Server', 2024"
)

@hatch_mcp.server.tool()
def reverse_text(text: str) -> str:
    """Reverse the input text.
    
    Args:
        text: The text to reverse
        
    Returns:
        str: The reversed text
    """
    hatch_mcp.logger.info(f"Reversing text: {text[:20]}...")
    return text[::-1]

@hatch_mcp.server.tool()
def count_words(text: str) -> int:
    """Count words in the input text.
    
    Args:
        text: The text to analyze
        
    Returns:
        int: Number of words
    """
    word_count = len(text.split())
    hatch_mcp.logger.info(f"Counted {word_count} words")
    return word_count

if __name__ == "__main__":
    hatch_mcp.logger.info("Starting Text Processing server")
    hatch_mcp.server.run()
```

### Wrapping an Existing FastMCP Server

```python
from mcp.server.fastmcp import FastMCP
from hatch_mcp_server import HatchMCP

# Create an existing FastMCP server
math_server = FastMCP("MathOperations")

@math_server.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@math_server.tool()
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

# Wrap with HatchMCP for citation capabilities
hatch_mcp = HatchMCP(
    name="MathOperations",
    fast_mcp=math_server,
    origin_citation="Basic arithmetic operations - elementary mathematics",
    mcp_citation="Math Team, 'Arithmetic MCP Server', Educational Project, 2024"
)

if __name__ == "__main__":
    hatch_mcp.server.run()
```

## Scientific Computing Examples

### Data Analysis Server

```python
from hatch_mcp_server import HatchMCP
import json

# Server for basic data analysis with proper attribution
hatch_mcp = HatchMCP(
    name="DataAnalyzer",
    origin_citation="Statistics algorithms: Pearson (1895), Student t-test (1908)",
    mcp_citation="Research Lab, 'Statistical Analysis MCP Server', University, 2024"
)

@hatch_mcp.server.tool()
def calculate_mean(numbers: list) -> float:
    """Calculate the arithmetic mean of a list of numbers.
    
    Args:
        numbers: List of numeric values
        
    Returns:
        float: The arithmetic mean
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    
    result = sum(numbers) / len(numbers)
    hatch_mcp.logger.info(f"Calculated mean of {len(numbers)} values: {result}")
    return result

@hatch_mcp.server.tool()
def calculate_variance(numbers: list) -> float:
    """Calculate the variance of a list of numbers.
    
    Args:
        numbers: List of numeric values
        
    Returns:
        float: The variance
    """
    if len(numbers) < 2:
        raise ValueError("Need at least 2 values to calculate variance")
    
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    
    hatch_mcp.logger.info(f"Calculated variance: {variance}")
    return variance

@hatch_mcp.server.tool()
def basic_statistics(numbers: list) -> dict:
    """Calculate basic statistics for a dataset.
    
    Args:
        numbers: List of numeric values
        
    Returns:
        dict: Dictionary containing mean, variance, min, max, count
    """
    if not numbers:
        raise ValueError("Cannot calculate statistics for empty dataset")
    
    stats = {
        "count": len(numbers),
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "variance": 0.0 if len(numbers) < 2 else 
                   sum((x - sum(numbers) / len(numbers)) ** 2 for x in numbers) / (len(numbers) - 1)
    }
    
    hatch_mcp.logger.info(f"Calculated statistics for {len(numbers)} values")
    return stats

if __name__ == "__main__":
    hatch_mcp.logger.info("Starting Data Analyzer server")
    hatch_mcp.server.run()
```

### Algorithm Implementation Server

```python
from hatch_mcp_server import HatchMCP

# Server implementing a specific algorithm with proper citation
hatch_mcp = HatchMCP(
    name="SortingAlgorithms",
    origin_citation="Quicksort: Hoare, C.A.R. 'Quicksort', Computer Journal, 1962",
    mcp_citation="Algorithm Team, 'Sorting Algorithms MCP Server', CS Department, 2024"
)

@hatch_mcp.server.tool()
def quicksort(arr: list) -> list:
    """Sort an array using the quicksort algorithm.
    
    Args:
        arr: List of comparable items to sort
        
    Returns:
        list: Sorted list
    """
    hatch_mcp.logger.info(f"Sorting array of {len(arr)} elements")
    
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    result = quicksort(left) + middle + quicksort(right)
    hatch_mcp.logger.info("Sorting completed")
    return result

@hatch_mcp.server.tool()
def binary_search(sorted_arr: list, target) -> int:
    """Search for a target in a sorted array using binary search.
    
    Args:
        sorted_arr: Sorted list to search in
        target: Value to search for
        
    Returns:
        int: Index of target if found, -1 otherwise
    """
    hatch_mcp.logger.info(f"Searching for {target} in array of {len(sorted_arr)} elements")
    
    left, right = 0, len(sorted_arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] == target:
            hatch_mcp.logger.info(f"Found target at index {mid}")
            return mid
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    hatch_mcp.logger.info("Target not found")
    return -1

if __name__ == "__main__":
    hatch_mcp.logger.info("Starting Sorting Algorithms server")
    hatch_mcp.server.run()
```

## Advanced Examples

### Multi-Resource Server

```python
from hatch_mcp_server import HatchMCP

# Server with both tools and additional resources
hatch_mcp = HatchMCP(
    name="DocumentProcessor",
    origin_citation="Text processing algorithms and NLP techniques",
    mcp_citation="NLP Team, 'Document Processing MCP Server', AI Lab, 2024"
)

# Add custom resources alongside automatic citation resources
@hatch_mcp.server.resource(
    uri="info://processor/capabilities",
    name="Processor Capabilities",
    description="Information about document processing capabilities",
    mime_type="application/json"
)
def get_capabilities() -> str:
    """Return information about server capabilities."""
    capabilities = {
        "supported_formats": ["txt", "json"],
        "operations": ["word_count", "sentence_count", "extract_keywords"],
        "max_document_size": "10MB"
    }
    return json.dumps(capabilities, indent=2)

@hatch_mcp.server.tool()
def count_sentences(text: str) -> int:
    """Count sentences in text by counting periods, exclamation marks, and question marks.
    
    Args:
        text: The text to analyze
        
    Returns:
        int: Number of sentences
    """
    sentence_endings = ['.', '!', '?']
    count = sum(1 for char in text if char in sentence_endings)
    hatch_mcp.logger.info(f"Counted {count} sentences")
    return count

@hatch_mcp.server.tool()
def extract_keywords(text: str, max_keywords: int = 10) -> list:
    """Extract potential keywords from text (simple word frequency approach).
    
    Args:
        text: The text to analyze
        max_keywords: Maximum number of keywords to return
        
    Returns:
        list: List of potential keywords
    """
    # Simple keyword extraction (in practice, you'd use NLP libraries)
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Filter out common words (simplified stop words)
    common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should'}
    
    filtered_words = [word for word in words if word not in common_words and len(word) > 3]
    
    # Count word frequency
    word_freq = {}
    for word in filtered_words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort by frequency and return top keywords
    keywords = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:max_keywords]
    result = [word for word, freq in keywords]
    
    hatch_mcp.logger.info(f"Extracted {len(result)} keywords")
    return result

if __name__ == "__main__":
    hatch_mcp.logger.info("Starting Document Processor server")
    hatch_mcp.server.run()
```

### Server with Error Handling

```python
from hatch_mcp_server import HatchMCP

# Server demonstrating comprehensive error handling
hatch_mcp = HatchMCP(
    name="RobustCalculator",
    origin_citation="Mathematical operations with error handling patterns",
    mcp_citation="Engineering Team, 'Robust Calculator MCP Server', Company, 2024"
)

@hatch_mcp.server.tool()
def safe_divide(dividend: float, divisor: float) -> dict:
    """Safely divide two numbers with comprehensive error handling.
    
    Args:
        dividend: The number to be divided
        divisor: The number to divide by
        
    Returns:
        dict: Result with success status and value or error message
    """
    try:
        hatch_mcp.logger.info(f"Dividing {dividend} by {divisor}")
        
        if divisor == 0:
            hatch_mcp.logger.warning("Division by zero attempted")
            return {
                "success": False,
                "error": "Division by zero is not allowed",
                "result": None
            }
        
        result = dividend / divisor
        hatch_mcp.logger.info(f"Division successful: {result}")
        
        return {
            "success": True,
            "error": None,
            "result": result
        }
        
    except TypeError as e:
        hatch_mcp.logger.error(f"Type error in division: {e}")
        return {
            "success": False,
            "error": f"Invalid input types: {e}",
            "result": None
        }
    except Exception as e:
        hatch_mcp.logger.error(f"Unexpected error in division: {e}")
        return {
            "success": False,
            "error": f"Unexpected error: {e}",
            "result": None
        }

@hatch_mcp.server.tool()
def calculate_square_root(number: float) -> dict:
    """Calculate square root with input validation.
    
    Args:
        number: The number to find the square root of
        
    Returns:
        dict: Result with success status and value or error message
    """
    try:
        hatch_mcp.logger.info(f"Calculating square root of {number}")
        
        if number < 0:
            hatch_mcp.logger.warning(f"Negative input for square root: {number}")
            return {
                "success": False,
                "error": "Cannot calculate square root of negative number",
                "result": None
            }
        
        result = number ** 0.5
        hatch_mcp.logger.info(f"Square root calculated: {result}")
        
        return {
            "success": True,
            "error": None,
            "result": result
        }
        
    except Exception as e:
        hatch_mcp.logger.error(f"Error calculating square root: {e}")
        return {
            "success": False,
            "error": f"Calculation error: {e}",
            "result": None
        }

if __name__ == "__main__":
    hatch_mcp.logger.info("Starting Robust Calculator server")
    hatch_mcp.server.run()
```

## Testing Your Implementation

### Basic Testing

```python
# test_server.py - Basic functionality test
from hatch_mcp_server import HatchMCP

def test_basic_functionality():
    """Test basic server creation and citation setup."""
    try:
        # Create server
        server = HatchMCP(
            name="TestServer",
            origin_citation="Test origin citation",
            mcp_citation="Test MCP citation"
        )
        
        # Verify basic attributes
        assert server.name == "TestServer"
        assert server._origin_citation == "Test origin citation"
        assert server._mcp_citation == "Test MCP citation"
        assert hasattr(server, 'server')  # FastMCP instance
        assert hasattr(server, 'logger')  # Logger instance
        
        print("✓ Basic functionality test passed")
        return True
        
    except Exception as e:
        print(f"✗ Basic functionality test failed: {e}")
        return False

def test_tool_registration():
    """Test that tools can be registered normally."""
    try:
        server = HatchMCP("ToolTest")
        
        @server.server.tool()
        def test_tool(param: str) -> str:
            return f"Test: {param}"
        
        print("✓ Tool registration test passed")
        return True
        
    except Exception as e:
        print(f"✗ Tool registration test failed: {e}")
        return False

if __name__ == "__main__":
    print("Running basic tests...")
    
    success = True
    success &= test_basic_functionality()
    success &= test_tool_registration()
    
    if success:
        print("\n🎉 All basic tests passed!")
        print("Your HatchMCP implementation is working correctly.")
    else:
        print("\n❌ Some tests failed.")
        print("Check your installation and try again.")
```

## Common Patterns

### Hatch Package Entry Point

For Hatch package integration:

```python
# hatch_mcp_server_entry.py
from hatch_mcp_server import HatchMCP
from my_server import mcp  # Your FastMCP server

# Entry point for Hatch package system
hatch_mcp = HatchMCP(
    name="MyPackageName",
    fast_mcp=mcp,
    origin_citation="Smith, J. 'Original Research', Journal, 2024",
    mcp_citation="Your Name, 'MCP Implementation for MyPackage', 2024"
)

if __name__ == "__main__":
    hatch_mcp.server.run()
```

### Development vs Production Configuration

```python
import os
import logging
from hatch_mcp_server import HatchMCP

# Configure logging based on environment
if os.getenv("ENVIRONMENT") == "development":
    logging.getLogger("hatch_mcp_server.HatchMCP").setLevel(logging.DEBUG)
else:
    logging.getLogger("hatch_mcp_server.HatchMCP").setLevel(logging.WARNING)

# Create server with environment-specific citations
hatch_mcp = HatchMCP(
    name="MyServer",
    origin_citation=os.getenv("ORIGIN_CITATION", "Default origin citation"),
    mcp_citation=os.getenv("MCP_CITATION", "Default MCP citation")
)

# Add tools...

if __name__ == "__main__":
    hatch_mcp.logger.info(f"Starting server in {os.getenv('ENVIRONMENT', 'production')} mode")
    hatch_mcp.server.run()
```

These examples demonstrate the flexibility and power of HatchMCP while maintaining the scientific attribution that makes it valuable for research and autonomous systems.
