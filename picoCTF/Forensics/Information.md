đề bài : Files can always be changed in a secret way. Can you find the flag? https://mercury.picoctf.net/static/7cf6a33f90deeeac5c73407a1bdc99b6/cat.jpg
HINT:
- Look at the details of the file
- Make sure to submit the flag as picoCTF{XXXXX}
Cách 1 : 
- Đầu tiên tôi dùng exiftool để xem dữ liệu hình ảnh 
ở mục License tôi thấy đoạn mã cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9. sau khi decode base64 thì tôi được flag :
picoCTF{the_m3tadata_1s_modified}
Cách 2 : 
- Dùng cat cat.jpg hoặc strings.jpg để xem dữ liệu hình ảnh (ưu tiên dùng strings vì nó đỡ rối mắt)
- Sau 1 hồi lần mò thì tôi thấy 1 đoạn : 
"JFIF
0Photoshop 3.0
8BIM
PicoCTF
http://ns.adobe.com/xap/1.0/
<?xpacket begin='
' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='Image::ExifTool 10.80'>
<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
 <rdf:Description rdf:about=''
  xmlns:cc='http://creativecommons.org/ns#'>
  <cc:license rdf:resource='cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'/>
 </rdf:Description>
 <rdf:Description rdf:about=''
  xmlns:dc='http://purl.org/dc/elements/1.1/'>
  <dc:rights>
   <rdf:Alt>
    <rdf:li xml:lang='x-default'>PicoCTF</rdf:li>
   </rdf:Alt>
  </dc:rights>
 </rdf:Description>
</rdf:RDF>
</x:xmpmeta>"
- Chú ý kĩ dòng này "<cc:license rdf:resource='cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'/>" decode ra ta được flag
