import os
from mixpeek import Mixpeek

# test stuff
api_key = "Much3A6xrsFTC2Oaf2wuLY314S-lE8eJlB0vFujCaa2kA89ALOpvzUOyFptNy03WPHM"
sample_file = "/Users/ethan/Desktop/Business/Mixpeek_2022/mixpeek_demo/prescription.pdf"

# s3 stuff
s3_bucket = "mixpeek-public-demo"
aws_access_key = "AKIA5RWB335C76XEXX4U"
aws_secret_key = "vEEznZasiOZY8TIZJVs7qHTlaYKdnKb6C7SKPR3u"
region = "us-east-2"


def run():
    # class init
    mix = Mixpeek(api_key=api_key)

    # index one file
    r = mix.index(sample_file, user_id="billy bob", tags="bob, is, a, dweeb",
                  static_file_url="s3://file.pdf", save=True)
    print(r)

    # # s3 bucket
    # s3_mix = Mixpeek(
    #     api_key=api_key,
    #     access_key=aws_access_key,
    #     secret_key=aws_secret_key,
    #     region=region
    # )

    # # index bucket
    # p = s3_mix.index_bucket(s3_bucket)
    # print(p)

    # # search

    # s = mix.search("test", user_id="john_smith_123",
    #                context="true", semantics="true")
    # print(s)


if __name__ == '__main__':
    run()
