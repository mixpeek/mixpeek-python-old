# Mixpeek

Mixpeek let's you run full-text-search on your files

**Stuff you might be looking for**:

- [API Documentation](https://docs.mixpeek.com)
- [Installing Mixpeek](https://github.com/mixpeek/mixpeek-python#installation)
- [S3 Support](https://github.com/mixpeek/mixpeek-python#s3-support)
- [Bugs & Questions](https://github.com/mixpeek/mixpeek-python#bugs-&-questions)

## Quickstart

Upload any filetype from the supported filetype [list here](https://mixpeek.com/learn)

```python
from mixpeek import Mixpeek

mix = Mixpeek(api_key="API_KEY")

# index one local pdf document without any extra metadata
mix.index("/user/desktop/file.pdf")

# with extra metadata
mix.index(
    "/user/desktop/file.pdf",
    user_id="123",
    tags="document, legal",
    static_file_url="cdn.host.com/file.pdf",
    save=True,
    description="this is a cat"
)
```

...or any audio filetype

```python
mix.index("/user/desktop/never_gonna_give_you_up.mp3")
```

... or an image, video, document or [anything else mixpeek supports](https://mixpeek.com/learn)

```python
video = mix.index("/user/desktop/video.avi")
image = mix.index("/user/desktop/image.png")
markdown = mix.index("/user/desktop/markdown.md")
```

The API will return the `file_id`, be sure to store this:

```python
# response
{
    "file_id": "63a32cca0de5e4ce354a4b1c"
}
```

Now you can search across all your files:

```python
mix.search(query="let you down")

# response
[
    {
        "file_id": "6377c98b3c4f239f17663d79",
        "filename": "prescription.pdf",
        "importance": "100%",
        "static_file_url": "s3://audio.mp3"
    }
]

```

And you can include other parameters in your search query:

```python
mix.search(
    "readme",
    user_id="john_smith_123",
    context="true",
    tags="legal, document"
)

# response
[
    {
        "file_id": "63a32cd70de5e4ce354a4b1f",
        "filename": "system-design-primer.md",
        "static_file_url": "s3://audio.mp3",
        "user_id": "john_smith_123",
        "tags":["legal", "document"],
        "highlights": [
            {
                "texts": [
                    {
                        "type": "text",
                        "value": "- What is the expected "
                    },
                    {
                        "type": "hit",
                        "value": "read"
                    },
                    {
                        "type": "text",
                        "value": " to write ratio?\n\n"
                    }
                ]
            }
        ],
        "importance": "100%"
    }
]
```

## Installation

Installing mixpeek is easy

```shell
pip install git+https://github.com/mixpeek/mixpeek-python.git@master
```

## S3 Support

Be sure you create an AWS access key/secret key combo with S3 bucket read permissions using [this guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).

Files are never stored on our servers, review our [security principles](https://mixpeek.com/security).

```python
from mixpeek import Mixpeek

mix = Mixpeek(
    api_key="mixpeek_api_key",
    access_key="aws_access_key",
    secret_key="aws_secret_key",
    region="region"
)

mix.index_bucket("mixpeek-public-demo")

# response (list of File_ids)

{
    "file_ids": [
        "63a33611660c021b50271666",
        "63a33611660c021b50271667",
        "63a33611660c021b50271668",
        "63a33613660c021b50271669"
    ]
}

```

## Bugs & Questions

If this was helpful, please upvote [this StackOverflow comment](https://stackoverflow.com/a/69475102/5956579)

You can file bugs in our [github issues tracker](https://github.com/mixpeek/mixpeek-python/issues),
and ask any technical questions on
[Stack Overflow using the mixpeek tag](http://stackoverflow.com/questions/ask?tags=mixpeek).
We keep an eye on both.

## 🚀 Features

- Supports for `Python 3.8` and higher.
- Full text search
- AWS S3 Integration
- Fuzzy text matching

## Articles:

[Learning Center](https://mixpeek.com/learn)

## License ([MIT License](http://opensource.org/licenses/mit-license.php))

Copyright © 2022 Mixpeek, https://mixpeek.com

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
