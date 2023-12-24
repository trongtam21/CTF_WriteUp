- Đề : Someone might have hidden the password in the trace file. Find the key to unlock this file. This tracefile might be good to analyze.
- Link : https://artifacts.picoctf.net/c/498/flag.zip
- Link : https://artifacts.picoctf.net/c/498/dump.pcap
- HINT : Download the pcap and look for the password or flag.
- HINT : Don't try to use a password cracking tool, there are easier ways here.
- Đọc đề ta có thể dễ dàng phần nào đoANS ĐƯỢC Là sẽ có 2 file trong đó có 1 file nén với mật khẩu. Mục tiêu của ta là tìm mật khẩu đó
- Mở file pcapng ra rồi tìm xem có gì không 
- Sau 1 lúc tìm kiếm thì tôi thấy trong các gói tin có 1 số gợi ý nữa như sau :
- 1. Flying on Ethernet secret : is this the flag	
- 2. +Chromecast-18e2a8da30459b730aec93a71af19988
- 3. iBwaWNvQ1RGe1 Could the flag have been splitted?
- 4. PBwaWUvQ1RGesaba babkjaASKBKSBACV VAVSDDSSSSDSKJBJS
- 5. PBwaWUvQ1RGe1 May be try checking  the other file.
- 6. AABBHHPJGTFRLK VGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=
- Thấy tại cái thứ 6 có dấu = có thể nó được decode base64
- picoCTF{R34DING_LOKd_ sau khi decode được như thế này :
- Giờ lấy key đó ũnip file zip
- ta được file flag : `picoCTF{R34DING_LOKd_fil56_succ3ss_494c4f32}`
- 



