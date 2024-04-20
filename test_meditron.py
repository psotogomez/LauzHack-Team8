# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="epfl-llm/meditron-7b")

