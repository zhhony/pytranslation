import setuptools  # 导入setuptools打包工具

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="translation-pkg-zhhony",  
    version="0.0.1",  # 包版本号
    author="zhhony",  # 作者
    author_email="zhhony@126.com",  # 联系方式
    description="",  # 包的简述
    long_description=long_description,  # 包的详细介绍
    long_description_content_type="text/markdown",
    url="https://github.com/zhhony/pytranslation.git",  # 项目地址
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',  # 对python的最低版本要求
)
