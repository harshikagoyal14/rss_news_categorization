from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# Load pre-trained model and tokenizer
model_name = 'distilbert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Define keyword categories with example sentences
CATEGORIES = {
    "Terrorism / protest / political unrest / riot": "The protest was met with violence and political unrest.",
    "Positive/Uplifting": "The community celebrated the success of their initiatives.",
    "Natural Disasters": "The earthquake caused significant destruction and a natural disaster was declared."
}

def get_embedding(text):
    """
    Get the embedding of the given text.
    :param text: The text to embed
    :return: The embedding as a numpy array
    """
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embedding = outputs.last_hidden_state[:, 0, :].numpy()
    return embedding

def categorize_article(content):
    """
    Classify the article into one of the predefined categories based on embeddings.
    :param content: The content of the article
    :return: The category as a string
    """
    if not content.strip():  # Handle empty content case
        return "Others"

    content_embedding = get_embedding(content)

    best_category = "Others"
    best_similarity = -1  # Initialize similarity to a low value

    # Calculate cosine similarity with each category's embedding
    for category, example_sentence in CATEGORIES.items():
        category_embedding = get_embedding(example_sentence)
        similarity = cosine_similarity(content_embedding, category_embedding)[0][0]

        # If similarity is better, update best category
        if similarity > best_similarity:
            best_similarity = similarity
            best_category = category

    # Adding a threshold check to ensure a valid category is selected
    SIMILARITY_THRESHOLD = 0.1
    if best_similarity < SIMILARITY_THRESHOLD:
        return "Others"  # Return "Others" if no suitable category is found

    return best_category

# Example usage
if __name__ == "__main__":
    article_content = "The community came together to support each other after the devastating earthquake."
    category = categorize_article(article_content)
    print(f"The article is categorized as: {category}")
