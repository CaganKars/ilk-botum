import discord
from discord.ext import commands
import random 
import os
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

sporcu_sozluğu = {"okcu":"Mete Gazoz (d. 8 Haziran 1999, İstanbul), Türk olimpik okçudur.[1] İstanbul Okçuluk Gençlik ve Spor Kulübü sporcusudur. Tokyo 2020 Olimpiyatları'nda ve 2023 Dünya Okçuluk Şampiyonası'nda altın madalya kazanarak Türk okçuluk tarihinin ilk Olimpiyat ve dünya şampiyonu olmuştur.[2]",
                  "halterci": "Naim Süleymanoğlu (Bulgaristan'da değiştirilen adı: Naum Şalamanov; 23 Ocak 1967, Kırcaali - 18 Kasım 2017, İstanbul), Türk haltercidir. Birçok otoriteye göre tüm zamanların en iyi haltercisi olarak kabul edilir.[1][2] Yapıca ufak tefek ancak çok güçlü olması nedeniyle Cep Herkül'ü olarak anılan Naim Süleymanoğlu, Türk Süpermen adıyla da anılır.[3]",
                  "cimnastikci":"İbrahim Çolak (d. 7 Ocak 1995), dünya ve Avrupa şampiyonu Türk artistik jimnastikçidir. Ege Üniversitesi Beden Eğitimi ve Spor Öğretmenliği mezunu ve İzmir'deki Şavkar Cimnastik Spor Kulübü'nün aktif sporcusudur.[1]"
                  }

@bot.command()
async def mem9(ctx):
    olasiliklar= [0.2,0.4,0.4]
    gorsel = random.choices(os.listdir('C:/Users/win/kodlama/spor/'),weights = olasiliklar , k = 1)[0]
    with open(f'C:/Users/win/kodlama/spor/{gorsel}','rb') as f:
        picture = discord.File(f)
        if f.name == 'mete.jpg':
            await ctx.send(file=picture)
            await ctx.send(sporcu_sozluğu["okcu"])

        if f.name == 'spor/thumbs_b_c_4dbc083ebd4260c4447603d4c3ab6a42.jpg':
            await ctx.send(file=picture)
            await ctx.send(sporcu_sozluğu["cimnastikci"])
            
        if f.name == 'naim.jpg':
            await ctx.send(file=picture)
            await ctx.send(sporcu_sozluğu["halterci"])




bot.run("") 
