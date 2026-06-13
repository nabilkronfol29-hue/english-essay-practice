#!/usr/bin/env python3
"""One-off generator for the question pages. Run once, then can be deleted."""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

ROMEO_PROMPT = (
    "Using the play Romeo and Juliet by William Shakespeare, write a "
    "3-paragraph essay discussing how a main character changes throughout "
    "the course of the text to help develop the theme of the story."
)

QUESTIONS = [
    {
        "title": "Romeo and Juliet",
        "type": "play",
        "author": "William Shakespeare",
        "link": "https://en.wikisource.org/wiki/Romeo_and_Juliet",
        "prompt": ROMEO_PROMPT,
    },
    {
        "title": "A Christmas Carol",
        "type": "novella",
        "author": "Charles Dickens",
        "link": "https://en.wikisource.org/wiki/A_Christmas_Carol",
        "prompt": (
            "Using the novella A Christmas Carol by Charles Dickens, write a "
            "3-paragraph essay discussing how Ebenezer Scrooge changes "
            "throughout the course of the text to help develop the theme of "
            "the story."
        ),
    },
    {
        "title": "The Selfish Giant",
        "type": "short story",
        "author": "Oscar Wilde",
        "link": "https://en.wikisource.org/wiki/The_Happy_Prince_and_Other_Tales/The_Selfish_Giant",
        "prompt": (
            "Using the short story \"The Selfish Giant\" by Oscar Wilde, write "
            "a 3-paragraph essay discussing how the Giant changes throughout "
            "the course of the text to help develop the theme of the story."
        ),
    },
    {
        "title": "The Story of an Hour",
        "type": "short story",
        "author": "Kate Chopin",
        "link": "https://en.wikisource.org/wiki/The_Story_of_an_Hour",
        "prompt": (
            "Using the short story \"The Story of an Hour\" by Kate Chopin, "
            "write a 3-paragraph essay discussing how Louise Mallard changes "
            "throughout the course of the text to help develop the theme of "
            "the story."
        ),
    },
    {
        "title": "Rip Van Winkle",
        "type": "short story",
        "author": "Washington Irving",
        "link": "https://en.wikisource.org/wiki/Rip_Van_Winkle_(Irving)",
        "prompt": (
            "Using the short story \"Rip Van Winkle\" by Washington Irving, "
            "write a 3-paragraph essay discussing how Rip Van Winkle changes "
            "throughout the course of the text to help develop the theme of "
            "the story."
        ),
    },
    {
        "title": "The Most Dangerous Game",
        "type": "short story",
        "author": "Richard Connell",
        "link": "https://en.wikisource.org/wiki/The_Most_Dangerous_Game",
        "prompt": (
            "Using the short story \"The Most Dangerous Game\" by Richard "
            "Connell, write a 3-paragraph essay discussing how Rainsford "
            "changes throughout the course of the text to help develop the "
            "theme of the story."
        ),
    },
    {
        "title": "The Necklace",
        "type": "short story",
        "author": "Guy de Maupassant",
        "link": "https://en.wikisource.org/wiki/The_Necklace",
        "prompt": (
            "Using the short story \"The Necklace\" by Guy de Maupassant, "
            "write a 3-paragraph essay discussing how Mathilde Loisel changes "
            "throughout the course of the text to help develop the theme of "
            "the story."
        ),
    },
    {
        "title": "The Gift of the Magi",
        "type": "short story",
        "author": "O. Henry",
        "link": "https://en.wikisource.org/wiki/The_Gift_of_the_Magi",
        "prompt": (
            "Using the short story \"The Gift of the Magi\" by O. Henry, write "
            "a 3-paragraph essay discussing how Della changes throughout the "
            "course of the text to help develop the theme of the story."
        ),
    },
    {
        "title": "To Build a Fire",
        "type": "short story",
        "author": "Jack London",
        "link": "https://en.wikisource.org/wiki/To_Build_a_Fire",
        "prompt": (
            "Using the short story \"To Build a Fire\" by Jack London, write a "
            "3-paragraph essay discussing how the man changes throughout the "
            "course of the text to help develop the theme of the story."
        ),
    },
    {
        "title": "The Tell-Tale Heart",
        "type": "short story",
        "author": "Edgar Allan Poe",
        "link": "https://en.wikisource.org/wiki/The_Tell-Tale_Heart",
        "prompt": (
            "Using the short story \"The Tell-Tale Heart\" by Edgar Allan Poe, "
            "write a 3-paragraph essay discussing how the narrator changes "
            "throughout the course of the text to help develop the theme of "
            "the story."
        ),
    },
]

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Question {num}: {title} - English Essay Practice</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site-header">
  <span class="eyebrow">Literary Analysis Practice</span>
  <h1>English Essay Practice</h1>
  <p>Question {num} of {total}</p>
