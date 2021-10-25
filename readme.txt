An installation guide on how to setup your system
1. Download Anaconda at: https://www.anaconda.com/products/individual

2. Build anaconda environment from yml file, environment.yml. 
	a. conda env create -f environment.yml
	b. conda activate cz4045-2
	c. conda install spaCy
	d. python -m spacy download en_core_web_sm
    Note: fasttext package may need additional steps to install, please follow https://medium.com/@oleg.tarasov/building-fasttext-python-wrapper-from-source-under-windows-68e693a68cbb to successfully install fasttext

3. Dataset Analysis
	a. Tokenization, Stemming and POS tagging
		File name: tokenization.ipynb
		Purpose: Documentation of the process of tokenization, stemming and POS tagging.
		How to use: Run all cells
		Explanation of sample output: Provided in the notebook
		
	b. Writing Style
		
		File name: '3.2 Writing Style'/writing_style.ipynb
		Purpose: Documentation of the process of understanding writing styles
		How to use: Run all cells
		Explanation of sample output: Provided in the notebook
	
	c. Most Frequent (Noun - Adjective) Pairs for each rating
	
		File name: '3.2 Most Frequent Noun-Adj Pair'/2.4 Most Frequent (Noun - Adjective) Pairs.ipynb
		Purpose: Documentation of the process of retriving indicative noun-adjective pairs
		How to use: Run all cells
		Explanation of sample output: Provided in the notebook
	
4. Extraction of indicative adjective phrases

	File name: '3.3 Indicative Adjective Phrases'/indicative_adjective.ipynb
	Purpose: Documentation of the process of retrieving indicative adjective phrases
	How to use: Run all cells
	Explanation of sample output: Provided in the notebook

5. Application

	Folder name: last
	Purpose: Command line interface to generate text from prompt
	How to use: 1. Open Anaconda Prompt terminal
                    2. Ensure environment cz4045-2 is activated and 'last' folder is unzipped
                    3. Run this command: 'python run_eval.py --model_type=gpt2 --model_name_or_path=last/checkpoint-420000 --length=60 --repetition_penalty=2.0'
                    4. Type prompt and enter
	Explanation of sample output: Output text is automatically generated from our GPT2 model that is finetuned on Yelp dataset (full)

Directory:

├── 3.2\ Most\ Frequent\ Noun-Adj\ Pair
│   └── Most\ Frequent\ (Noun\ -\ Adjective)\ Pairs.ipynb
├── 3.2\ Writing\ Style
│   ├── __pycache__
│   │   ├── get_random_urls.cpython-39.pyc
│   │   └── get_urls.cpython-39.pyc
│   ├── get_urls.py
│   └── writing_style.ipynb
├── 3.3\ Indicative\ Adjective\ Phrases
│   ├── __pycache__
│   │   ├── _get_adj_phrases.cpython-39.pyc
│   │   └── get_adj_phrases.cpython-39.pyc
│   └── indicative_adjective.ipynb
├── data
│   ├── reviewSamples20.json
│   └── reviewSelected100.json
├── environment.yml
├── readme.txt
├── run_eval.py
├── run_lm_finetuning.py
├── test_trainer
└── tokenization.ipynb

