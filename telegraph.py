from telegraph.aio import Telegraph

class TelegraphHTML:

    def __init__(self, short_name: str, title: str, html: str):
        self.telegraph = Telegraph()
        self.title = title
        self.html = html
        self.short_name = short_name
        
    async def create_page(self) -> str:
        await self.telegraph.create_account(short_name=self.short_name)
        response = await self.telegraph.create_page(self.title, html_content=self.html)
        return response['url']