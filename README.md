# Industrial Machine Fault Diagnosis Expert System

## 1. Project Title and Introduction

### Project Title
**Industrial Machine Fault Diagnosis Expert System**

### Introduction
The Industrial Machine Fault Diagnosis Expert System is a Python-based artificial intelligence application designed to identify possible faults in industrial machinery based on symptoms and information provided by users.

The system uses a knowledge-based approach, in which machine-related knowledge is represented through assertions and IF-THEN rules. It processes user descriptions using Natural Language Processing (NLP) techniques and applies an inference engine to identify possible machine faults.

The application provides an interactive interface developed with Streamlit, allowing users to describe machine problems in ordinary English and receive possible diagnoses and recommendations.

The system covers ten categories of industrial machinery and is developed as an educational prototype to demonstrate the practical implementation of artificial intelligence and expert system concepts.

---

## 2. Project Objectives

The main objectives of this project are:

1. To develop an AI-based expert system for industrial machine fault diagnosis.
2. To represent machine knowledge using assertions and production rules.
3. To implement an inference engine that evaluates symptoms and identifies possible faults.
4. To allow users to describe machine problems using natural English sentences.
5. To implement Natural Language Processing techniques for recognizing machine-related symptoms.
6. To handle negation and contradictory information during symptom extraction.
7. To provide an interactive interface for entering symptoms and viewing diagnostic results.
8. To help users understand possible machine faults and their suggested solutions.

---

## 3. Technologies Used

The following technologies and tools are used in this project:

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Development of the interactive web interface |
| Natural Language Processing (NLP) | Processing and understanding user descriptions |
| Rule-Based Expert System | Knowledge representation and reasoning |
| Regular Expressions (Regex) | Text normalization and phrase matching |
| PowerShell | Project execution and environment management |
| Visual Studio Code | Source code editing and project development |

### Main Python Components

- Knowledge Base: Stores machine assertions and diagnostic rules.
- NLP Processor: Extracts relevant machine-related facts from user descriptions.
- Inference Engine: Evaluates recognized facts against predefined rules.
- Streamlit Interface: Provides interaction between the user and the expert system.

---

## 4. System Architecture

The system follows a modular architecture in which different components perform specific tasks.

### System Workflow

1. The user selects a machine category.
2. The user enters a description of the machine problem.
3. The NLP processor analyzes the description.
4. Relevant symptoms and facts are extracted.
5. The inference engine compares recognized facts with predefined diagnostic rules.
6. If all conditions of a rule are satisfied, the corresponding diagnosis is generated.
7. If some conditions are missing, the system can request additional symptom confirmation from the user.
8. The system displays diagnostic results and suggested solutions.

### Architecture Diagram

```text
              USER
                |
                v
       STREAMLIT INTERFACE
                |
                v
        NLP PROCESSOR
                |
                v
       FACT EXTRACTION
                |
                v
          KNOWLEDGE BASE
          /           \
         /             \
   ASSERTIONS          RULES
         \             /
          \           /
                |
                v
         INFERENCE ENGINE
                |
                v
        DIAGNOSIS RESULTS
                |
                v
       SUGGESTED SOLUTIONS
                |
                v
          USER INTERFACE
```

### Main System Components

- **User Interface:** Accepts machine categories and problem descriptions.
- **NLP Module:** Processes natural-language descriptions and extracts relevant facts.
- **Knowledge Base:** Contains machine-related assertions and diagnostic rules.
- **Inference Engine:** Applies logical reasoning to identify possible faults.
- **Diagnosis Module:** Presents possible diagnoses and suggested corrective actions.

---

## 5. Knowledge Base and Inference Engine

### Knowledge Base

The knowledge base is the central component of the expert system. It contains predefined information about industrial machine symptoms, causes, and possible diagnoses.

The current knowledge base contains:

- **300 assertions**
- **109 diagnostic rules**
- **10 machine categories**

The assertions are divided into three main types:

1. Symptoms: Observable signs of machine problems.
2. Causes: Possible reasons behind machine faults.
3. Diagnoses: Possible machine fault conditions.

### Machine Categories

The system supports the following ten categories:

1. Electric Motors
2. Gearboxes
3. Bearings
4. Conveyor Systems
5. Hydraulic Systems
6. Compressors
7. Electrical Systems
8. CNC Machines
9. Cooling Systems
10. General Mechanical Faults

Each category contains 30 assertions.

### Inference Engine

The inference engine evaluates recognized facts against the diagnostic rules stored in the knowledge base.

The system uses IF-THEN production rules.

**Example:**

