# mixpeek.py
import requests
import json


class Mixpeek:
    def __init__(self, api_key):
        self.base_url = "http://localhost:8000"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        self.generate = self.Generate(self)
        self.parse = self.Parse(self)

    def _send_post(self, url, payload):
        return requests.post(url, headers=self.headers, data=json.dumps(payload)).json()

    def _send_get(self, url):
        return requests.get(url, headers=self.headers).json()

    class Generate:
        def __init__(self, mixpeek):
            self.mixpeek = mixpeek
            self.openai = self.OpenAI(self.mixpeek)

        class OpenAI:
            def __init__(self, mixpeek):
                self.mixpeek = mixpeek
                self.generate_openai_url = f"{self.mixpeek.base_url}/generate"

            def _construct_request_format(
                self, model, context, response_format, settings=None
            ):
                payload = {
                    "model": {"provider": "gpt", "model": model},
                    "context": context,
                    "messages": [{"role": "user", "content": ""}],
                    **settings,
                }

                if response_format is not None:
                    json_schema = response_format.model_json_schema()
                    payload["response_format"] = json_schema

                return payload

            def chat(self, model, response_format, context, settings=None):
                payload = self._construct_request_format(
                    model, context, response_format, settings
                )
                return self.mixpeek._send_post(self.generate_openai_url, payload)

    class Parse:
        def __init__(self, mixpeek):
            self.mixpeek = mixpeek
            self.text = self.Text(self.mixpeek)

        class Text:
            def __init__(self, mixpeek):
                self.mixpeek = mixpeek
                self.parse_url = f"{self.mixpeek.base_url}/parsers"

            def extract(self, file_url, should_chunk=True):
                url = self.parse_url + "?should_chunk=" + str(should_chunk)
                return self.mixpeek._send_post(url, {"file_url": file_url})

            def chunk(self, corpus):
                pass

        class Index:
            def __init__(self):
                pass
