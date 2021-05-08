* [m-n]: 

select * from table where column REGEXP '[0-9a-z]'

* [^...]

不能只有其中的这些字符，一定要有些别的

select * from table where column REGEXP '[^abc]'

指不能只有abc，可以1c，3a。。。。

* a*

匹配0个或N个a

select * from table where column REGEXP 'bb*'

一定要有个b，之后的b* 可以有N个b也可以0个b

* a+

匹配1个或N个a

![image](https://user-images.githubusercontent.com/23666146/117550948-f3fa9280-aff7-11eb-9ca1-c2fb508e7a78.png)






