# AntaBaka Review Demo

这是 AntaBaka-Review 的演示仓库，用于触发 GitHub Pull Request Webhook，并展示 AI PR Review 评论效果。

项目包含一个简单的计算器模块，方便构造正常修复、风险变更、无意义变更等不同类型的 PR。

具体方法：

1. 克隆测试仓库的 `dev` 分支到本地
```bash
git clone -b dev https://github.com/SakuraMagic225/test-repo.git
```
2. 随意修改仓库中的代码，例如修改 src/calculator.py或补充一个测试文件
3. 提交并推送到 `dev` 分支
```bash
git add .
git commit -m "test: trigger AntaBaka review"
git push origin dev
```
4. 在Github页面中，从 `dev` 分支向 `main` 分支创建 PR
5. 等待约10-30s，即可在PR下看到AntaBaka-Review自动生成的评审评论

> 当然，如果赶时间可以直接去已经关闭了的pr中查看效果，都是我自己测过的。之前的一些pr没有评论，是因为开发阶段的副产物，效果不太好就删除了。
