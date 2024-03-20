## DESCRIPTION
> A robber has broken through the Windows into the municipal bank! The civilians of the city have called upon you to identify and capture the villain.

Use your heroic forensics superpowers to find the SID of the user robbr using the Windows registry files provided!
## SOLUSION
- Baseed on description, my idea is find `user id` in hives. After check with `SID`.
- We wil find `user id` in `SAM\Account\Users`
- ![image](image/6.png)
- We can see user robbr have` user ID` is 1001
- Continue, I check in SAM\Builtin\Aliases so see SID corresponding (tương ứng).
- ![image](image/7.PNG)
> Flag : jctf{S-1-5-21-1410353290-3892556988-1991803543-1001}
