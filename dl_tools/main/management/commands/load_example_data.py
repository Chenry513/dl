from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load example data into the database'

    def handle(self, *args, **kwargs):
        load_example_data()

# main/load_example_data.py
from django.contrib.auth.models import User
from main.models import ModelInfo, UserPreference

# main/load_example_data.py
from django.contrib.auth.models import User
from main.models import ModelInfo, UserPreference

def load_example_data():
    # Create example models
    models = [
        {
            "name": "ChatGPT",
            "organization": "OpenAI",
            "use_cases": "General-purpose AI",
            "practices": "Responsible AI",
            "data_info": "Uses diverse internet data for training",
            "concerning_practices": "May use data without explicit consent"
        },
        {
            "name": "Claude",
            "organization": "Anthropic",
            "use_cases": "Conversational AI",
            "practices": "Ethical AI",
            "data_info": "Trained on large-scale conversational data",
            "concerning_practices": "Potential bias in training data"
        },
        {
            "name": "Gemini",
            "organization": "Google DeepMind",
            "use_cases": "Research AI",
            "practices": "Transparent AI",
            "data_info": "Uses research papers and scholarly articles",
            "concerning_practices": "Data might not be anonymized"
        },
        {
            "name": "DALL-E",
            "organization": "OpenAI",
            "use_cases": "Image generation",
            "practices": "Creative AI",
            "data_info": "Trained on vast image datasets",
            "concerning_practices": "Risk of generating inappropriate images"
        },
        {
            "name": "BERT",
            "organization": "Google",
            "use_cases": "Natural language processing",
            "practices": "Linguistic AI",
            "data_info": "Utilizes text corpora for training",
            "concerning_practices": "May perpetuate existing biases in text"
        },
        {
            "name": "GPT-3",
            "organization": "OpenAI",
            "use_cases": "Text generation",
            "practices": "Innovative AI",
            "data_info": "Trained on a variety of internet texts",
            "concerning_practices": "May produce harmful or biased content"
        },
        {
            "name": "Mistral",
            "organization": "Mistral AI",
            "use_cases": "Text analysis",
            "practices": "Accurate AI",
            "data_info": "Analyzes text data for insights",
            "concerning_practices": "Potential misuse of sensitive data"
        },
        {
            "name": "Turing-NLG",
            "organization": "Microsoft",
            "use_cases": "Language understanding",
            "practices": "Robust AI",
            "data_info": "Trained on diverse language datasets",
            "concerning_practices": "Data privacy concerns"
        },
        {
            "name": "XLNet",
            "organization": "Google",
            "use_cases": "Sequence prediction",
            "practices": "Adaptive AI",
            "data_info": "Uses sequential data for predictions",
            "concerning_practices": "Might infer sensitive information"
        },
        {
            "name": "RoBERTa",
            "organization": "Facebook AI",
            "use_cases": "Text classification",
            "practices": "Efficient AI",
            "data_info": "Enhanced training on large text corpora",
            "concerning_practices": "Risk of data bias in outcomes"
        }
    ]

    # Clear existing data
    ModelInfo.objects.all().delete()
    UserPreference.objects.all().delete()

    # Create ModelInfo instances
    for model in models:
        ModelInfo.objects.create(**model)

    # Create example user
    user, created = User.objects.get_or_create(username="example_user", email="user@example.com")
    if created:
        user.set_password("password")
        user.save()

    # Create UserPreference instances
    for model in ModelInfo.objects.all():
        UserPreference.objects.create(user=user, model=model, preference=f"Preference for {model.name}")

    print("Example data loaded successfully.")