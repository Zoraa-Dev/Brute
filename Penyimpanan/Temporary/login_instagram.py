#!/usr/bin/env python3
# -*- coding:utf-8

from Penyimpanan.Database.data import *
from Penyimpanan.banner_terminal import Terminal

class RequestTL:
    def __init__(self) -> None:
        pass      

    def android_ID(self, username, password):
        self.xyz = hashlib.md5()
        self.xyz.update(username.encode('utf-8') + password.encode('utf-8'))
        self.hex = self.xyz.hexdigest()
        self.xyz.update(self.hex.encode('utf-8') + '12345'.encode('utf-8'))
        return self.xyz
        
    def timezone_offset(self):
        self.tim = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
        self.ofs = self.tim.utcoffset().total_seconds()/60/60
        return self.ofs    
        
    def HeadersApiLogin(self):
        return {
           'host': 'b.i.instagram.com',
           'x-ig-app-locale': 'in_ID',
           'x-ig-device-locale': 'in_ID',
           'x-ig-mapped-locale': 'id_ID',
           'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
           'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
           'x-ig-bandwidth-speed-kbps': '-1.000',
           'x-ig-bandwidth-totalbytes-b': '0',
           'x-ig-bandwidth-totaltime-ms': '0',
           'x-bloks-version-id': '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
           'x-ig-www-claim': '0',
           'x-bloks-is-prism-enabled': 'false',
           'x-bloks-is-layout-rtl': 'false',
           'x-ig-device-id': 'b7b95886-a663-41e4-8025-941a72c9ac4d',
           'x-ig-family-device-id': '2ce88cf6-20e8-4b2e-bb67-8d8ed5dda357',
           'x-ig-android-id': 'android-f4d8eb2bd1b86a47',
           'x-ig-timezone-offset': str(self.timezone_offset()),
           'x-fb-connection-type': 'MOBILE.LTE',
           'x-ig-connection-type': 'MOBILE(LTE)',
           'x-ig-capabilities': '3brTv10=',
           'x-ig-app-id': '567067343352427',
           'priority': 'u=3',
           'user-agent': 'Instagram 309.1.0.41.113 Android (31/10; 360dpi; 1080x2326; Vivo; V2020CA; V1950A; qcom; id_ID; 541635863)',
           'accept-language': 'id-ID, en-US',
           'ig-intended-user-id': '0',
           'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'content-length': '2702',
           'x-fb-http-engine': 'Liger',
           'x-fb-client-ip': 'True',
           'x-fb-server-cluster': 'True'
       }
               
