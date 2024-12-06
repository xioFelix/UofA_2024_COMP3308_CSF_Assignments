### **Part I - Linux Basics**

#### 1. Secret in `test.txt`
- **Command**:
  ```bash
  grep -A 1 "^And.*it$" /home/student/linux_basics/q01/test.txt
  ```
- **Explanation**: `grep` searches for lines starting with "And" and ending with "it", and `-A 1` includes the following line.  
- **Result**: Document the secret passphrase.

---

#### 2. Passphrase in `here.txt`
- **Command**:
  ```bash
  sort /home/student/linux_basics/q02/here.txt | uniq -c | grep " 14 "
  ```
- **Explanation**: `sort` sorts lines, `uniq -c` counts occurrences, and `grep " 14 "` finds lines occurring exactly 14 times.
- **Result**: Note the passphrase.

---

#### 3. SHA256 checksum in `/home/student/linux_basics/q03`
- **Command**:
  ```bash
  for file in /home/student/linux_basics/q03/*; do sha256sum "$file"; done | grep "389f0d2df51e5553118e2de48b40e1cc67ae2b477cf6d27ca1faf1c548f78f0c"
  ```
- **Explanation**: Computes SHA256 for all files in the directory and matches the given checksum.
- **Result**: Record the file name.

---

#### 4. Brute-forcing GPG file
- **Commands**:
  1. Generate the password list:
     ```bash
     sed 'y/aeio/4310/' /home/student/linux_basics/q04/words.txt > passwords.txt
     ```
  2. Brute-force decryption:
     ```bash
     for pass in $(cat passwords.txt); do
       gpg --batch --passphrase "$pass" -d /home/student/linux_basics/q04/encrypted.gpg 2>/dev/null && echo "Password: $pass" && break
     done
     ```
- **Result**: Record the password and decrypted content.

---

#### 5. Decode secret using `cyber.py`
- **Command**:
  ```bash
  python3 /home/student/linux_basics/q05/cyber.py decode /home/student/linux_basics/q05/secret.txt
  ```
- **Result**: Note the decoded flag.

---

#### 6. File with 47 bytes
- **Command**:
  ```bash
  find /home/student/linux_basics/q06 -type f -size 47c
  ```
- **Explanation**: `find` locates files with exactly 47 bytes (`47c`).
- **Result**: Note the file name.

---

#### 7. Run `a.out`
- **Command**:
  ```bash
  /home/student/linux_basics/q07/a.out
  ```
- **Explanation**: Run the executable and document your process to deduce the secret.
- **Result**: Record the guessed secret.

---

#### 8. Decode secret in `/q08`
- **Command**: Use decoding tools or methods depending on the file format (e.g., Base64 or XOR).
- **Result**: Provide the decoded secret.

---

### **Part II - Cryptography**

#### 1. Decrypt `secret.txt.enc`
- **Python Code**:
  ```python
  import random

  def decrypt(filename, seed):
      random.seed(seed)
      with open(filename, 'r') as enc_file:
          content = enc_file.read()
          decrypted = ''.join([chr(ord(char) ^ random.randrange(255)) for char in content])
      print(decrypted)

  decrypt('/home/student/crypto/q01/secret.txt.enc', 312024)
  ```
- **Result**: Note the decrypted secret and discuss the weak encryption and key space.

---

#### 2. Textbook RSA decryption
- **Python Code**:
  ```python
  n = 0x9B51C20306EDE535C8FCAADBC3F3515E52A0D005703DD449BEC66B23E2932313
  e = 0x010001
  d = 0x0D067636BAC6088AD2281E4BFFCACFEFEF9BC1A69FB9E701063DFBAAB436E4C1
  ciphertext = 0x... # Encrypted message (replace with actual hex)

  plaintext = pow(ciphertext, d, n)
  print(bytearray.fromhex(hex(plaintext)[2:]).decode())
  ```
- **Result**: Provide the decrypted message.

---

#### 3. Hidden message in bitmap
- **Command**:
  ```bash
  strings encrypted_image.bmp
  ```
- **Explanation**: Extract human-readable text from the image file.
- **Result**: Note the hidden message.

---

#### 4. Classical cipher decryption
- **Command**: Use tools like `cyberchef` or manual methods based on frequency analysis to decode `ciphertext.txt`.
- **Result**: Provide the plaintext and key.

---

#### 5. Cracking `yoda` password
- **Command**:
  ```bash
  hashcat -m 500 -a 0 -o cracked.txt /path/to/shadow /usr/share/wordlists/rockyou.txt
  ```
- **Result**: Note the cracked password for the `yoda` account.

---

### **Final Submission**
- Ensure the PDF contains:
  1. Commands executed (with explanations).
  2. Scripts used.
  3. Screenshots of outputs (where applicable).
  4. Results for each task.