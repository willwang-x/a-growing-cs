# 看美剧学英语 


## Todo 

1. [x] 完成[src2md](https://gist.github.com/01f63bfaca2bfa32eb5288053235a7de#file-src2md-py): 字幕格式生成markdown格式，便于清晰的网页浏览，配合chrome插件[Readlang Web Reader
	- [x] 对markdown中的生词(知识点)进行高亮。 如 `知识点` 。
	- [x] 将同一句话进行合并。便于之后整句调取。  
	- [ ] 配合[Readlang](https://chrome.google.com/webstore/detail/readlang-web-reader/odpdkefpnfejbfnmdilmfhephfffmfoh) 使用。 
2. [x] 完成单词库的检查，即设计一个txt, 用来查找新的src中有没有生词。
	- 本质是设计一个可“持久化”的hashmap
	- [ ] 这个阶段只完成最最简单的单词, 格式如 `{magnate:2} `, 单词：遇到的次数。之后可以加入，词组，句型等。(知识点)
	- [ ] 在后者，需要使用一个**数据库**来完成这些事情。
	- [ ] 可能的要求：单词：出现此单词的句子
3. [ ] 1368个过滤器，便于加深对1368个单词的深化理解
	- [x] word + table(文中出现此单词的句子), [效果](https://i.imgur.com/xeqBKUm.jpg)
	- 有没有办法句型匹配？习语拼配。
	- e.g. push + push的说明 + 相关句子
	- e.g. push的习语，以push为核心周边词汇。
	- e.g. push的相关统计。push: 2, shove(push forcefully): 3; push about: 2; 
4. [x]导出到[quizlet](https://quizlet.com/zh-cn )， 自动化处理，加速复习的方便。 [效果](https://quizlet.com/353489683/flashcards)
5. [x] 生词本，统计未遇到的生词的，"word count"
6. 形成完成的《看美剧学英语》的学习流程，参考已有的经验分享。
7. [] 优化笔记本
	- [x] 增加summary 模块， [效果](https://i.imgur.com/HDeF9LR.png)
	- [x] 增加词语的归属 模块, [效果](https://i.imgur.com/JRp4M4O.png)
	- [ ] 增加词语的发音
 
## Version 


* 2018.12.29, 0.1
	* [x] 初步更新了句型识别，导出到md。[句型笔记效果](https://i.imgur.com/VtskjJc.png) 
	* [x] 生成 sentence-pattern.txt, 收到写入。需要改进。 
	*  [ ] 优化代码结构，数据结构和算法，self.sentence_map, self.sentence_exmaple, to_sentence()


## 数据库设计

### 技术选型

**Solution 1: 原始方法 file.txt as hashtable** 

```
word1 count1
word2 count2
``` 

读取 -> 建立HashTable:O(n) -> 使用:O(1) ->  回写: O(n)

* 优点：实现方便
* 缺点：
	* 每次使用和会写都需要 O(n) where n = len(hash_table)
	* 数据量大之后的本地hashtable不够用，拓展性差。


**solution 2: MySQL** 

* 优点：容易学 
* 缺点：当一个key需要补充内容，拓展性差。

**solution 3: NoSQL, e.g. MongoDB** 

* 优点：灵活性高，便于之后加入新的条目。
* 缺点：需要学习。
 
## 代码

 ![notes_generators](https://i.imgur.com/8WONLro.png)