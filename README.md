# Blogger.com Helper
Just a simple script I wrote for helping me with blogger.com's inconveniences. In fancier terms, I would call it a text processor engine, but I dunno how far that applies to this project.


## What it does
It takes in input through the article.txt, does some python magic and outputs a out.txt file with the converted text. It uses symbols as the first word for it's conversion.

an example: <br>

[article.txt](https://github.com/mulitate4/script_Blogging_helper/files/6448082/article.txt)
```txt
p bruh moment
# lol


p some text here *too*
```

to <br>
[out.txt](https://github.com/mulitate4/script_Blogging_helper/files/6448084/out.txt)
```html
<span style="font-family: Comfortaa; font-size: medium;">bruh moment</span><br>
<span style="font-family: Comfortaa; font-size: xx-large;">lol</span><br>
<br>
<br>
<span style="font-family: Comfortaa; font-size: medium;">some text here <b>too</b></span><br>
```


----
## What do the symbols mean?
The symbols borrow their origin partially from Markdown (a file type).

| Symbol      | Description  |
| ----------- | ------------ |
| #           | Huge Title   |
| ##          | Smaller Title|
| p           | Paragraph    |
| \*text\*    | Bold Text    |

Currently, this is the scope for the Script. I'll probably add more features in the near future as and when I need them!
