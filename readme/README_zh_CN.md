# xy_settings

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## 说明

通用设置模块

## 源码仓库

- <a href="https://github.com/xy-base/xy_settings.git" target="_blank">Github地址</a>  
- <a href="https://gitee.com/xy-base/xy_settings.git" target="_blank">Gitee地址</a>

## 安装

```bash
# bash
pip install xy_settings
```

## 使用

###### python脚本

```toml
# xy_test_settings.toml
# ######################## xy_work配置 ###########################
# 默认配置文件位置为 当前工作目录下的 config/xy_work.toml


# ######################## xy_work项目配置 ###########################
[xy_work_project]

# 项目名称, 仅支持英文
name = "xy_test_settings"

# 项目标识
identifier = "xy_test_settings"

# 项目名称, 支持中英文
verbose_name = "xy_test_settings"

# 项目说明, 支持中英文
description = "xy_test_settings"

# 项目路径
path = "./"

# ######################## xy_work运行配置 ###########################

[xy_work_runner]

# 服务源码目录自动添加到sys.path 
# 默认 当前项目目录下的 source/Runner
path = "./runner_path"

# 服务入口类，根据上文的path寻找对应的类初始化即为启动，字符串，若包含模块使用module.class根据importlib引入
# 默认 Runner.Runner
runner = "xy_runner"

```

```python
# main.py
from uuid import uuid4
from pathlib import Path
from xy_settings.Settings import Settings as xy_s
from xy_settings.Section.Section import Section


class Runner(Section):
    path: Path | None = Path("./Runner/")

    # 表示Runner.py中的Runner类
    runner: str | None = "Runner.xyTestRunner"

    source_path: Path | None = Path("./")

    def get_name(self) -> str | None:
        return "xy_work_runner"

    def _load(self):
        self.path = self._fetch_path("path", self.path)
        self.runner = self._sync_data("runner", self.runner)
        super()._load()


class Project(Section):
    name: str | None
    verbose_name: str | None

    identifier: str = uuid4().hex
    description: str | None

    path: Path | None

    def get_name(self) -> str | None:
        return "xy_work_project"

    def _load(self):
        try:
            ##################### fetch_path ###############

            self.path = self._fetch_path("path", self.path)  # type: ignore

            ##################### sync_data ################

            self.name = self._sync_data("name", self.name)
            self.verbose_name = self._sync_data("verbose_name", self.verbose_name)
            self.identifier = self._sync_data("identifier", self.identifier)  # type: ignore
            self.description = self._sync_data("description", self.description)
        except:
            pass
        super()._load()


class Settings(xy_s):
    project: Project | None = Project()
    runner: Runner | None = Runner()
    GLOBAL_CFG_SETTINGS_PATH_KEY = "__xy_work_cfg_path_key"
    default_cfg_relative_path: Path = Path("./xy_test_settings.toml")

    def reload(self, settings_cfg_path: Path):
        super().reload(settings_cfg_path)
        self.project = self.__make_section(Project)
        self.runner = self.__make_section(Runner)


if __name__ == "__main__":
    settings = Settings()
    settings.reload(Path("./xy_test_settings.toml"))
    print(settings.runner.path)
    
```


```bash
# bash
python main.py
# /mnt/bs-media/Workspace/project/opensource/xy-base/xy_settings/test/runner_path
```

## 许可证
xy_settings 根据 <木兰宽松许可证, 第2版> 获得许可。有关详细信息，请参阅 [LICENSE](../LICENSE) 文件。


## 捐赠

如果小伙伴们觉得这些工具还不错的话，能否请咱喝一杯咖啡呢?  

![Pay-Total](./Pay-Total.png)


## 联系方式

```
微信: yuyangiit
邮箱: yuyangit.0515@qq.com
```