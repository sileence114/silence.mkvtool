from urllib.request import urlopen
from tkinter import filedialog
import unicodedata
import subprocess
import tkinter
import urllib
import time
import math
import json
import csv
import sys
import os


# 退出
def exitSelf():
    print('''------------
运行已结束。如有问题请Ctrl+A Ctrl+C 将上方内容全选并复制，保存至文本文档，与日志文件一同发给我。
------------
本项目GitHub地址：https://github.com/Preliterate/silence.mkvtool
视频介绍：<这个版本完成时还没有开始录，请等下个版本>
Bilibili个人空间：https://space.bilibili.com/88096135
███████████████████████████████████
█　　　　　　　█　█　█　　██　███　　█　　█　　　　　　　█
█　█████　█　　██　██　　　　　████　█　█████　█
█　█　　　█　█　　█　　　　　█　██　　█　　█　█　　　█　█
█　█　　　█　█████　　█　　　　███　　　█　█　　　█　█
█　█　　　█　██　████　　　　█　█　██　█　█　　　█　█
█　█████　█　　　　█　█　　██　████　█　█████　█
█　　　　　　　█　█　█　█　█　█　█　█　█　█　　　　　　　█
█████████　██　　████　█　　　　　██████████
███　　　█　█　███　　████████　　　　　　██　　　█
███　　█　█████　████　██　　██　█　　████　　█
██　█　　█　　　　███　██　　██████　██　█　　　██
█　██　　██　████　██　█　　　█　█　█　　██　　　　█
██　██　█　　█　█　　█　██　█　　██　　　█　██████
█　　█████　　　　█　█　█　　　　　█　　██　　██　█　█
█　　　　█　　██　█　█　　　　█████　█　　　　　█　　██
██　█　████　　　█　　　███　██　　　███　██　█　█
█　█　　██　██　██　　　█　　　████　█　█　　█　█　█
█　　　　　███　　　█　███　██　　██　　█　█████　█
█　　　　　█　　██　　█　　███　　█　███　████　███
██　　█　　███　██　　　　　█　█　　　　　██　　　　　██
█　██　██　　█　　　　███　　　█　█　██　█　　　█　　█
█　　　████　█████　　　██　　████　█　███　█　█
█　██　　█　　█　██　　　　██　　██　█　█████　　██
█　███　██　█　　████　█　███　　　███　█　　███
█　███　　　　　　　　　　　█　██　　█　　　　　　　██　　█
█████████　　█　　██　██　　█　██　███　█　　　█
█　　　　　　　██　　██　　　　　　　　　█　　█　█　██　██
█　█████　█████　█　　　　██　　██　███　　　　　█
█　█　　　█　█　　█　　██　　██　█　██　　　　　██　　█
█　█　　　█　█　　█　　████　█　　██　　　██　　█　██
█　█　　　█　█　██████　██　███　██　　██　　███
█　█████　██　　██　　　　　██　████　█　█　　███
█　　　　　　　██　　█　　█　█████　　█　　█████　██
███████████████████████████████████
( ↑ ) 用PIL模块折腾了好久的个人空间二维码，你扫的出来么?
(若错乱可以尝试设置控制台字体为新宋体)
------------
现在你可以关闭本窗口。
''')
    os.system('cmd')


# 导入设置文件
try:
    import setting
    extraAttachmentFloder = setting.extraAttachmentFloder
    mode = setting.mode
    Hitokoto = setting.Hitokoto
    ffmpegLocation = setting.ffmpegLocation
    overWrite = setting.overWrite
    writeLog = setting.writeLog
    fontFiles = setting.fontFiles
    subtitleSuffixDict = setting.subtitleSuffixDict
except ModuleNotFoundError:
    print('''------------
未发现设置文件，将按默认设置加载，请将设置文件与本程序置于同一目录。
设置文件模板请在命令行后添加"-s"或"--setting"领取。''')
    extraAttachmentFloder = True
    mode = 'single'
    Hitokoto = True
    ffmpegLocation = r'ffmpeg.exe'
    overWrite = True
    writeLog = True
    fontFiles = ['ttf', 'ttc', 'otf', 'pfa', 'dfont', 'vlw', 'txf', 'woff', 'vnf', 'ytf', 'cha', 'gdr', 'pfb', 'tte',
                 'afm', 'pfr', 'xfn', 'gxf', 't65', 'sfd', 'fon', 'mxf', 'pfm', 'vfb', 'gf', 'amfm', 'acfm', 'xft',
                 'pmt', 'f3f', 'chr', 'etx', 'pk', 'mcf', 'suit', 'fnt', 'ffil', 'compositefont', 'euf', 'sfp', 'mf',
                 'lwfn', 'nftr', 'abf', 'eot', 'fot', 'bdf', 'tfm']
    subtitleSuffixDict = {'ass': 'ass', 'subrip': 'srt', 'hdmv_pgs_subtitle': 'sup'}
