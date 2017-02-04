# 每天一篇 SwiftGG 译文到新浪微博

用 Python 模拟 HTTP 操作，实现微博登录，获取 SwiftGG 当日的文章，发送到微博。

## 特别感谢

基于 [chaolongzhang](https://github.com/chaolongzhang) 的 [sinaWeibo](https://github.com/chaolongzhang/sinaWeibo) 实现。

## 使用

1. 修改配置文件 `config.py`，把微博账号和密码改为你自己的，还可以设置发送时间（默认是30分钟一次）。
2. 在 `TextFactory.py` 可以设置微博内容生成规则，也可以使用默认的规则。
3. 运行 `main.py`，`python main.py`。

## 注意
1. 该代码 [requests](http://docs.python-requests.org/en/master/)、[rsa](https://pypi.python.org/pypi/rsa) 和 [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)，没有安装的话需要先安装：

```
pip install rsa
pip install requests
pip install beautifulsoup4
```

2. 如果你的微博登录时要输入验证码，该代码是登录不成功的。

## License

SwiftGGSinaWeibo is published under GNU GPLv3 License. See the LICENSE file for more.
