## Đề 
> The password for the next level is stored in the file data.txt and is the only line of text that occurs only once
## Kết nối máy chủ 
> ssh bandit8@bandit.labs.overthewire.org -p 2220 (password : TESKZC0XvTetK0S9xNwm25STk5iWrBvP)
## Giải 
- Muốn làm được bài này phải tìm hiểu về lệnh `uniq`
```text
Nói một cách đơn giản, uniq là công cụ giúp phát hiện các dòng trùng lặp liền kề và xóa các dòng trùng lặp. uniq lọc ra các dòng khớp liền kề từ tệp đầu vào (được yêu cầu làm đối số) và ghi dữ liệu đã lọc vào tệp đầu ra. 
Usage: uniq [OPTION]... [INPUT [OUTPUT]]
Filter adjacent matching lines from INPUT (or standard input),
writing to OUTPUT (or standard output).

With no options, matching lines are merged to the first occurrence.

Mandatory arguments to long options are mandatory for short options too.
  -c, --count           prefix lines by the number of occurrences
  -d, --repeated        only print duplicate lines, one for each group
  -D                    print all duplicate lines
      --all-repeated[=METHOD]  like -D, but allow separating groups
                                 with an empty line;
                                 METHOD={none(default),prepend,separate}
  -f, --skip-fields=N   avoid comparing the first N fields
      --group[=METHOD]  show all items, separating groups with an empty line;
                          METHOD={separate(default),prepend,append,both}
  -i, --ignore-case     ignore differences in case when comparing
  -s, --skip-chars=N    avoid comparing the first N characters
  -u, --unique          only print unique lines
  -z, --zero-terminated     line delimiter is NUL, not newline
  -w, --check-chars=N   compare no more than N characters in lines
      --help     display this help and exit
      --version  output version information and exit
```
- Để làm được điều đó đầu tiên ta phải sắp xếp các dòng theo thứ tự bằng lệnh sort
> sort data.txt
- Sau đó là dùng lệnh uniq để đếm
> uniq -u
- Câu lệnh hoàn chỉnh là 
> sort data.txt | uniq -u
- Password 
> EN632PlfYiZbn3PhVK3XOGSlNInNE00t