# 处理设置参数
if type(extraAttachmentFloder) != bool:
    extraAttachmentFloder = True
    print("------------\n请检查extraAttachmentFloder参数是否为'True'或'False'\n目前无法识别，视为'True'")
if mode not in ['single', 'multiple', 'custom']:
    mode = 'single'
    print("------------\n请检查mode参数是否为'single'或'multiple'或'custom'\n目前无法识别，视为'single'")
if type(Hitokoto) != bool:
    Hitokoto = True
    print("------------\n请检查Hitokoto参数是否为'True'或'False'\n目前无法识别，视为'True'")
if overWrite and type(overWrite) == bool:
    overWrite = ' -y'
elif (not overWrite) and type(overWrite) == bool:
    overWrite = ''
else:
    overWrite = ' -y'
    print("------------\n请检查overWrite参数是否为'True'或'False'\n目前无法识别，视为'True'")
if type(writeLog) != bool:
    writeLog = True
    print("------------\n请检查writeLog参数是否为'True'或'False'\n目前无法识别，视为'True'")
ffmpegLocation = os.path.abspath(ffmpegLocation)
if os.path.exists(ffmpegLocation):
    print('------------\n已经找到ffmpeg。该路径正确：\n%s' % ffmpegLocation)
else:
    print('------------\n找不到ffmpeg！：\n%s' % ffmpegLocation)
    exitSelf()


# 返回字符串宽度，用于对齐文本
def getStringWidth(inputString):
    width = 0
    for c in inputString:
        if unicodedata.east_asian_width(c) in ('F', 'W', 'A'):
            width += 2
        else:
            width += 1
    return width


# 追加日志信息
def logWrite(inputFile, outputFile, command):
    if not writeLog:
        return
    try:
        with open(logFileName, 'a', encoding='ansi') as logfile:
            logfile.writelines('"%s","%s","%s","%s","%s"\n' %
                               (time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()),
                                '√' if os.path.exists(outputFile) else '×',
                                inputFile,
                                outputFile,
                                command.replace('"', '""')))
    except UnicodeEncodeError:
        outStr = '"%s","%s","%s","%s","%s"\n' % (time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()),
                                                 '√' if os.path.exists(outputFile) else '×',
                                                 inputFile,
                                                 outputFile,
                                                 command.replace('"', '""'))
        newStr = ''
        for c in outStr:
            try:
                newStr += c.encode('ansi').decode('ansi')
            except UnicodeEncodeError:
                newStr += c.encode("unicode-escape").__str__()
        with open(logFileName, 'a', encoding='ansi') as logfile:
            logfile.writelines(newStr)


