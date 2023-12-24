## Đề :
> We need to gain access to some routers. Let's try and see if we can find the password in the captured network data: https://mega.nz/#!XDBDRAQD!4jRcJvAhMkaVaZCOT3z3zkyHre2KHfmkbCN5lYpiEoY Hint 1: It looks like someone logged in with their password earlier. Where would log in data be located in a network capture?<br /> Hint 2: If you think you found the flag, but it doesn't work, consider that the data may be encrypted.
## Giải
- Đầu tiên tôi mở file pcap ra và bắt đầu dò tìm 
- Tôi nghĩ nó sẽ có liên quan tới password nên tôi tìm `tcp contains "pass"` thì nó hiện ra 2 gói
- Kiểm tra lần lượt từng gói 
- Gói đầu tiên là gói html có code như này 
>    form name="login" class="contentstuff" method="post" action="pages/main.html" onsubmit="modifyPass()">
    <table>
    	<tr>
        	<td>Username</td>
            <td><input type="text" name="userid"/></td>
        </tr>
        <tr>
        	<td>Password</td>
            <td><input type="password" name="pswrd"/></td>
        </tr>
    </table>
- Thấy trong đoạn code mật khẩu được gán tên là paswrd nên tôi tìm theo chuỗi kí tự đó `tcp contains "pswrd"` thì nó hiện ra 5 gói tin 
- Kiểm tra từng gói thì gói thứ 105 có dữ liệu của `HTML Form URL Encoded: application/x-www-form-urlencoded` là :
  > Form item: "userid" = "hardawayn"
  > Form item: "pswrd" = "UEFwZHNqUlRhZQ=="
- Nhìn vào mật khẩu ta thấy nó có dấu == nên khả năng cao là nó được mã hoá theo phương thức base64
- Decode ta ra được flag : `CTFlearn{PApdsjRTae}`