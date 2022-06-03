import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wlb-utils",
    version="0.0.1",
    author="我的代码温柔如风",
    author_email="liukunup@outlook.com",
    maintainer="我的代码温柔如风",
    maintainer_email="liukunup@outlook.com",
    description="愿这套工具给您的工作和生活带来平衡～",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liukunup/wlb-utils",
    project_urls={
        "Bug Tracker": "https://github.com/liukunup/wlb-utils/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.5",
    setup_requires=[
        'pytz',
    ],
    tests_require=[
        'unittest',
    ],
)
