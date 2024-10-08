from pydantic_settings import BaseSettings, SettingsConfigDict


class SettingTest(BaseSettings):
    MODE: str
    DB_TEST_HOST: str
    DB_TEST_PORT: int
    DB_TEST_NAME: str
    DB_TEST_USER: str
    DB_TEST_PASS: str
    BASE_TEST_PATH: str

    @property
    def DB_TEST_URL(self) -> str:
        return (f"postgresql+asyncpg://{self.DB_TEST_USER}:{self.DB_TEST_PASS}@{self.DB_TEST_HOST}:"
                f"{self.DB_TEST_PORT}/{self.DB_TEST_NAME}")

    model_config = SettingsConfigDict(env_file="tests/.test.env")


config_test = SettingTest()
