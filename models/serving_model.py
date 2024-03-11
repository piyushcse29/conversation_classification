
from transformers import RobertaTokenizerFast, AutoModelForSequenceClassification
from peft import LoraConfig, TaskType, PeftModel

lora_config = LoraConfig(
    r=32, # Rank
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.SEQ_CLS
)

# Load the trained model from local
model = AutoModelForSequenceClassification.from_pretrained('roberta-base', num_labels = 5)
tokenizer = RobertaTokenizerFast.from_pretrained('roberta-base', max_length = 512)
peft_model = PeftModel.from_pretrained(model,'models/artifacts/peft-conversation-classification-local', local_files_only=True)


def predict_scenario(text):
    # Tokenize the input
    tokenized = tokenizer(text, return_tensors='pt', padding = True, truncation=True)

    # Predict using the trained model
    output = peft_model(**tokenized)
    print(output)
    prediction = output.logits.argmax(dim=-1).item()

    return prediction

# test the model
#print(predict_scenario("Asking about how Clare works or if Clare calls via phone or WhatsApp."))  # 0