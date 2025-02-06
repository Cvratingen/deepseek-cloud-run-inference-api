from transformers import AutoModelForCausalLM, AutoTokenizer
AutoTokenizer.from_pretrained('deepseek-ai/deepseek-r1-distill-qwen-7b')
AutoModelForCausalLM.from_pretrained('deepseek-ai/deepseek-r1-distill-qwen-7b')