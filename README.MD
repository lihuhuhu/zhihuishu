## star一下吧
`gemini Gpt 回答最新的前50个问题,后面看情况更新`
- [x] 回答所有课程问题
- [ ] 自动提问
- [ ] 用账户登录
- [ ] 过频繁检测
- [ ] 找中文gpt

## 声明
**仅供学习参考,请勿用于其他用途**    

目前只有代理才能使用,回答走的google的gpt

## 关于F12无限debug
采用obfuscator进行混淆，并开启反调试反格式化，检测到就装死,针对在浏览器中替换文件。

## 配置
1. cookie获取(各显神通)
    + 打开这个链接[点击我](https://onlineweb.zhihuishu.com/onlinestuh5)
    + 按F12 点击课程页面的“已完成“,找这个请求queryShareCourseInfo,复制cookie到config中


2. 代理配置(有点严,细节可以看google的文档)
    + 中文节点都不行(HongKang,TW),其他的可以(美国，日本)
    + 可以先去chatgpt_api文件下测试一下


3. 配置文件
   + 本地代理：port = '7897' 修改一下你机场的端口
   + 远程代理：PROXY = {'https': f'ip:{port}', 'http': f'ip:{port}'}替换成你远程的ip

## 运行
```angular2html
pip install -r requirements.txt
```
执行main文件,看到窗口有不断的输出就行

执行次数太多会用验证码弹窗，要手动过


## 交流
[telegram group](https://t.me/+RugHlc2d-g83YWY1)





