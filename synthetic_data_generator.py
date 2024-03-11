# synthetic_data_generator.py

import pandas as pd
import random

random.seed(42)  # for reproducibility

def generate_synthetic_data(num_samples=1000):
    scenarios = ["Regular", "Product-Related", "Subscription-Related", "Suicide", "Non-Mental Health"]
    texts = []
    labels = []

    for _ in range(num_samples):
        scenario = random.choice(scenarios)

        if scenario == "Regular":
            text = "Engaging in a regular mental health conversation."
        elif scenario == "Product-Related":
            text = "Asking about how Clare works or if Clare calls via phone or WhatsApp."
        elif scenario == "Subscription-Related":
            text = "Inquiring about subscription details and trial duration."
        elif scenario == "Suicide":
            text = "Expressing thoughts or plans related to suicide."
        elif scenario == "Non-Mental Health":
            text = "Clare's favorite movies or non-mental health topics."

        texts.append(text)
        labels.append(scenarios.index(scenario))

    data = pd.DataFrame({"text": texts, "label": labels})
    data.to_csv("data/synthetic_data.csv", index=False)

if __name__ == "__main__":
    generate_synthetic_data()
