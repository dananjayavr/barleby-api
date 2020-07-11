from flask import Flask, escape, request
from scraper import get_quotes_index, get_quotes_by_subject
from config import INDEXES
import random
import json

app = Flask(__name__)


@app.route('/')
def index():
    # Testing
    # Importing random Subject
    json_subjects = json.loads(get_quotes_index(random.choice(INDEXES)))['results']
    random_subject = random.choices(list(json_subjects.keys()))[0]
    random_subject_url = json_subjects[random_subject]

    return get_quotes_by_subject(random_subject, random_subject_url)
