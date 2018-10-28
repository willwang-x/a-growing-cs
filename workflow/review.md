# Review system

## To do 
* [x] [morning routine](https://i.imgur.com/xZVfpTV.png): 把Alfred中的命令(m1, m2, m3)三合一: `screenshots to evernote`
* [ ] 如何提高 @review 整理的时间效率，让其**Focus**在最重要的事情上？

## tools

<img src="https://i.imgur.com/lywdaP3.png" alt="right" width="20"/> <img src="https://i.imgur.com/5L0C5zD.png" alt="shortcuts" width="20"/>
<img src="https://i.imgur.com/xeFNz0B.png" alt="review" width="20"/>
<img src="https://i.imgur.com/wkAKmBc.png" alt="evernote" width="20"/>
<img src="https://i.imgur.com/8MyBvDP.png" alt="drawing" width="20"/>

1. Shortcuts 
1. Alfred - review  
1. Evernote 
1. workflowy.com 


## workflow 

* **截图**： 包括电脑和手机，条件是值得复习和深入了解的知识点
* **归档**：Shortcuts & Alfred 
	* 每天早上使用App: 「Shortcuts」将手机截图传到特定目录。
	* 然后使用我自己的做的Alfred的「workflow - review」, 将所有传到Evernote, 并打开笔记。
* **记录**: 在evernote中浏览，在「workflowy」中记录所有知识点
* **分类**：对知识点分类
	* 值得系统化的，进一步阅读，归纳
	* To do list

## 操作操作度(10步)

1. **拿**起iPhone
1. 右**滑**屏幕
1. **点击**workflow1
1. **点击**workflow2
1. 跳出Alert窗口，**点击**“Delete”
1. Mac: **快捷键**`option + command + space`唤出Alfred
1. 输入`m,`, 回车`return`: 得到`evernote` 
1. Evernote: 快捷键`shift + return`进入“Present”模式
1. 鼠标**点击**图片: 进入图片模式
1. 开始在workflowy中记录“知识点”

## show me 

<img src="https://i.imgur.com/TdhUSIf.png" alt="shortcuts" width="100"/> <img src="https://i.imgur.com/lywdaP3.png" alt="right" width="20"/>
<img src="https://i.imgur.com/9XqaseO.png" alt="alfred-review" width="100"/>
<img src="https://i.imgur.com/lywdaP3.png" alt="right" width="20"/>
<img src="https://i.imgur.com/2OIL9Zf.jpg" alt="evernote" width="100"/>
<img src="https://i.imgur.com/lywdaP3.png" alt="right" width="20"/>
<img src="https://i.imgur.com/ADELdZ0.jpg" alt="workflowy" width="100"/>

## How 

### Alfred 

![morning routine: review](https://i.imgur.com/5nVzNlV.png)


First step:

* move files in iCloud to Desktop: combine iPhone screenshot and Mac screenshot 
* convert png to jpeg in low quality: to save space 

``` bash 
cd /Users/wangzhixiang/Library/Mobile\ Documents/iCloud~is~workflow~my~workflows/Documents/screenshots
mv *.png /Users/wangzhixiang/Desktop/review
cd /Users/wangzhixiang/Desktop/review
for i in *.png; do sips -s format jpeg -s formatOptions 5 "${i}" --out "${i%png}jpg"; done
rm *.png
exit
```

Second step:

* write `applescript` to send files in `review` to evernote

``` applescript   
on alfred_script(q)
  -- your script here

tell application "Finder"	set fl to files of folder POSIX file "/Users/wangzhixiang/Desktop/review" as alias listend tellset theDate to current dateset today to date string of theDateon theSplit(theString, theDelimiter)	-- save delimiters to restore old settings	set oldDelimiters to AppleScript's text item delimiters	-- set delimiters to delimiter to be used	set AppleScript's text item delimiters to theDelimiter	-- create the array	set theArray to every text item of theString	-- restore the old setting	set AppleScript's text item delimiters to oldDelimiters	-- return the result	return theArrayend theSplittell application "Finder"	set NoOfFiles to count of (files of folder POSIX file "/Users/wangzhixiang/Desktop/review")end telltell application id "com.evernote.evernote"	set note1 to create note title today & " 🎟 " & NoOfFiles & " Cards" with text "知识卡片🎟-路标★&焦点❶-一生所学(术语&人名&反常识)" notebook "N1 - 浇水集1 - 正反卡片⚡️"	tell note1 to append text " "			repeat with f in fl		tell note1 to append attachment f				-- get the time of screenshot		set temp to f as string		set myTestString to temp		set myArray to my theSplit(myTestString, " ")		set choice to item 6 of myArray		tell note1 to append text choice		tell note1 to append text "⬆️"			end repeat		open note window with note1	-- delay NoOfFiles: no need 	NoOfFiles		tell application "Terminal"		do script "trash -v /Users/wangzhixiang/Desktop/review/*"
		do script "exit"	end tell	end tell

end alfred_script
-- -----------------------
-- reference
-- https://dev.evernote.com/doc/articles/applescript.php
-- http://www.documentsnap.com/evernote-mac-import-folder/
-- http://macscripter.net/viewtopic.php?id=27926 (count the number of files)
```



## log 

- 2018.10.28: 
	- 把 rm 改成 `trash`, 以备意外，可以回复。
	- 完成一键操作：files to evernote. 过程试图用javascript 取代 applescript，但是这是低频事件，提前优化，是一个错误策略。
