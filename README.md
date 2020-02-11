# jdlingyu-crawler
绝对领域网站爬虫

需安装selenium 配合 google chrome 版本74，可以百度查询如何安装。该项目暂时针对会使用python的童鞋，后续可以添加依赖。

咳咳，网上图片太多，必须联网才能看，多不方便(*/ω＼*)，刚好会一点爬虫，想着把图片下载打包就完美了ε=ε=ε=(~￣▽￣)~

针对jdlingyu.com的图片，购买了会员。检查了robots.txt文件，应该没有违反网站规定，而且也没有多线程，不会对网站产生大负荷（绝对不是多线程运用不熟练的原因。。  (○｀ 3′○) ）

方案很简单，配合selenium和chrome 进行登陆验证和按钮点击，如果用requests 会比较麻烦。针对图片下载则使用requests 库添加header,不添加的话不知道会不会有问题。使用前需要在py文件内添加自己的账号和密码

目前爬取了cos套图（百度云链接），自拍区（图片），特点区（图片）。

通过搜索爬取特定内容是被网站禁止了，虽然可以弄，但是还是小心一点，毕竟别人做网站越不容易。网站的反爬措施应该是没有的。

![image](https://github.com/citsrevo/jdlingyu-crawler/blob/master/1.png)
![image](https://github.com/citsrevo/jdlingyu-crawler/blob/master/2.png)

