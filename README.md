# Auto Git Clone

Automatically clone git repositories using Windows right click menu.

![Git Clone Here](https://user-images.githubusercontent.com/69170322/175966101-0d08ca53-6ba1-415e-b45c-8c70d9feb34e.png)

## How to Use

1. Copy the clone URL of the repository you want to clone.

![Copy Clone URL](https://user-images.githubusercontent.com/69170322/175967725-51e19a63-e73b-45a4-8f75-bdfbfbad578b.png)

2. Inside a folder in file explorer, right click -> 'Git Clone Here'.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

1. Open a terminal * **as an administrator** *.
   
2. Clone this repository:

```sh
git clone https://github.com/ArthurSudbrackIbarra/Auto-Git-Clone.git
```

3. Go to the repository directory:

```sh
cd Auto-Git-Clone
```

4. Install pip dependencies with:

```sh
pip install -r .\requirements.txt
```

5. Run add_to_reg.py script:

```sh
python add_to_reg.py
```

6. Done! Now, if you go to a folder in file explorer and right click inside it, you should be able to see the 'Git Clone Here' option.
