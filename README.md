
---

# Github PR Summarizer Bot ➤

> “PRs too long? TL;DR got you :)"

---

## Overview ➤

A smart **GitHub Pull Request Summarizer** powered by **Gemini 2.5 Flash**. Automatically generates PR summaries using the PR description and code changes.

---

## How It Works ➤

1. **Trigger:** GitHub Actions runs whenever a PR is opened.
2. **Data Collection:** The bot reads the PR number and repository name from environment variables.
3. **Processing:** It fetches the PR description and code diff.
4. **Summary Generation:** Passes the data to **Gemini 2.5 Flash** to produce a summary.
5. **Output:** The generated summary is posted directly in the PR conversation.

---

## Setup ➤

1. **Clone or add** this repository to any project.

2. Go to **Settings > Secrets and Variables > Actions** in your repository.

3. Add a new secret:

   ```
   GEMINI_API_KEY = <your-gemini-api-key>
   ```

4. **Done!** The bot will automatically trigger on new PRs and post summaries in the PR conversation.

---
