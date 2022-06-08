import discum
bot = discum.Client(token="OTYyODc2NTc2MDQ1ODYyOTQy.Yltg5w.n2yvKafSb0Je_FH-pR3SRdF8sdk")
guildid = "950264077857476638"
channelid = "950265152291344394"

def close_after_fetching(resp, guild_id):
	if bot.gateway.finishedMemberFetching(guild_id):
		lenmembersfetched = len(bot.gateway.session.guild(guild_id).members) #this line is optional
		print(str(lenmembersfetched)+' members fetched') #this line is optional
		bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
		bot.gateway.close()
def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1) #get all user attributes, wait 1 second between requests
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession() #saves 10 seconds when gateway is run again
    return bot.gateway.session.guild(guild_id).members

members = get_members(guildid,channelid)
str = "";
for member in members:
    str=str+"<@!"+member+">"
#bot.sendMessage(channelid,str)
print(str)
