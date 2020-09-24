# Anki 

> 以知识点为单位的卡片

## Why?

从大一就听说这个软件，但一直不知道好在哪里。在准备 [system-design](https://github.com/donnemartin/system-design-primer)，介绍写着 

> Includes Anki flashcards.

既然那么多人推荐，那就系统了解一下这个程序员们(≈可编程)也喜欢的工具。

- **核心**稳定，**扩展**繁荣: 全平台支持，高度自定义
- **问答**知识的**记忆面包**: 构建自己的`{key: val}`知识库，实现`O(1)`时间读取知识


## How?

* 用于记忆已经**理解**的东西
* 在拥有**知识地图**后打磨细节

### workflow 

- 每日@recap，把新学习的知道放到anki中。

### Principle

- Anki只放自己**已经理解**的内容

### Tutorial

- [How I Learn Everything : Anki Tutorial](https://www.youtube.com/watch?v=5urUZUWoTLo&t=946s) 
- [13 Steps to Better ANKI Flashcards | Part 1/2](https://www.youtube.com/watch?v=AbvaITy3oeQ)
	*   1) Keep Your Decks **Simple**
	*   2) First **Understand**, Then Memorize
	*   3) Lay the **Foundations** First
	*   4) Follow the **Minimum** Information Principle
	*   5) **Cloze** Deletions Are Your Best Friend
	*   6) Use **Images**, Photos, & Figures

### 组合使用

- [Anki x Kindle](https://zhuanlan.zhihu.com/p/37079582) 
- [Anki x MarginNote](https://zhuanlan.zhihu.com/p/34512119)
- [Anki x Youtube](https://zhuanlan.zhihu.com/p/40037096)
	- [youtube2Anki](https://github.com/dobladov/youtube2Anki): allows to download the transcript of a YouTube video to a csv that can be imported into Anki or directly send the cards to Anki using AnkiConnect, allowing to use the original audio/video of the current sentence and without having to download the original media. 
- [Anki x workflow](https://zhuanlan.zhihu.com/p/47025287)
- [Aiki x Web Query](https://zhuanlan.zhihu.com/p/33792983)
- [Aiki x Chrome extension](?): Anki划词助手
- [Anki x sub2srs](?): 学习电影


## What?

> Anki is a free and open-source spaced repetition flashcard program. "Anki" (暗記) is the Japanese word for "memorization".
> 
> by [wiki](https://www.wikiwand.com/en/Anki_(software))


Anki can be summed up with two bullets:

- **Questions & Answers**: Anki presents you with a question -- be it a fill-in-the-blank，a definition, or a standard quesiton-marked sentense —— and your job is to recall the correct answer.
- **Scheduling**: Based on how difficult or easy it was to recall the answer to the question, Anki determines the best amount of time to wait before asking you the same question again, thereby strengthening the memory at just the right moment. 

### My wiki Strusture 

- 2019-design 
- @map
- @project
- @recap
- cornerstone
	- cs/10-testing
	- cs/11-management
	- cs/18--BQ
	- cs/18--algo
- cs/02
- cs/19
- cs4 

### Adds-on

- review heatmap

### tool

- [Anki Quick Adder](https://chrome.google.com/webstore/detail/anki-quick-adder/gpbcbbajoagdgnokieocaplbhkiidmmb): to create anki cards directly from Google Chrome

### Concept 

* 按钮当中的“数”: **20 + 5 + 100**
	* 1 新卡片未学习       
	* 2 点击重来或者犹豫后正在循环运行中        
	* 3 以前学过现在待学习

	
Editing and More

- **Bury Card / Note**: Hides a card or all of the note’s cards from review **until the next day**. This is useful if you cannot answer the card at the moment or you want to come back to it another time.
- **Suspend Card / Note**: Hides a card or all of the note’s cards from review **until they are manually unsuspended**.  This is useful if you want to avoid reviewing the note **for some time**, but don’t want to delete it.


## When?

### When to use it?

- 系统概念
- 知识点记忆
- Anki适合所有终身学习的人

### When not to use it?

- 对于想要短期备考，快速提高词汇量的人来说，anki确实被神话了，使用效果肯定不如某些单词软件。
- 甚至觉得不适合**初学者**学语言。因为语言核心在于用。例子 [2+ Years of Anki and the (Near) Impossibility of Learning Languages](https://www.dannycrichton.com/2016/05/15/the-near-impossibility-of-learning-languages/)
- 在理解概念之前，去重复记忆。(painful and useless)

## Q&A

## More 

- [How to Study Effectively with Flash Cards - College Info Geek](https://www.youtube.com/watch?v=mzCEJVtED0U)
- [How To Do 500+ Anki Cards PER Hour!](https://www.youtube.com/watch?v=_ER9NQcwKm8): When you are familiar enough with what you've learned
- [Flashcard App Showdown: Quizlet vs. Anki vs. Memrise](http://lexplorers.com/flashcard-app-showdown-quizlet-vs-anki-vs-memrise/)
- [List of flashcard software](https://www.wikiwand.com/en/List_of_flashcard_software)
- [anki是否被神化了？](https://www.zhihu.com/question/57569577)
- [Anki——近乎完美的神器](https://zhuanlan.zhihu.com/-anki)
- [Anki电脑端上值得推荐的十个插件](https://zhuanlan.zhihu.com/p/24650483)
- [awesome-anki](https://github.com/tianshanghong/awesome-anki)
- [Study with Me + Anki Flashcard Method - Ali Abdaal](https://www.youtube.com/watch?v=W-EpiaPcgTk): @recap的灵感来源，把每日所学放入到anki中。
- [Anki学习笔记](https://www.yuque.com/purequant/anki)