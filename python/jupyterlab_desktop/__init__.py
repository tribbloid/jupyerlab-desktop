import logging
import runpy
import sys
from concurrent.futures import Future, ProcessPoolExecutor

import jupyterlab

argv = [
    "--LabApp.shutdown_no_activity_timeout=5",
    """--browser="chromium-browser --app=%s" """,
    "--KernelManager.shutdown_wait_time=5",
    "--MappingKernelManager.cull_idle_timeout=5",
    "--MappingKernelManager.cull_interval=5"
]


class Launcher(object):

    def executor(self):
        return ProcessPoolExecutor(2)

    def startJupyter(self):
        _argv = argv

        oldArgv = sys.argv
        sys.argv = _argv

        try:
            runpy.run_module(jupyterlab.__name__, {}, "__main__")

        except Exception as e:
            logging.exception("Jupyter launching error")
            raise e

        finally:
            sys.argv = oldArgv

    # def startJupyter_Asynch(self) -> Future:
    #
    #     ff: Future = executor.submit(self.startJupyter)
    #     return ff
    #
    # def startBrowser(selfself, url: str):
    #     subprocess.call(
    #         [
    #             """chromium-browser""",
    #             f"""--app="{url}" """
    #         ]
    #     )

    # def startBrowser_Asynch(self, url: str):
    #
    #     ff: Future = executor.submit(
    #         subprocess.call,
    #
    #     )
    #     return ff

    def launchAll(self):

        ff: Future = self.startJupyter()