# hitokotoapi调用函数。。。以前写的
def APIHitokoto(returnType='return', returnData='Dic-Resolved',
                cat='', length=None, encode='json', fun='', source=None):
    """一言（Hitokoto/ヒトコト），调用API说明：https://api.imjad.cn/hitokoto.md
================================================参数说明========================================
returnType【string】（"return"）：函数调用后返回数据的方式
    "return"：return返回值
    "print"：print打印值
returnData【string】（"Dic-Resolved"）：函数返回数据类型
    "Dic"：返回字典
    "Dic-Resolved"：将字典解释为字符串返回
    "No-Resolved"：原文返回服务器的响应
    ##选择"Dic"或"Dic-Resolved"自动将encode转为"json"。
cat【string】（""）：指定source为「0」时的分类
    ""：任意分类
    "a"：Anime-动画
    "b"：Comic-漫画
    "c"：Game-游戏
    "d"：Novel-小说
    "e"：原创
    "f"：来自网络
    "g"：其他
length【int】（None）：返回一句话的长度限制，超出则打断并添加省略号（None为无限制）
encode【string】（"json"）：返回数据格式
    ""：返回纯文本
    "json"：返回JSON格式数据
    "js"：返回函数名为hitokoto的JavaScript脚本，用于同步调用
    "jsc"：返回指定CallBack函数名的JavaScript脚本，可用于异步调用
fun【string】（""）：异步调用时，指定CallBack的函数名
source【int】（None）值为0获取「系统收录」，为1获取「我的一言」（None为随机选择）
##API的charset参数为返回字符集的格式，没有必要增加函数的参数。若有需要在下面对'charset'变量进行修改，可修改为'gbk'或'utf-8'。"""
    charset = 'utf-8'
    # 判断输入参数是否正确，正确则按需转换成需要的参数类型，不正确抛出异常。
    if (returnType != "return") and (returnType != "print"):
        raise TypeError('"returnType"参数错误！执行"help(APIHitokoto)"代码查看帮助。')
    if (returnData != "Dic") and (returnData != "Dic-Resolved") and (returnData != "No-Resolved"):
        raise TypeError('"returnData"参数错误！执行"help(APIHitokoto)"代码查看帮助。')
    elif (returnData == "Dic") or (returnData == 'Dic-Resolved'):
        encode = 'json'
    if (cat != "") and (cat != "a") and (cat != "b") and (cat != "c") and (cat != "d") and (cat != "e") and (
            cat != "f") and (cat != "g"):
        raise TypeError('"cat"参数错误！执行"help(APIHitokoto)"代码查看帮助。')
    if (length is not None) and (not isinstance(length, int)):
        raise TypeError('"length"参数错误！执行"help(APIHitokoto)"代码查看帮助。')
    elif length is None:
        length = ""
    elif isinstance(length, int):
        length = "%d" % length
    if (encode != "") and (encode != "json") and (encode != "js") and (encode != "jsc"):
        raise TypeError('"encode"参数错误！执行"help(APIHitokoto)"代码查看帮助。')
    if not isinstance(fun, str):
        raise TypeError('"fun"参数错误！执行"help(APIHitokoto)"代码查看帮助。')
    if (source != 0) and (source != 1) and (source is not None):
        raise TypeError('"source"参数错误！执行"help(APIHitokoto)"代码查看帮助。')
    elif source is None:
        source = ""
    elif (source == 0) and (source == 1):
        source = "%d" % source
    # 生成请求链接并发起请求
    try:
        url = 'https://api.imjad.cn/hitokoto/?cat=' + cat + '&charset=' + charset + '&length=' + length + '&encode=' + encode + '&fun=' + fun + '&source=' + source
        response = urlopen(url)
    except urllib.error.URLError as error:
        if returnType == "print":
            print('提交数据时出现错误！' + str(error))
            return None
        else:
            return '提交数据时出现错误！' + str(error)
    # 接受并处理服务器返回信息
    response = response.read().decode('utf-8')
    if returnData == "No-Resolved":
        if returnType == "print":
            print(response)
            return None
        else:
            return response
    response = json.loads(response)
    if returnData == "Dic":
        if returnType == "print":
            print(response)
            return None
        else:
            return response
    if returnData == "Dic-Resolved":
        responseDic = ""
        for key in response:
            responseDic += key + "：" + response[key] + "\n"
        if returnType == "print":
            print(responseDic)
            return None
        else:
            return responseDic


# 执行ffmpeg命令，发送压制请求
def ffmpegCommand(args, workDir=None):
    if workDir is not None:
        os.chdir(workDir)
        print('------------\n本次运行目录：\n%s' % workDir)
    print('------------\n本次调用命令行：\n%s %s' % (ffmpegLocation, args))
    subprocess.Popen('"%s" %s' % (ffmpegLocation, args), shell=True).wait()


# 获取Mkv文件轨道信息
def getTrackInfo(mkv):
    # 检查输入
    if os.path.splitext(mkv)[-1].lower() != '.mkv':
        print('输入似乎不是mkv文件，ffmpeg对于后缀名要求很高，请仔细检查。')
        return None
    # 通过系统命令行调用ffmpeg
    command = '"%s" -i "%s"' % (ffmpegLocation, mkv)
    # print(command)
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.readlines()
    for index, line in zip(range(len(result)), result):
        result[index] = line.decode('utf-8')[:-1]
    # 查找轨道信息的位置在ffmpeg返回消息中的位置
    (infoStart, infoEnd) = (-1, -1)
    for index, line in zip(range(len(result)), result):
        if line.find("Input #0,") == 0:
            infoStart = index
        if infoStart != -1 and line.find(' ') != 0:
            infoEnd = index
    # print("[%d,%d)" % (infoStart, infoEnd))
    # 查找轨道信息的位置：异常处理
    if (infoStart, infoEnd) == (-1, -1):
        print('发生了一些诡异的事件，导致没有从ffmpeg的响应信息中发现轨道信息。')
        return None
    trackInfo = result[infoStart:infoEnd]
    # 每行用于对缩进空格数进行记录的列表
    tags = []
    for index, line in zip(range(len(trackInfo)), trackInfo):
        indexOfString = 0
        while line[indexOfString] == ' ':
            indexOfString += 1
        tags.append(indexOfString)
    # 将轨道信息记录成字典
    tracks = []
    for index, line, tag in zip(range(len(trackInfo)), trackInfo, tags):
        if tag == 4 and line.find('Stream #0:') == 4:
            stream = {'info': line[4:-1].replace('0:', '', 1)}
            if stream['info'].find(': Attachment: ') != -1:
                stream.update(filename=trackInfo[index + 2].split(': ')[1][:-1])
            tracks.append(stream)
        # print("%3d|%3d|%s" % (index, tag, line))
    return tracks


