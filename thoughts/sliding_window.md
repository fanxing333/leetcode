# 滑动窗口

在一般情况下，滑动窗口维护两个指针 left 和 right。其中有一个指针会依次加一从头遍历到尾，而另一个指针会随着遍历更改其值以达到最大效率。那么，以哪个指针为基准遍历是首要考虑的问题。第二，另一个指针什么时候改动，改动多少是下一个考虑的问题。