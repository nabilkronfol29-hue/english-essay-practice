# English Essay Practice

A simple static website with 10 essay-writing practice questions, each based
on a "character change & theme" prompt (modeled on the Romeo and Juliet
example).

## How it works

- `index.html` lists all 10 questions.
- Each question page (`questions/q1.html`-`q10.html`) includes:
  - A link to the full text of the story/play (public domain, hosted on Wikisource).
  - The essay prompt and grading requirements.
  - A textarea to write your essay (auto-saved in your browser's local storage).
  - A **"Get Feedback & Score"** button that copies your essay + the grading
    rubric to your clipboard and opens [claude.ai](https://claude.ai/new) so
    you can paste it in and get a score with detailed feedback.

## Running locally

This is a static site with no build step. Open `index.html` directly in a
browser, or serve it locally:

```bash
python3 -m http.server 4321
```

Then visit `http://localhost:4321`.

## Publishing with GitHub Pages

1. Create a new repository on GitHub (e.g. `english-essay-practice`).
2. Push this folder to the repo (see commands below).
3. In the repo, go to **Settings -> Pages**, set "Source" to the `main`
   branch and `/ (root)` folder, then save.
4. Your site will be live at `https://<your-username>.github.io/english-essay-practice/`.

## Adding more questions

`generate_questions.py` was used to generate the question pages from a list
of texts/prompts. Edit the `QUESTIONS` list and re-run it to regenerate the
pages (it will overwrite `questions/qN.html` files).