class Login:    
    def __init__(self) -> None:
        self.data = ('data/user/login/')
        pass
        
    def Removed_Cookies(self):
        try: os.system('rm -rf {}.Cookies_IGS.json'.format(self.data))
        except (Exception) as e: pass
        self.Login_Akun_Instagram()
       
    def Login_Akun_Instagram(self):
        try:
           Terminal().banner_instagram()
           Console().print('\n\
[white] 01. Login Instagram Via Cookies\n\
[white] 02. Login Instagram Via Username Dan Password\n\
            ')
           query = Console().input("[white] ?) choose: ")
           if len(query) >0:
               if query == '01' or query == '1':
                   try:
                       self.Via_Ekstention_Dough()
                   except (Exception) as e:
                       Console().print(f"[red] ! {str(e).title()}")
                       exit()       
               elif query == '02' or query == '2':
                   try:
                       Terminal().banner_instagram()
                       Console().print("\n[white] # [white]Masukan [green]Username [white]Dan[green] Password[white] Akun Instagram Anda, Gunakan Pemisah [red]|[white] Untuk Username Dengan Password, Contoh: zora203|zora123 Dan Pastikan Akun Tidak [yellow]Checkpoint[white] Atau Terpasang [red]A2F")
                       querty = Console().input("[white] ?) [green]username and password[white]: ")
                       if len(querty) >0:
                           try:
                               self.username = querty.split('|')[0]
                               self.password = querty.split('|')[1]
                               self.Via_Username_And_Password(self.username,self.password)
                           except (Exception) as e:
                               Console().print(f"[red] ! {str(e).title()}")
                               exit()   
                       else:
                           Console().print("[white] ! Maaf, Anda Tidak Memasukan Apapun, Harap Masukan ([green]Username Dan Password[white]) Akun Instagram")
                           exit()     
                   except (Exception) as e:
                       Console().print(f"[red] ! {str(e).title()}")
                       exit()   
               else:
                   Console().print("[white] ! Maaf, Menu Yang Anda Masukan Tidak Terdaftar Di Menu Ini")
                   exit()      
           else:
               Console().print("[white] ! Maaf, Anda Tidak Memasukan Apapun, Harap Masukan ([green]Menu[white]) Di Atas")
               exit()          
        except (KeyboardInterrupt, Exception) as e:
            Console().print(f"[red] ! {str(e).title()}")
            exit()        
             
    def Via_Ekstention_Dough(self):
        try:
            Terminal().banner_instagram()
            Console().print("\n[white] # Masukan [green]Cookie Akun Instagram[white] Anda, Di Larang Keras Menggunakan [red]Akun Pribadi[white] Dan Pastikan Akun Tidak [yellow]Checkpoint[white] Dan Terpasang [red]A2F")
            cookies = Console().input("[white] ?) [green]cookie dough extension[white]: ")
            if len(cookies) >0:
                self.username, self.fullname = self.Validasi_Cookies(cookies)
                with open(self.data+'.Cookies_IGS.json', mode='w') as wr:
                    wr.write(json.dumps({
                        'Cookie': cookies
                     }))
                    wr.close()
                Console().print(f"\n[white] * Selamat Datang [green]{self.username}[white]/[green]{self.fullname}[white], Masukan Ulang Perintahnya [green]python Main.py")
                exit()
            else:
                Console().print("[white] ! Maaf, Anda Tidak Memasukan Apapun, Harap Masukan ([green]Cookies[white]) Instagram")
                exit()
        except (KeyboardInterrupt, Exception) as e:
            Console().print(f"[red] ! {str(e).title()}")
            exit()     
        
    def Validasi_Cookies(self, cookies):
        with requests.Session() as r:
            r.headers.update({
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
            })
            response = r.get('https://i.instagram.com/api/v1/users/{}/info/'.format(re.search('ds_user_id=(\d+)',str(cookies)).group(1)), cookies = {
                'cookie': cookies
            })
            self.payload = json.loads(response.text)
            if "'status': 'ok'" in str(self.payload):
                return(self.payload['user']['username'], self.payload['user']['full_name'])
            else:
                Terminal().clear_terminalize()
                Console().print(f"[white] ! Maaf, Tidak Dapat Mengakses Cookie Anda Perkiraan Akun [yellow]Terkena Spam [white]Atau[red] Di Nonaktifkan[white], Harap Cek Akun Anda Atau Ganti Akun Lain")
                time.sleep(3.5)
                self.Removed_Cookies()
        
    def Via_Username_And_Password(self, username, password):
        byps = requests.Session()
        try:
            byps.headers.update({**RequestTL().HeadersApiLogin(),
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,999)),
                'x-ig-bandwidth-totalbytes-b': str(random.randint(2000,5000)),
                'x-ig-bandwidth-totaltime-ms': str(random.randint(500,4000)),
                'x-ig-device-id': str(uuid.uuid4()),
                'x-ig-android-id': 'android-%s'%(RequestTL().android_ID(username,password).hexdigest()[:16]),
                'x-ig-timezone-offset': str(RequestTL().timezone_offset()),
                'x-ig-app-id': '567067343352427',
                'user-agent': 'Barcelona 63.0.0.17.94 Android (31/10; 360dpi; 1080x2326; Vivo; V2020CA; V1950A; qcom; id_ID; 253447817)'
            })
            payload = {'params': '{"client_input_params":{"device_id":"'+ str(byps.headers['x-ig-android-id']) +'","lois_settings":{"lois_token":"","lara_override":""},"name":"'+str(username)+'","machine_id":"'+str(uuid.uuid4())+'","profile_pic_url":null,"contact_point":"'+str(username)+'","encrypted_password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(password)+'"},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":"'+str(byps.headers['x-ig-family-device-id'])+'","device_id":"'+str(byps.headers['x-ig-device-id'])+'","offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","waterfall_id":"'+str(uuid.uuid4())+'","login_source":"Login","INTERNAL__latency_qpl_instance_id":73767726200338,"is_from_logged_in_switcher":0,"is_platform_login":0}}', 'bk_client_context': '{"bloks_version":"'+ str(byps.headers['x-bloks-version-id']) +'","styles_id":"instagram"}','bloks_versioning_id': str(byps.headers['x-bloks-version-id'])}
            encode = ('params=%s&bk_client_context=%s&bloks_versioning_id=%s'%(urllib.parse.quote(payload['params']), urllib.parse.quote(payload['bk_client_context']), payload['bloks_versioning_id'])+'&ig_sig_key_version=4')
            response2 = byps.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/', data = encode, allow_redirects=True).text
            if 'logged_in_user' in str(response2.replace('\\','')):
               try:
                   ig_set_autorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response2.replace('\\', ''))).group(1)
                   decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_autorization.split('Bearer IGT:2:')[1]))
                   cookies = (';'.join(['%s=%s'%(name, value) for name, value in decode_ig_set_authorization.items()]))
               except (Exception) as e: cookie = ('[red] ! Extension Error Not Found 404')
               Console().print(f'[white] # cookie dough extension ([green]{cookies}[white])')
               if len(cookies) >0:
                   self.username, self.fullname = self.Validasi_Cookies(cookies)
                   with open(self.data+'.Cookies_IGS.json', mode='w') as wr:
                        wr.write(json.dumps({
                            'Cookie': cookies
                         }))
                        wr.close()
                   Console().print(f"\n[white] * Selamat Datang [green]{self.username}[white]/[green]{self.fullname}[white], Masukan Ulang Perintahnya [green]python Main.py")
                   exit()
               else:
                   Console().print(f"[white] ! Maaf, Tidak Dapat Mengakses Cookie Anda Perkiraan Akun [yellow]Terkena Spam [white]Atau[red] Di Nonaktifkan[white], Harap Cek Akun Anda Atau Ganti Akun Lain")
                   exit()
            elif 'two_factor_required' in str(response2.replace('\\','')):
                Console().print("[white] ! Maaf, Tidak Dapat Mengakses Akun Anda, Akun Anda Terpasang [red]A2F")
                exit()
            elif 'challenge_required' in str(response2.replace('\\','')):
                Console().print("[white] ! Maaf, Tidak Dapat Mengakses Akun Anda, Akun Anda [yellow]Checkpoint")
                exit()
            elif 'ip_block' in str(response2.replace('\\','')):
                Console().print("[white] ! Maaf, Terjadi Kesalahan Alamat Ip Anda Terblokir, Silakan Mode Pesawat 5 Detik")
                exit()
            else:
                Console().print("[white] ! Maaf, Terjadi Kesalahan ([green]Username Atau Password[white]) Yang Anda Masukan Salah, Silakan Cek ([green]Username Dan Password[white]) Anda Pastikan Benar")
                exit()
        except (KeyboardInterrupt, Exception, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects) as e:
            Console().print(f"[red] ! {str(e).title()}")
            exit()   