```text
IF:
    Motor overheating
    AND Motor excessive vibration
    AND Motor unusual noise

THEN:
    Possible motor bearing failure
```

When all conditions of a rule are satisfied, the inference engine generates the corresponding diagnosis.

If some conditions are missing, the system can identify the missing symptoms and allow the user to confirm whether they are present.

The inference engine also considers negated and contradictory facts to avoid treating explicitly denied symptoms as positive evidence.

---

## 6. Natural Language Processing (NLP) Functionality

The system includes an NLP module that allows users to describe machine problems using ordinary English instead of requiring predefined assertion names.

### Main NLP Features

**1. Text Normalization**

The system normalizes user input to make text processing and phrase matching easier.

**2. Synonym Recognition**

The NLP processor uses additional phrases and synonyms to recognize different expressions describing similar machine problems.

Example:

```text
"The motor gives off a burning smell."

"Burning smell comes from motor."

"Motor smells burnt."
```

These descriptions can be mapped to the same assertion:

```text
motor_burning_smell
```

**3. Concept-Based Recognition**

The concept extension module provides additional phrase rewrites and component-related mappings to improve recognition of machine descriptions.

**4. Negation Detection**

The system distinguishes between positive and negative statements.

Example:

```text
Input:
"The motor is not overheating."

Recognized:
No positive overheating fact.

Negated:
motor_overheating
```

**5. Contradiction Handling**

The NLP processor identifies conflicting information in user descriptions and keeps contradictory facts separate from positive facts.

**6. Natural Language Input**

Users can describe problems in their own words, making the system easier to use for people who are not familiar with internal assertion names.

---

## 7. Installation and Setup Instructions

### Prerequisites

Before running the project, install:

- Python 3.10 or a compatible Python version.
- pip (Python package installer).
- A code editor such as Visual Studio Code.

### Step 1: Extract the Project

Extract the project folder to your computer.

Open the project folder in Visual Studio Code or PowerShell.

### Step 2: Create a Virtual Environment

Run:

```powershell
python -m venv venv
```

### Step 3: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the environment again.

### Step 4: Install Dependencies

Run:

```powershell
pip install -r requirements.txt
```

### Step 5: Run the Application

Execute:

```powershell
streamlit run interface/app.py
```

Streamlit will start the application and provide a local URL, usually:

```text
http://localhost:8501
```

Open this URL in your web browser to access the expert system.

---

## 8. How to Use the Application and Test the System

### Using the Application

1. Start the application using the Streamlit command.
2. Open the application in your browser.
3. Select the relevant machine category from the available options.
4. Enter a description of the machine problem in the input area.
5. Click the Analyze button.
6. Review the symptoms recognized by the NLP processor.
7. Review the possible diagnoses generated by the inference engine.
8. If the system identifies missing symptoms, review the suggested conditions and confirm the ones that are actually present.
9. Update the diagnosis to obtain the revised results.

### Example Input

```text
The motor is overheating, shaking heavily,
and making unusual grinding noises.
```

### Expected Processing

The NLP processor attempts to identify relevant facts, such as:

```text
motor_overheating
motor_excessive_vibration
motor_unusual_noise
```

The inference engine then checks whether the recognized facts satisfy any diagnostic rules.

### Testing and Validation

The project has been tested through:

- Knowledge base validation.
- Rule base validation.
- Natural-language symptom recognition.
- Negation detection.
- Positive and negative symptom combinations.
- Interactive confirmation of missing symptoms.
- Testing across different machine categories.

The knowledge base validation confirms 300 assertions across ten categories. The rule base validation confirms 109 rules with valid conditions, diagnoses, and unique rule IDs.

### Project Limitations

This project is an educational prototype and is not a replacement for professional industrial inspection or maintenance.

Its diagnostic accuracy depends on the quality of the knowledge base, predefined rules, and NLP recognition. Unrecognized descriptions or incomplete information may prevent the system from generating a diagnosis.

### Conclusion

The Industrial Machine Fault Diagnosis Expert System demonstrates how artificial intelligence techniques can be applied to industrial maintenance problems.

By combining a knowledge base, rule-based reasoning, natural-language processing, and an interactive interface, the project provides a practical demonstration of an expert system developed using Python.

The project also demonstrates important AI concepts, including knowledge representation, inference, fact extraction, and intelligent decision support.

---

**Project Type:** Academic Artificial Intelligence Project  
**Programming Language:** Python  
**Interface Framework:** Streamlit  
**Domain:** Industrial Machine Fault Diagnosis#   E x p e r t - S y t e m  
 #   E x p e r t - S y t e m  
 #   I n d u s t r i a l - M a c h i n e - E x p e r t - S y s t e m  
 