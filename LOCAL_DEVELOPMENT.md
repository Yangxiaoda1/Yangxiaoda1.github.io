# 本地调试

## 中英文审查链接

- 中文版：`http://127.0.0.1:4000/`，源文件 `_pages/about.md`。
- 英文版：`http://127.0.0.1:4000/en/`，源文件 `_pages/about-en.md`。

顶部导航提供 English / 中文切换（小屏幕可能位于折叠菜单中）。
两版共用照片、论文图片、邮箱、微信及引用量缓存；正文分别维护。

## 环境

项目使用 `Gemfile.lock` 固定的 GitHub Pages / Jekyll 依赖。
当前机器已有 Ruby 2.7.8、RubyGems 3.1.6、Bundler 2.3.24、GCC 11.2.1 和 GNU Make 4.3。
此环境用于兼容现有模板的本地预览，不要作为公网生产服务器。

```bash
cd /apdcephfs_gy2/share_302507476/xiaodayang/zh-cn
export http_proxy=http://star-proxy.oa.com:3128
export https_proxy=http://star-proxy.oa.com:3128
export no_proxy="${no_proxy:+${no_proxy},}localhost,127.0.0.1"

# 首次安装；之后依赖已齐全时无需重复
bundle config set --local path vendor/bundle
bundle install

# 前台启动，Ctrl+C 停止
bash run_server.sh
```

打开 `http://127.0.0.1:4000`。LiveReload 使用 `35729` 端口。
脚本默认开启轮询监听，以适配当前共享文件系统。
修改 Markdown、样式或模板后自动重建；修改 `_config.yml` 后需重启服务。
依赖已经安装好时，启动和浏览本地页面不需要代理。

本次配置已将服务启动到后台，日志为 `log/jekyll.log`，PID 记录在 `log/jekyll.pid`。
如果已有服务占用端口，不要重复启动：

```bash
# 查看日志
tail -f log/jekyll.log
# 停止本次后台服务
kill "$(cat log/jekyll.pid)"
# 之后可以重新在前台启动
bash run_server.sh
```

已验证首页、照片、CSS、JavaScript 返回 200，桌面与手机视口可正常浏览，
LiveReload WebSocket 连接和源码修改后的自动刷新正常；原始简历访问返回 404。
浏览器验证未发现 JavaScript 异常或资源请求失败。

如 Gem 索引因网络问题不可访问，但 `vendor/cache` 中已有所需 Gem 包：

```bash
bundle install --local
```

## 在自己电脑上访问远程开发机

如果命令运行在远程服务器，电脑浏览器中的 `127.0.0.1` 不是远程服务器。
在 VS Code / CodeBuddy 的“端口”面板同时转发 `4000` 和 `35729`，
并尽量保持本地与远程端口号一致，然后访问本地的 `http://127.0.0.1:4000`。

也可在自己电脑终端建立 SSH 隧道（替换用户名及服务器地址）：

```bash
ssh -N -L 4000:127.0.0.1:4000 -L 35729:127.0.0.1:35729 用户名@服务器地址
```

不要为了远程访问而直接将开发服务暴露到公网。

## 常改文件

- `_pages/about.md`：简介、教育、实习、项目、论文和荣誉。
- `_config.yml`：姓名、邮箱、照片、Scholar 链接等。
- `_data/navigation.yml`：顶部导航。
- `images/photo.jpg`：展示照片，来源为用户提供的 `my_information/photo.jpg`。
- `assets/css/main.scss` 与 `_sass/`：页面样式。

简历中的联系电话和原始 PDF 不公开；`my_information/` 已从构建及 Git 新增文件中排除。
主页公开联系方式按用户确认设置为邮箱 `1992426088@qq.com`、微信 `Flying_penguin_T`。
论文状态根据简历及用户确认整理，没有推测未提供的年份。引用量使用带更新时间的本地缓存，不将缓存称为实时数据。
模板作者的 GitHub、ORCID、ResearchGate、站点验证信息及引用数据请求已移除。

## Scholar 引用量

主页和侧栏直接展示引用量，不显示更新日期；抓取时间仍保存在缓存中。徽章采用本地 HTML/CSS 渲染，
不依赖外部图片服务，数据来自 `_data/scholar.json`。
使用已配置的网络代理更新：

```bash
python3 google_scholar_crawler/update_local.py
```

脚本仅使用 Python 标准库，从指定 Scholar 主页提取总引用数，并写入抓取时间。
更新后 Jekyll 会自动重建；断网、限流或验证码导致更新失败时保留上一次成功数据。
当前没有配置后台定时更新，发布后如需自动刷新，可定时执行此脚本并重新构建网站。
模板的旧 Scholar 工作流已移除，避免无效抓取和强制推送。更新缓存并推送后会自动部署。

## 提交与发布

当前 origin 为 `https://github.com/Yangxiaoda1/Yangxiaoda1.github.io.git`，
模板仓库保留为 `template` remote。GitHub Actions 在推送 `main` 后自动构建并发布 Pages。

正式网址：
- 中文：`https://yangxiaoda1.github.io/`
- 英文：`https://yangxiaoda1.github.io/en/`

```bash
git remote -v
git config --local user.name "Yangxiaoda1"
git config --local user.email "1992426088@qq.com"
git diff --check
git diff
git status --short
# 检查后选择性添加；不要提交 vendor、日志或原始简历
git add _pages/about.md _pages/about-en.md
git commit -m "Update bilingual homepage"
git push origin main
```

认证由本机凭据管理器或 SSH 提供，不要将 Token 放在文件、提交或 remote URL 中。
`_config.yml` 已设置正式域名和空 `baseurl`，导航与资源路径使用 `relative_url`。
