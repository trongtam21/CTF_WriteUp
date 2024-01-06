## Đề :
>  Solve the equations embedded in the jpeg to find the flag. Solve this problem before solving my Scope challenge which is worth 100 points.
## Link :
> https://ctflearn.com/challenge/download/972
## Giải
- Mở file ra xem em thấy 1 bài toán gì gì đấy mà thấy không hết, em nghĩ nó không phải là bài toán mà đề cho
- `strings math.jpg` xem thử thế nào
- "The flag for this challenge is of the form:   
- CTFlearn{I_Like_Math_x_y}  
- where x and y are the solution to these equations:
- 3x + 5y = 31 
- 7x + 9y = 59"
- Sau khi giải hệ phương trình ta thu được 
> Đáp án là `x=2 và y=5`
- Thay vào flag rồi submit `CTFlearn{I_Like_Math_2_5}`