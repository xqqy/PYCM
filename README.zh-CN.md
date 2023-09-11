# PYCM 电子教室管理系统

[![GitHub issues](https://img.shields.io/github/issues/yangzhongtian001/PYCM)](https://github.com/yangzhongtian001/PYCM/issues)
[![GitHub forks](https://img.shields.io/github/forks/yangzhongtian001/PYCM)](https://github.com/yangzhongtian001/PYCM/network)
[![GitHub stars](https://img.shields.io/github/stars/yangzhongtian001/PYCM)](https://github.com/yangzhongtian001/PYCM/stargazers)
[![GitHub license](https://img.shields.io/github/license/yangzhongtian001/PYCM)](https://github.com/yangzhongtian001/PYCM)
[![Code Factor](https://www.codefactor.io/repository/github/yangzhongtian001/pycm/badge/master)](https://www.codefactor.io/repository/github/yangzhongtian001/pycm/overview/master)
![Build Windows](https://github.com/yangzhongtian001/PYCM/actions/workflows/build-windows.yml/badge.svg)
![Build MacOS](https://github.com/yangzhongtian001/PYCM/actions/workflows/build-mac.yml/badge.svg)
![Build Linux](https://github.com/yangzhongtian001/PYCM/actions/workflows/build-linux.yml/badge.svg)

[English](README.md) [简体中文](README.zh-CN.md)

## 镜像仓库

* [Github(主要)](https://github.com/yangzhongtian001/PYCM)
* [Gitee(镜像)](https://gitee.com/yangzhongtian/PYCM)

## 简介

此程序为一个使用Python编写的电子教室管理系统，包含 `Client(学生端)` 和 `Console(教师端)`。图形界面由 `PySide6` 编写，支持所有平台。

## 功能

* [x] 局域网自动上线
* [x] 教师端屏幕广播
* [x] 教师端屏幕监控
* [X] 教师端文件共享
* [x] 学生端文件提交
* [x] 教师端消息发送
* [x] 学生端消息发送
* [x] `PyInstaller` 编译发布

## 程序

* **Client(学生端):** 用于多个用户，例如：学生、访客。
* **Console(教师端):** 用于一个用户，例如：教师、主持人。

## 发布版安装指南

* 下载发布版本于 [这里](https://github.com/yangzhongtian001/PYCM/releases)
* 运行 `ConsoleMain` 或 `ClientMain`

## 源码版安装指南

* 克隆此仓库
* 运行 `pip install -r requirements.txt` 以安装依赖组件
* 运行 `python ConsoleMain.py` 或 `python ClientMain.py` 以启动程序

## 截图

### Console(教师端)

![控制台](Images/Console/Dashboard.zh-CN.png)

![发送消息](Images/Console/MessageSend.zh-CN.png)

![远程命令](Images/Console/RemoteCommand.zh-CN.png)

### Client(学生端)

![主程序](Images/Client/Main.zh-CN.png)

![文件发送](Images/Client/FileTransfer.zh-CN.png)

## 联系

* 作者：Richard Yang
* 学校：北京十一学校
* 社团：HCC Computer Community

---

![GPLv3 or later](Images/Logo/GPLv3OrLater.png)
![HCC Computer Community](Images/Logo/HCC.png)
![BNDSE](Images/Logo/BNDSE.png)