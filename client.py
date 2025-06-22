import asyncio #支持异步操作
from mcp import ClientSession # MCP Client会话管理
from contextlib import AsyncExitStack  # 资源管理（确保客户端关闭时释放资源）

class MCPClient:
    def __init__(self):
        """初始化 MCP Client"""
        self.session = None
        self.exit_stack = AsyncExitStack()
        
    async def connect_to_mock_server(self):
        """模拟 MCP 服务器的连接（暂不连接真实服务器）"""
        print("MCP Client已初始化，但未连接到服务器")
        
    async def chat_loop(self):
        """运行交互式聊天循环"""
        print("\nMCP Client已启动！输入 'quit' 退出")
        while True:
            try:
                query = input("\nPrompt: ").strip()
                if query.lower() == 'quit':
                    break
                print(f"\n [模拟回复] 你说的是：{query}")
            except Exception as e:
                print(f"\n发生错误: {str(e)}")
                
    async def cleanup(self):
        """清理资源"""
        await self.exit_stack.aclose()
                
async def main():
    client = MCPClient()
    try:
        await client.connect_to_mock_server()
        await client.chat_loop()
    finally:
        await client.cleanup()
            
if __name__ == "__main__":
    asyncio.run(main())