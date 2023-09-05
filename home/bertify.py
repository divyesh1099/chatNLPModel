# from transformers import T5ForConditionalGeneration, T5Tokenizer
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# model = T5ForConditionalGeneration.from_pretrained('home/model', from_tf=True)
# tokenizer = T5Tokenizer.from_pretrained('home/tokenizer')

# def generate_answer(question):
#     input_text = question + " </s>"
#     input_ids = tokenizer.encode(input_text, return_tensors="pt")
#     output = model.generate(input_ids)
#     answer = tokenizer.decode(output[0], skip_special_tokens=True)
#     return answer

# def generate_summary(text_to_summarize):
#     input_text = "Summarize the following: " + text_to_summarize + " </s>"
#     input_ids = tokenizer.encode(input_text, return_tensors="pt")
#     output = model.generate(input_ids)
#     answer = tokenizer.decode(output[0], skip_special_tokens=True)
#     return answer


# GPT2 Model 
model_path = "gpt2model"  # Replace with the actual path
tokenizer = GPT2Tokenizer.from_pretrained("./gpt2model")
model = GPT2LMHeadModel.from_pretrained("./gpt2model")

def generate_answer(question):
    input_ids = tokenizer.encode(question, return_tensors="pt")

    # Generate a response
    with torch.no_grad():
        output = model.generate(input_ids, max_length=100, num_return_sequences=1)

    # Decode and print the response
    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    return answer

def generate_summary(text_to_summarize):
    input_text = "Summarize the following: " + text_to_summarize + "</s>"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    # Generate a response
    with torch.no_grad():
        output = model.generate(input_ids, max_length=100, num_return_sequences=1)
    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    return answer