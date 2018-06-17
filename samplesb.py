from LINEPY import *
from akad.ttypes import *
from datetime import datetime
from time import sleep
from googletrans import Translator
from bs4 import BeautifulSoup
import time, random, multiprocessing, pafy, sys, json, codecs, threading, glob, re, string, os, pytz, requests, subprocess, six, urllib, urllib.parse
import youtube_dl
# Untuk Login Via Qr link 
#line = LINE()
#line.log("Auth Token : " + str(line.authToken))
#line.log("Timeline Token : " + str(line.tl.channelAccessToken))

# Untuk Login Via Email & password
#line = LINE('EMAIL', 'PASSWORD')
#line.log("Auth Token : " + str(line.authToken))
#line.log("Timeline Token : " + str(line.tl.channelAccessToken))

line = LINE()
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))

#ki = LINE("EttsSAtwN3CxCDgitz09.0etLz6ZbEjya81BwyooD/q.0Gp/Orxie34+9bjrRj+wEpdSUH6f7K+Wi5yRVPHPoTQ=")
#ki.log("Auth Token : " + str(ki.authToken))
#ki.log("Timeline Token :  "+ str(ki.tl.channelAccessToken))

mulai = time.time()
cl = line
call = cl
oepoll = OEPoll(cl)
All=[cl]
DEF=[cl]

