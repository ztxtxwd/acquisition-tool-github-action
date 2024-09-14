# 网页监控项目

这个项目使用 GitHub Actions 每小时从指定 URL 下载网页,并与之前的最新版本进行比较。如果检测到变化,新版本将被保存并推送到远程仓库。

## 工作原理

1. GitHub Actions 工作流每小时触发一次。
2. Python 脚本下载指定网页的内容。
3. 将新下载的内容与最近保存的版本进行比较。
4. 如果检测到变化,新版本将被保存为一个新文件。
5. 所有更改都会被提交并推送到 GitHub 仓库。

## 配置

要监控不同的网页,请在 `download_and_compare.py` 文件中修改 `URL` 变量。

## 手动触发

您可以通过 GitHub 界面手动触发工作流来立即运行检查。
