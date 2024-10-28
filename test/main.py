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
        self.project = self.make_section(Project)
        self.runner = self.make_section(Runner)


if __name__ == "__main__":
    settings = Settings()
    settings.reload(Path("./xy_test_settings.toml"))
    print(settings.runner.path)
