from settings import Settings


def test_settings_load_from_test_env() -> None:
    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "ml-app-test"
    assert settings.API_KEY == "fake-test-key"
