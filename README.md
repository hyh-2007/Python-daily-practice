# Python 每日练习

每天保存一份学习笔记和一份 Python 代码，按练习天数分目录，方便复习。

## 目录结构

```text
Python-daily-practice/
├── day01/
│   ├── day.md          # Day1 学习笔记
│   └── day.py          # Day1 三道题的参考代码
├── templates/
│   ├── day.md          # 每日笔记模板
│   └── day.py          # 每日代码模板
├── new_day.py          # 自动创建下一天的目录和两个文件
├── .gitignore
└── README.md
```

- [Day1：列表循环练习笔记](day01/day.md)
- [Day1：三道题参考代码](day01/day.py)

Day1 的笔记来自原来的 `day.md/day.md.txt`，已修正 Markdown 代码块。原来的代码文本文档为空，现按笔记题目补充参考代码。

## 每天怎么记录

1. 在本地仓库文件夹中打开终端，运行：

   ```powershell
   python new_day.py
   ```

   程序会依次创建 `day02`、`day03` 等目录，每个目录都有真正的 `day.md` 和 `day.py` 文件。已有文件不会被覆盖；目录中的日期取电脑当天日期。

2. 用 VS Code 或其他文本编辑器打开当天的两个文件，填写学习笔记、代码和运行结果。
3. 运行当天代码，例如：

   ```powershell
   python day02/day.py
   ```

4. 按下面的方法上传，最后在 GitHub 上检查两个文件内容。

## 上传方法一：网页上传

适合刚开始使用 GitHub 时操作。

1. 打开 [仓库首页](https://github.com/hyh-2007/Python-daily-practice)。
2. 点击 **Add file → Upload files**。
3. 把当天的整个目录（例如 `day02`）拖进页面，一起上传两个文件，保留目录层级。
4. 等两个文件都出现在上传列表后，填写提交说明，例如 `Day2：列表练习与学习笔记`，然后点击 **Commit changes**。
5. 回到仓库，进入 `day02`，确认 `day.md` 和 `day.py` 都存在且内容正确。

## 上传方法二：Git 命令

在本地仓库文件夹里执行；第一次推送时按 GitHub 官方页面提示登录。以下以 Day2 为例，之后把目录名和提交说明换成当天的即可。

```powershell
git pull --ff-only origin main
git add day02/day.md day02/day.py
git commit -m "Day2: add practice notes and code"
git push origin main
```

建议日常固定使用一种上传方法。如果也在网页上改了文件，先用 `git pull --ff-only origin main` 同步；若提示本地文件有未提交修改，先保存并提交自己的修改，再同步。

## 文件名注意事项

- 在资源管理器里打开“查看 → 显示 → 文件扩展名”，确认文件名不是 `day.md.txt` 或 `day.py.txt`。
- `day01`、`day02` 是文件夹；`day.md`、`day.py` 是放在里面的文件。
- 使用 UTF-8 编码保存中文。
- `git push` 成功后仍要在 GitHub 页面核对一次；单把文件拖到上传页面还没有保存到仓库。
