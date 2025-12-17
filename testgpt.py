from transformers import GPT2Tokenizer, GPT2LMHeadModel

path = r"C:\Users\asgaj\models\gpt2"

tokenizer = GPT2Tokenizer.from_pretrained(path, local_files_only=True)
model = GPT2LMHeadModel.from_pretrained(path, local_files_only=True)

print("Model loaded successfully!")
