YAML_string = """
task: realvul
dataset_path: realvul
dataset_name: null
dataset_kwargs:
  test: F:/LLMs/dataset/realvul/test-00000-of-00004.parquet
output_type: multiple_choice
training_split: null
validation_split: null
test_split: test
doc_to_text: "{{code}}\nQuestion: Is there any vulnerability in the code segment?\nAnswer:"
doc_to_target: target
doc_to_choice: ["0", "1"]
should_decontaminate: true
doc_to_decontamination_query: code
metric_list:
  - metric: acc
"""
with open("examples/realvul.yaml", "w") as f:
    f.write(YAML_string)