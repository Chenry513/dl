---
title: LLM Entry Instructions
description: Explanation of each field for LLM database entries
---

# LLM Entry Instructions

This file describes what should be entered for each section in a model entry.

---

organization:
- The name of the company, organization, or group that created or maintains the LLM.
- Example: OpenAI, Google (DeepMind), Anthropic, Mistral AI.

use_cases:
- A list of what the LLM is commonly used for.
- Each item should start with a short bolded phrase and then a clear explanation.
- Focus on real-world uses like chatbots, writing tools, developer aids, or enterprise integrations.

practices:
- Describe what the organization does with user data when someone uses the model.
- Include whether data is collected, whether it is used for training, whether humans can review it, and how long it is stored.
- Mention if there are opt-out options or special settings.

data_info:
- Explain what kind of data the model was trained on.
- List types like web pages, books, licensed datasets, or internal data.
- If exact sources are not known, say so clearly.

concerning_practices:
- List specific ways the company or model might mishandle or over-collect data.
- These should be supported by public information.
- Mention things like default data collection, unclear deletion policies, human review without consent, or prior security issues.

concerning_practices_urls:
- Provide direct links to articles, documentation, or reports that support the concerns listed.
- Use reliable sources such as official documentation, major news outlets, or security analyses.

severity:
- Choose one of the following:
  - low: The model does not collect user data by default and gives users full control over data use.
  - medium: The model may collect or retain some data, but users have meaningful ways to limit or delete it.
  - high: The model collects data by default, may store it indefinitely, lacks clear opt-out options, or has had leaks or breaches.

# [Model Name] Details
Write a one-line summary that describes what the model is and what makes it notable.