# 分析轨道信息并统计：(字幕,附件,字体)的轨道数和位置
def including(trackInfo):
    # 一通遍历，没啥好注释的
    (Subtitles, Attachments, Fonts) = ([0, []], [0, []], [0, []])
    for index, track in zip(range(len(trackInfo)), trackInfo):
        if track['info'].find(': Subtitle: ') != -1:
            Subtitles[0] += 1
            Subtitles[1].append(index)
        if track['info'].find(': Attachment: ') != -1:
            Attachments[0] += 1
            Attachments[1].append(index)
            for fontFile in fontFiles:
                if track['info'].find(': Attachment: ' + fontFile) != -1:
                    Fonts[0] += 1
                    Fonts[1].append(index)
    return Subtitles, Attachments, Fonts


# 分离出字幕
def separateSubtitle(inputFile, outputFolder=None, inputFileTrackInfo=None, inputFileTrackIncluding=None):
    # 规范输入文件路径为绝对路径，若不是文件则返回False
    if not os.path.isfile(inputFile):
        print('输入的好像不是文件。')
        return False
        # 检查输入
    if os.path.splitext(inputFile)[1].lower() != '.mkv':
        print('输入似乎不是mkv文件，ffmpeg对于后缀名要求很高，请仔细检查。')
        return False
    if not os.path.isabs(inputFile):
        inputFile = os.path.abspath(inputFile)
    inputFile = os.path.normpath(inputFile)
    # 规范输出目录为绝对路径，若输入错误则与输入文件目录相同
    try:
        os.makedirs(outputFolder)
    except Exception:
        pass
    if (outputFolder is None) or (not os.path.isdir(outputFolder)):
        outputFolder = os.path.split(inputFile)[0]
    outputFolder = os.path.abspath(outputFolder)
    # 若未输入轨道信息，则自动获取
    if (inputFileTrackInfo is None) or (type(inputFileTrackInfo) != list):
        inputFileTrackInfo = getTrackInfo(inputFile)
    # 若未输入轨道分析结果，则自动获取（顺手检查一下轨道信息输入格式是否正确）
    try:
        if (inputFileTrackIncluding is None) or (type(inputFileTrackInfo) != list):
            inputFileTrackIncluding = including(inputFileTrackInfo)
    except KeyError:
        inputFileTrackInfo = getTrackInfo(inputFile)
        inputFileTrackIncluding = including(inputFileTrackInfo)
    # 编写ffmpeg的指令，用于剥离字幕轨道，并检查inputFileTrackIncluding参数
    # # 如果先遍历检查的话虽然代码会短一点但可能会影响效率……毕竟不是每一次都会出错……
    # # # （python你追求个锤子效率
    languages = {}
    try:
        for trackIndex in inputFileTrackIncluding[0][1]:
            if type(trackIndex) != int:
                raise TypeError
            # 字幕语言获取
            # # 不会正则表达式，难受.jpg
            languageIndex = ''
            subtitleLanguage = \
                inputFileTrackInfo[trackIndex]['info'].replace(' (default)', '').split('(')[1].split(')')[0]
            if languages.get(subtitleLanguage) is None:
                languages.update(**{subtitleLanguage: 2})
            else:
                languageIndex = '(%d)' % languages[subtitleLanguage]
                languages[subtitleLanguage] += 1
            # 字幕类型获取
            suffixType = inputFileTrackInfo[trackIndex]['info'].replace(' (default)',
                                                                        '').split(': Subtitle: ')[1].split(',')[0]
            # 对照设置中的映射表获取字幕后缀名，若映射表没有收录，则不导出该字幕
            try:
                suffix = subtitleSuffixDict[suffixType]
            except KeyError:
                print('------------\n未知的字幕类型:', suffixType)
                print(inputFileTrackInfo)
                continue
            subName = '%s.%s.%s' % (os.path.split(inputFile)[1][:-4], subtitleLanguage + languageIndex, suffix)
            commandArgs = '-i "%s" -map 0:%d "%s"%s' % (
                inputFile, trackIndex, os.path.join(outputFolder, subName), overWrite)
            ffmpegCommand(commandArgs)
            logWrite(inputFile, os.path.join(outputFolder, subName), commandArgs)
    # 如果有问题多半是因为inputFileTrackIncluding参数错误，而且会在for的第一次迭代之前抛出异常，所以不用担心同一个字幕轨道输出两次。
    # # 如果有例外情况的话把overWrite=True就行
    except (IndexError, TypeError):
        inputFileTrackIncluding = including(inputFileTrackInfo)
        languages.clear()
        for trackIndex in inputFileTrackIncluding[0][1]:
            if type(trackIndex) != int:
                raise TypeError
            # 字幕语言获取
            # # 不会正则表达式，难受.jpg
            languageIndex = ''
            subtitleLanguage = \
                inputFileTrackInfo[trackIndex]['info'].replace(' (default)', '').split('(')[1].split(')')[0]
            if languages.get(subtitleLanguage) is None:
                languages.update(**{subtitleLanguage: 2})
            else:
                languageIndex = '(%d)' % languages[subtitleLanguage]
                languages[subtitleLanguage] += 1
            # 字幕类型获取
            suffixType = inputFileTrackInfo[trackIndex]['info'].replace(' (default)', '').split(': Subtitle: ')[1]
            # 对照设置中的映射表获取字幕后缀名，若映射表没有收录，则不导出该字幕
            try:
                suffix = subtitleSuffixDict[suffixType]
            except KeyError:
                print('未知的字幕类型:', suffixType)
                continue
            subName = '%s.%s.%s' % (os.path.split(inputFile)[1][:-4], subtitleLanguage + languageIndex, suffix)
            commandArgs = '-i "%s" -map 0:%d "%s"%s' % (
                inputFile, trackIndex, os.path.join(outputFolder, subName), overWrite)
            ffmpegCommand(commandArgs, outputFolder)
            logWrite(inputFile, os.path.join(outputFolder, subName), commandArgs)
    return True


