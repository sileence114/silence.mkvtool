# silence.mkvtool
一个调用ffmpeg以完成批量MKV转码任务的小工具。

A gadget that calls ffmpeg to complete batch MKV transcoding tasks.

分离MKV文件中的字幕轨道、字体附件，并将MKV的默认视频轨道与音频轨道封装为MP4,并保留章节信息。
# 食用（熟食）：
```shell
> silence.mkvtool.exe
```
若有需要请使用
```shell
> silence.mkvtool.exe -s
or
> silence.mkvtool.exe --setting
```
领取设置文件一份。请将其命名为“setting.py”并放入命令行当前目录。否则将以默认设置加载。

# 设置ffmpeg位置：
第一次使用请将ffmpeg.exe放入命令行当前目录下，或在setting.py中设置其路径ffmpegLocation(绝对路径)。

若位置不正确将直接退出。

ffmpeg下载:[ffmpeg](https://ffmpeg.org/)[(on GitHub)](https://github.com/FFmpeg/FFmpeg/)

# 命令行参数：
若不想使用设置文件更改设置，可以追加命令行参数：
```
'-s' '--setting'   : 生成设置模板
'-t' '--template'  : 生成任务模板
---以下选项优先级高于设置文件---
'-m' '--multiple'  : 设置模式为"multiple"
'-c' '--custom'    : 设置模式为"custom"
(注：以上两个若同时加入后者覆盖前者)
'-e' '--extra'     : 禁用附件单独保存
'-h' '--hitokoto'  : 禁用Hitokoto
'-o' '--overWrite' : 关闭文件覆盖
'-l' '--writelog'  : 禁用日志
```

# 模式
## 单文件模式(默认)：
```py
mode = 'single'
```
当前模式下，运行会弹出文件选择窗口与文件夹选择窗口：请在第一次弹窗选择需要处理的MKV视频文件，第二次选择输出目录，不选将与原视频在同一目录下。

例：

输入："E:\Documents\Desktop\Fate／kaleid liner\Fate／kaleid liner プリズマ☆イリヤ(第1期) 第10話(終)「Kaleidoscope」(1920x1080 HEVC 10bit FLACx2 softSub(chi+eng) chap).mkv"

输出："E:\Documents\Desktop\myVideo\"

则输出的文件是"E:\Documents\Desktop\myVideo\Fate／kaleid liner プリズマ☆イリヤ(第1期) 第10話(終)「Kaleidoscope」(1920x1080 HEVC 10bit FLACx2 softSub(chi+eng) chap).???"

视频文件、字幕文件都将以此为文件名。

* 若extraAttachmentFloder = True，则附件保存在"E:\Documents\Desktop\myVideo\Fate／kaleid liner プリズマ☆イリヤ(第1期) 第10話(終)「Kaleidoscope」(1920x1080 HEVC 10bit FLACx2 softSub(chi+eng) chap).attachments\"文件夹下。

* 若输出文件夹没有选择，则输出到"E:\Documents\Desktop\Fate／kaleid liner\"文件夹下。

## 多文件模式：
```py
> mode = 'multiple'
```
或
```shell
> silence.mkvtool.exe -m
or
> silence.mkvtool.exe --multiple
```
当前模式下，运行会弹出两次文件夹选择窗口：请在第一次弹窗选择需要处理的MKV视频所在的文件夹，第二次选择输出文件夹，不选将与输入文件夹在同一目录下。

例：

输入："E:\Documents\Desktop\Fate／kaleid liner\"

输出："E:\Documents\Desktop\myVideo\"


则输出的文件会在"E:\Documents\Desktop\myVideo\Fate／kaleid liner.treated"文件夹下，具体文件结构与原始目录相同。

* 若extraAttachmentFloder = True，则附件保存在"E:\Documents\Desktop\myVideo\[Attachments]\文件夹下。

* 若输出文件夹没有选择，则输出到"E:\Documents\Desktop\Fate／kaleid liner.treated\"文件夹下。

## 自定义模式：
```py
mode = 'custom'
```
或
```shell
> silence.mkvtool.exe -c
or
> silence.mkvtool.exe --custom
```
当前模式下，需要提前准备队列任务csv文件,运行时选择csv文件，将根据队列依次完成任务。

使用
```shell
> silence.mkvtool.exe -t
or
> silence.mkvtool.exe --template
```
领取设置文件一份。

例：
```csv
输入,输出
(输入文件或文件夹路径),(选填，输出路径)
E:\Documents\Desktop\Fate Stay Night[UBW],
E:\Documents\Desktop\Fate stay night[HF] I.presage flower.mkv,E:\Documents\Desktop\
E:\Documents\Desktop\我是来捣乱的.jpg,
```
按输入文件类型分别进入上文的两张模式，输出位置参考上文。

未能加入任务队列的除模板第一行、模板第二行和空行外都将在任务结束后提示，请注意查看。
```csv
输入,输出
(输入文件或文件夹路径),(选填，输出路径)
,
```
* 模板第一行和第二行可以删去，请尽量使用表格编辑软件编辑csv，以免文件名中有半角逗号、半角双引号。

## [Hitokoto](https://api.imjad.cn/hitokoto.md)：
不喜欢或网络环境较差可以关闭
```py
Hitokoto = False
```
或
```shell
> silence.mkvtool.exe -h
or
> silence.mkvtool.exe --hitokoto
```
(该功能是学习urllib模块时的副产物。)

# 字体附件与字幕轨道
因资料查找不够充足，故将常见的字体后缀名、MKV封装的字幕类型封装入程序，若有需要请另行在setting.py中补充。
```py
# 字体文件后缀名（错删少补）
# 格式：['后缀名A', '后缀名B']
# 请将常见文件格式前置以提高运行效率
fontFiles = [
    'ttf', 'ttc', 'otf', 'pfa', 'dfont', 'vlw', 'txf', 'woff',
    'vnf', 'ytf', 'cha', 'gdr', 'pfb', 'tte', 'afm', 'pfr',
    'xfn', 'gxf', 't65', 'sfd', 'fon', 'mxf', 'pfm', 'vfb',
    'gf', 'amfm', 'acfm', 'xft', 'pmt', 'f3f', 'chr', 'etx',
    'pk', 'mcf', 'suit', 'fnt', 'ffil', 'compositefont', 
    'euf', 'sfp', 'mf', 'lwfn', 'nftr', 'abf', 'eot', 'fot',
    'bdf', 'tfm'
]

# 字幕格式与后缀名对照表
# 格式：{'A字幕文件类型': 'A字幕文件后缀名', 'B字幕文件类型': 'B字幕文件后缀名', }
subtitleSuffixDict = {
    'ass': 'ass',
    'subrip': 'srt',
    'hdmv_pgs_subtitle': 'sup'
}
```
其中：字幕文件类型使用ffmpeg查看
```shell
> ffmpeg -i Fate stay night[HF] I.presage flower.mkv
......
Stream #0:2(chi): Subtitle: hdmv_pgs_subtitle (default)
......
Stream #0:3(eng): Subtitle: ass
......
Stream #0:4(jpn): Subtitle: subrip
......
```
如：

流 #0:轨道4(日语): 字幕： subrip

其中'subrip'为字幕类型，对应的后缀名为'.srt'

# 食用（生吃）：
```shell
> python silence.mkvtool.py[ argv]
```

## 所需模块：
```py
unicodedata
subprocess
tkinter
urllib
time
math
json
csv
sys
os
```

# 鸣谢：
感谢以下项目提供的支持
- 视频转码与轨道抽取：[ffmpeg](https://ffmpeg.org/)[(GitHub)](https://github.com/FFmpeg/FFmpeg/)
- Python脚本文件打包：[pyinstaller](http://www.pyinstaller.org/)[(GitHub)](https://github.com/pyinstaller/pyinstaller)
- [一言(Hitokoto/ヒトコト)](https://api.imjad.cn/hitokoto.md)API：[journey.ad](https://imjad.cn/)

