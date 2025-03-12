#!/usr/bin/env python3
# -*- coding:utf-8

from Penyimpanan.Database.data import *

class Guirequest:
    def __init__(self) -> None:
        self.csrftoken, self.mid, self.ig_did = self.AsetCookies()
        pass
        
    def Android_ID(self, username, password):
        self.xyz = hashlib.md5()
        self.xyz.update(username.encode('utf-8') + password.encode('utf-8'))
        self.hex = self.xyz.hexdigest()
        self.xyz.update(self.hex.encode('utf-8') + '12345'.encode('utf-8'))
        return (self.xyz)
        
    def UseNet(self):
        return('MOBILE.LTE','MOBILE(LTE)')
        
    def AsetCookies(self):
      with requests.Session() as r:
          response = r.get('https://i.instagram.com/api/v1/public/landing_info/',headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1'}).cookies
          try:
              self.csrftoken = response['csrftoken']
              self.mid = response['mid']
              self.ig_did = response['ig_did']
              return(self.csrftoken,self.mid,self.ig_did)
          except (Exception) as e:
              return('qRrp7C6mjOtQj5YkInaVemOXMXlkPGNP','Z8eDqAAAAAEqp9QGqTFLzmZx4TW_','A9C5C8D3-D5DD-413B-B539-5F4920E7749F')
              
    def HeadersApiLogin(self):
        return {
            'authority': 'i.instagram.com',
            'x-ig-app-locale': 'in_ID',
            'x-ig-device-locale': 'in_ID',
            'x-ig-mapped-locale': 'id_ID',
            'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
            'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
            'x-ig-bandwidth-speed-kbps': '-1.000',
            'x-ig-bandwidth-totalbytes-b': '0',
            'x-ig-bandwidth-totaltime-ms': '0',
            'x-bloks-version-id': self.Blok_ID(),
            'x-ig-www-claim': '0',
            'x-bloks-prism-button-version': 'CONTROL',
            'x-bloks-prism-indigo-link-version': '0',
            'x-bloks-prism-colors-enabled': 'false',
            'x-bloks-prism-ax-base-colors-enabled': 'false',
            'x-bloks-prism-font-enabled': 'false',
            'x-ig-attest-params': '{"attestation":[{"version":2,"type":"keystore","errors":[-1013],"challenge_nonce":"%s","signed_nonce":"","key_hash":""}]}' % ('{:.3f}'.format(time.time())),
            'x-bloks-is-layout-rtl': 'false',
            'x-ig-device-id': 'ec76c649-d663-48f1-b6bb-bcadc556d340',
            'x-ig-family-device-id': '293c83cd-45d8-4ea9-956d-357f7c476be4',
            'x-ig-android-id': 'android-bc2b6bd10fb8fbe6',
            'x-ig-timezone-offset': str(self.timezone_offset()),
            'x-ig-nav-chain': 'com.bloks.www.caa.login.home_template:com.bloks.www.caa.login.home_template:1:button:{:.3f}'.format(time.time()),
            'x-ig-client-endpoint': 'com.bloks.www.caa.login.home_template',
            'x-fb-connection-type': self.UseNet()[0],
           'x-ig-connection-type': self.UseNet()[1],
            'x-ig-capabilities': '3brTv10=',
            'x-ig-app-id': '567067343352427',
            'priority': 'u=3',
            'user-agent': 'Instagram 309.1.0.41.113 Android (31/10; 360dpi; 1080x2326; Vivo; V2020CA; V1950A; qcom; id_ID; 541635863)',
            'accept-language': 'id-ID, en-US',
            'x-mid': str(self.mid),
            'ig-intended-user-id': '0',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'accept-encoding': 'gzip, deflate',
            'x-fb-http-engine': 'Liger',
            'x-fb-client-ip': 'True',
            'x-fb-server-cluster': 'True',
            'cookie': (f'{self.csrftoken}; {self.ig_did}; {self.mid}')
        }
        
    def Blok_ID(self):
        self.v01 = 'c0540eb85d97f640e878730536aaa77395f8948a761b2ae64a259208df42a306'
        self.v02 = 'ee55d61628b17424a72248a17431be7303200a6e7fa08b0de1736f393f1017bd'
        self.v03 = '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a'
        return(random.choice([self.v01,self.v02,self.v03]))
       
    def timezone_offset(self):
        self.tim = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
        self.ofs = self.tim.utcoffset().total_seconds()/60/60
        return (self.ofs)