---
organization: Mistral AI
use_cases:
  - Mistral 7B, Mixtral, and other models are used by developers for custom applications—fine-tuning, hosting, and research.
  - Models are typically run locally or in private environments, avoiding centralized data handling.
  - Powers tools like “Le Chat” that emphasize user data control and transparency.
practices:
  - Mistral does not offer a centralized, hosted chatbot—models are downloaded and run in user environments.
  - Developers manage their own data; Mistral does not collect prompts, logs, or usage metadata.
  - All models are released with permissive open-source licenses, granting full control over deployment and data handling.
  - The inference library, `mistral-inference`, provides no telemetry or back‑channel communication to Mistral AI.
data_info:
  - Pretrained using publicly available sources; exact datasets not disclosed, but no proprietary user data involved.
concerning_practices:
  - Since there's no hosted interface, users must implement their own safety and moderation.
  - Mistral hasn’t released a detailed breakdown of training sources, though they’re believed to be open‑web data.
  - Responsibility for data security lies entirely with the deployer, not Mistral.
concerning_practices_urls:
  - https://github.com/mistralai/mistral-inference
  - https://www.techinasia.com/news/mistral-named-privacyfriendly-ai-google-ranks-report
severity: low
---

# Mistral Details
Privacy-first, open-weight models designed for developer control and on-premises deployment.
