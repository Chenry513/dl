---
organization: Meta (Facebook's parent company)
use_cases:
  - Initially released under a non-commercial license to help academic researchers study LLMs.
  - Despite restrictions, LLaMA has been widely used as a base for various chatbots, productivity tools, and coding assistants.
  - Developers often fine-tune LLaMA models for specific tasks like customer service, healthcare insights, and creative writing.
practices:
  - Meta states that LLaMA was trained on publicly available data, including books, web pages, and other internet sources. This includes user-generated content that may not have been intended for such use.
  - LLaMA itself doesn’t collect data, but when integrated into third-party tools, user inputs may be logged and used by developers unless opt-outs are provided.
  - As of Meta's official documentation, LLaMA is not fine-tuned on user interactions unless the organization using it does so independently.
  - Meta has not published the full training dataset, citing proprietary considerations, raising concerns about transparency and consent.
data_info:
    - Personal info (emails, social media posts scraped without permission).
    - Copyrighted books/articles (used without paying the authors).  
concerning_practices:
  - Used Facebook/Instagram posts without asking users.
  - Leaked version lets anyone generate harmful content.
  - If your info was scraped, it's stuck in the model forever.
concerning_practices_urls:
  - https://www.vice.com/en/article/facebooks-powerful-large-language-model-leaks-online-4chan-llama/
  - https://www.theverge.com/2022/11/28/23481786/meta-fine-facebook-data-leak-ireland-dpc-gdpr
severity: high
---

# LLaMA 2 Details
Meta's open-source large language model.