# 提取全部附件
def separateAttachment(inputFile, outputFolder=None):
    # 规范输入文件路径为绝对路径，若不是文件则返回False
    if not os.path.isfile(inputFile):
        print('输入的好像不是文件。')
        return False
        # 检查输入
    if os.path.splitext(inputFile)[1].lower() != '.mkv':
        print('输入似乎不是mkv文件，ffmpeg对于后缀名要求很高，请仔细检查。')
        return False
    if not os.path.isabs(inputFile):
        inputFile = os.path.abspath(inputFile)
    inputFile = os.path.normpath(inputFile)
    # 规范输出目录为绝对路径，若输入错误则与输入文件目录相同
    try:
        os.makedirs(outputFolder)
    except Exception:
        pass
    if (outputFolder is None) or (not os.path.isdir(outputFolder)):
        outputFolder = os.path.split(inputFile)[0]
    outputFolder = os.path.abspath(outputFolder)
    command = '-dump_attachment:t "" -i "%s"%s' % (inputFile, overWrite)
    ffmpegCommand(command, workDir=outputFolder)
    logWrite(inputFile, outputFolder, command)
    return True


# 转MKV为MP4
def transformMKVtoMP4(inputFile, outputFolder=None, outputFile=None):
    # 规范输入文件路径为绝对路径，若不是文件则返回False
    if not os.path.isfile(inputFile):
        print('输入的好像不是文件。')
        return False
        # 检查输入
    if os.path.splitext(inputFile)[1].lower() != '.mkv':
        print('输入似乎不是mkv文件，ffmpeg对于后缀名要求很高，请仔细检查。')
        return False
    if not os.path.isabs(inputFile):
        inputFile = os.path.abspath(inputFile)
    inputFile = os.path.normpath(inputFile)
    # 规范输出目录为绝对路径，若输入错误则与输入文件目录相同
    try:
        os.makedirs(outputFolder)
    except Exception:
        pass
    if (outputFolder is None) or (not os.path.isdir(outputFolder)):
        outputFolder = os.path.split(inputFile)[0]
    outputFolder = os.path.abspath(outputFolder)
    # 规范输出文件名
    if outputFile is None:
        outputFile = os.path.split(inputFile)[1][:-4] + '.mp4'
    elif outputFile[-4:].lower() != '.mp4':
        outputFile += '.mp4'
    command = '-i "%s" -c:v copy -c:a aac -strict -2 "%s"%s' % (inputFile,
                                                                os.path.join(outputFolder, outputFile),
                                                                overWrite)
    ffmpegCommand(command, workDir=outputFolder)
    logWrite(inputFile, os.path.join(outputFolder, outputFile), command)
    return True


# 视频一条龙服务
def mkvFileOneDragonService(inputFile, outputFolder=None):
    # 规范输入文件路径为绝对路径，若不是文件则返回False
    if not os.path.isfile(inputFile):
        print('输入的好像不是文件。')
        return False
        # 检查输入
    if os.path.splitext(inputFile)[1].lower() != '.mkv':
        print('输入似乎不是mkv文件，ffmpeg对于后缀名要求很高，请仔细检查。')
        return False
    if not os.path.isabs(inputFile):
        inputFile = os.path.abspath(inputFile)
    inputFile = os.path.normpath(inputFile)
    # 规范输出目录为绝对路径，若输入错误则与输入文件目录相同
    try:
        os.makedirs(outputFolder)
    except Exception:
        pass
    if (outputFolder is None) or (not os.path.isdir(outputFolder)):
        outputFolder = os.path.split(inputFile)[0]
    outputFolder = os.path.abspath(outputFolder)
    # 获取文件信息
    trackInfo = getTrackInfo(inputFile)
    count = including(trackInfo)
    # 干活！
    if count[0][0] > 0:
        separateSubtitle(inputFile=inputFile,
                         outputFolder=outputFolder,
                         inputFileTrackInfo=trackInfo,
                         inputFileTrackIncluding=count)
    if count[1][0] > 0:
        if extraAttachmentFloder:
            separateAttachment(inputFile=inputFile,
                               outputFolder=os.path.join(outputFolder,
                                                         '%s.attachments' % os.path.basename(inputFile)[:-4]))
        else:
            separateAttachment(inputFile=inputFile,
                               outputFolder=outputFolder)
    transformMKVtoMP4(inputFile=inputFile,
                      outputFolder=outputFolder)
    return True


