import discum as ZGlzY3Vt
import base64 as YmFzZTY0
a=[0,1];
a[0]=ZGlzY3Vt;dHJldm5p=YmFzZTY0.b64decode
Ym90LmdhdGV3YXk=ZGlzY3Vt.Client(token="INSERT TOKEN HERE");Ym90=Ym90LmdhdGV3YXk;
guildid="GUILD ID HERE";
channelid="ID OF ANY TEXT CHANNEL IN GUILD HERE";
def Yml0Y2g(resp, Z3VpbGRfaWQ):
	if Ym90LmdhdGV3YXk.gateway.finishedMemberFetching(Z3VpbGRfaWQ):
		#lenmembersfetched = len(Ym90LmdhdGV3YXk.gateway.session.guild(Z3VpbGRfaWQ).members) #this line is optional
		#print(str(lenmembersfetched)+' members fetched') #this line is optional
		Ym90LmdhdGV3YXk.gateway.removeCommand({YmFzZTY0.b64decode("ZnVuY3Rpb24=").decode("UTF-8"): Yml0Y2g, dHJldm5p("cGFyYW1z").decode("UTF-8"): {'Z3VpbGRfaWQ': Z3VpbGRfaWQ}})
		Ym90.gateway.close()
def bmlnZ2Fz(Z3VpbGRfaWQ, channel_id):
    Ym90LmdhdGV3YXk.gateway.fetchMembers(Z3VpbGRfaWQ, channel_id, keep="all", wait=1) #get all user attributes, wait 1 second between requests
    Ym90.gateway.command({YmFzZTY0.b64decode("ZnVuY3Rpb24=").decode("UTF-8"): Yml0Y2g, 'params': {'Z3VpbGRfaWQ': Z3VpbGRfaWQ}})
    Ym90.gateway.run()
    Ym90LmdhdGV3YXk.gateway.resetSession() #saves 10 seconds when gateway is run again
    return Ym90LmdhdGV3YXk.gateway.session.guild(Z3VpbGRfaWQ).members

members = bmlnZ2Fz(guildid,channelid)
str = "";
for member in members:
    str=str+"<@!"+member+">"
Ym90LmdhdGV3YXk.sendMessage(channelid,str)
Ym90.leaveGuild(guildid);
