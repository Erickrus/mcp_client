from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math", log_level='ERROR')

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print(f"{a} + {b}")
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print(f"{a} * {b}")
    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio")
