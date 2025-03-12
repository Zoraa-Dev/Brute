
from Penyimpanan.Database.data import *

class Encrypted:
    def __init__(self) -> None:
        pass
        
    def enc_browsers(self,password):
        with requests.Session() as r:
            try:
                resp = r.get("https://i.instagram.com/api/v1/web/accounts/login/ajax/")
                key_id = int(resp.headers.get("ig-set-password-encryption-web-key-id"))
                pub_key = resp.headers.get("ig-set-password-encryption-web-pub-key")
                version = resp.headers.get("ig-set-password-encryption-web-key-version")
                key = Random.get_random_bytes(32)
                iv = bytes([0] * 12)
                time = int(datetime.datetime.now().timestamp())
                aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
                aes.update(str(time).encode('utf-8'))
                encrypted_password, cipher_tag = aes.encrypt_and_digest(password.encode('utf-8'))
                pub_key_bytes = binascii.unhexlify(pub_key)
                seal_box = SealedBox(PublicKey(pub_key_bytes))
                encrypted_key = seal_box.encrypt(key)
                encrypted = bytes([1,key_id, *list(struct.pack('<h', len(encrypted_key))), *list(encrypted_key), *list(cipher_tag), *list(encrypted_password)])
                encrypted = base64.b64encode(encrypted).decode('utf-8')
                return ('#PWD_INSTAGRAM_BROWSER:%s:%s:%s'%(version, time, encrypted)) 
            except (Exception) as e:
                return ('#PWD_INSTAGRAM_BROWSER:0:%s:%s'%(int(time.time()), password))
                