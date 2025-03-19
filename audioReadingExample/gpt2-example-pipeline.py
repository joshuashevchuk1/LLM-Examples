# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="openai-community/gpt2")


print(pipe("i have a dog",max_length=30,num_return_sequences=1,truncation=True))

print(pipe("i have a dog",max_length=30,num_return_sequences=5,truncation=True))