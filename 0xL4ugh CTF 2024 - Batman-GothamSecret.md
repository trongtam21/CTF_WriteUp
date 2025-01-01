## Batman-GothamSecret
### Description
![public2](https://hackmd.io/_uploads/B1wMxG-IJg.png)
### Solution
##### Trong challenge này cung cấp cho ta 1 folder LiveResponseData chứa các thông tin của 1 máy tính MacOS nào đó, phần mô tả nói rằng ta cần khôi phục lại dữ liệu bị đánh cắp đặc biệt là `encrypted secret notes`. -> Nó được lưu ở keychain
![image](https://hackmd.io/_uploads/HJXHNPG81l.png)
##### Tìm kiếm trên google, mình tìm thấy liên kết liên quan như sau :
https://apple.stackexchange.com/questions/307189/how-to-decrypt-the-system-keychain-from-another-mac-at-the-command-line
##### Theo đó nếu ta muốn giải mã được dữ liệu keychain trước tiên ta phải có 2 file, 1 file System.keychain và SystemKey (chứa mật khẩu thực tế)
![image](https://hackmd.io/_uploads/S18WSvGIkg.png)
![image](https://hackmd.io/_uploads/SJpXBvGLyl.png)
##### Tuy nhiên, vấn đề là không có file SystemKey tại đây, vì vậy ta không thể giải mã nó.
##### Kiểm tra tại `/Library/Preferences` ta thấy nó tồn tại 1 file tên là `com.apple.loginwindow.plist` cho thấy rằng chế độ tự động đăng nhập đã được bật, ta có thể khôi phục mật khẩu tại đây.
##### Dựa vào 1 vài thông tin hiện có mình tiếp tục mình tìm thấy 1 blog khá hữu ích : https://www.offsec.com/blog/in-the-hunt-for-the-macos-autologin-setup-process/
##### Blog này cho ta biết rằng dữ liệu user password sẽ được lưu trữ dưới dạng `obfuscated` trong file `/etc/kcpassword` và nó được obfuscated bằng cách xor với 1 chuỗi (0x7D 0x89 0x52 0x23 0xD2 0xBC 0xDD 0xEA 0xA3 0xB9 0x1F)
![image](https://hackmd.io/_uploads/SyyatDGLye.png)
![image](https://hackmd.io/_uploads/ryf1qDGIkl.png)
##### Bây giờ dùng Cyberchef để giải mã nó. 
![image](https://hackmd.io/_uploads/S1-0qwfL1x.png)
##### Đã có user password và file login.keychain.db, ta dùng công cụ [Chainbreaker - Mac OS X Keychain Forensic Tool](https://github.com/n0fate/chainbreaker/releases/tag/v0.9) để giải mã.
> Payload : python2 chainbreaker.py -f login.keychain-db -p a1l894m^@gÆis
![image](https://hackmd.io/_uploads/rJg4hPGIJl.png)
> Flag : 0xL4ugh{4ut0l0g1n5_4nd_k3ych41n5_54y_brrrrrr}