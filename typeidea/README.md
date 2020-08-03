## Typeidea 介绍
项目改自：https://github.com/the5fire/typeidea
+ 安装前准备：
    + pypi私有镜像源
    + 配置.pypirc文件

+ 安装：
    + 配置版本号
    + 打包并上传
```
    fab build --version 0.4
```
+ 部署
     + 确认虚拟环境已经配置
     + 激活虚拟环境
     + 安装软件包
     + 启动

```
    fab -H myserver -S ssh_config deploy 0.4 develop
```
