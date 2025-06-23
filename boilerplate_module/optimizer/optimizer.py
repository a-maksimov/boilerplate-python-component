from boilerplate_module.logger import get_logger


class Optimizer:
    def __init__(self, **kwargs):
        self._logger = get_logger(kwargs.get("loglevel"))

    def run(self) -> None:
        self._logger.info(f"{self} is running...")
