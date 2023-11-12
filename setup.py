from setuptools import setup, find_packages

setup(
    name='math-quiz',
    version='0.1.dev6+g7fd7d2f',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'setuptools==68.2.2',
        'wheel==0.41.3',
    ],
    entry_points={
        'console_scripts': [
            'math-quiz = math_quiz.module:main_function',
        ],
    },
    author='Zixuan Chai',
    author_email='zixuanchai_czx@outlook.com',
    description=' math quiz project',
    long_description='',
    url='https://github.com/zixuanccc/dsss_homework_2.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    use_scm_version=True,
)
