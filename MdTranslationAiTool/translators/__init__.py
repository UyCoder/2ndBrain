from .claude_translator import ClaudeTranslator
from .gemini_translator import GeminiTranslator
from .openai_translator import OpenAITranslator
from .groq_translator import GroqTranslator
from .deepseek_translator import DeepSeekTranslator
from .mistral_translator import MistralTranslator
from .cohere_translator import CohereTranslator
from .interfaze_translator import InterfazeTranslator
from .niutrans_translator import NiuTransTranslator
from .lmstudio_translator import LMStudioTranslator

TRANSLATORS = {
    "Claude (Anthropic)": ClaudeTranslator,
    "Gemini (Google)": GeminiTranslator,
    "GPT / Codex (OpenAI)": OpenAITranslator,
    "Groq (Llama / Mixtral)": GroqTranslator,
    "DeepSeek": DeepSeekTranslator,
    "Mistral": MistralTranslator,
    "Cohere": CohereTranslator,
    "Interfaze": InterfazeTranslator,
    "NiuTrans (牛翻译)": NiuTransTranslator,
    "LM Studio (Local)": LMStudioTranslator,
}
