# MockAppCrawl

项目目的是为了解决使用 App 获取数据，核心的思路是通过 Appium 模拟操作 App 的同时，使用 mitmproxy 作为中间人代理解析或者获取相关的 request 以及 response。

**注意⚠️**，本次使用测试 App 为豆果美食（版本为 6.9.45.2）

## Requirements

* [Appium](https://github.com/appium/appium-desktop/releases) 以及 Appium-Client

  Appium-Client 可以通过 pip 进行安装 `pip install Appium-Python-Client`——*注意单词首字母大写*

* [mitmproxy](https://mitmproxy.org/)

* Anaconda

* 模拟器或者真机——可选模拟器

## Files

```bash
├── env # 运行虚拟环境
├── LICENSE
├── mock_app_control.py
└── parse_content.py
```

`env` 是创建的虚拟环境，运行文件包括：

*  `mock_app_control.py` 用于模拟操作 App
* `parse_content.py` 中间人 proxy 的脚本，用于解析和保存数据

## Usage

1. 因为需要通过 mitmproxy 获取数据，所以需要优先启动

   ```bash
   mitmdump -s parse_content.py
   ```

   `parse_content.py` 是用于解析需要的数据，并采取相应的保存处理。

2. 直接运行 `mock_app_control.py` 文件，完成 App 操作

   ```bash
   python mock_app_control.py
   ```

   

