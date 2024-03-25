from mixpeek import Mixpeek

mixpeek = Mixpeek(api_key="API_KEY")

embedding = mixpeek.embed.text("Hello, world!")

print(embedding)
