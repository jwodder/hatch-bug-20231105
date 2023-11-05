from __future__ import annotations
import os
import os.path
import tempfile
from typing import Any
from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    PLUGIN_NAME = "custom"

    def initialize(self, _version: str, build_data: dict[str, Any]) -> None:
        with open(
            os.path.join(self.root, "src", "mypackage", "__init__.py"),
            "r",
            encoding="utf-8",
        ) as infp:
            fd, tmp_path = tempfile.mkstemp()
            with os.fdopen(fd, "w", encoding="utf-8") as outfp:
                for line in infp:
                    if line.startswith("__file_source__ = "):
                        line = f"__file_source__ = {self.target_name!r}\n"
                    outfp.write(line)
        if self.target_name == "sdist":
            path = "src/mypackage/__init__.py"
        else:
            path = "mypackage/__init__.py"
        build_data["force_include"][tmp_path] = path