# 文件夹一条龙服务
def mkvDirectoryOneDragonService(inputFolder, outputFolder=None):
    # 规范输入路径为绝对路径，若不是文件则返回False
    if os.path.isfile(inputFolder):
        print('输入的好像不是文件夹。')
        return False
        # 检查输入
    if not os.path.isabs(inputFolder):
        inputFolder = os.path.abspath(inputFolder)
    inputFolder = os.path.normpath(inputFolder)
    # 规范输出目录为绝对路径，若输入错误则与输入文件目录相同
    try:
        os.makedirs(outputFolder)
    except Exception:
        pass
    if (outputFolder is None) or (not os.path.isdir(outputFolder)):
        outputFolder = os.path.split(inputFolder)[0]
    outputFolder = os.path.abspath(outputFolder)
    # 遍历输入目录
    mkvList = []
    for item in os.walk(inputFolder):
        for file in item[2]:
            if os.path.splitext(file)[1].lower() == '.mkv':
                filePath = os.path.join(item[0], file)
                mkvList.append((os.path.relpath(filePath, inputFolder)[:-4], filePath))
    outputFolder = os.path.join(outputFolder, '%s.treated' % os.path.split(inputFolder)[1])
    for item in mkvList:
        itemOutputFolder = outputFolder
        trackInfo = getTrackInfo(item[1])
        count = including(trackInfo)
        # 干活！
        if count[0][0] > 0:
            separateSubtitle(inputFile=item[1],
                             outputFolder=os.path.join(itemOutputFolder, os.path.split(item[0])[0]),
                             inputFileTrackInfo=trackInfo,
                             inputFileTrackIncluding=count)
        if count[1][0] > 0:
            if extraAttachmentFloder:
                separateAttachment(inputFile=item[1],
                                   outputFolder=os.path.join(itemOutputFolder, '[Attachments]'))
            else:
                separateAttachment(inputFile=item[1],
                                   outputFolder=os.path.join(itemOutputFolder, os.path.split(item[0])[0]))
        transformMKVtoMP4(inputFile=item[1],
                          outputFolder=os.path.join(itemOutputFolder, os.path.split(item[0])[0]))


# 打开文件
def openFile(**options):
    base = tkinter.Tk()
    base.withdraw()
    filePath = filedialog.askopenfilename(**options)
    return filePath


# 保存文件
def saveFile(**options):
    base = tkinter.Tk()
    base.withdraw()
    filePath = filedialog.asksaveasfilename(**options)
    return filePath


# 打开目录
def openDirectory(**options):
    base = tkinter.Tk()
    base.withdraw()
    directoryPath = filedialog.askdirectory(**options)
    return directoryPath


# 单文件模式
def singleMode(inputFile, outputFolder=None):
    mkvFileOneDragonService(inputFile=inputFile, outputFolder=outputFolder)


# 文件夹模式
def multipleMode(inputFolder, outputFolder=None, schedule=True):
    mkvDirectoryOneDragonService(inputFolder=inputFolder, outputFolder=outputFolder)


# 自定义模式
def customMode(csvFile):
    queue = set()
    errorMission = []
    # 打开csv文件，并添加任务至队列
    with open(csvFile) as table:
        reader = list(csv.reader(table))
        for index, line in zip(range(len(reader)), reader):
            if os.path.exists(line[0]) and os.path.splitext(line[0])[1].lower() == '.mkv':
                queue.add((line[0], line[1]))
            elif os.path.exists(line[0]) and os.path.isdir(line[0]):
                queue.add((line[0], line[1]))
            elif line in [['输入', '输出'], ['(输入文件或文件夹路径)', '(选填，输出路径)'], ['', '']]:
                continue
            else:
                errorMission.append((index, line[0], line[1]))
    # 输出任务列表
    if len(queue) != 0:
        print('------------\n接受任务：(输入 | 输出)')
        maxLen = 0
        for i in queue:
            if getStringWidth(i[0]) > maxLen:
                maxLen = getStringWidth(i[0])
        for i in queue:
            print(i[0] + ' ' * (maxLen - getStringWidth(i[0])) + '\t| ',
                  i[1] if i[1] != '' else '[未指定输出，将与输入保存到相同目录]')
    else:
        print('------------\n没有找到一条可执行的任务……')
        exitSelf()
    queue = list(queue)
    # 执行队列中的任务
    for index, item in zip(range(len(queue)), list(queue)):
        if os.path.isfile(item[0]):
            mkvFileOneDragonService(item[0],item[1] if item[1] != '' else None)
        elif os.path.isdir(item[0]):
            mkvDirectoryOneDragonService(item[0],item[1] if item[1] != '' else None)
    # 输出无法处理的列表
    if len(errorMission) != 0:
        print('------------\n无法处理：(| 输入 | 输出)')
        maxLen = getStringWidth(errorMission[0][1])
        for i in errorMission[1:]:
            if getStringWidth(i[1]) > maxLen:
                maxLen = getStringWidth(i[1])
        for i in errorMission:
            print('Line: ' + i[0].__str__() + ' ' * (int(math.log10(errorMission[-1][0])) - int(math.log10(i[0])))
                  + ' |',
                  i[1] + ' ' * (maxLen - getStringWidth(i[1])) + '\t|',
                  i[2])


