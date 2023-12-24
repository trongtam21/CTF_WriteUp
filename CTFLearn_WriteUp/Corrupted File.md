## Đề 
> Help! I can't open this file. Something to do with the file header… Whatever that is. 
## Link 
> https://mega.nz/#!aKwGFARR!rS60DdUh8-jHMac572TSsdsANClqEsl9PD2sGl-SyDk
## Giải 
- Ngay từ cái đề chúng ta có thể dễ dàng nhìn thấy hướng đi là sửa phần header bị hỏng của file gif
- Tôi bắt đầu sửa nó bằng phần mềm Ghex nhưng tôi éo biết cách chèn thêm 4 byte là chèn sao hết nên sử dụng web `https://hexed.it/` để sửa
- Tra google thì nhận ra phần header là `GIF89a` và hex tương ứng là `47 49 46 38 39 61` nhưng trong ảnh đã có sẵn 9a rồi nên chỉ cần GIF8 nữa thôi
- Để chèn thêm 4 byte thì chỉ cần nhấn shift > insert > 4 > `47 49 46 38`
- Sau đó lưu file lại ta được file gif nhưng nó chạy nhanh quá khó đọc thông tin
- Ta cần chuyển nó sang file ảnh bằng cách sử dụng trang web `https://ezgif.com/gif-to-jpg`
- Ta sẽ được chuỗi sau : `the flag is ZmxhZ3tnMWZfb3JfajFmfQ== decode it`
- Sau khi thấy nó tôi nghĩ ngay đến mã base64 
- Decode thì được flag : `flag{g1f_or_j1f}`