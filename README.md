这个仓库记录了我第一次在云服务器上动手学习软件测试的全过程。
2025-10-16 
1.  在阿里云服务器上创建了一个极简的`calculator.py` 程序。
2.  使用 `pytest` 框架编写了`test_calculator.py` 来进行单元测试。
3.  成功运行了测试，看到了 `1 passed`的成功结果。
4.  通过故意改错代码，观察到了 `1 failed`的失败结果，并学会了阅读 `pytest`的错误报告来定位问题。
5.  修复了代码，让测试重新通过。
6.最后，实践了TDD（测试驱动开发）
      流程：先为新的`subtract`功能编写测试，在测试失败的情况
	下，再编写功能代码让测试通过。
这是我测试迈出的第一步，从初学者到这有些难，遇到了很多问题，我也是憋着一股劲，自己慢慢学，学校教的很基础，我深知凭着那些东西找工作很难，这算是进阶吧。
系统把问题反馈给我，我学着怎么看懂错误报告，然后去修改，重新测试，然后通过测试，这是非常有成就感的。期待我之后的学习成果。

##下面是基础命令的相关内容

将代码推送到 GitHub
1. 确保你当前在项目文件夹里
如果你不确定，可以执行 ls，应该能看到 
  calculator.py 和 test_calculator.py
2. 初始化 Git 仓库  git init 
3. 将所有文件添加到暂存区  ‘git add .’
4. 创建你的第一个提交记录
git commit -m "Initial commit: Add calculator and 
  basic tests"
	#m是message的缩写，“ 。。。”里的是你对这次提交的备注信息，也可以不写
5. 将本地仓库与远程 GitHub 仓库关联
   仓库页面上复制 HTTPS 地址
   格式是：https://github.com/你的用户名/你的仓库名.git
   实际命令：git remote add origin https://github.com/YOUR_USERNAME/python-testing-practice.git
6. (推荐) 将默认分支名从 master 改为 main  --》 git branch -M main
7. 推送你的代码到 GitHub！
	 git push -u origin main
8. 执行最后一步 `git push` 时，终端会提示你输入：
   * Username for 'https://github.com': 输入你的 GitHub 用户名，然后按
     Enter。
   * Password for 'https://YOUR_USERNAME@github.com':
     输入密码时，请粘贴你刚才生成的个人访问令牌 (PAT)。注意：粘贴和输入
     时屏幕上不会显示任何字符，这是正常的，输完直接按 Enter 即可。
     
  成功后，刷新你的 GitHub 仓库页面，就能看到 calculator.py 和
  test_calculator.py 已经上传上去了！

创建并编辑 README.md 文件：
1     nano README.md
2. 在 nano 编辑器里，输入后保存并退出 (Ctrl + O, Enter, Ctrl + X)。
3. 将这个新文件也推送到 GitHub：
    添加 README.md 文件  git add README.md
4. # 提交这个改动  git commit -m "Add README with learning summary"
6 # 推送到 GitHub --》 git push origin main
  （这次推送可能不需要再输入用户名和令牌，git 会缓存一小段时间）。


养成清理垃圾的习惯还是很不错的哈哈 
1. 清理 apt 的软件包缓存
	这是最常用，也是最能有效释放空间的一步。当你用 apt
  安装软件时，它会下载软件包（.deb
  文件）并保存在本地作为缓存。安装完成后，这些缓存文件基本就没用了。
   1 # 这个命令会安全地删除所有已下载的软件包缓存
   2 # 它不会卸载你已安装的任何软件，非常安全
   3 sudo apt clean
2. 卸载不再需要的依赖包
  有时候，你安装一个软件A，它会自动安装依赖软件B和C。但当你卸载A之后
  ，B和C可能还留在系统里，占着空间。这个命令就是用来卸载这些“孤儿”依
  赖包的。sudo apt autoremove
     这个命令会自动查找并卸载那些不再被任何软件需要的依赖
     包，执行时，它会列出将要被删除的包，并询问你是否继续（Y/
     n），确认无误后按 Y 即可
  这个命令通常也能帮你自动删除不再使用的旧版本 Linux
  内核，也能释放不少空间。
 3. 清理 systemd 的日志文件（可选）
  现代 Linux 系统使用 journald
  来管理日志。日志文件可能会变得很大。我们可以限制一下它的大小。
   1 # 查看当前日志占用了多少空间
     journalctl --disk-usage
    2 将日志文件大小限制在 100M 
     以内，它会自动删除旧的日志
     sudo journalctl --vacuum-size=100M

  ---

  推荐的“一键清理”组合命令

  在日常维护中，可以使用下面这个组合命令，它会更新系统、清理缓存
  、并移除孤儿依赖，一气呵成。

   1 sudo apt update && sudo apt upgrade -y && sudo apt
     clean && sudo apt autoremove -y

  命令分解：
   * sudo apt update: 刷新可用的软件包列表。
   * sudo apt upgrade -y: 升级所有已安装的软件包到最新版本（-y
     表示自动回答“是”）。保持系统更新是安全的第一步。
   * sudo apt clean: 执行我们上面讲的第一步，清理缓存。
   * sudo apt autoremove -y: 执行第二步，自动移除不再需要的包。
