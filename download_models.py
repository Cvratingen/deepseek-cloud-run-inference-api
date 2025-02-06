from transformers import AutoModelForCausalLM, AutoTokenizer
AutoModelForCausalLM.from_pretrained('deepseek-ai/deepseek-r1-distill-qwen-7b')
AutoTokenizer.from_pretrained('deepseek-ai/deepseek-r1-distill-qwen-7b')