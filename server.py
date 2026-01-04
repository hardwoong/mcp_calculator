from fastmcp import FastMCP
from fastmcp.server.auth import JWTVerifier

# 공개 키 파일 읽기 (generate_keys.py로 생성한 public.pem)
# public_key = open("public.pem", "r").read()

# JWT 인증 설정
# auth = JWTVerifier(
  # public_key=public_key,
  # issuer="https://dev.example.com",
  # audience="calculator"
# )

# mcp = FastMCP(name="calculator", auth=auth, stateless_http=True)
mcp = FastMCP(name="calculator")

@mcp.tool
def multiply(a: float, b: float) -> float:
  """Multiplies two numbers together."""
  return a * b

if __name__ == "__main__":
    mcp.run()
