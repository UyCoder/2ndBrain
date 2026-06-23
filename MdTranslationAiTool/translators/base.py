from abc import ABC, abstractmethod


class FatalTranslationError(Exception):
    """API ھېسابات مەسىلىسى — داۋاملاشتۇرۇش پايدىسىز (كرېدىت يوق، كۈنلۈك چەك تولغان...)"""
    pass


class BaseTranslator(ABC):
    """بارلىق AI تەرجىمانلىرىنىڭ ئاساسىي كلاسى"""

    def __init__(self, api_key: str, model: str = None):
        self.api_key = api_key
        self.model = model
        self._client = None

    @abstractmethod
    def translate(self, text: str, system_prompt: str) -> str:
        """مەتىننى تەرجىمە قىلىدۇ"""
        pass

    @abstractmethod
    def test_connection(self) -> bool:
        """API ئۇلىنىشىنى سىناق قىلىدۇ"""
        pass

    @staticmethod
    def get_default_model() -> str:
        return ""

    @staticmethod
    def get_available_models() -> list[str]:
        return []
