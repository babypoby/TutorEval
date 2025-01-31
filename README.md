# 🎓 Automatic Evaluation of Tutor Responses Using Large Language Models

This project introduces an **automatic evaluation framework** designed to assess the pedagogical effectiveness of tutor responses using prompting and fine-tuning approaches. Our framework evaluates tutor responses based on four key rubrics:

### 📋 Evaluation Rubrics:

1. **Do not reveal the answer** 
2. **Promote active engagement** 
3. **Communicate with positive tone** 
4. **Identify and address misconceptions** 

## 🔍 Overview

We use the Bridge and MathDial datasets, consisting of real-life student-teacher dialogues and synthetic conversations, manually **annotated** based on rubrics. We utilize large language models of different sizes and methods to evaluate these rubrics.

1. We **prompt** language models to evaluate the dialogues according to the rubrics.
2. We showcase a **practical application**, by rating tutors in the Bridge and MathDial datasets according to the rubrics.
3. We **fine-tune** models to check if this improves performance for the rubric "Communicate with positive tone."

For the performance evaluation, we compare the models' performance with human annotations to evaluate their accuracy in predicting human-like judgments.

![Project Plan](https://github.com/babypoby/bachelorarbeit/blob/main/images/plan.png)

> **Note:** This work was part of my Bachelor's thesis at **ETH Zurich**, completed in **January 2025**.

---

### 📂 Project Structure

```plaintext
project-root/
├── data-visualisation/
│   └── Code for generating matplotlib graphs used in the thesis
├── datasets/
│   └── Raw, filtered, and annotated datasets
├── datasources/
│   └── References to MathDial and Bridge repositories
├── finetuning/
│   └── Code for the fine-tuning approach
├── images/
│   └── Graphs used in the thesis
├── label-web-bridge/
│   └── Annotation interface and data processing code for MathDial and Bridge datasets
├── prompt_eval/
│   └── Code for the prompting approach
└── README.md
```