mid = cl.getProfile().mid
#Amid = ki.getProfile().mid
Bots=[mid]
CITLBots=[mid] #,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid]
CITLself = ["u7484af57472be14114801703f5069c62"]
own = ["u7484af57472be14114801703f5069c62"]
admin = ["u7484af57472be14114801703f5069c62"]
staff = ["u7484af57472be14114801703f5069c62"]
#CITLFamily = CITLself + CITLBots + owner + admin + staff
msg_dict = {}
protect = []
protectqr = []
protectjoin = []
protectinvite = []
#protectpict = []
protectname = []
backupqr = []
welcome = []
lastTimeLiking = time.time()
settings = {
    "Picture":False,
    "group":{},
    "groupPicture":{},
    "responTag": "lagi sibuk",
    "ChangeVideoProfilevid": {},
    "ChangeVideoProfilePicture": {},
    "changePicture":{},
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

read = {
    'readPoint':{},
    'readMember':{},
    'readTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

cctv = {
  'point':{},
  'sidermem':{},
  'cyduk':{}
  }

mulai = time.time()
Setbot = codecs.open("selfbot.json","r","utf-8")
Setmain = json.load(Setbot)
settingsOpen = codecs.open("temp.json","r","utf-8")

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    time.sleep(10)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def autoRestart():
    if time.time() - mulai > int(Setmain["timeRestart"]):
        backupData()
        time.sleep(5)
        restartBot()
def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)


def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
       
        backup = Setmain
        f = codecs.open('aq.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        
        return True
    except Exception as error:
        logError(error)
        return False

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
        
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
   
def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
   


def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def mentionMembers(to, mid,name,url,iconlink):
    try:
        arrData = ""
        textx = "┌━━━━]「 Mention {} User 」[━━━━\n1• ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i• " % (num)
                num = (num+1)
            else:
                textx += "\n└━━━━「Done mention user」━━━━"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}'),'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink },0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def bot(op):
    try:
        if op.type == 5:
            if Setmain["CITLautoadd"] == True:
                ra = cl.getContact(op.param1)
                cl.findAndAddContactsByMid(ra.mid)
                cl.sendMessageWithMention(op.param1, op.param1,"Hai","\n\n{}".format(str(Setmain["CITLmessage"])))

        if op.param3 == "1":
            if op.param1 in protectname:
              	  #  if op.param2 not in admin and op.param2 not in Bots and op.param2 not in CITLBots:
                G = cl.getGroup(op.param1)
                try:
                   G.name = Setmain['pro_name'][op.param1]
                   cl.updateGroup(G)
                   cl.sendMessageWithMention(op.param1,op.param2 , "", "Groupname protect now")
                   Setmain["CITLblacklist"][op.param2] = True
                            #f=codecs.open('protectname.json','w','utf-8')
                           # json.dump(Setmain["CITLblacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                   print (e)
                   pass
        if op.type == 11:     
            if op.param3 == "4":
                if op.param1 in protectqr:
                    if op.param2 not in admin and op.param2 not in Bots and op.param2 not in CITLBots:
                        group = cl.getGroup(op.param1)
                        if group.preventedJoinByTicket == False:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendText(op.param1,"protect URL sedang aktif")
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            Setmain["CITLblacklist"][op.param2] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(Setmain["CITLblacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        else:
                            pass   
        #------Protect Group Kick start------#
        if op.type == 11:
            if op.param1 in backupqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                      #  if op.param2 not in Bots and op.param2 not in own and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    pass


        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in Setmain['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = ka.getGroup(op.param1)
                                    except:
                                        try:
                                            G = kb.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = Setmain['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        ka.updateGroup(G)
                                    except:
                                        try:
                                            kb.updateGroup(G)
                                        except:
                                            pass
                    if len in op.param3:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ka.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Nama group di kunci")
                                        ki.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        kk.sendText(op.param1,"Wekawekaweka 􀜁􀅔Har Har􏿿")
                                        c = Message(to=op.param1, _from=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
        if op.type == 22:
            if mid in op.param3:
                if Setmain["CITLautojoin"] == True:
                    cl.leaveRoom(op.param1)        
                
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in own and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        pass
        if op.type == 13:
            if mid in op.param3:
                if Setmain["CITLautojoin"] == True:
                    if Setmain["CITLbatas"]["on"] == True:
                        G = cl.getGroup(op.param1)
                        if len(G.members) > Setmain["CITLbatas"]["members"]:
                            cl.acceptGroupInvitation(op.param1)
                            ra = cl.getGroup(op.param1)
                            cl.sendText(op.param1,"Maaf jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["CITLbatas"]["members"]))
                            cl.leaveGroup(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            ra = cl.getGroup(op.param1)
                            cl.sendMessageWithMention(op.param1, op.param2,"hai ","\nterima kasih sudah diinvite...")
                            
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            if Setmain["CITLautojoin"] == True:
                if Setmain["autoReject"]["status"] == True:
                    if len(group.members) > Setmain["autoReject"]["members"]:
                        cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.rejectGroupInvitation(op.param1)
                else:
                    cl.acceptGroupInvitation(op.param1)
            gInviMids = []
            for z in group.invitee:
                if z.mid in op.param3:
                    gInviMids.append(z.mid)
            listContact = ""
            if gInviMids != []:
                for j in gInviMids:
                    name_ = cl.getContact(j).displayName
                    listContact += "\n      + {}".format(str(name_))

            arg = "   Group Name : {}".format(str(group.name))
            arg += "\n   Executor : {}".format(str(contact.displayName))
            arg += "\n   List User Invited : {}".format(str(listContact))
            print (arg)

        #------Joined User Kick start------#
        if op.type == 17:
            if op.param2 in Setmain["CITLblacklist"]:
                try:
                    random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                except:
                    random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                first=['hai kak','halloo kak..','Nah']
                sendMention(op.param1,op.param2,str(random.choice(first))+"","\n"+str(Setmain["welcome"]))
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in own and op.param2 not in admin and op.param2 not in staff:
                    Setmain["CITLblacklist"][op.param2] = True
                    try:
                        if op.param3 not in Setmain["CITLblacklist"]:
                        	cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                return

        #------Joined User Kick start------#
        if op.type == 19:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif op.param1 in protect:
                    Setmain ["CITLblacklist"][op.param2] = True
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[op.param3])
#-----------------------------------------------     
        if op.type == 19:
           if op.param3 in admin:
              random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
              random.choice(DEF).inviteIntoGroup(op.param1,admin)
           else:
               pass          
        
        if op.type == 46:
            if op.param2 in Bots:
                cl.removeAllMessages()
                
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                 if msg._from in admin:
                  if Setmain["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Add to Bot list succes")
                        Setmain["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        Setmain["addbots"] = True
                        cl.sendMessage(msg.to,"Add to Bot list succes")
                 if Setmain["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"delete from bot list succes")
                    else:
                        Setmain["dellbots"] = True
                        ki.sendMessage(msg.to,"Contact not in botlist")
#ADD STAFF
                 if msg._from in admin:
                  if Setmain["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Add to staff list Succes")
                        Setmain["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        Setmain["addstaff"] = True
                        cl.sendMessage(msg.to,"done add to staff list")
                 if Setmain["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Done delete from Stafflist")
                        Setmain["dellstaff"] = True
                    else:
                        Setmain["dellstaff"] = True
                        ki.sendMessage(msg.to,"Contact not in stafflist")
#ADD ADMIN
                 if msg._from in admin:
                  if Setmain["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Add to Admin list Succes")
                        Setmain["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        Setmain["addadmin"] = True
                        cl.sendMessage(msg.to,"Done Add To addminlist")
                 if Setmain["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes delete from adminlist")
                    else:
                        Setmain["delladmin"] = True
                        ki.sendMessage(msg.to,"Contact not in adminlist")
            if msg.contentType == 13:
                if Setmain["CITLwblack"] == True:
                    if msg.contentMetadata["mid"] in Setmain["CITLcommentBlack"]:
                        cl.sendText(msg.to,"In Blacklist")
                        Setmain["CITLwblack"] = False
                    else:
                        Setmain["CITLcommentBlack"][msg.contentMetadata["mid"]] = True
                        Setmain["CITLwblack"] = False
                        cl.sendText(msg.to,"Nothing")
                elif Setmain["CITLdblack"] == True:
                    if msg.contentMetadata["mid"] in Setmain["CITLcommentBlack"]:
                        del Setmain["CITLcommentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        Setmain["CITLdblack"] = False
                    else:
                        Setmain["CITLdblack"] = False
                        cl.sendText(msg.to,"Not in Blacklist")
                elif Setmain["CITLwblacklist"] == True:
                    if msg.contentMetadata["mid"] in Setmain["CITLblacklist"]:
                        cl.sendText(msg.to,"In Blacklist")
                        Setmain["CITLwblacklist"] = False
                    else:
                        Setmain["CITLblacklist"][msg.contentMetadata["mid"]] = True
                        Setmain["CITLwblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif Setmain["CITLdblacklist"] == True:
                    if msg.contentMetadata["mid"] in Setmain["CITLblacklist"]:
                        del Setmain["CITLblacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        Setmain["CITLdblacklist"] = False
                    else:
                        Setmain["CITLdblacklist"] = False
                        cl.sendText(msg.to,"Done")   

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                return            
            if msg.contentType == 16:
                if Setmain["checkPost"] == True:
                    if 'text' not in msg.contentMetadata:
                        if 'mediaOid' in msg.contentMetadata:
                            Object = msg.contentMetadata['mediaOid'].replace("svc=myhome|sid=h|","")
                            if msg.contentMetadata['mediaType'] == 'V':
                                if msg.contentMetadata['serviceType'] == 'GB':
                                    cl.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +cl.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&oid=" + msg.contentMetadata['mediaOid'] + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                                else:
                                    cl.sendMessage(msg.to, "━━━━「Detect Post」━━━━\n\n[Nama]: "+cl.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&" + Object + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                            else:
                                if msg.contentMetadata['serviceType'] == 'GB':
                                    cl.sendMessage(msg.to, "━━━━「Detect Post」━━━━\n\n[Nama]: "+cl.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                                else:
                                    cl.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +cl.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                        elif 'stickerId' in msg.contentMetadata:
                            if msg.contentMetadata['serviceType'] == 'GB':
                                cl.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +cl.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                            else:
                                cl.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +cl.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                        else:
                            if msg.contentMetadata['serviceType'] == 'GB':
                                cl.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +cl.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'])
                            else:
                                cl.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +cl.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'])
                    else:
                        if 'mediaOid' in msg.contentMetadata:
                            Object = msg.contentMetadata['mediaOid'].replace("svc=myhome|sid=h|","")
                            if msg.contentMetadata['mediaType'] == 'V':
                               if msg.contentMetadata['serviceType'] == 'GB':
                                    cl.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +cl.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&oid=" + msg.contentMetadata['mediaOid'] + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                               else:
                                    cl.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +cl.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&" + Object + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                            else:
                                if msg.contentMetadata['serviceType'] == 'GB':
                                    cl.sendMessage(msg.to, "━━━━「Detect Post」━━━━\n\n[Nama]: "+cl.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl']+ "\n\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                                else:
                                    cl.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +cl.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n[postURL]\n" + msg.contentMetadata['postEndUrl']+ "\n\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                        elif 'stickerId' in msg.contentMetadata:
                            if msg.contentMetadata['serviceType'] == 'GB':
                                cl.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +cl.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n\n[text]\n" + msg.contentMetadata['text'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                            else:
                                cl.sendMessage(msg.to, "━━━━「Detect Post」━━━━\n\n[Nama]: " +cl.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n\n[text]\n" + msg.contentMetadata['text'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                        else:
                            if msg.contentMetadata['serviceType'] == 'GB':
                                cl.sendMessage(msg.to, cl.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'])
                            else:
                                cl.sendMessage(msg.to, "━━━━「Detect Post」━━━━\n\n[Nama]: " +cl.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n\n[text]\n" + msg.contentMetadata['text'])
#==============================================================================#
        if op.type == 26:
           if Setmain["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if Setmain["talkban"] == True:
                   if msg._from in Setmain["Talkblacklist"]:
                      try:
                          random.choice(Bots).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(Bots).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(Bots).kickoutFromGroup(msg.to, [msg._from])

#===========================================================================
               if msg.text in ["Nuke",".","Kickall","kick on","Kick","kick","Crash","Cleanse","Kick on","Kicker","Spam","Mayhem","Nk @"]:
                   if Setmain ["kick"] == True:
                       try:
                           cl.sendText(msg.to,"Detect Danger message,,, Sorry I kill you from grup..")
                           cl.kickoutFromGroup(msg.to,[msg._from])
                       except:
                           pass
#========================================================================
               if msg.text in ["Ngentot","Kontol","Memek","Coli","Asww","Asw","Bego","Fuck","Babi"]:
                   if Setmain ["kick"] == True:
                       try:
                           cl.sendText(msg.to,"Ngomongnya dijaga bos...Kick yaaa.!!!")
                           cl.kickoutFromGroup(msg.to,[msg._from])
                       except:
                           pass
#=================================================================
               if msg.contentType == 7:
                 if Setmain["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\n🎖 STKID : " + msg.contentMetadata["STKID"] + "\n🎖 STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n🎖 STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if Setmain["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"🎖 Nama : " + msg.contentMetadata["displayName"] + "\n🎖 MID : " + msg.contentMetadata["mid"] + "\n🎖 Status Msg : " + contact.statusMessage + "\n🎖 Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)


        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if Setmain["cekUnsend"] == True:
                    try:
                        msg = op.message
                        if msg.toType == 0:
                            cl.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                        else:
                            cl.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                            ret_ = "🔰「Detect Pesan unsend」🔰"
                            msg_dict[msg.id] = {"txt":str(ret_), "text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        if msg.contentType == 1:
                            path = cl.downloadObjectMsg(msg_id) #, saveAs="unsend.png")
                           # msg.text = "Image"
                            ret_ = "🔰「Detect Image unsend」🔰"
                            msg_dict[msg_id] = {"path": path, "txt": str(ret_), "from":msg._from,"createdTime":msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        if msg.contentType == 7:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            text = "🔰「Detect sticker unsend」🔰"
                            ret_ = "\n\n「info sticker」"
                            ret_ += "\nSTICKER ID : {}".format(stk_id)
                            ret_ += "\nSTICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\nSTICKER VERSION : {}".format(stk_ver)
                            ret_ += "\nSTICKER URL : line://shop/detail/{}".format(pkg_id)
                            image = "http://dl.stickershop.line.naver.jp/products/0/0/{}/{}/android/stickers/{}.png".format(str(msg_dict[msg_id]["contentMetadata"]["STKVER"]),(msg_dict[msg_id]["contentMetadata"]["STKPKGID"]),(msg_dict[msg_id]["contentMetadata"]["STKID"]))
                            msg_dict[msg_id] = {"image":image, "text":str(ret_), "txt": text, "from":msg._from,"createdTime":msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    except Exception as error:
                        logError(error)
        if op.type == 65:
            #print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if Setmain["cekUnsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            ginfo = cl.getGroup(at)
                            contact = cl.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                            else:
                                name_ = contact.displayName
                                ret_ = "{}".format(str(msg_dict[msg_id]["txt"]))
                                ret_ += "\nPengirim : {}".format(str(contact.displayName))
                                ret_ += "\nWaktu pengiriman : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\nDi grup : {}".format(str(ginfo.name))
                                ret_ += "\nPesan: {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendText(at, ret_)
                                cl.sendImageWithURL(at, str(msg_dict[msg_id]["image"]))
                                cl.sendImage(at, str(msg_dict[msg_id]["path"]))
                            del msg_dict[msg_id]
                        else:
                            cl.sendMessage(at,"SentMessage cancelled,But I didn't have log data.\nSorry > <")
                except Exception as error:
                    logError(error)
        if op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if 'MENTION' in msg.contentMetadata.keys() != None:
                     if Setmain["detectMention"] == True:          
                        contact = cl.getContact(msg._from)
                        cName = contact.displayName
                        balas = Setmain["Respontag"]
                        path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        ret_ = "「 Auto Respon  」~\n\n" + (balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                               if mention['M'] in admin:
                                      citl = cl.getContact(msg._from)
                                      name = "[AUTO RESPON]"
                                      url = "http://line.me/ti/p/bJ3NcNuJX3"
                                      iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                                      cl.sendMessageWithContent(msg.to,str(ret_),name,url,iconlink)
                                      cl.sendImageWithURL(msg.to,path)
                                 # msg.contentType = 7   
                                #  msg.text = None
                                #  msg.contentMetadata = tikel
                                 # cl.sendMessage(msg)                                
                                      break
                if 'MENTION' in msg.contentMetadata.keys() != None:
                     if Setmain["Mentionkick"] == True:
                       name = re.findall(r'@(\w+)', msg.text)
                       mention = eval(msg.contentMetadata['MENTION'])
                       mentionees = mention['MENTIONEES']
                       for mention in mentionees:
                            if mention ['M'] in Bots:
                             #  cl.mentiontag(msg.to,[msg._from])
                               cl.sendMessageWithMention(msg.to, msg._from, "maaf kak ","Respon Kick aktif...")
                               cl.kickoutFromGroup(msg.to, [msg._from])
                               break


        if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Pic Group telah di ganti")

                if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = cl.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     cl.updateProfilePicture(path1)
                     cl.sendMessage(msg.to, "Pp telah di ganti")
                if msg.contentType == 2:
                  if msg._from in admin:
                    
                    path = cl.downloadObjectMsg(msg_id,returnAs='path',saveAs="tmp/vid.bin")
                    settings["ChangeVideoProfilevid"] = False
                    settings["ChangeVideoProfilePicture"] = True
                    cl.sendMessage(msg.to, "Send Gambarnya")
                if msg.contentType == 1:
                  if msg._from in admin:
                    path = cl.downloadObjectMsg(msg_id)
                    settings["ChangeVideoProfilePicture"] = False
                    cl.updateProfileVideoPicture(path)
                    cl.sendMessage(msg.to, "success")
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.contentType == 13:
                    if Setmain["CITLautoscan"] == True:
                        msg.contentType = 0
                        cl.sendText(msg.to,msg.contentMetadata["mid"])
                if msg.contentType == 1:
                    if Setmain["CITLaddimage"] == True:
                        try:
                            cl.downloadObjectMsg(msg_id,'path','dataSeen/%s.jpg' % Setmain["CITLimg"])
                            cl.sendMessage(msg.to, " 「 Picture 」\nType: Add Picture\nStatus: Success Add Picture♪")
                        except Exception as e:
                            cl.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                        Setmain["CITLimg"] = {}
                        Setmain["CITLaddimage"] = False
                        backupData()
                if msg.contentType == 16:
                    cl.likePost(msg.contentMetadata["mid"], msg.contentMetadata["postId"], likeType=1001)
                if msg.contentType == 7:
                    if Setmain["CITLaddsticker"] == True:
                        try:
                            Setmain["CITLsticker"][Setmain["CITLimg"]] = msg.contentMetadata
                            cl.sendMessage(msg.to, " 「 Sticker 」\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                        except Exception as e:
                            cl.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                        Setmain["CITLimg"] = {}
                        Setmain["CITLaddsticker"] = False
                        backupData()
                elif msg.contentType == 0:
                    if Setmain["CITLautoread"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
              
                    if text is None:    
                        return
                    else:
                        
            #---------------------- Start Command ------------------------#
                        
                        if text.lower() == "menu":
                          if msg._from in admin:
                            md = "🔰 |RA|Family Version 0.1\n\n"
                            md += "🔰 .cek「@」\n"
                            md += "🔰 .gid\n"
                            md += "🔰 .yid\n"
                            md += "🔰 .me\n"
                            md += "🔰 .informasi\n"
                            md += "🔰 .myname\n"
                            md += "🔰 .mybio\n"
                            md += "🔰 .mycover\n"
                            md += "🔰 .mypict\n"
                            md += "🔰 .steal contact「 Mention 」\n"
                            md += "🔰 .steal mid 「 Mention 」\n"
                            md += "🔰 .steal name 「 Mention 」\n"
                            md += "🔰 .steal bio 「 Mention 」\n"
                            md += "🔰 .steal pict 「 Mention 」\n"
                            md += "🔰 .steal vid 「 Mention 」\n"
                            md += "🔰 .steal cover 「 Mention 」\n"
                            md += "🔰 .spbot\n"
                            md += "🔰 .info set\n"
                            md += "🔰 .restart\n"
                            md += "🔰 .runtime\n"
                            md += "🔰 .removechat\n"
                            md += "🔰 .changevideoprofile\n"
                            md += "🔰 .changeprofile\n"
                            md += "🔰 .changegroup\n"
                            citl = cl.getContact(msg._from)
                            name = "「 King Bii 」"
                            url = "http://line.me/ti/p/whiterascals1"
                            iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                            cl.sendMessageWithContent(msg.to,md,name,url,iconlink)
                        elif text.lower() == "pengaturan":
                          if msg._from in admin:
                            md = "🔰 |RA|Family Version 0.1\n\n"
                            md += "🔰 .ceksider 「on/off」\n"
                            md += "🔰 .cekmid 「on/off」\n"
                            md += "🔰 .ceksticker 「on/off」\n"
                            md += "🔰 .cekcontact 「on/off」\n"
                            md += "🔰 .welcome 「on/off」\n"
                            md += "🔰 .cekunsend 「on/off」\n"
                            md += "🔰 .responkick 「on/off」\n"
                            md += "🔰 .autorespon 「on/off」\n"
                            md += "🔰 .autoread 「on/off」\n"
                            citl = cl.getContact(msg._from)
                            name = "「 King Bii 」"
                            url = "http://line.me/ti/p/whiterascals1"
                            iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                            cl.sendMessageWithContent(msg.to,md,name,url,iconlink)
                        elif text.lower() == "group":
                          if msg._from in admin:
                            md = "🔰 |RA|Family Version 0.1\n\n"
                            md += "🔰 .cek mention\n"
                            md += "🔰 .t mention 「 text 」\n"
                            md += "🔰 .open\n"
                            md += "🔰 .close\n"
                            md += "🔰 .gurl\n"
                            md += "🔰 .ginfo\n"
                            md += "🔰 .gcreator\n"
                            md += "🔰 .group name\n"
                            md += "🔰 .group pict\n"
                            md += "🔰 .infogrup 「 Number 」\n"
                            md += "🔰 .infomem 「 Number 」\n"
                            md += "🔰 .leave: 「 Number 」\n"
                            md += "🔰 .bpc 「 Text 」\n"
                            md += "🔰 .bgroup 「 Text 」\n"
                            md += "🔰 .allbroadcast 「 Text 」\n"
                            md += "🔰 .bipc: 「 Link image 」\n"
                            md += "🔰 .bigroup: 「 Link image 」\n"
                            md += "🔰 .bye\n"
                            md += "🔰 .absen\n"
                            md += "🔰 .kick「 Mention 」\n"
                            citl = cl.getContact(msg._from)
                            name = "「 King Bii 」"
                            url = "http://line.me/ti/p/whiterascals1"
                            iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                            cl.sendMessageWithContent(msg.to,md,name,url,iconlink)
                        elif text.lower() == "setting":
                          if msg._from in admin:
                            md = "🔰 |RA|Family Version 0.1\n\n"
                            md += "🔰 .cpesan add\n"
                            md += "🔰 .cpesan respon\n"
                            md += "🔰 .cpesan welcomemessage\n"
                            md += "🔰 .cpesan spam\n"
                            md += "🔰 .cpesan add: 「 Text 」\n"
                            md += "🔰 .cpesan respon: 「 Text 」\n"
                            md += "🔰 .cpesan welcomemessage: 「 Text 」\n"
                            md += "🔰 .cpesan spam: 「 Text 」\n"
                            citl = cl.getContact(msg._from)
                            name = "「 King Bii 」"
                            url = "http://line.me/ti/p/whiterascals"
                            iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                            cl.sendMessageWithContent(msg.to,md,name,url,iconlink)
                        elif text.lower() == "media":
                          if msg._from in admin:
                            md = "🔰 |RA|Family Version 0.1\n\n"
                            md += "🔰 .cekcuaca 「 Location 」\n"
                            md += "🔰 .ceksholat: 「 Location 」\n"
                            md += "🔰 .ceklokasi: 「 Location 」\n"
                            md += "🔰 .artinama: 「 Nama 」\n"
                            md += "🔰 .artimimpi: 「 mimpi 」\n"
                            md += "🔰 .telpon: 「 No. tujuan 」\n"
                            md += "🔰 .sms: 「 No. tujuan 」\n"
                            md += "🔰 .lirik: 「 judul 」\n"
                            md += "🔰 .music: 「 Nama penyanyi 」\n"
                            md += "🔰 .ytmp3: 「 Judul lagu 」\n"
                            md += "🔰 .ytmp4: 「 Judul video 」\n"
                            md += "🔰 .zodiak: 「 nama zodiak 」\n"
                            md += "🔰 .retrowave: 「 text1:text2:text3 」\n"
                            md += "🔰 .cooltext: 「 Text 」\n"
                            md += "🔰 .addsticker 「 Text 」\n"
                            md += "🔰 .list sticker\n"
                            md += "🔰 .kalender\n"
                            md += "🔰 .carigambar: 「 Text 」\n"
                            md += "🔰 .cariaplikasi: 「 Nama Aplikasi 」\n"
                            md += "🔰 .jumlahtag: 「 Jumlahnya 」\n"
                            md += "🔰 .jumlahcall: 「 Jumlahnya 」\n"
                            md += "🔰 .spamtag 「 Mention 」\n"
                            md += "🔰 .spamcall\n"
                            citl = cl.getContact(msg._from)
                            name = "「 King Bii 」"
                            url = "http://line.me/ti/p/whiterascals"
                            iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                            cl.sendMessageWithContent(msg.to,md,name,url,iconlink)
                        elif text.lower() == "blacklist":
                          if msg._from in admin:
                            md = "🔰 |RA|Family Version 0.1\n\n"
                            md += "🔰 .contactban\n"
                            md += "🔰 .addbanned:on\n"
                            md += "🔰 .dellbanned:on\n"
                            md += "🔰 .addtalkban:on\n"
                            md += "🔰 .delltalkban:on\n"
                            md += "🔰 .addbanned 「 Mention 」\n"
                            md += "🔰 .dellbanned 「 Mention 」\n"
                            md += "🔰 .addtalkban 「 Mention 」\n"
                            md += "🔰 .delltalkban 「 Mention 」\n"
                            md += "🔰 .cekbanned\n"
                            md += "🔰 .bersihkanbl\n"
                            md += "🔰 .refresh\n"
                            md += "🔰 scan blacklist\n"
                            citl = cl.getContact(msg._from)
                            name = "「 King Bii 」"
                            url = "http://line.me/ti/p/whiterascals1"
                            iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                            cl.sendMessageWithContent(msg.to,md,name,url,iconlink)
                        elif text.lower() == "help":
                          if msg._from in admin:
                            md = "🔰 |RA|Selfbot Version 0.1 \n\n"
                            md += "🔰 Menu\n"
                            md += "🔰 group\n"
                            md += "🔰 pengaturan\n"
                            md += "🔰 media\n"
                            md += "🔰 setting\n"
                            md += "🔰 blacklist\n"
                            md += "🔰 protect\n"
                            citl = cl.getContact(msg._from)
                            name = "「 King Bii 」"
                            url = "http://line.me/ti/p/whiterascals1"
                            iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                            cl.sendMessageWithContent(msg.to,md,name,url,iconlink)
                            
                        elif text.lower() == ".info set":
                            if msg._from in admin:
                                ginfo = cl.getGroup(msg.to)
                                md = "🔰 |RA|Settings\nGroup Name : " + str(ginfo.name)+"\n\n"
                                if Setmain["CITLautoscan"] == True: md+="┏━━━━━━━━━━━━\n┃• Cekmid「✅」\n"
                                else: md+="┏━━━━━━━━━━━━\n┃• Cekmid「✖」\n"
                                if Setmain["contact"] == True: md+="┃• Contact「✅」\n"
                                else: md+="┃• Contact「✖」\n"
                                if Setmain["cekUnsend"] == True: md+="┃• Unsend「✅」\n"
                                else: md+="┃• Unsend「✖」\n"
                                if Setmain["checkPost"] == True: md+="┃• Share「✅」\n"
                                else: md+="┃• Share「✖」\n"
                                if Setmain["sticker"] == True: md+="┃• Sticker「✅」\n"
                                else: md+="┃• Sticker「✖」\n"
                                if Setmain["CITLautoread"] == True: md+="┃• Auto read「✅」\n"
                                else: md+="┃• Auto read「✖」\n"
                                if Setmain["CITLautojoin"] == True: md+="┃• Auto join「✅」\n"
                                else: md+="┃• Auto join「✖」\n"
                                if Setmain["CITLautoadd"] == True: md+="┃• Auto add「✅」\n"
                                else: md+="┃• Auto add「✖」\n"
                                if Setmain["autoReject"] == True: md+="┃• Auto reject「✅」\n"
                                else: md+="┃• Auto reject「✖」\n"
                                if Setmain["detectMention"] == True: md+="┃• Auto respon「✅」\n"
                                else: md+="┃• Auto respon「✖」\n"
                                if msg.to in welcome: md+="┃• Welcomemessage「✅」\n"
                                else: md+="┃• Welcomemessage「✖」\n"
                                if msg.to in protectqr: md+="┃• Protect Qr「✅」\n"
                                else: md+="┃• Protect Qr「✖」\n"
                                if msg.to in protectjoin: md+="┃• Protect Join「✅」\n"
                                else: md+="┃• Protect Join「✖」\n"
                                if msg.to in protect: md+="┃• Protect「✅」\n"
                                else: md+="┃• Protect「✖」\n"
                                if msg.to in protectinvite: md+="┃• Protect Invite「✅」\n"
                                else: md+="┃• Protect Invite「✖」\n"
                                if msg.to in protectname: md+="┃• Namelock「✅」\n"
                                else: md+="┃• Namelock「✖」\n"
                                if msg.to in backupqr: md+="┃• Qrlock「✅」\n"
                                else: md+="┃• Qrlock「✖」\n"
                                if Setmain["kick"] == True: md+="┃• Kata Larangan「✅」\n┗━━━━━━━━━━━━"
                                else: md+="┃• Kata Larangan「✖」\n┗━━━━━━━━━━━━"
                                cl.sendText(msg.to, md)
                                
            #---------------------- On/Off Command -------------------# 
                        elif text.lower() == "bot on":
                            if msg._from in admin:
                                Setmain["selfbot"] = True
                                cl.sendText(msg.to, "Bot Aktif")
                                
                        elif text.lower() == "bot off":
                            if msg._from in admin:
                                Setmain["selfbot"] = False
                                cl.sendText(msg.to, "Bot Nonaktif")
                                            
                        elif text.lower() == '.responkick on':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                              if Setmain["Mentionkick"] == False:
                                Setmain["Mentionkick"] = True
                                cl.sendMessageWithMention(msg.to,msg._from,"","Auto Respon Kick Di Aktifkan")

                        elif text.lower() == '.responkick off':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                              if Setmain["Mentionkick"] == True:
                                Setmain["MentionKick"] = False
                                cl.sendMessageWithMention(msg.to,msg._from,"","Auto Respon Kick Di Matikan")

                        elif text.lower() == '.cekcontact on':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["contact"] = True
                                cl.sendMessageWithMention(msg.to,msg._from,"","Cek Contact Di Aktifkan")

                        elif text.lower() == '.cekcontact off':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["contact"] = False
                                cl.sendMessageWithMention(msg.to,msg._from,"","Cek Contact Di Matikan")

                        elif text.lower() == '.autorespon on':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["detectMention"] = True
                                cl.sendMessageWithMention(msg.to,msg._from,"","Auto Respon Di Aktifkan")

                        elif text.lower() == '.autorespon off':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["detectMention"] = False
                                cl.sendMessageWithMention(msg.to,msg._from,"","Auto Respon Di Matikan")
                        elif text.lower() == '.ceksticker on':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["sticker"] = True
                                cl.sendMessageWithMention(msg.to,msg._from,"","Cek Sticker Di Aktifkan")

                        elif text.lower() == '.ceksticker off':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["sticker"] = False
                                cl.sendMessageWithMention(msg.to,msg._from,"","Cek Sticker Di Matikan")
                        elif text.lower() == '.cekunsend on':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["cekUnsend"] = True
                                cl.sendMessageWithMention(msg.to,msg._from,"","Cek Unsend Di Aktifkan")

                        elif text.lower() == '.cekunsend off':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["cekUnsend"] = False
                                cl.sendMessageWithMention(msg.to,msg._from,"","Cek Unsend Di Matikan")
                        elif text.lower() == '.cekpost on':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["checkPost"] = True
                                cl.sendMessageWithMention(msg.to,msg._from,"","Cek Post Di Aktifkan")

                        elif text.lower() == '.cekpost off':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["checkPost"] = False
                                cl.sendMessageWithMention(msg.to,msg._from,"","Cek Post Di Matikan")
                        elif text.lower() == ".autoreject on":
                            if msg._from in admin:
                                if Setmain["autoReject"] == False:
                                    Setmain["autoReject"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Auto Reject Di Aktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Auto Reject Di Aktifkan")
                                    
                        elif text.lower() == ".autoreject off":
                            if msg._from in admin:
                                if Setmain["autoReject"] == True:
                                    Setmain["autoReject"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Auto Reject Di Matikan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Auto Reject Di Matikan")           
                        elif text.lower() == ".autojoin on":
                            if msg._from in admin:
                                if Setmain["CITLautojoin"] == False:
                                    Setmain["CITLautojoin"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Auto Join Di Aktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Auto Join Di Aktifkan")
                                    
                        elif text.lower() == ".autojoin off":
                            if msg._from in admin:
                                if Setmain["CITLautojoin"] == True:
                                    Setmain["CITLautojoin"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Auto join Di Matikan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Auto join Di Matikan")    

                        elif text.lower() == ".autoadd on":
                            if msg._from in admin:
                                if Setmain["CITLautojoin"] == False:
                                    Setmain["CITLautojoin"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Auto Add Di Aktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Auto Add Di Aktifkan")
                                    
                        elif text.lower() == ".autoadd off":
                            if msg._from in admin:
                                if Setmain["CITLautoadd"] == True:
                                    Setmain["CITLautoadd"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Auto Add Di Matikan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Auto Add Di Matikan")                             
                        elif text.lower() == '.kata terlarang on':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["kick"] = True
                                cl.sendMessageWithMention(msg.to,msg._from,"","Kata Terlarang Di Aktifkan\nDilarang mengunakan kata kotor atau kata larangan lain nya")

                        elif text.lower() == '.kata terlarang off':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["kick"] = False
                                cl.sendMessageWithMention(msg.to,msg._from,"","Kata Terlarang Di Matikan")

                        elif text.lower() == ".autoread on":
                            if msg._from in admin:
                                if Setmain["CITLautoread"] == False:
                                    Setmain["CITLautoread"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Autoread diaktifkan")
                                else:
                                    ki.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".autoread off":
                            if msg._from in admin:
                                if Setmain["CITLautoread"] == True:
                                    Setmain["CITLautoread"] = False
                                    ki.sendMessageWithMention(msg.to,msg._from,"","Autoread dinonaktifkan")
                                else:
                                    ki.sendMessageWithMention(msg.to,msg._from,"","Sudah off")
                                    
                        elif text.lower() == ".cekmid on":
                            if msg._from in admin:
                                if Setmain["CITLautoscan"] == False:
                                    Setmain["CITLautoscan"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Cekmid diaktifkan")
                                else:
                                    ki.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".cekmid off":
                            if msg._from in admin:
                                if Setmain["CITLautoscan"] == True:
                                    Setmain["CITLautoscan"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Cekmid dinonaktifkan")
                                else:
                                    ki.sendMessageWithMention(msg.to,msg._from,"","Sudah off")           
                        elif '.welcomemessage ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome allready on"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome On\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Sudah on"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectqr ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectqr ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Succes"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url On\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url Off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url Off"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                        elif 'Lockqr ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Lockqr ','')
                              if spl == 'on':
                                  if msg.to in backupqr:
                                       msgs = "Succes"
                                  else:
                                       backupqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Qr Lock On\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in backupqr:
                                         backupqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Qr Lock Off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Qr Lock Off"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite on"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect invite On\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect invite Off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite off"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join on"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect join on\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect join off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join off"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                        elif 'Lockpict ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Lockpict ','')
                              if spl == 'on':
                                  if msg.to in protectpict:
                                       msgs = "Succes"
                                  else:
                                       protectpict.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Picture Lock On\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectpict:
                                         protectpict.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Picture Lock Off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Picture Lock Off"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protect ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protect ','')
                              if spl == 'on':
                                  if msg.to in protect:
                                       msgs = "Protect on"
                                  else:
                                       protect.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect on\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect:
                                         protect.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect off"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Namelock ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Namelock ','')
                              if spl == 'on':
                                  if msg.to in protectname:
                                       msgs = "Namelock on"
                                  else:
                                       protectname.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       Setmain['pro_name'][msg.to] = ginfo.name
                                       msgs = "Namelock on\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectname:
                                         protectname.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Namelock off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Namelock off"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                        elif text.lower() == "operator":
                            if msg._from in admin:
                                ab = ""
                                cd = ""
                                ef = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in own:
                                    a = a + 1
                                    end = '\n'
                                    ab += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    cd += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    ef += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🔏「 List Operator 」🔏\n\n⏺Owner:\n"+ab+"\n⏺Admin:\n"+cd+"\n⏺Staff:\n"+ef+"\n「%s」List Operator" %(str(len(own)+len(admin)+len(staff))))

                        elif text.lower() == ".list protect":
                            if msg._from in admin:
                                ab = ""
                                cd = ""
                                ef = ""
                                gh = ""
                                ij = ""
                                kl = ""
                                c = 0
                                i = 0
                                t = 0
                                l = 0
                                s = 0
                                t = 0
                                gid = protect
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    ab += str(c) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectqr
                                for group in gid:
                                    i = i + 1
                                    end = '\n'
                                    cd += str(i) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    t = t + 1
                                    end = '\n'
                                    ef += str(t) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    l = l + 1
                                    end = '\n'
                                    gh += str(l) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectname
                                for group in gid:
                                    s = s + 1
                                    end = '\n'
                                    ij += str(s) + ". " +cl.getGroup(group).name + "\n"
                                gid = backupqr
                                for group in gid:
                                    t = t + 1
                                    end = '\n'
                                    kl += str(t) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"🔰|RA|Protect\n\n🔰 Protect kick:\n"+ab+"\n🔰 Protect qr:\n"+cd+"\n🔰 Protect join: \n"+ef+"\n🔰 Protect invite: \n"+gh+"\n🔰 Protect name: \n"+ij+"\n🔰 Backup qr: \n"+kl+"\n「%s」🔏List Protect Group🔏" %(str(len(protect)+len(protectqr)+len(protectjoin)+len(protectinvite)+len(protectname)+len(backupqr))))

            
                        elif text.lower().startswith(".cek "):
                          if msg._from in admin:
                            key = eval(msg.contentMetadata["MENTION"])
                            keys = key["MENTIONEES"][0]["M"]
                            ra = cl.getContact(keys)
                            try:
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/{}".format(str(ra.pictureStatus)))
                                cl.sendMessageWithMention(msg.to,ra.mid,"[Nama]\n","\n\n[Bio]\n{}".format(str(ra.statusMessage)))
                            except:
                                pass
                            
                        elif text.lower() == ".gid":
                          if msg._from in admin:
                            cl.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                            cl.sendText(msg.to,msg.to)
                            
                        elif text.lower() == ".yid":
                          if msg._from in admin:
                            cl.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                            cl.sendText(msg.to,msg._from)
                        
                        elif text.lower() == ".me":
                          if msg._from in admin:
                            cl.sendMessageWithMention(msg.to, msg._from, "","Hadirr")
                            cl.sendContact(msg.to,msg._from)
                        elif text.lower() == 'mid':
                            citl = cl.getContact(msg._from)
                            name = "[Your Id]"
                            url = "http://line.me/ti/p/whiterascals1"
                            iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                            cl.sendMessageWithContent(msg.to,msg._from,name,url,iconlink)
                        elif text.lower() == '.myname':
                          if msg._from in admin :
                            me = cl.getContact(msg._from)
                            cl.sendMessageWithMention(msg.to, msg._from, "","Your Name\n" + me.displayName)
                        elif text.lower() == '.mybio':
                          if msg._from in admin:
                            me = cl.getContact(msg._from)
                            cl.sendMessageWithMention(msg.to, msg._from, "","Your Bio\n" + me.statusMessage)
                        elif text.lower() == '.mypicture':
                          if msg._from in admin:
                            me = cl.getContact(msg._from)
                            cl.sendMessageWithMention(msg.to, msg._from, "Ini Foto Profile kamu "," yg paling keceh")
                            cl.sendImageWithURL(msg.to, "http://dl.profile.line-cdn.net/{}".format(me.pictureStatus))
                        elif text.lower() == '.mycover':
                          if msg._from in admin :
                            #me = cl.getContact(msg._from)
                            channel = cl.getProfileCoverURL(msg._from)
                            path = str(channel)
                            cl.sendImageWithURL(msg.to, path)
                        elif ".cpesan add:" in msg.text:
                          if msg._from in admin :
                            Setmain["pesan"] = msg.text.replace(".cpesan add:","")
                            cl.sendText(msg.to,"We changed the message")
                        elif ".cpesan welcomemessage: " in msg.text:
                          if msg._from in admin:
                            Setmain["welcome"] = msg.text.replace(".cpesan welcomemessage: ","")
                            cl.sendText(msg.to,"update welcome message succes"+ datetime.today().strftime('%H:%M:%S'))

                        elif '.cpesan respon: ' in msg.text:
                           if msg._from in admin:
                              c = msg.text.replace('.cpesan respon: ','')
                              if c in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon")
                              else:
                                  Setmain["Respontag"] = c
                                  cl.sendMessage(msg.to, "「 Auto Respon 」\nRespon diganti jadi :\n\n「"+ c +"」")

                        elif '.cpesan spam: ' in msg.text:
                          if msg._from in admin:
                             Setmain["CITLspam"] = msg.text.replace('.cpesan spam: ','')
                             cl.sendMessage(msg.to, "「 Spam 」\nSpam diganti jadi :\n\n「"+ Setmain["CITLspam"] +"」")
                        elif text.lower() == ".cpesan add":
                          if msg._from in admin:
                             cl.sendMessage(msg.to, "「 Pesan 」\n\n" + Setmain["pesan"])

                        elif text.lower() == ".cpesan welcomemessage":
                          if msg._from in admin:
                             cl.sendMessage(msg.to, "「 Welcome Message 」\n\n" + Setmain["welcome"])

                        elif text.lower() == ".cpesan respon":
                          if msg._from in admin:
                             cl.sendMessage(msg.to, "「 Auto Respon 」\n\n" + Setmain["Respontag"])

                        elif text.lower() == ".cpesan spam":
                          if msg._from in admin:
                             cl.sendMessage(msg.to, "「 Spam 」\n\n" + Setmain["CITLspam"])

#================[script steal]==================

                        elif msg.text.lower().startswith(".steal contact "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    mi_d = contact.mid
                                    cl.sendContact(msg.to, mi_d)
                        elif msg.text.lower().startswith(".steal mid "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = "[ Mid User ]"
                                for ls in lists:
                                    ret_ += "\n{}" + ls
                                cl.sendMessage(msg.to, str(ret_))
                        elif msg.text.lower().startswith(".steal name "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                        elif msg.text.lower().startswith(".steal bio "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                        elif msg.text.lower().startswith(".steal pict "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.line.naver.jp/" + cl.getContact(ls).pictureStatus
                                    cl.sendImageWithURL(msg.to, str(path))
                        elif msg.text.lower().startswith(".steal vid "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.line.naver.jp/" + cl.getContact(ls).pictureStatus + "/vp"
                                    cl.sendImageWithURL(msg.to, str(path))
                        elif msg.text.lower().startswith(".steal cover "):
                          if msg._from in admin:
                            if line != None:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = cl.getProfileCoverURL(ls)
                                        cl.sendImageWithURL(msg.to, str(path))
                        elif msg.text.lower() == 'kata':
                            try:
                                r = requests.get('https://fendisamuel.cf/api/quote/')
                                data = r.json()
                                result = "[Quotes :]\nAuthor : %s\nQuotes :\n%s " % (data['author'],data['result'])
                                cl.sendText(msg.to, result)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))
 #================[script steal Done]==================                                       
                        elif text.lower() == ".spbot":
                          if msg._from in admin :
                            start = time.time()
                            cl.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start
                            cl.sendText(msg.to, "%s " % (elapsed_time))
                        elif msg.text.lower().startswith('.addsticker'):
                          if msg._from in admin :
                            separate = text.split(" ")
                            text = text.replace(separate[0]+" ","")
                            Setmain["CITLsticker"][text] = '%s' % text
                            Setmain["CITLimg"] = '%s' % text
                            Setmain["CITLaddsticker"] = True
                            backupData()
                            cl.sendMessage(msg.to, " 「 Sticker 」\nSend the sticker")
                        elif msg.text.lower() in Setmain["CITLsticker"]:
                          if msg._from in admin :
                            try:
                                cl.sendMessage(msg.to,text=None,contentMetadata=Setmain['CITLsticker'][text.lower()], contentType=7)
                            except Exception as e:
                                cl.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                        elif msg.text.lower() == ".list sticker":
                          if msg._from in admin :
                            if Setmain["CITLsticker"] == {}:
                                cl.sendMessage(msg.to, " 「 Sticker List 」\nNo Sticker")
                            else:
                                num=1
                                msgs=" 「 Sticker List 」\nSticker List:"
                                for a in Setmain["CITLsticker"]:
                                    msgs+="\n%i. %s" % (num, a)
                                    num=(num+1)
                                msgs+="\n\nTotal Sticker List: %i" % len(Setmain["CITLsticker"])
                                cl.sendMessage(msg.to, msgs)

                        elif text.lower() == ".restart":
                          if msg._from in admin:
                            cl.sendMessage(msg.to, "Mencoba restart...")
                            cl.sendMessageWithMention(msg.to, msg._from, " ", "Mohon tunggu beberapa saat...")
                            Setmain["restartPoint"] = msg.to
                            restartBot()
                        elif msg.text.lower() == '.runtime':
                            citl = cl.getContact(msg._from)
                            cl.sendMessage(msg.to ,"「Please wait..」")
                            eltime = time.time() - lastTimeLiking
                            van = "Bot sudah berjalan selama "+waktu(eltime)
                            name = "[RUN TIME]"
                            url = "http://line.me/ti/p/bJ3NcNuJX3"
                            iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                            cl.sendMessageWithContent(msg.to,van,name,url,iconlink)
                           
                        elif text.lower() == "time":
                            cl.sendMessage(to, "Goblok cek sendiri di tanggal jangan manja")
                        elif text.lower() == '.informasi':
                          if msg._from in admin:
                            try:
                                arr = []
                                creator = "u7484af57472be14114801703f5069c62"
                                creator = cl.getContact(creator)
                                eltime = time.time() - lastTimeLiking
                                contact = cl.getContact(mid)
                                grouplist = cl.getGroupIdsJoined()
                                contactlist = cl.getAllContactIds()
                                blockedlist = cl.getBlockedContactIds()
                                name = "[INFO BOT]"
                                url = "http://line.me/ti/p/bJ3NcNuJX3"
                                iconlink = "http://dl.profile.line-cdn.net/{}".format(str(creator.pictureStatus))
                                ret_ = "🔰|RA|Informasi"
                                ret_ += "\n🔰 Pemain : {}".format(contact.displayName)
                                ret_ += "\n🔰 Jumlah Group : {}".format(str(len(grouplist)))
                                ret_ += "\n🔰 Jumlah Teman : {}".format(str(len(contactlist)))
                                ret_ += "\n🔰 Jumlah Block : {}".format(str(len(blockedlist)))
                                ret_ += "\n🔰 Runtime : "+waktu(eltime)
                                ret_ += "\n🔰 Version : 0.1"
                                ret_ += "\n🔰 Creator : {}".format(creator.displayName)
                                ret_ += "\n\nThanks For White Rascals\nSuported By 「🔰ᴿᴬFᴀᴍɪʟʏ™」"
                                cl.sendMessageWithContent(msg.to,str(ret_),name,url,iconlink) #,{'AGENT_NAME': [INFO BOT],'AGENT_LINK': Link OA/kontak,'AGENT_ICON': Link icon profile/gambar lain},0)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))
                        elif text.lower() == "hapus chat":
                            if msg._from in admin:
                                try:
                                    cl.removeAllMessages(op.param2)
                                    
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Chat bersih...")
                                except:
                                    pass        
                            

                        elif text.lower() == "bye me":
                          if msg._from in admin:
                              ra = ki.getGroup(msg.to)
                              cl.sendMessageWithMention(msg.to, msg._from, "Siap kak ","Pamit yah kak,, terima kasih sudah di invite")
                              cl.leaveGroup(msg.to)
                        elif text.lower().startswith(".kick "):
                            if msg._from in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in own:
                                        pass
                                    else:
                                        try:
                                            cl.sendMessageWithMention(msg.to,target,"Maaf","aku kick")
                                            klist = [cl]
                                            kicker = random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                        except:
                                            pass       
                        elif (".addalkban " in msg.text):
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Setmain["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Succses")
                                       except:
                                           pass

                        elif (".delltalkban " in msg.text):
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del Setmain["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Succes")
                                       except:
                                           pass

                        elif text.lower() == '.addtalkban:on':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["Talkwblacklist"] = True
                                cl.sendText(msg.to,"Send Contact...")

                        elif text.lower() == '.delltalkban:on':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["Talkdblacklist"] = True
                                cl.sendText(msg.to,"Send Contact...")

                        elif (".addbanned " in msg.text):
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Setmain["CITLblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Succes")
                                       except:
                                           pass

                        elif (".dellbanned " in msg.text):
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del Setmain["CITLblacklist"][target]
                                           cl.sendMessage(msg.to,"Succes")
                                       except:
                                           pass

                        elif text.lower() == '.addbanned:on':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["CITLwblacklist"] = True
                                cl.sendText(msg.to,"Send Contact...")

                        elif text.lower() == '.dellbanned:on':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["CITLdblacklist"] = True
                                cl.sendText(msg.to,"Send Contact...")

                        elif text.lower() == '.cekbanned':
                            if msg._from in admin:
                              if Setmain["CITLblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in Setmain["CITLblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🔰|RA|Blacklist\n\n"+ma+"\nJumlah「%s」Blacklist User" %(str(len(Setmain["CITLblacklist"]))))

                        elif text.lower() == '.talkbanlist':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                              if Setmain["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"No Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in Setmain["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🔰|RA|Talkban\n\n"+ma+"\nJumlah「%s」Talkban User" %(str(len(Setmain["Talkblacklist"]))))

                        elif text.lower() == '.contactban':
                            if msg._from in admin:
                              if Setmain["CITLblacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in Setmain["CITLblacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif text.lower() == 'clearban':
                            if msg._from in admin:
                              Setmain["CITLblacklist"] = {}
                              ragets = cl.getContacts(Setmain["CITLblacklist"])
                              mc = "Jumlah「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"Sukses clear blacklist " +mc)
                        elif msg.text.lower() == 'scan blacklist':
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = cl.getGroup(msg.to)
                                gMembMids = [contact.mid for contact in group.members]
                                matched_list = []
                                for tag in Setmain["CITLblacklist"]:
                                    matched_list+=filter(lambda str: str == tag, gMembMids)
                                if matched_list == []:
                                    cl.sendText(msg.to,"Tidak ada Daftar Blacklist")
                                    return
                                for jj in matched_list:
                                    try:
                                        cl.kickoutFromGroup(msg.to,[jj])
                                        print (msg.to,[jj])
                                    except:
                                        pass       

                        elif text.lower() == 'lurk on':
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            if msg.to in read['readPoint']:
                                    try:
                                        del read['readPoint'][msg.to]
                                        del read['readMember'][msg.to]
                                        del read['readTime'][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][msg.to] = msg.id
                                    read['readMember'][msg.to] = ""
                                    read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                    read['ROM'][msg.to] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(read, fp, sort_keys=True, indent=4)
                                        cl.sendText(msg.to,"Lurking already on")
                            else:
                                try:
                                    del read['readPoint'][msg.to]
                                    del read['readMember'][msg.to]
                                    del read['readTime'][msg.to]
                                except:
                                    pass
                                read['readPoint'][msg.to] = msg.id
                                read['readMember'][msg.to] = ""
                                read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                read['ROM'][msg.to] = {}
                                with open('sider.json', 'w') as fp:
                                    json.dump(read, fp, sort_keys=True, indent=4)
                                    cl.sendText(msg.to, "Set reading point:\n" + readTime)
                            
                        elif text.lower() == 'lurk off':
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            if msg.to not in read['readPoint']:
                                cl.sendText(msg.to,"Lurking already off")
                            else:
                                try:
                                        del read['readPoint'][msg.to]
                                        del read['readMember'][msg.to]
                                        del read['readTime'][msg.to]
                                except:
                                      pass
                                cl.sendText(msg.to, "Delete reading point:\n" + readTime)
    
                        elif text.lower() == 'lurk reset':
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            if msg.to in read["readPoint"]:
                                try:
                                    read["readPoint"][msg.to] = True
                                    read["readMember"][msg.to] = {}
                                    read["readTime"][msg.to] = readTime
                                    read["ROM"][msg.to] = {}
                                except:
                                    pass
                                cl.sendText(msg.to, "Reset reading point:\n" + readTime)
                            else:
                                cl.sendText(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                        elif text.lower() == 'lurking':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read['readPoint']:
                                    if read["ROM"][msg.to].items() == []:
                                         cl.sendText(msg.to, "Lurkers:\nNone")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][msg.to].items():
                                            chiya.append(rom[1])
                                   
                                        cmem = cl.getContacts(chiya)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '[ Total Hasil Reader {}]\n'
                                    for x in range(len(cmem)):
                                            xname = str(cmem[x].displayName)
                                            pesan = ''
                                            pesan2 = pesan+"@x\n"
                                            xlen = str(len(zxc)+len(xpesan))
                                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                            zx2.append(zx)
                                            zxc += pesan2
                                    txt = xpesan+ zxc + "\nLurking time: \n" + readTime
                                    try:
                                      cl.sendMessage(msg.to, text=txt, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')})
                                    except Exception as error:
                                          print (error)
                                    pass
                                else:
                                    cl.sendText(msg.to, "Lurking has not been set.")
                        elif text.lower() == "sider on":
                          if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek sider On")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif text.lower() == "sider off":
                          if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "Cek sider Off")
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")
                        elif msg.text.lower() == ".cek mention":
                          if msg._from in admin :
                            if Setmain["mention"] == {}:
                                cl.sendMessage(msg.to, " 「 list not found 」")
                            else:
                                num=1
                                msgs=" 「 mention list 」:"
                                for a in Setmain["mention"]:
                                    msgs+="\n%i. %s" % (num, a)
                                    num=(num+1)
                                msgs+="\n\nTotal mention List: %i" % len(Setmain["mention"])
                                cl.sendMessage(msg.to, msgs)

                        elif msg.text.lower().startswith('.t mention'):
                          if msg._from in admin :
                            separate = text.split(" ")
                            text = text.replace(separate[0]+" ","")
                            Setmain["mention"][text] = '%s' % text
                            Setmain["comand"] = '%s' % text
                            backupData()
                            cl.sendMessage(msg.to, " comand mention telah di tambah ")
                        elif text.lower() in Setmain["mention"]:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               name = "[Mention Grup {}]".format(str(group.name))
                               url = "http://line.me/ti/p/whiterascals1"
                               iconlink = "http://dl.profile.line-cdn.net/{}".format(str(group.pictureStatus))
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 100:
                                   mentionMembers(msg.to, nama,name,url,iconlink)
                               if jml > 100 and jml < 200:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1,name,url,iconlink)
                                   for j in range (100, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2,name,url,iconlink)
                               if jml > 200 and jml < 300:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1,name,url,iconlink)
                                   for j in range (100, 199):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2,name,url,iconlink)
                                   for k in range (200, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3,name,url,iconlink)
                               if jml > 300 and jml < 400:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1,name,url,iconlink)
                                   for j in range (100, 199):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2,name,url,iconlink)
                                   for k in range (200, 299):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3,name,url,iconlink)
                                   for l in range (300, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4,name,url,iconlink)
                               if jml > 400 and jml < 500:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1,name,url,iconlink)
                                   for j in range (100, 199):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2,name,url,iconlink)
                                   for k in range (200, 299):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3,name,url,iconlink)
                                   for l in range (300, 399):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (400, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)



#===========Hiburan============#
                        elif text.lower() == 'kalender':
                            tz = pytz.timezone("Asia/Makassar")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            cl.sendMessage(msg.to, readTime)                 
                        elif ".sholat:" in msg.text:
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n🎖Lokasi : " + data[0]
                                         ret_ += "\n🎖 " + data[1]
                                         ret_ += "\n🎖 " + data[2]
                                         ret_ += "\n🎖 " + data[3]
                                         ret_ += "\n🎖 " + data[4]
                                         ret_ += "\n🎖 " + data[5]
                                         ret_ += "\n\n🎖Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\n??Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  cl.sendMessage(msg.to, str(ret_))
                        elif text.lower().startswith(".telpon: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            nomor = text.replace(sep[0] + " ","")
                            r = requests.get("http://apisora2.herokuapp.com/prank/call/?no={}".format(urllib.parse.quote(nomor)))
                            data = r.text
                            data = json.loads(data)
                            ret_ = "「 Prangked Telpon 」"
                            ret_ += "\n🔹 Status : {}".format(str(data["status"]))
                            ret_ += "\n🔹 Tujuan "+str(data["result"])
                            cl.sendMessage(msg.to, str(ret_))

                        elif text.lower().startswith(".sms: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            nomor = text.replace(sep[0] + " ","")
                            r = requests.get("http://apisora2.herokuapp.com/prank/sms/?no={}".format(urllib.parse.quote(nomor)))
                            data = r.text
                            data = json.loads(data)
                            ret_ = "「 Prangked Sms 」"
                            ret_ += "\n🔹 Status : {}".format(str(data["status"]))
                            ret_ += "\n🔹 Tujuan "+str(data["result"])
                            cl.sendMessage(msg.to, str(ret_))

                        elif text.lower().startswith(".artimimpi: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            mimpi = msg.text.replace(sep[0] + " ","")  
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0'
                                r = s.get("http://primbon.com/tafsir_mimpi.php?mimpi={}&submit=+Submit+".format(urllib.parse.quote(mimpi)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                for anu in soup.find_all('i'):
                                    ret_ = anu.get_text()
                                    cl.sendMessage(msg.to,ret_)

                        elif ".cuaca: " in msg.text:
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「Status Cuaca」"
                                    ret_ += "\n🎖 Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n🎖 Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n🎖 Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n🎖 Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n🎖 Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\n🎖Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n🎖Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))                  
#===================================================

                        elif ".lokasi: " in msg.text:
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「Info Lokasi」"
                                    ret_ += "\n🎖 Location : " + data[0]
                                    ret_ += "\n🎖 Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif text.lower().startswith(".cariaplikasi: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " ","")
                            cond = query.split("=")
                            search = str(cond[0])
                            with requests.session() as s:
                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                r = s.get("https://apkpure.com/id/search?q={}".format(str(search)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                data = soup.findAll('dl', attrs={'class':'search-dl'})
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "「 List Aplikasi 」\n"
                                    for apk in data:
                                        num += 1
                                        link = "https://apkpure.com"+apk.find('a')['href']
                                        title = apk.find('a')['title']
                                        ret_ += "\n🔹 {}. {}".format(str(num), str(title))
                                    ret_ += "\n\n Total {} Result".format(str(len(data)))
                                    ret = "untuk melihat link download silahkan ketik Aplikasi: {} = No,urut".format(str(search))
                                  
                                    citl = cl.getContact(msg._from)
                                    name = "[LIST APLIKASI]"
                                    url = "http://line.me/ti/p/bJ3NcNuJX3"
                                    iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                                    cl.sendMessageWithContent(msg.to,str(ret_),name,url,iconlink)
                                    cl.sendMessage(to, str(ret))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data):
                                        apk = data[num - 1]
                                        with requests.session() as s:
                                            s.headers['user-agent'] = random.choice(settings["userAgent"])
                                            r = s.get("https://apkpure.com{}/download?from=details".format(str(apk.find('a')['href'])))
                                            soup = BeautifulSoup(r.content, 'html5lib')
                                            data = soup.findAll('div', attrs={'class':'fast-download-box'})
                                            for down in data:
                                                load = down.select("a[href*=https://download.apkpure.com/]")[0]
                                                file = load['href']
                                                ret_ = "File info :\n"+down.find('span', attrs={'class':'file'}).text
                                                with requests.session() as web:
                                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                                    r = web.get("https://api-ssl.bitly.com/v3/shorten?access_token=497e74afd44780116ed281ea35c7317285694bf1&longUrl={}".format(urllib.parse.quote(file)))
                                                    data = r.text
                                                    data = json.loads(data)
                                                    ret_ += "\nLink Download :\n"+data["data"]["url"]
                                                cl.sendMessage(to, str(ret_))
                        elif text.lower().startswith(".lirik: "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   url = "http://rahandiapi.herokuapp.com/lyricapi?key=betakey&q={}".format(urllib.parse.quote(search))
                                   link = web.get(url)
                                   data = link.text
                                   data = json.loads(data)
                                   start = time.time()
                                   ret_ = "「 Lirik Search 」"
                                   ret_ += "\n🔹 Judul : {}".format(str(data["title"]))
                                   ret_ += "\n🔹 Time Taken : {}".format(str(start))
                                   ret_ += "\n\n{}".format(str(data["lyric"]))
                                   citl = cl.getContact(msg._from)
                                   name = "[Lirik lagu]"
                                   url = "http://line.me/ti/p/bJ3NcNuJX3"
                                   iconlink = "http://dl.profile.line-cdn.net/"+ citl.pictureStatus
                                   cl.sendMessageWithContent(msg.to,str(ret_),name,url,iconlink)

                        elif text.lower().startswith("getmusic "):
                            try:
                                search = text.lower().replace("getmusic ","")
                                r = requests.get("https://farzain.xyz/api/joox.php?apikey=K8737IRCoQxRx9T71I7fP7YAotEYIm&id={}".format(urllib.parse.quote(search))) #untuk api key bisa requests ke web http://www.farzain.xyz/requests.php
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "「 Hasil Musik 」\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                hasil += "\n\nLink : \n3. M4A : {}".format(str(audio["m4a"]))
                                cl.sendImageWithURL(msg.to, str(data["gambar"]))
                                cl.sendMessage(msg.to, str(hasil))
                                cl.sendMessage(msg.to, "Downloading...")
                                cl.sendMessage(msg.to, "「 Result MP3 」")
                                cl.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                cl.sendMessage(msg.to, "「 Result M4A 」")
                                cl.sendVideoWithURL(msg.to, str(audio["m4a"]))
                                cl.sendMessage(msg.to, "Success Download...")
                            except Exception as error:
                            	cl.sendMessage(msg.to, str(error))
                            print(traceback.format_exc())
                        elif msg.text.lower().startswith(".music: "):
                          if msg._from in admin + staff:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " ","")
                            cond = query.split("=")
                            search = str(cond[0])
                            result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                            data = result.text
                            data = json.loads(data)
                            if len(cond) == 1:
                                num = 0
                                ret_ = "┏━━[ Result Music ]━━"
                                for music in data["result"]:
                                    num += 1
                                    ret_ += "\n┃• {}. {}".format(str(num), str(music["single"]))
                                ret_ += "\n┗━━[ Total {} Music ]━━".format(str(len(data["result"])))
                                citl = cl.getContact(msg._from)
                                name = "[LIST MUSIC]"
                                url = "http://line.me/ti/p/bJ3NcNuJX3"
                                iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                                cl.sendMessageWithContent(msg.to,str(ret_),name,url,iconlink)
                                cl.sendMessage(msg.to, "Untuk play Music, silahkan gunakan command music [Nama penyanyi]=「number」")
                            elif len(cond) == 2:
                                num = int(cond[1])
                                if num <= len(data["result"]):
                                    music = data["result"][num - 1]
                                    result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                    data = result.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        ret_ = "┏━━━「 Music 」━━━━"
                                        ret_ += "\n┃ Title : {}".format(str(data["result"]["song"]))
                                        ret_ += "\n┃ Album : {}".format(str(data["result"]["album"]))
                                        ret_ += "\n┃ Size : {}".format(str(data["result"]["size"]))
                                        ret_ += "\n┃ Link : {}".format(str(data["result"]["mp3"][0]))
                                        ret_ += "\n┗━━━「Done」━━━━"
                                        cl.sendMessage(msg.to, str(ret_))
                                        cl.sendMessageWithMention(msg.to, msg._from, "Sek ya kak","Audio msih dalam proses rekaman")
                                        cl.sendAudioWithURL(msg.to, str(data["result"]["mp3"][0]))     

                        elif text.lower().startswith(".carigambar: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    start = timeit.timeit()
                                    items = data["result"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    citl = cl.getContact(msg._from)
                                    name = "[DONE CARI GAMBAR]"
                                    url = "http://line.me/ti/p/bJ3NcNuJX3"
                                    iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                                    cl.sendMessageWithContant(msg.to,"「 Google Image 」\nType : Search Image\nTime taken : %seconds" % (start),name,url,iconlink)
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif text.lower().startswith(".zodiak: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = text.replace(sep[0] + " ","")
                            r = requests.post("https://aztro.herokuapp.com/?sign={}&day=today".format(urllib.parse.quote(query)))
                            data = r.text
                            data = json.loads(data)
                            data1 = data["description"]
                            data2 = data["color"]
                            translator = Translator()
                            hasil = translator.translate(data1, dest='id')
                            hasil1 = translator.translate(data2, dest='id')
                            citl1 = hasil.text
                            citl2 = hasil1.text
                            ret_ = "「 Ramalan zodiak {} hari ini 」\n".format(str(query))
                            ret_ += str(citl1)
                            ret_ += "\n✨ Tanggal : " +str(data["current_date"])
                            ret_ += "\n✨ Rasi bintang : "+query
                            ret_ += " ("+str(data["date_range"]+")")
                            ret_ += "\n✨ Pasangan Zodiak : " +str(data["compatibility"])
                            ret_ += "\n✨ Angka keberuntungan : " +str(data["lucky_number"])
                            ret_ += "\n✨ Waktu keberuntungan : " +str(data["lucky_time"])
                            ret_ += "\n✨ Warna kesukaan : " +str(citl2)
                            citl = cl.getContact(msg._from)
                            name = "[INFO ZODIAK]"
                            url = "http://line.me/ti/p/bJ3NcNuJX3"
                            iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                            cl.sendMessageWithContent(msg.to,str(ret_),name,url,iconlink)
                        elif msg.text.lower().startswith(".cooltext: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                nama = msg.text.replace(separate[0] + " ","")                                
                                nmor = ["1","2","3","4","5","6","7"]
                                plih = random.choice(nmor)
                                url = ("https://farzain.xyz/api/cooltext.php?text="+nama+"&type="+plih)
                                cl.sendImageWithURL(msg.to, url)
                            except Exception as error:
                                pass
                        elif msg.text.lower().startswith(".retrowave: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                teks = msg.text.replace(separate[0] + " ","")
                                pemisah = teks.split(":")
                                nad1 = pemisah[0]
                                nad2 = pemisah[1]
                                nad3 = pemisah[2] 
                                nmor = ["1","2","3","4","5"]
                                bg = random.choice(nmor)
                                nmor2 = ["1","2","3","4"]
                                tt = random.choice(nmor2)
                                url = requests.get("http://leert.corrykalam.gq/retrowave.php?text1="+nad1+"&text2="+nad2+"&text3="+nad3+"&btype="+bg+"&ttype="+tt)
                                data = url.json()
                                cl.sendImageWithURL(msg.to, str(data["image"]))
                            except Exception as error:
                                pass
                        elif msg.text.lower().startswith(".artinama: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.dzin.xyz/api/name/?apikey=beta&name={}".format(urllib.parse.quote(query)))
                                data = r.text
                                data = json.loads(data)
                            for citl in data["result"]:
                                hasil = "[✨Api Creator By ➡ "+data["creator"]+"✨]\n\n"
                                hasil += "Hasil: "+citl["name"]
                                citl = cl.getContact(msg._from)
                                name = "[ARTI NAMA]"
                                url = "http://line.me/ti/p/whiterascals1"
                                iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                                cl.sendMessageWithContent(msg.to,hasil,name,url,iconlink)
                        elif "Ytmp4: " in msg.text:
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n🎖 Author : ' + str(vid.author)
                                    durasi = '\n🎖 Duration : ' + str(vid.duration)
                                    suka = '\n🎖 Likes : ' + str(vid.likes)
                                    rating = '\n🎖 Rating : ' + str(vid.rating)
                                 #   deskripsi = '\n🎖 Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))
                        elif msg.text.lower().startswith("youtube: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://leert.corrykalam.gq/yt.php?url={}".format(urllib.parse.quote(query)))
                                data = r.text
                                data = json.loads(data)
                           #     image = data["thumnail"]
                                video = data["mp4"]["360"]
                           #     cl.sendImageWithURL(mag.to, image)
                                cl.sendVideoWithURL(mag.to, video)
                             
                        elif "Ytmp3: " in msg.text:
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n🎖 Author : ' + str(vid.author)
                                    durasi = '\n🎖 Duration : ' + str(vid.duration)
                                    suka = '\n🎖 Likes : ' + str(vid.likes)
                                    rating = '\n🎖 Rating : ' + str(vid.rating)
                             #       deskripsi = '\n🎖 Deskripsi : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))
                        elif "infoig" in msg.text.lower():
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                                try:
                                    data = json.loads(r.text)
                                    ret_ = "┌━━━「Profile instagram」━━━━"
                                    ret_ += "\n├🎖「Nama」 : {}".format(str(data["user"]["full_name"]))
                                    ret_ += "\n├🎖「Username」 : {}".format(str(data["user"]["username"]))
                                    ret_ += "\n├🎖「Bio」 : {}".format(str(data["user"]["biography"]))
                                    ret_ += "\n├🎖「Pengikut」 : {}".format(format_number(data["user"]["followed_by"]["count"]))
                                    ret_ += "\n├🎖「Diikuti」 : {}".format(format_number(data["user"]["follows"]["count"]))
                                    if data["user"]["is_verified"] == True:
                                        ret_ += "\n├🎖「Verifikasi」 : Sudah"
                                    else:
                                        ret_ += "\n├🎖「Verifikasi」: Belum"
                                    if data["user"]["is_private"] == True:
                                        ret_ += "\n├🎖「Akun Pribadi」 : Iya"
                                    else:
                                        ret_ += "\n├🎖「Akun Pribadi」 : Tidak"
                                    ret_ += "\n├🎖「Total Post」 : {}".format(format_number(data["user"]["media"]["count"]))
                                    ret_ += "\n└━━[ https://www.instagram.com/{} ]".format(search)
                                    path = data["user"]["profile_pic_url_hd"]
                                    cl.sendImageWithURL(msg.to, str(path))
                                    cl.sendMessage(msg.to, str(ret_))
                                except:
                                    cl.sendMessage(msg.to, "Pengguna tidak ditemukan")
                        elif "Profileig: " in msg.text:
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = str(data['user']['profile_pic_url_hd'])
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "🎖 Link : " + "https://www.instagram.com/" + instagram
                                text = "🎖 Name : "+namaIG+"\n🎖 Username : "+usernameIG+"\n🎖 Biography : "+bioIG+"\n🎖 Follower : "+followerIG+"\n🎖 Following : "+followIG+"\n🎖 Post : "+mediaIG+"\n🎖 Verified : "+verifIG+"\n🎖 Private : "+privateIG+"" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif "Cekdate: " in msg.text:
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"🎖I N F O🎖\n🎖Tanggal lahir : "+lahir+"\n🎖Umur : "+usia+"\n🎖Ultah : "+ultah+"\n🎖Zodiak : "+zodiak)

                        elif "Jumlahtag: " in msg.text:
                          if Setmain["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["CITLspamtag"] = num
                                cl.sendText(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif "Jumlahcall: " in msg.text:
                          if Setmain["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["spamcall"] = num
                                cl.sendText(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif msg.text.lower().startswith("spamtag "):
                             if msg._from in admin or msg._from in Own and msg._from in Creator:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = line.getContact(ls)
                                        jmlh = int(Setmain["CITLspamtag"])
                                        for x in range(jmlh):
                                            try:
                                                text = "@!"
                                                mids = [contact.mid]
                                                sendMentionV2(msg.to, text, mids)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                else:
                                    cl.sendMessage(msg.to,"")
                        elif text.lower() == 'spamcall':
                          if Setmain["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(msg.to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(Setmain["spamcall"])
                                cl.sendMessage(msg.to, "Succes {} Spam Call Grup".format(str(Setmain["spamcall"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(msg.to)
                                        call.inviteIntoGroupCall(msg.to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                else:
                                    cl.sendText(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if Setmain["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if Setmain["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["CITLspam"]))
                                      ki.sendMessage(midd, str(Setmain["CITLspam"]))
                                      kk.sendMessage(midd, str(Setmain["CITLspam"]))
                                      kc.sendMessage(midd, str(Setmain["CITLspam"]))

                        elif 'ID line: ' in msg.text:
                          if Setmain["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)
                        elif "ID smule " in msg.text:
                            tob = msg.text.replace("ID smule ","")
                            cl.sendText(msg.to,"Sedang Mencari...")
                            cl.sendText(msg.to,"ID SMULE : "+tob+"\nLink : https://smule.com/" + tob)
                            cl.sendMessageWithMention(msg.to,msg._from,"Tuh kak "," linknya, jangn lupa di follow yak")

                        elif ".bgroup " in msg.text:
                          if msg._from in admin:
                      #      sep = text.split(" ")
                            txt = text.replace(".bgroup ","")
                            a = cl.getGroupIdsJoined()
                            citl = cl.getContact(msg._from)
                            for b in a:
                                G = cl.getGroup(b)
                                name = "[BROADCAST] Click Here"
                                url = "http://line.me/ti/p/whiterascals1"
                                iconlink = "http://dl.profile.line-cdn.net/{}".format(str(citl.pictureStatus))
                           #     cl.sendMessage(b, "[ Broadcast ]\n{}".format(str(txt)))
                                cl.sendMessageWithContent(b, "[ Broadcast ]\n{}".format(str(txt)),name,url,iconlink)
                            cl.sendMessage(msg.to, "Berhasil broadcast ke {} group".format(str(len(a))))
                        elif ".bpc " in msg.text:
                          if msg._from in admin:
                         
                            txt =  msg.text.replace(".bpc ","")
                            friends = cl.getAllContactIds()
                            for friend in friends:
                                cl.sendMessage(friend, "[ Broadcast ]\n{}".format(str(txt)))
                            cl.sendMessage(msg.to, "Berhasil broadcast ke {} teman".format(str(len(friends))))
                        elif ".allbroadcast " in msg.text:
                          if msg._from in admin:
                          
                            txt = text.replace(".allbroadcast ","")
                            friends = cl.getAllContactIds()
                            groups = cl.getGroupIdsJoined()
                            for group in groups:
                                cl.sendMessage(group, "[ Broadcast ]\n{}".format(str(txt)))
                            cl.sendMessage(msg.to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                            for friend in friends:
                                cl.sendMessage(friend, "[ Broadcast ]\n{}".format(str(txt)))
                            cl.sendMessage(to, "Berhasil broadcast ke {} teman".format(str(len(friends))))
                        elif ".bigroup: "in msg.text:
                          if msg._from in admin:
                            bc = msg.text.replace(".bigroup: ","")
                            gid = cl.getGroupIdsJoined()
                            for i in gid:
                                cl.sendImageWithURL(i, bc)
                    
                        elif ".bipc: " in msg.text:
                          if msg._from in admin:
                            bc = msg.text.replace(".bipc: ","")
                            gid = cl.getAllContactIds()
                            for i in gid:
                                cl.sendImageWithURL(i, bc)
            
                        elif text.lower() == '.gcreator':
                            group = cl.getGroup(msg.to)
                            GS = group.creator.mid
                            cl.sendContact(msg.to, GS)
                        elif text.lower() == 'id grup':
                            gid = cl.getGroup(msg.to)
                            cl.sendMessage(msg.to, "「ID Group」 : ]\n" + gid.id)
                        elif text.lower() == '.group pict':
                          if msg._from in admin:
                            group = cl.getGroup(msg.to)
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        elif text.lower() == '.group name':
                            gid = cl.getGroup(msg.to)
                            cl.sendMessage(msg.to, "「Nama Group」 : \n" + gid.name)
                        elif text.lower() == '.gurl':
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = cl.getGroup(msg.to)
                                if group.preventedJoinByTicket == False:
                                    ticket = cl.reissueGroupTicket(msg.to)
                                    cl.sendMessage(msg.to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                                else:
                                    cl.sendMessage(msg.to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                        elif text.lower() == '.open':
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = cl.getGroup(msg.to)
                                if group.preventedJoinByTicket == False:
                                    cl.sendMessage(msg.to, "Grup qr sudah terbuka")
                                else:
                                    group.preventedJoinByTicket = False
                                    cl.updateGroup(group)
                                    cl.sendMessage(msg.to, "Berhasil membuka grup qr")
                        elif text.lower() == '.close':
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = cl.getGroup(msg.to)
                                if group.preventedJoinByTicket == True:
                                    cl.sendMessage(msg.to, "Grup qr sudah tertutup")
                                else:
                                    group.preventedJoinByTicket = True
                                    cl.updateGroup(group)
                                    cl.sendMessage(msg.to, "Berhasil menutup grup qr")
                        elif text.lower() == '.ginfo':
                          if msg._from in admin:
                            group = cl.getGroup(msg.to)
                            try:
                                gCreator = group.creator.displayName
                            except:
                                gCreator = "Tidak ditemukan"
                            if group.invitee is None:
                                gPending = "0"
                            else:
                                gPending = str(len(group.invitee))
                            if group.preventedJoinByTicket == True:
                                gQr = "Tertutup"
                                gTicket = "Tidak ada"
                            else:
                                gQr = "Terbuka"
                                gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            ret_ = "🔰|RA|Group Info"
                            ret_ += "\n\n🔰 「Nama Group」 : {}".format(str(group.name))
                            ret_ += "\n🔰 ID Group : {}".format(group.id)
                            ret_ += "\n🔰 Pembuat : {}".format(str(gCreator))
                            ret_ += "\n🔰 Jumlah Member : {}".format(str(len(group.members)))
                            ret_ += "\n🔰 Jumlah Pending : {}".format(gPending)
                            ret_ += "\n🔰 Group Qr : {}".format(gQr)
                            ret_ += "\n🔰 Group Ticket : {}".format(gTicket)
                          
                            name = "[INFO GRUP]"
                            url = "http://line.me/ti/p/whiterascals1"
                            iconlink = "http://dl.profile.line-cdn.net/{}".format(str(group.pictureStatus))
                            cl.sendMessageWithContent(msg.to,str(ret_),name,url,iconlink)
                            cl.sendImageWithURL(msg.to, path)
                        elif text.lower() == '.list grup':
                            if msg._from in CITLself:
                                groups = cl.getGroupIdsJoined()
                                ret_ = "🔰|RA|Group"
                                no = 0 + 1
                                for gid in groups:
                                    group = cl.getGroup(gid)
                                    ret_ += "\n {}. {} | 「{}」".format(str(no), str(group.name), str(len(group.members)))
                                    no += 1
                                ret_ += "\n Total {} Groups ".format(str(len(groups)))
                                citl = cl.getContact(msg._from)
                                name = "[LIST GRUP]"
                                url = "http://line.me/ti/p/whiterascals1"
                                iconlink = "http://dl.profile.line-cdn.net/"+ citl.pictureStatus
                                cl.sendMessageWithContent(msg.to,str(ret_),name,url,iconlink)
                        elif ".infogrup " in msg.text:
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "No file"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "🔰|RA|Group Info\n"
                                ret_ += "\n🔰 Nama Group : {}".format(G.name)
                                ret_ += "\n🔰 ID Group : {}".format(G.id)
                                ret_ += "\n🔰 Pembuat : {}".format(gCreator)
                                ret_ += "\n🔰 Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n🔰 Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n🔰 Jumlah Pending : {}".format(gPending)
                                ret_ += "\n🔰 Group Qr : {}".format(gQr)
                                ret_ += "\n🔰Group Ticket : {}".format(gTicket)
                                ret_ += "\nThanks For White Rascals"
                                cl.sendMessage(msg.to, str(ret_))
                            except:
                                pass
                        elif text.lower() == 'add admin: on':
                            if msg._from in admin:
                                Setmain["addadmin"] = True
                                cl.sendText(msg.to,"Send Contact...")

                        elif text.lower() == 'del admin':
                            if msg._from in admin:
                                Setmain["delladmin"] = True
                                cl.sendText(msg.to,"Send Contact...")

                        elif text.lower() == 'add staff: on':
                            if msg._from in admin:
                                Setmain["addstaff"] = True
                                cl.sendText(msg.to,"Send Contact...")

                        elif text.lower() == 'del staff':
                            if msg._from in admin:
                                Setmain["dellstaff"] = True
                                cl.sendText(msg.to,"Send Contact...")

                        elif text.lower() == 'add bot: on':
                            if msg._from in admin:
                                Setmain["addbots"] = True
                                cl.sendText(msg.to,"Send Contact...")

                        elif text.lower() == 'del bot':
                            if msg._from in admin:
                                Setmain["dellbots"] = True
                                cl.sendText(msg.to,"Send Contact...")

                        elif text.lower() == 'refresh':
                            if msg._from in admin:
                                Setmain["addadmin"] = False
                                Setmain["delladmin"] = False
                                Setmain["addstaff"] = False
                                Setmain["dellstaff"] = False
                                Setmain["addbots"] = False
                                Setmain["dellbots"] = False
                                Setmain["wblacklist"] = False
                                Setmain["dblacklist"] = False
                                Setmain["Talkwblacklist"] = False
                                Setmain["Talkdblacklist"] = False
                                cl.sendText(msg.to,"Berhasil di Refresh...")

                        elif text.lower() == 'kontak admin':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        elif text.lower() == 'kontak staff':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        elif text.lower() == 'kontak bot':
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif ".infomem " in msg.text:
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "🎖 "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(msg.to,"🎖 Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass
                        elif "Add admin @" in msg.text:
                            if msg._from in own:
                                print ("[Command]admin add executing")
                                _name = msg.text.replace("Add admin @","")
                                _nametarget = _name.rstrip('  ')
                                gs = cl.getGroup(msg.to)
                                gs = ki.getGroup(msg.to)
                                gs = kk.getGroup(msg.to)
                                gs = kc.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    if _nametarget == g.displayName:
                                        targets.append(g.mid)
                                if targets == []:
                                    cl.sendText(msg.to,"Contact not found")
                                else:
                                    for target in targets:
                                        try:
                                            admin.append(target)
                                            cl.sendText(msg.to,"Admin added")
                                        except:
                                            pass
                                print ("[Command]Staff add executed")
                            else:
                                cl.sendText(msg.to,"Command denied.")
                                cl.sendText(msg.to,"crator permission required.")

                        elif "Remove admin @" in msg.text:
                            if msg._from in own:
                                print ("[Command]Staff remove executing")
                                _name = msg.text.replace("Remove admin @","")
                                _nametarget = _name.rstrip('  ')
                                gs = cl.getGroup(msg.to)
                                gs = ki.getGroup(msg.to)
                                gs = kk.getGroup(msg.to)
                                gs = kc.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    if _nametarget == g.displayName:
                                        targets.append(g.mid)
                                if targets == []:
                                    cl.sendText(msg.to,"Contact not found")
                                else:
                                    for target in targets:
                                        try:
                                            admin.remove(target)
                                            cl.sendText(msg.to,"Admin deleted")
                                        except:
                                            pass
                                print ("[Command]admin remove executed")
                            else:
                                cl.sendText(msg.to,"Command denied.")
                                cl.sendText(msg.to,"crator permission required.")

                        elif msg.text in ["Adminlist","List admin"]:
                            if admin == []:
                                cl.sendText(msg.to,"The Adminlist is empty")
                            else:
                                cl.sendText(msg.to,"please Setmain...")
                                mc = ""
                                mb = 0
                                for mi_d in admin:
                                    mb = mb + 1
                                    done = '\n'
                                    mc += str(mb) + "🔹|" + cl.getContact(mi_d).displayName+"\n"
                                cl.sendText(msg.to, "🄳🄰🄵🅃🄰🅁 🄰🄳🄼🄸🄽 🄱🄾🅃\n" + mc)
                                print ("[Command]Stafflist executed")
                        elif "Add staff @" in msg.text:
                            if msg._from in admin:
                                print ("[Command]admin add executing")
                                _name = msg.text.replace("Add admin @","")
                                _nametarget = _name.rstrip('  ')
                                gs = cl.getGroup(msg.to)
                                gs = ki.getGroup(msg.to)
                                gs = kk.getGroup(msg.to)
                                gs = kc.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    if _nametarget == g.displayName:
                                        targets.append(g.mid)
                                if targets == []:
                                    cl.sendText(msg.to,"Contact not found")
                                else:
                                    for target in targets:
                                        try:
                                            staff.append(target)
                                            cl.sendText(msg.to,"staff added")
                                        except:
                                            pass
                                print ("[Command]Staff add executed")
                            else:
                                cl.sendText(msg.to,"Command denied.")
                                cl.sendText(msg.to,"crator permission required.")

                        elif "Remove staff @" in msg.text:
                            if msg._from in admin:
                                print ("[Command]Staff remove executing")
                                _name = msg.text.replace("Remove admin @","")
                                _nametarget = _name.rstrip('  ')
                                gs = cl.getGroup(msg.to)
                                gs = ki.getGroup(msg.to)
                                gs = kk.getGroup(msg.to)
                                gs = kc.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    if _nametarget == g.displayName:
                                        targets.append(g.mid)
                                if targets == []:
                                    cl.sendText(msg.to,"Contact not found")
                                else:
                                    for target in targets:
                                        try:
                                            staff.remove(target)
                                            cl.sendText(msg.to,"staff deleted")
                                        except:
                                            pass
                                print ("[Command]admin remove executed")
                            else:
                                cl.sendText(msg.to,"Command denied.")
                                cl.sendText(msg.to,"crator permission required.")

                        elif msg.text in ["Stafflist","List staff"]:
                            if staff == []:
                                cl.sendText(msg.to,"The Adminlist is empty")
                            else:
                                cl.sendText(msg.to,"please Setmain...")
                                mc = ""
                                mb = 0
                                for mi_d in staff:
                                    mb = mb + 1
                                    done = '\n'
                                    mc += str(mb) + "•|" + cl.getContact(mi_d).displayName+"\n"
                                cl.sendText(msg.to, "Daftar Staff\n" + mc)
                                print ("[Command]Stafflist executed")
                    
                        elif "Add Bots @" in msg.text:
                            if msg._from in admin:
                                print ("[Command]admin add executing")
                                _name = msg.text.replace("Add Bots @","")
                                _nametarget = _name.rstrip('  ')
                                gs = cl.getGroup(msg.to)
                                gs = ki.getGroup(msg.to)
                                gs = kk.getGroup(msg.to)
                                gs = kc.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    if _nametarget == g.displayName:
                                        targets.append(g.mid)
                                if targets == []:
                                    cl.sendText(msg.to,"Contact not found")
                                else:
                                    for target in targets:
                                        try:
                                            Bots.append(target)
                                            cl.sendText(msg.to,"Bot telah di tambah")
                                        except:
                                            pass
                                print ("[Command]bot add executed")
                            else:
                                cl.sendText(msg.to,"Command denied.")
                                cl.sendText(msg.to,"crator permission required.")

                        elif "Delete bot @" in msg.text:
                            if msg._from in admin:
                                print ("[Command]Staff remove executing")
                                _name = msg.text.replace("Delete bot @","")
                                _nametarget = _name.rstrip('  ')
                                gs = cl.getGroup(msg.to)
                                gs = ki.getGroup(msg.to)
                                gs = kk.getGroup(msg.to)
                                gs = kc.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    if _nametarget == g.displayName:
                                        targets.append(g.mid)
                                if targets == []:
                                    ki.sendText(msg.to,"Contact not found")
                                else:
                                    for target in targets:
                                        try:
                                            Bots.remove(target)
                                            cl.sendText(msg.to,"Telah terhapus dari daftar bot")
                                        except:
                                            pass
                                print ("[Command]bot remove executed")
                            else:
                                cl.sendText(msg.to,"Command denied.")
                                cl.sendText(msg.to,"crator permission required.")

                        elif msg.text in ["Botlist","Bot list"]:
                            if Bots == []:
                                cl.sendText(msg.to,"The Botslist is empty")
                            else:
                                cl.sendText(msg.to,"please Setmain...")
                                mc = ""
                                mb = 0
                                for mi_d in Bots:
                                    mb = mb + 1
                                    done = '\n'
                                    mc += str(mb) +"• " + cl.getContact(mi_d).displayName +"\n"
                                cl.sendText(msg.to, "🄳🄰🄵🅃🄰🅁 🄱🄾🅃 \n" + mc)
                                print ("[Command]Stafflist executed")
					

                        elif text.lower() == "updategrup":
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya..")

                        elif text.lower() == "update pp":
                          if Setmain["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya..")
                                
                        elif text.lower() == "changedual":
                            if msg.contentType == 0:
                                settings["ChangeVideoProfilevid"] = True
                                cl.sendMessage(msg.to, "Send Videonnya")
                 
                        elif '/ti/g/' in msg.text.lower():
                            if msg._from in CITLself:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Setmain["CITLautojoin"] == True:
                                        ra = cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        
                                        
                                    else:    
                                        ki.sendMessageWithMention(msg.to,msg._from,"Maaf","\naktifkan auotojoin dulu")
        if op.type == 55:
            try:
                if op.param1 in read["readPoint"]:
                   if op.param2 in read["readMember"][op.param1]:
                       pass
                   else:
                       read["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            try:
                if cctv['cyduk'][op.param1]==True:
                    if op.param1 in cctv['point']:
                      if op.param2 not in admin:
                        name = cl.getContact(op.param2).displayName
                        if name in cctv['sidermem'][op.param1]:
                            pass
                        else:
                            cctv['sidermem'][op.param1] += "\n• " + name
                            first=['eh ada','hai kak','aloo..','nah','lg ngapain','halo','sini kak']
                            last=['ngintip aja nih...!!!','gabung sini...!!!','chat yuk...,biar ga sepi.','udah ngopi belum?']
                            sendMention(op.param1,op.param2,str(random.choice(first))+"","\n"+str(random.choice(last)))
                    else:
                        pass
                else:
                    pass
            except:
                pass

        else:
            pass
    except Exception as error:
        print (error)
#------------------------------------------------------------------------------------

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                oepoll.setRevision(op.revision)
 #               thread = threading.Thread(target=bot, args=(op,))
#                thread.start()
    except Exception as e:
        print(e)
