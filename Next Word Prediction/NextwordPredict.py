import random

def train_markov_chain(text, order=1):
    words = text.split()
    markov_chain = {}

    for i in range(len(words) - order):
        prefix = tuple(words[i:i + order])
        suffix = words[i + order]
        if prefix in markov_chain:
            markov_chain[prefix].append(suffix)
        else:
            markov_chain[prefix] = [suffix]

    return markov_chain

def generate_next_word(markov_chain, prefix):
    if prefix in markov_chain:
        return random.choice(markov_chain[prefix])
    else:
        return None

if __name__ == "__main__":
    # Example text
    text = "This is a simple example text for next word prediction. Next word prediction is interesting."

    # Train the Markov chain model
    markov_chain = train_markov_chain(text)

    # Prefix to predict the next word
    prefix = tuple("next word".split())

    # Generate next word
    next_word = generate_next_word(markov_chain, prefix)

    if next_word:
        print(f"The next word after '{' '.join(prefix)}' is '{next_word}'.")
    else:
        print("No prediction available.")
