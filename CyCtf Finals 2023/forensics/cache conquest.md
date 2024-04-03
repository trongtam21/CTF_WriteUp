## Description
- ![image](image/4.PNG)
## Link challenge 
> https://drive.google.com/file/d/1WtwppfPCvg19wUOwk_pDX-c2ACpH64jC/view?usp=sharing
## Solution 
- After download, I got file .ad1
- I will analyze by `FTK Image`
- After looking through all the directory paths, I saw a registry file, I took it down and analyzed it using the Registry Explorer tool
- ![image](image/5.PNG)
- ![image](image/6.PNG)
- In `D:\share\Amcache.hve: Root\InventoryApplicationFile`, I searched for the path containing the external drive
- ![image](image/8.PNG)
> Flag : cyctf{f4f868d4fa6b3730f4ff24f9bc03c65a2d78c244}
