# 22 通过 IDEMaven 部署 Serverless 应用实践 

Source: https://learn.lianglianglee.com/专栏/Serverless 技术公开课（完）/22 通过 IDEMaven 部署 Serverless 应用实践.md

因收到Google相关通知，网站将会择期关闭。[相关通知内容](https://lumendatabase.org/notices/44265620)

---

# 22 通过 IDEMaven 部署 Serverless 应用实践

### SAE 应用部署方式

#### 1. SAE 概述

![img](assets/2020-09-07-110109.png)

首先，简单介绍一下 SAE。SAE 是一款面向应用的 Serverless PaaS 平台，支持 Spring Cloud、Dubbo、HSF 等主流开发框架，用户可以零代码改造直接将应用部署到 SAE，并且按需使用、按量计费、秒级弹性。SAE 充分发挥 Serverless 的优势，为用户节省闲置资源成本；在体验上，SAE 采用全托管、免运维的方式，用户只需聚焦核心业务的开发，而应用生命周期管理、微服务管理、日志、监控等功能交由 SAE 完成。

#### 2. SAE 应用部署方式

![image.gif](assets/2020-09-07-105849.png)![2.jpg](assets/2020-09-07-105851.jpg)

在使用 SAE 时，您可以在控制台上看到 SAE 支持三种部署方式，即可以通过 WAR 包、JAR 包和镜像的方式进行部署，如果您采用 Spring Cloud、Dubbo、HSF 这类应用，可以直接打包上传，或者填入包的地址便可以部署到 SAE 上；对于非 Java 语言的场景，您也可以使用镜像直接来部署，后续我们也会支持其他语言直接上传包的形式进行部署。

SAE 除上述控制台界面部署的方式之外，还支持通过 Maven 插件或者 IDE 插件的方式进行部署，这样您无需登录控制台，就可以执行自动化部署操作，同时可以集成如云效、Jenkins 等工具实现 CICD 流程。

### Maven 插件部署

![3.jpg](assets/2020-09-07-110027.jpg)

如何使用 Maven 插件进行部署？首先需要为应用添加 Maven 依赖 toolkit-maven-plugin，接下来需要编写配置文件来配置插件的具体行为，这里定义了三个配置文件：

* **toolkit\_profile.yaml 账号配置文件**，用来配置阿里云 ak、sk 来标识阿里云用户，这里推荐使用子账号 ak、sk 以降低安全风险。
* **toolkit\_package.yaml 打包配置文件**，用来声明部署应用的类型，可以选择 war、jar、url 以及镜像的方式来进行部署，若采用 war、jar 的方式，则会将当前应用进行打包上传，而 url 或者镜像的方式则要显示的填写对应的包地址或者镜像地址进行部署。
* **toolkit\_deploy.yaml 部署配置**，即可以配置该应用的环境变量、启动参数、健康检查等内容，这与控制台上的配置选项是一致的。

这三个文件都有对应的模板，具体的模板选项可以查看[产品文档](https://help.aliyun.com/document_detail/110639.html?spm=a2c4g.11186623.6.611.5a3473c76owo99)，接下来通过运行 Maven 打包部署命令 mvn clean package toolkit:deploy 即可自动化部署到 SAE 上。

### IDE 插件部署

![img](assets/2020-09-07-110135.jpg)

再看一下如何通过您的 IDE 直接进行部署，这个是借助 Alibaba Cloud Toolkit IDE 插件的能力，它可以在主流的 Java IDE IDEA 和 Eclipse 上面安装，这里以 IDEA 为例，您可以在 IDEA 插件市场中搜索并安装。之后重启 IDEA 后即可看到 Cloud Toolkit 的选项。下面我们要做的配置和刚才的 Maven 插件部署的配置比较类似，先要配置阿里云账号信息，即 ak、sk。接下来选择部署到 SAE 这个选项，里面有多种部署方式：Maven 打包、上传文件、镜像，同时在高级选项中可以配置应用的环境变量、启动参数、健康检查等内容。

### 总结

相信您通过本文已经了解了 SAE 的几种部署方式和基本使用，在这里也推荐您选用 SAE，在不改变当前开发运维方式的同时，享受 Serverless 技术带来的价值。

**相关文档：**

[通过 Maven 插件自动部署应用](https://help.aliyun.com/document_detail/110639.html?spm=a2c4g.11186623.6.611.5a3473c76owo99) [通过 IntelliJ IDEA 插件部署应用](https://help.aliyun.com/document_detail/110665.html?spm=a2c4g.11186623.6.612.77f16905iduxEH) [通过 Eclipse 插件一键部署应用](https://help.aliyun.com/document_detail/110664.html?spm=a2c4g.11186623.6.613.616144e2vDAuFc)

### 课程推荐

为了更多开发者能够享受到 Serverless 带来的红利，这一次，我们集结了 10+ 位阿里巴巴 Serverless 领域技术专家，打造出最适合开发者入门的 Serverless 公开课，让你即学即用，轻松拥抱云计算的新范式——Serverless。

点击即可免费观看课程：<https://developer.aliyun.com/learning/roadmap/serverless>