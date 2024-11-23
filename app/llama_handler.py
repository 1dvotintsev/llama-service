import subprocess

def query_model(prompt: str) -> str:
    """
    Вызывает модель Llama через Ollama CLI и возвращает результат.
    """
    try:
        # Запуск команды Ollama
        result = subprocess.run(
            ["ollama", "run", "llama"],
            input=prompt,
            text=True,
            capture_output=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Ошибка при запуске модели: {e.stderr.strip()}")