if __name__ == '__main__':
    # 初始化标题
    title = '沉默的MKV批处理'
    os.system('title %s' % title)
    # 没有参数显示参数列表
    if len(sys.argv[1:]) == 0:
        print('''------------
参数列表，纵向可叠加：
	'-s' '--setting'   : 生成设置模板
	'-t' '--template'  : 生成任务模板
	---以下选项优先级高于设置文件---
	'-e' '--extra'     : 禁用附件单独保存
	'-m' '--multiple' / '-c' '--custom' :
	设置模式为"multiple"/"custom"
	'-h' '--hitokoto'  : 禁用Hitokoto
	'-o' '--overWrite' : 关闭文件覆盖
	'-l' '--writelog'  : 禁用日志''')
    else:
        print('------------')
    # 处理命令行参数
    getFile = False
    for line in sys.argv[1:]:
        if line == '-s' or line == '--setting':
            fileName = saveFile(title='选择保存设置模板的位置',
                                defaultextension='.py',
                                filetypes=[("Python脚本文件", ".py")])
            if fileName == '':
                print('你点了取消~')
            else:
                with open(fileName, mode='w', encoding='utf-8') as f:
                    f.write('''# 将附件存放到单独的文件夹中
# True：是
# False：否
extraAttachmentFloder = True

# 默认运行模式
# 'single': ——单文件模式。
# 弹窗选择单个需要处理的文件和保存的位置。
# 'multiple': ——多文件模式。
# 弹窗选择单个需要处理的文件夹和保存的位置（单独处理目录下的每个文件）。
# 'custom': ——自定义模式。
# 弹窗选择csv表格文件，并根据表格挨个处理。
mode = 'single'

# 启用Hitokoto（需要联网）
# https://api.imjad.cn/hitokoto.md
# True：启用
# False：不启用
Hitokoto = True


# ffmpeg的位置
# 默认为于环境变量或与主程序于同一路径
ffmpegLocation = r"ffmpeg.exe"

# 覆盖
# 若遇到相同文件名的文件则覆盖，请谨慎考虑。
# True：覆盖
# False：不覆盖
overWrite = True

# 记录日志
# True：是
# False：否
writeLog = True

# 字体文件后缀名（错删少补）
# 格式：['后缀名A', '后缀名B']
# 请将常见文件格式前置以提高运行效率
fontFiles = [
    'ttf', 'ttc', 'otf', 'pfa', 'dfont', 'vlw', 'txf', 'woff', 'vnf', 'ytf', 'cha', 'gdr', 'pfb', 'tte', 'afm', 'pfr',
    'xfn', 'gxf', 't65', 'sfd', 'fon', 'mxf', 'pfm', 'vfb', 'gf', 'amfm', 'acfm', 'xft', 'pmt', 'f3f', 'chr', 'etx',
    'pk', 'mcf', 'suit', 'fnt', 'ffil', 'compositefont', 'euf', 'sfp', 'mf', 'lwfn', 'nftr', 'abf', 'eot', 'fot',
    'bdf', 'tfm'
]

# 字幕格式与后缀名对照表
# 格式：{'A字幕文件类型': 'A字幕文件后缀名', 'B字幕文件类型': 'B字幕文件后缀名', }
subtitleSuffixDict = {
    'ass': 'ass',
    'subrip': 'srt',
    'hdmv_pgs_subtitle': 'sup'
}''')
                print('已生成设置文件模板，请享用~')
                print('已保存至：%s' % fileName)
            getFile = True
        elif line == '-t' or line == '--template':
            fileName = saveFile(title='选择保存任务模板的位置', defaultextension='.csv', filetypes=[("CSV表格文件", ".csv")])
            if fileName == '':
                print('你点了取消~')
            else:
                print(fileName)
                with open(fileName, mode='w', encoding='ansi') as f:
                    f.write('''输入,输出,
(输入文件或文件夹路径),(选填，输出路径),''')
                print('已生成自定义文件任务模板，请享用~')
                print('已保存至：%s' % fileName)
            getFile = True
        elif line == '-e' or line == '--extra':
            extraAttachmentFloder = False
            print('通过快捷入口设置附件不用单独保存。')
        elif line == '-m' or line == '--multiple':
            mode = 'multiple'
            print('通过快捷入口设置模式为"multiple"。')
        elif line == '-c' or line == '--custom':
            mode = 'custom'
            print('通过快捷入口设置模式为"custom"。')
        elif line == '-h' or line == '--hitokoto':
            Hitokoto = False
            print('通过快捷入口禁用Hitokoto。')
        elif line == '-o' or line == '--overWrite':
            overWrite = False
            print('通过快捷入口关闭文件覆盖。')
        elif line == '-l' or line == '--writelog':
            writeLog = False
            print('通过快捷入口禁用日志。')
    if getFile:
        exitSelf()
    # 调用Hitokoto API
    if Hitokoto:
        print('------------\n等待Hitokoto服务器回应，若时间过长请禁用Hitokoto:')
        HitokotoInfo = APIHitokoto(returnData='Dic')
        if type(HitokotoInfo) == dict:
            try:
                print('------------\nHitokoto:')
                print(HitokotoInfo['hitokoto'])
                print('出处    \t: %s' % HitokotoInfo['source'])
                print('投稿者   \t: %s' % HitokotoInfo['author'])
                print('上传日期 \t: %s' % HitokotoInfo['date'])
                print('类别    \t: %s' % HitokotoInfo['catname'])
                print('序号    \t: %s' % HitokotoInfo['id'])
                HitokotoStr = '%s ——%s' % (HitokotoInfo['hitokoto'], HitokotoInfo['source'])
                if HitokotoInfo['source'] == '':
                    HitokotoStr = '%s ——%s' % (HitokotoInfo['hitokoto'], HitokotoInfo['author'])
                    if HitokotoInfo['source'] == '':
                        HitokotoStr = '%s' % (HitokotoInfo['hitokoto'])
                title = HitokotoStr
                os.system('title %s' % title)
            # 免得因为协议更新导致用不了
            # # 有问题我一定会更新的！ 咕！
            except KeyError:
                print('------------\nHitokoto API数据异常，请等待软件更新。')
    # 创建日志文件
    if writeLog:
        logFileName = 'log.(%s).csv' % time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        with open(logFileName, 'a', encoding='ansi') as outfile:
            outfile.writelines('时间,已完成,输入,输出,命令行' + '\n')
        logFileName = os.path.abspath(logFileName)
    # 根据模式进入支线
    if mode == 'single':
        print('------------\n等待选择视频文件(=・ω・=)')
        inputFile = openFile(title='打开你需要处理的MKV视频文件', filetypes=[("MKV视频文件", ".mkv")])
        if inputFile == '':
            print('------------\n啊啦~啊啦~~你点了取消了呢，那下次再见~')
            exitSelf()
        print('------------\n你选择的是：\n%s' % inputFile)
        print('------------\n等待选择输出目录(｀・ω・´)')
        outputFolder = openDirectory(title='选择保存位置')
        if outputFolder == '':
            outputFolder = None
            print('------------\n(ﾟДﾟ≡ﾟдﾟ)!? 没选!? 那我帮你和输入的文件放一起了昂?')
        else:
            print('------------\n你选择的是：\n%s' % outputFolder)
        singleMode(inputFile, outputFolder)
    elif mode == 'multiple':
        print('------------\n等待选择文件夹(^・ω・^ )')
        inputFolder = openDirectory(title='打开你需要处理的MKV视频文件目录')
        if inputFolder == '':
            print('------------\n阿勒??你点了取消了呢，那下次见~拜拜~')
            exitSelf()
        print('------------\n你选择的是：\n%s' % inputFolder)
        print('------------\n等待选择输出目录("▔□▔)/')
        outputFolder = openDirectory(title='打开MKV视频文件输出目录')
        if outputFolder == '':
            outputFolder = None
            print('------------\nΣ(ﾟдﾟ;)没选!? 那我帮你放到输入的文件那边咯?')
        else:
            print('------------\n你选择的是：\n%s' % outputFolder)
        multipleMode(inputFolder, outputFolder)
    elif mode == 'custom':
        print('------------\n等待选择队列CSV(｡･ω･｡)')
        csvFile = openFile(title='打开你私人订制的CSV队列', filetypes=[("CSV表格文件", ".csv")])
        if csvFile == '':
            print('------------\nあのね あのね 你点了取消，我怎么知道你要谁? (･∀･)')
            exitSelf()
        customMode(csvFile)
    exitSelf()
