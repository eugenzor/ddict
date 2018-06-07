# Django based English learning helper

This project is made for my own purposes and for internal usage.
But probably it may be helpful for anyone who would like to learn or improve English.

This is set of utils which was helpful for me. Let's see what we have here:

1. Word stat with transcription
This is a list of words, ordered by frequency of usage. Each word has a transcription. You can check if you have
correct pronunciation of the most common words. E.g. it was a big surprise for me that one of the most common words "of"
should be pronounced like "əv" not "of". The word stat looks like this:
![Word stat](https://raw.githubusercontent.com/eugenzor/ddict/master/docs/example1.png)


You can also check yourself if all the most common words are in your vocabulary. If not you can add them to learning.


2. Sentences for a sound test
It selects randomly list of sentences per each sound. So you can read sentences for the native speaker and ask to rate
your sound pronunciation. Later you can return back to you problematic sounds and train them. The test sentences looks
like this:
![Sentences for a sound test](https://raw.githubusercontent.com/eugenzor/ddict/master/docs/example2.png)


3. Sentences the sound training
Since you have your sound rate you can focus on each particular sound and train it by pronouncing in different
words and sentences. It looks like this:
![Sentences the sound training](https://raw.githubusercontent.com/eugenzor/ddict/master/docs/example3.png)



## Installation
E.g. on Ubuntu 16.04

Create the virtualenv for the project:
```bash
virtualenv -p python3 ddict
cd ddict
source bin/activate
```

Clone the project:
```bash
git clone https://github.com/eugenzor/ddict`
```

Install the requirements
```bash
cd ddict
pip install -r requirements
```

Create the database structure
```bash
./manager.py makemigrations
```

Create a user for yourself
```bash
./manager.py createsuperuser
```

Go and find the dictionary with transcription in stardict format. You can find it somewhere in the Internet.
The Macmillan Dictionary is a very good dictionary. It has American pronunciation with international transcription.
You should find files with *.dict, *.idx and *.info. Copy all of them into the "sources" folder.

Then load the word stat:
```bash
./manager.py wordstat
```

Import transcription from the dictionary
```bash
./manager.py dictionary
```

Fill out the sounds:
```bash
./manager.py sounds
```

Import sentences from the dictionary
```bash
./manager.py import_sentences
```

Now everything is ready and you can run the dev server:
```bash
./manager.py runserver
```


## Usage
Open in browser http://localhost:8000/admin/ and log in.

Wordstat: http://localhost:8000/admin/ddict/word/

Sound trainer: http://localhost:8000/blender/

Create the csv table for rating your sounds (Should be rated by native speaker):
```bash
./manager.py sound_rate_csv > ~/sound_rate.csv
```

Create the sound test sentences:
```
./manager.py sentences > ~/train_sentences.txt
```

Enjoy learning
