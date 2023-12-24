## Đề 
> We found this packet capture and key. Recover the flag.
## Link 
> https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/capture.pcap
> https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/picopico.key
## Hint 
> Try using a tool like Wireshark.
> How can you decrypt the TLS stream?
## Giải 
- Sau khi tôi tải file về và mở lần lượt từng file lên 
- Tại file `picopico.key` tôi thu được 1 đoạn khoá 
```text
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCwKlFPNKjseJF5
puCJU5x38XcT1eQge5zOKNahAlYudvGVOEs61TnIgvcER4ko8i3OCwak2/atcGk3
oz9jFKep7XFEYNP31IwwD9j/YazlKy4DRLGObOyIZUU1f2WRA7Uhf0POQXsDT1oU
X32jMKZkQSSDW4MRZd9trJYdO2TrcEPMsBiZQlFlvgnNwl3QlawozTHLAJKI36j1
cPwSMMeNca1e0Zi1s7R5IxfhpNXOBF0FmxiWvmeOHbaspyHg8UEmGBrkd4k4wXSK
GQvrc8QjycP4ScEdquxJiYnDT8iEbAq70/7f/5NIN1DE9YoGJqKYjTS9nRPB4Yvj
JN/SJnhvAgMBAAECggEACCnd3LrG/TZVH3sROqvqO1CwQPYPfUXdLVyNHab7EWon
pc+XBOHurJENG2CpRYF7h+nQ5ADhfIYSCicBf/jsEB7VueJ20CxEVtHVL3h6R6Bp
oHMle0Em8OcofuMpdL/kO+om3T8BkVSzCvCl5NMTUuAF7iRmfX7oDLALwM0IzzQv
2un+2UmT15rgAZfl3IL1PGvJhbhLxfeeyPE9MBy1SqBjQ9rNFn8sQv959J6BHz4b
EpK//ErtNP2yh7oiVBBgKEQ1gEuOjQC/4oxoqCFfZaf9XNRCxB/zY1nUprvJyz09
NMQWNF2EmvmBVGfoTxmuut5N0GbVr2UyHxWMKm2sOQKBgQDpb2+AWgWlGtetuLKJ
fJs8dnd6LhnafbKCOXMOT68qMBRoTpBtVTLRVSNvWCm8m4TTEazX4+ZA+bJFwUFw
aATDmHcr6lMI3tNKrcsnY2F7o5I4z6mwuRuSeszq/ndxZqCzwCu4nKixh3cznp7j
JiElNG0d8Lu5eQgmVAK1AhWXfQKBgQDBMa9ga7VJUP4pzcHnWAoi34OpfjvQYeGl
IKL3AKO4OedaHdH9qid41PQHnL7O3xzN669SkLZ5s0d88A/LFLk4oZNMKdkSTQIQ
+AMbXH01HGFvnCOuPg/FbNp1wS7zJEg5u5HFQWyMPNJLr/hZ6g2Yp+UGpAcGTwM/
RCPVAPhLWwKBgQDAB0OaOnPaVjKGXiHAqBirrGiswa/S5QQrzEaxxys5cUPYaoi0
6BldysPTnJr45JZna2rcTkXjvYTBjTDf3zHMFWgzYBfefC8kh8NPK5nNs8ldorbd
AemEnjBkP+DSELKyK6vLulOrdtzAQgRCp+MsT+xTbO2ArefeX826SXSpoQKBgC2v
nDOHBQXje1dTawlUToFUrgQE8AwlOYEdKKyUoCLOvqEW8DO2a0MtyM+MB6tQI7Wm
iH1T73L0LHGlK3bw3aRAwV5/fu/O+jAdFk8AHjPTFE+acu2fi4c6aKb0GjAxYksU
yjIFeK/pKinv4SESMkjpW0WowGiDgtcRPBAA/LaFAoGAfEM1rfM0v3UmB7PS6u0m
P3ckP2CFCdaryXPfC52GBcJ3Q46YpsQvLTVotM+teHvTjNw2jwwZxIl4NenGSEj3
KDhQoOiQC9BrDD+DB4I9+T9nxT3g7R6MrgITghB4We7TVhL/PljnJTyDqpjNA4kY
TveAJPv6Xq1ERt5PUtX3BqQ=
-----END PRIVATE KEY-----
```
- Ở đây tôi mở bằng lệnh strings trên cmd chứ mở không được =))
- Nhìn sơ qua thì đây là dạng mã hoá bất đối xứng 
- Thêm phần hint nữa thì có thể khẳng định đây là mã hoá bất đối xứng theo giao thức tls 
- Tiếp theo ta phải decrypt nó ra 
- Sau n+1 lần tra google thì tôi đã thấy được trang `https://packetpushers.net/using-ssldump-decode-ssltls-packets/` 
- Nội dung là sử dụng ssldump để decrypt 
- `ssldump -h` để xem cách dùng 
```text
Usage: ssldump [-r dumpfile] [-i interface] [-l sslkeylogfile] [-w outpcapfile]
               [-k keyfile] [-p password] [-vtaTnsAxVNde]
               [filter]
```
- Trước tiên phải đổi key qua .txt cho nó đọc đã (ý kiến riêng =)))
> ssldump -r capture.pcap -k key.txt -d
- Sau khi dùng mắt quét qua 1 lượt thì chỗ hex có flag 
```text 
48 54 54 50 2f 31 2e 31 20 32 30 30 20 4f 4b 0d    HTTP/1.1 200 OK.
    0a 44 61 74 65 3a 20 46 72 69 2c 20 32 33 20 41    .Date: Fri, 23 A
    75 67 20 32 30 31 39 20 31 35 3a 35 36 3a 33 36    ug 2019 15:56:36
    20 47 4d 54 0d 0a 53 65 72 76 65 72 3a 20 41 70     GMT..Server: Ap
    61 63 68 65 2f 32 2e 34 2e 32 39 20 28 55 62 75    ache/2.4.29 (Ubu
    6e 74 75 29 0d 0a 4c 61 73 74 2d 4d 6f 64 69 66    ntu)..Last-Modif
    69 65 64 3a 20 4d 6f 6e 2c 20 31 32 20 41 75 67    ied: Mon, 12 Aug
    20 32 30 31 39 20 31 36 3a 35 30 3a 30 35 20 47     2019 16:50:05 G
    4d 54 0d 0a 45 54 61 67 3a 20 22 35 66 66 2d 35    MT..ETag: "5ff-5
    38 66 65 65 35 30 64 63 33 66 62 30 2d 67 7a 69    8fee50dc3fb0-gzi
    70 22 0d 0a 41 63 63 65 70 74 2d 52 61 6e 67 65    p"..Accept-Range
    73 3a 20 62 79 74 65 73 0d 0a 56 61 72 79 3a 20    s: bytes..Vary: 
    41 63 63 65 70 74 2d 45 6e 63 6f 64 69 6e 67 0d    Accept-Encoding.
    0a 43 6f 6e 74 65 6e 74 2d 45 6e 63 6f 64 69 6e    .Content-Encodin
    67 3a 20 67 7a 69 70 0d 0a 50 69 63 6f 2d 46 6c    g: gzip..Pico-Fl
    61 67 3a 20 70 69 63 6f 43 54 46 7b 6e 6f 6e 67    ag: picoCTF{nong
    73 68 69 6d 2e 73 68 72 69 6d 70 2e 63 72 61 63    shim.shrimp.crac
    6b 65 72 73 7d 0d 0a 43 6f 6e 74 65 6e 74 2d 4c    kers}..Content-L
    65 6e 67 74 68 3a 20 38 32 31 0d 0a 4b 65 65 70    ength: 821..Keep
    2d 41 6c 69 76 65 3a 20 74 69 6d 65 6f 75 74 3d    -Alive: timeout=
    35 2c 20 6d 61 78 3d 31 30 30 0d 0a 43 6f 6e 6e    5, max=100..Conn
    65 63 74 69 6f 6e 3a 20 4b 65 65 70 2d 41 6c 69    ection: Keep-Ali
    76 65 0d 0a 43 6f 6e 74 65 6e 74 2d 54 79 70 65    ve..Content-Type
    3a 20 74 65 78 74 2f 68 74 6d 6c 0d 0a 0d 0a 1f    : text/html.....
    8b 08 00 00 00 00 00 00 03 a5 54 5d 73 da 3a 14    ..........T]s.:.
    7c 4e 7e 85 e2 d7 c4 16 2e 04 c8 1d 9b 99 24 34    |N~...........$4
    05 67 28 e1 23 40 f2 26 6c d9 96 2b 4b 42 12 1f    .g(.#@.&l..+KB..
    e6 d7 5f d9 84 90 66 da 4e ef 5c 5e 2c 1f 2d 47    .._...f.N.\^,.-G
    bb 7b d6 f2 2e 22 1e ea 42 60 90 ea 9c 76 ce bd    .{..."..B`...v..
    f2 01 28 62 89 6f 61 66 75 ce 01 f0 52 8c a2 72    ..(b.oafu...R..r
    61 96 17 b6 0d c6 78 b5 26 12 47 20 c7 1a 01 8d    a.....x.&.G ....
    12 05 6c fb 6d bf 2a 85 29 92 0a 6b df 5a eb d8    ..l.m.*.)..k.Z..
    6e 5b 1f b7 18 ca b1 6f 6d 08 de 0a 2e b5 05 42    n[.....om......B
    ce 34 66 06 ba 25 91 4e fd 08 6f 48 88 ed ea e5    .4f..%.N..oH....
    0a 10 46 34 41 d4 56 21 a2 d8 77 af 80 4a 25 61    ..F4A.V!..w..J%a
    3f 6c cd ed 98 68 9f 71 d3 fa 44 eb 8e 73 ad b4    ?l...h.q..D..s..
    44 02 dc 4f 26 27 46 d4 fc 03 48 4c 7d 4b e9 82    D..O&'F...HL}K..
    62 95 62 6c ce 4d 25 8e 7d 2b d5 5a a8 7f 20 54    b.bl.M%.}+.Z.. T
    1a 85 3f 04 d2 a9 b3 3c 36 09 23 e6 84 3c 87 ef    ..?....<6.#..<..
    05 d8 70 ea 8e 0b 43 a5 4e 35 27 27 06 a5 94 65    ..p...C.N5''...e
    a8 6a 9c 48 a2 0b 73 4c 8a ea ed 86 9d 24 c3 62    .j.H..sL.....$.b
```
> Flag : picoCTF{nongshim.shrimp.crackers}