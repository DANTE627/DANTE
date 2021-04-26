import discord
token = 'ODM2MTQ5MTE0MzI0MTIzNjY4.YIZyiw.dRKHYZW_wWm6rHDT8U7XEL-xdgU
client = discord.Client()
@client.event
async def on_ready():
    print('로그인되었습니다!')
    print(client.user.name)
    print(client.user.id)
    print('====================================')

@client.event
if message.content == "공지":
embed=discord.Embed(color=0xff00, title="[ 공지사항 ], description=" GTA5 에픽게임즈 새 계정 문화상품권 5000원에 판매 

유튜브 프리미엄 6개월 5000원에 판매 ")
await message.channel.send(embed=embed)

client.run(token)

