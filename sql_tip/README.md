* [m-n]: 

select * from table where column REGEXP '[0-9a-z]'

* [^...]

不能只有其中的这些字符，一定要有些别的

select * from table where column REGEXP '[^abc]'

指不能只有abc，可以1c，3a。。。。






