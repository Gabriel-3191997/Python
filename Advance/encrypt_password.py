from pathlib import Path
from typing import Dict, List, Optional

import json
from base64 import urlsafe_b64encode, urlsafe_b64decode

try:
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
except Exception:  # pragma: no cover - informative import error
    raise ImportError("PyCryptodome is required. Install with: pip install pycryptodome")


class PasswordManager:
   
    def __init__(self, key_file: str = 'secret.key', password_file: str = 'passwords.json') -> None:
        self.key_path = Path(key_file)
        self.password_path = Path(password_file)
        self.key = self._load_or_create_key()

    from pathlib import Path
    import json
    from base64 import urlsafe_b64encode, urlsafe_b64decode

    try:
        from Crypto.Cipher import AES
        from Crypto.Random import get_random_bytes
    except ImportError:
        raise ImportError("Install pycryptodome: pip install pycryptodome")


    class PasswordManager:
        def __init__(self, key_file='secret.key', password_file='passwords.json'):
            self.kp = Path(key_file)
            self.sp = Path(password_file)
            if not self.kp.exists():
                self.kp.write_bytes(get_random_bytes(32))
            self.key = self.kp.read_bytes()

        def _load(self):
            try:
                return json.loads(self.sp.read_text()) if self.sp.exists() else {}
            except json.JSONDecodeError:
                return {}

        def _save(self, data):
            self.sp.write_text(json.dumps(data, indent=2))

        def encrypt(self, plain: str) -> str:
            n = get_random_bytes(12)
            c = AES.new(self.key, AES.MODE_GCM, nonce=n)
            ct, tag = c.encrypt_and_digest(plain.encode())
            return urlsafe_b64encode(n + tag + ct).decode()

        def decrypt(self, token: str) -> str:
            raw = urlsafe_b64decode(token.encode())
            n, tag, ct = raw[:12], raw[12:28], raw[28:]
            p = AES.new(self.key, AES.MODE_GCM, nonce=n).decrypt_and_verify(ct, tag)
            return p.decode()

        def save(self, service: str, password: str):
            d = self._load(); d[service] = self.encrypt(password); self._save(d)

        def get(self, service: str):
            t = self._load().get(service)
            return self.decrypt(t) if t else None

        def delete(self, service: str):
            d = self._load()
            if service in d:
                del d[service]
                self._save(d)
                return True
            return False

        def list(self):
            return list(self._load().keys())


    if __name__ == '__main__':
        pm = PasswordManager()
        pm.save('gmail', 'my_secret_password')
        print(pm.get('gmail'))