</header>
<main>
  <a class="back-link" href="index.html">&larr; Back to all questions</a>

  <div class="text-link-box">
    <a class="story-link" href="{link}" target="_blank" rel="noopener">Read: {title} ({type}) by {author} &#8599;</a>
    <div class="meta">Opens in a new tab (Wikisource).</div>
  </div>

  <div class="prompt-box">
    <h2>Essay Prompt</h2>
    <p>{prompt_html}</p>
  </div>

  <div class="requirements">
    <h2>Requirements</h2>
    <ul>
      <li>Three-paragraph essay (Introduction, Body, and Conclusion).</li>
      <li>Strong, explicit thesis statement that addresses the prompt. This must include the character change and a theme statement.</li>
      <li>Two pieces of evidence integrated in a seamless manner in the body paragraph &mdash; one example of how the character was at the beginning of the text, and one example of how the character changed by the end &mdash; with proper citations.</li>
      <li>Commentary explaining how and why the character change matters and how it helps develop the theme.</li>
    </ul>
  </div>

  <div class="rubric-section">
    <h2>Grading Rubric</h2>
    <p>Your essay will be graded against these three standards. Click each one to see what each performance level looks like.</p>
    <div id="rubric-container"></div>
  </div>

  <div class="essay-section">
    <h2>Your Essay</h2>
    <textarea id="essay" placeholder="Write your essay here..."></textarea>
    <div class="essay-controls">
      <span class="word-count" id="word-count">0 words</span>
      <button class="action-btn" id="copy-feedback-btn">Get Feedback &amp; Score</button>
      <button class="action-btn secondary" id="clear-btn">Clear Draft</button>
    </div>
    <div class="save-status" id="save-status"></div>
  </div>

  <div class="nav-buttons">
    <span>{prev_link}</span>
    <span>{next_link}</span>
  </div>
</main>
<footer>Drafts are saved automatically in your browser&rsquo;s local storage only.</footer>
<div class="toast" id="toast"></div>

<script>
  window.QUESTION_ID = "q{num}";
  window.QUESTION_PROMPT = {prompt_json};
</script>
<script src="rubric.js"></script>
<script>
  window.renderRubric(document.getElementById("rubric-container"));
</script>
<script src="script.js"></script>
</body>
</html>
"""

total = len(QUESTIONS)
questions_dir = ROOT

for i, q in enumerate(QUESTIONS, start=1):
    if i > 1:
        prev_link = f'<a href="q{i-1}.html">&larr; Question {i-1}</a>'
    else:
        prev_link = '<a href="index.html">&larr; All questions</a>'

    if i < total:
        next_link = f'<a href="q{i+1}.html">Question {i+1} &rarr;</a>'
    else:
        next_link = '<a href="index.html">Back to all questions &rarr;</a>'

    html = PAGE_TEMPLATE.format(
        num=i,
        total=total,
        title=q["title"],
        type=q["type"],
        author=q["author"],
        link=q["link"],
        prompt_html=q["prompt"],
        prompt_json=json.dumps(q["prompt"]),
        prev_link=prev_link,
        next_link=next_link,
    )

    out_path = os.path.join(questions_dir, f"q{i}.html")
    with open(out_path, "w") as f:
        f.write(html)
    print("wrote", out_path)
