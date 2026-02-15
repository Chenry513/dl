---
organization: OpenAI
use_cases:
  - Used for general-purpose questions, tutoring, and summarizes content.
  - Integrated into workflows for coding assistance (Codex) and software automation.
  - Used in classrooms, personal projects, and creative writing tools.
practices:
  - ChatGPT improves its performance by training on conversations unless the user opts out through OpenAI’s privacy portal.
  - Users must explicitly disable training by navigating to the “Do Not Train on My Content” setting; it’s not off by default for individual users.
  - This special mode prevents the conversation from being saved, remembered, or used for training.
  - Even if you’ve opted out, giving a thumbs up/down still allows OpenAI to use that full conversation for training.
  - ChatGPT Team, Enterprise, and API users are opted out by default unless they explicitly opt in to data sharing.
data_info:
  - Includes web pages, documents, and optionally, user interactions if opted in.
concerning_practices:
  - A Redis bug exposed names, emails, payment addresses, and partial credit card details of ChatGPT Plus users to other users.
  - Conversations are stored and used to improve models unless users opt out.
  - Opt-out is buried in the privacy portal; feedback interactions still override training controls.
  - Users have no clear way to know what data was used in model training or whether their information is still stored.
concerning_practices_urls:
  - https://openai.com/index/march-20-chatgpt-outage/
  - https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance
severity: high
---

# GPT-4 Details
The latest flagship model from OpenAI.
