## Desciption 
> Can you find the matrix password again?
## Link challenge 
> https://ringzer0ctf.com/challenges/24
## Solution
- Fistly, I unzipped file `2b4d08e1a1eac8a8c9034036d420bd88.zip` and and got the BK file
- I check file BK with `file` tool
```
┌──(kali㉿kali)-[~/Downloads]
└─$ file BK 
BK: Linux rev 1.0 ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1c9a80
```
- Continue, I used tool `extext3grep` 
```
ext3grep is a simple tool intended to aid anyone who accidentally deletes a file on an ext3 filesystem, only to find that they wanted it shortly thereafter.
```
- 
```
 ext3grep --inode 2 BK  
Running ext3grep version 0.10.2
No --ls used; implying --print.

WARNING: I don't know what EXT3_FEATURE_COMPAT_EXT_ATTR is.
Number of groups: 1
Loading group metadata... done
Minimum / maximum journal block: 198 / 1227
Loading journal descriptors... sorting... done
The oldest inode block that is still in the journal, appears to be from 1391736883 = Thu Feb  6 20:34:43 2014
Number of descriptors in journal: 252; min / max sequence numbers: 3 / 47

Hex dump of inode 2:
0000 | ed 41 f4 01 00 04 00 00 55 42 f4 52 1b 42 f4 52 | .A......UB.R.B.R
0010 | 1b 42 f4 52 00 00 00 00 f4 01 05 00 02 00 00 00 | .B.R............
0020 | 00 00 00 00 00 00 00 00 b8 00 00 00 00 00 00 00 | ................
0030 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
0040 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
0050 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
0060 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
0070 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................

Inode is Allocated
Group: 0
Generation Id: 0
uid / gid: 500 / 500
mode: drwxr-xr-x
size: 1024
num of links: 5
sectors: 2 (--> 0 indirect blocks).

Inode Times:
Accessed:       1391739477 = Thu Feb  6 21:17:57 2014
File Modified:  1391739419 = Thu Feb  6 21:16:59 2014
Inode Modified: 1391739419 = Thu Feb  6 21:16:59 2014
Deletion time:  0

Direct Blocks: 184
Finding all blocks that might be directories.
D: block containing directory start, d: block containing more directory entries.
Each plus represents a directory start that references the same inode as a directory start that we found previously.

Searching group 0: DD+++++++++++++++++D++++D+++++
Writing analysis so far to 'BK.ext3grep.stage1'. Delete that file if you want to do this stage again.
Result of stage one:
  4 inodes are referenced by one or more directory blocks, 4 of those inodes are still allocated.
  3 inodes are referenced by more than one directory block, 3 of those inodes are still allocated.
  0 blocks contain an extended directory.
Result of stage two:
  4 of those inodes could be resolved because they are still allocated.
All directory inodes are accounted for!


Writing analysis so far to 'BK.ext3grep.stage2'. Delete that file if you want to do this stage again.
The first block of the directory is 184.
Inode 2 is directory "".
Directory block 184:
          .-- File type in dir_entry (r=regular file, d=directory, l=symlink)
          |          .-- D: Deleted ; R: Reallocated
Indx Next |  Inode   | Deletion time                        Mode        File name
==========+==========+----------------data-from-inode------+-----------+=========
   0    1 d       2                                         drwxr-xr-x  .
   1    2 d       2                                         drwxr-xr-x  ..
   2    3 d      11                                         drwx------  lost+found
   3    5 r      14                                         rrw-r--r--  TODO.me
   4    5 r      12  D 1391739419 Thu Feb  6 21:16:59 2014  rrw-r--r--  secret.sve
   5    6 d      13                                         drwxr-xr-x  .hide
   6  end d      17                                         drwxr-xr-x  .ls
   7  end r      16  D 1391739038 Thu Feb  6 21:10:38 2014  rrw-rw-r--  secret.odg

```
- I see a few files and recover it
```
 ext3grep --restore-all BK 
Running ext3grep version 0.10.2
WARNING: I don't know what EXT3_FEATURE_COMPAT_EXT_ATTR is.
Number of groups: 1
Minimum / maximum journal block: 198 / 1227
Loading journal descriptors... sorting... done
The oldest inode block that is still in the journal, appears to be from 1391736883 = Thu Feb  6 20:34:43 2014
Number of descriptors in journal: 252; min / max sequence numbers: 3 / 47
Writing output to directory RESTORED_FILES/
Loading BK.ext3grep.stage2... done
Restoring .hide/secret.odg
Restoring TODO.me
Restoring secret.odg
Restoring secret.sve
```
- I  got compressed file `.sve`
```
┌──(kali㉿kali)-[~/Downloads/RESTORED_FILES]
└─$ file secret.sve 
secret.sve: Zip archive data, at least v2.0 to extract, compression method=deflate
                                                                                          
```
- I changed the extension and unzipped it, but it was difficult because of the password
- I used john to crack it 
```
┌──(kali㉿kali)-[~/Downloads/RESTORED_FILES]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
12345            (secret.zip/secret.txt)     
1g 0:00:00:00 DONE (2024-04-02 06:57) 50.00g/s 409600p/s 409600c/s 409600C/s 123456..whitetiger
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```
- Open it with password, I can get flag 
> Flag : FLAG-menummenum