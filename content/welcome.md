Title: Welcome
Date: 2014-01-12 11:20
Category: Class Core
Tags: R, class, admin
Slug: welcome
Author: Christopher Grainger
Summary: Welcome to the class.

Welcome to the class. Over the next eleven weeks or so, you will learn how to use the R programming language for data analysis. My goal is to enable you to use R for your dissertation and to give you a skill you can use on the job market. As I will explain in the first class, this means more than just teaching you the R language. In this introductory post, I'll give you a few tips for getting started. Just to be clear, these things are foundational and required for the course.

Most of you have never used a programming language before, and it can be daunting. It's easy to fall into bad habits or to be frustrated or confused when first learning how to code. This is especially true when your first programming language is R. For reasons that will become clear in the coming weeks, it's very tempting to use R as a glorified 'command line interface' (CLI). And certainly we *will* use R in that way, but only some of the time. Most of the time we will be focusing on producing fully reproduceable, idiomatic R code.[^fn-1]

One of the most important things you can do at the beginning of this course is to get used to writing code in 'plain text' files.[^fn-2] Set up a directory somewhere on your computer for use with this course (for reasons that will become clear later, don't set this up on Dropbox or in any other cloud folder). In that folder, you will save your code files, which will be in the '.R' file format.

Over the next few days I will put up a post on how to get started with [GitHub](https://github.com). GitHub is a web-based service for hosting code and developing software using the [git](http://en.wikipedia.org/wiki/Git_(software)) revision control system. What this allows you to do is maintain a history of all of the edits that you've made to your code so you can always go back and fix it. It also allows us to work collaboratively, which will be part of the class. For example, I might ask you to 'fork' a 'repository' and make some changes to code. I will then be able to see your code and provide feedback. (Don't worry if this all sounds a bit confusing. It's very easy and I don't expect you to understand it just yet.)

Until then, I'll just ask that you install R on your computer. You can get it [here](http://cran.r-project.org) under 'Download and Install R'.

All of this will be made easier by the use of [RStudio](http://www.rstudio.com), which is an 'integrated development environment' (IDE) for R. Please install that as well. It will make your life easier, I promise! And I will teach everything in this course within RStudio, while also making overt what is going on 'behind the scenes' in terms of file management, etc.

Don't worry too much about using R on your own computer before the class begins. If you'd like to play around, you're welcome to do so. For example, R can work like a calculator: `1 + 1` will return `2`. There are a couple of resources on the web for trying out R. These only take an hour or two and they're definitely worth a go.

- [Code School: Try R](http://tryr.codeschool.com)
- [Data Camp: Introduction to R](https://www.datacamp.com/courses/introduction-to-r)

Just one last thing: comments are open on this site. Remember that they are public (so be smart about what you post), but they are a good way to get help or have discussion about the topics covered in the class.

I look forward to seeing you all next Wednesday.

[^fn-1]: Writing 'idiomatic' code means not just writing code that works, but code that follows best practices in terms of both understandability in the R community and optimising the performance of the code for R specifically. R is a bit of a funny language, especially since the vast majority of R 'users' don't see themselves as R 'programmers'. We'll be dismissing that false dichotomy. I'll post more on 'idiomatic R' as this course goes on.

[^fn-2]: If you are not familiar with plain text, a great primer is [here](http://www.linfo.org/plain_text.html).