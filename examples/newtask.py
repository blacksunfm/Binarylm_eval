YAML_boolq_string = """
task: demo_vuldetect
dataset_path: realvul
dataset_name: LineVul_Test_Dataset
output_type: multiple_choice
training_split: train
validation_split: validation
doc_to_text: "{{passage}}\nQuestion: {{question}}?\nAnswer:"
doc_to_target: label
doc_to_choice: ["no", "yes"]
should_decontaminate: true
doc_to_decontamination_query: passage
metric_list:
  - metric: acc
"""
with open("boolq.yaml", "w") as f:
    f.write(YAML_boolq_string)