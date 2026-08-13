from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Централизованная конфигурация проекта.

    Значения читаются из .env (или из переменных окружения — они всегда
    имеют приоритет над .env, это удобно для Docker/CI).
    Если обязательное поле отсутствует — приложение упадёт СРАЗУ при
    старте, с понятным сообщением, а не посреди диалога с пользователем.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # --- обязательные ключи ---
    groq_api_key: str = Field(..., description="API-ключ Groq (console.groq.com)")
    tavily_api_key: str = Field(..., description="API-ключ Tavily (app.tavily.com)")

    # --- необязательные настройки с дефолтами ---
    model_name: str = Field(
        default="openai/gpt-oss-20b",
        description="Модель, которую использует ChatGroq",
    )
    log_level: str = Field(default="INFO", description="Уровень логирования")


# Единственный экземпляр настроек на всё приложение.
# Создаётся один раз при первом импорте — и сразу же валидируется.
settings = Settings()