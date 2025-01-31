# Automatic Evaluation of Tutor Responses Using Large Language Models

This project presents an automatic evaluation framework for assessing the pedagogical effectiveness of tutor responses using prompting and fine-tuning techniques. The framework evaluates tutor responses based on four key rubrics:

1. **Do not reveal the answer**
2. **Promote active engagement**
3. **Communicate with positive tone**
4. **Address and Identify misconceptions**

## Overview

We utilize the Bridge and MathDial datasets, which contain real-life student-teacher dialogues and synthetic conversations. These datasets have been manually annotated according to the defined rubrics. Our approach involves prompting large language models of various sizes and methods to evaluate these rubrics. We then compare the models' predictions with human annotations to assess their performance.

In addition to prompting, we explore a fine-tuning approach to determine if performance improvements can be made, particularly for the rubric "Communicate with positive tone." As a practical application, we rate the tutors in the Bridge and MathDial datasets to assess their pedagogical effectiveness according to the rubrics.

![alt text]([https://github.com/babypoby/bachelorarbeit/images/plan.png](https://github.com/babypoby/bachelorarbeit/blob/main/images/plan.png))

This work was part of my Bachelor's thesis at ETH Zurich, completed in January 2025.

## Project Structure
project-root/
│
├── data-visualisation/
│ └── # Code for generating matplotlib graphs used in the thesis
│
├── datasets/
│ └── # Raw, filtered, and annotated datasets
│
├── datasources/
│ └── # References to MathDial and Bridge repositories
│
├── finetuning/
│ └── # Code for the fine-tuning approach
│
├── images/
│ └── # Graphs used in the thesis
│
├── label-web-bridge/
│ └── # Annotation interface and data processing code for MathDial and Bridge datasets
│
├── prompt_eval/
│ └── # Code for the prompting approach
│
└── README.md
