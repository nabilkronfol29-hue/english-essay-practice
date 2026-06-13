// Shared grading rubric used on every question page.
// Levels are ordered from highest to lowest.

window.RUBRIC = [
  {
    code: "RL1",
    title:
      "Cite strong and thorough textual evidence to support analysis of what the text says explicitly as well as inferences drawn from the text.",
    levels: [
      {
        name: "Exhibiting Depth",
        points: 4,
        desc:
          "You cite effective and highly elaborated textual evidence to support analysis of explicit meaning and inferences. Evidence can easily be labeled as the best piece(s) of supporting evidence.",
      },
      {
        name: "Achieving",
        points: 3,
        desc:
          "You cite specific textual detail to support analysis. The evidence is strong, but there was other evidence that would have strengthened your claim, OR you should have picked out the most important piece of the evidence provided (may have been too wordy).",
      },
      {
        name: "Approaching",
        points: 2,
        desc:
          "You make general reference to the text to support your explanations. You did not properly introduce and/or cite your textual evidence; situational context may be vague.",
      },
      {
        name: "Beginning",
        points: 1,
        desc:
          "You summarize mostly explicit details. You make minimal reference to the text to support your summary; situational context is missing.",
      },
      {
        name: "Did Not Demonstrate",
        points: 0,
        desc: "There is no written analysis. You do not cite any evidence from the text.",
      },
    ],
  },
  {
    code: "RL3",
    title:
      "Analyze how complex characters (e.g., those with multiple or conflicting motivations) develop over the course of a text, interact with other characters, and advance the plot or develop the theme.",
    levels: [
      {
        name: "Exhibiting Depth",
        points: 4,
        desc:
          "Clearly explain how the character changes in a meaningful way. Shows a deep understanding of what causes the change and how it connects to the theme of the story. Analysis is thoughtful and connects the evidence back to the thesis. Commentary explains how and why the change matters.",
      },
      {
        name: "Achieving",
        points: 3,
        desc:
          "Explains how the character changes. Shows a good understanding of what causes the change and connects it to the theme. Analysis supports the thesis and shows clear thinking. Commentary explains why the change is important, even if it isn't very detailed.",
      },
      {
        name: "Approaching",
        points: 2,
        desc:
          "Explains how the character changes, but ideas may be unclear or too simple. Connection to theme is present but underdeveloped or vague. Some analysis is present, but it doesn't fully support the thesis or is hard to follow. Commentary is brief or unclear—it may say what happened, but not why it matters.",
      },
      {
        name: "Beginning",
        points: 1,
        desc:
          "The character change is mentioned but not explained clearly. The theme may be incorrect, off-topic, or not clearly connected to the change. Little to no analysis is present; evidence may be listed but not explained. Commentary is missing or doesn't help the reader understand the character's development.",
      },
      {
        name: "Did Not Demonstrate",
        points: 0,
        desc:
          "Does not describe the character's change or gets it wrong. No connection to the theme or thesis. No real analysis—just summary or off-topic ideas. Commentary is missing or completely unrelated to the task.",
      },
    ],
  },
  {
    code: "W4",
    title:
      "Produce clear and coherent writing in which the development, organization, and style are appropriate to task, purpose, and audience.",
    levels: [
      {
        name: "Exhibiting Depth",
        points: 4,
        desc:
          "The essay demonstrates an insightful understanding of the character's change and its connection to the theme. Writing is fully developed and logically organized with a sophisticated introduction, focused body paragraph, and purposeful conclusion. The thesis is precise and thought-provoking. Evidence is smoothly integrated and skillfully analyzed. Style and tone are highly appropriate for academic writing.",
      },
      {
        name: "Achieving",
        points: 3,
        desc:
          "The essay clearly explains the character's change and how it develops the story's theme. It has a well-structured introduction, body paragraph, and conclusion. The thesis is clear and addresses the prompt directly. Evidence is clearly integrated and explained. Writing style is appropriate and consistent for the task and audience.",
      },
      {
        name: "Approaching",
        points: 2,
        desc:
          "The essay addresses the character's change but may be vague in connecting it to the theme. Structure is mostly clear but may be uneven or underdeveloped. The thesis may be present but too general. Evidence is included but may be awkwardly integrated or not fully explained. Style may occasionally shift or lack formality.",
      },
      {
        name: "Beginning",
        points: 1,
        desc:
          "The essay attempts to address the prompt but lacks clear development or organization. Paragraphs may be incomplete or off-task. The thesis may be missing or unclear. Evidence is minimal, dropped in without explanation, or not cited. Style is inconsistent and lacks academic tone.",
      },
      {
        name: "Did Not Demonstrate",
        points: 0,
        desc:
          "The writing does not address the task or is incomplete. There is no clear thesis or organization. No relevant evidence is provided. Writing may be off-topic or inappropriate for academic purposes.",
      },
    ],
  },
];

// Build a plain-text version of the rubric for the Claude grading prompt.
window.buildRubricText = function () {
  const lines = [];
  window.RUBRIC.forEach(function (standard) {
    lines.push(standard.code + " — " + standard.title);
    standard.levels.forEach(function (level) {
      lines.push("  - " + level.name + " (" + level.points + " pts): " + level.desc);
    });
    lines.push("");
  });
  return lines.join("\n");
};

// Render the rubric as an accordion into the given container element.
window.renderRubric = function (container) {
  if (!container) return;
  window.RUBRIC.forEach(function (standard) {
    const details = document.createElement("details");
    details.className = "rubric-standard";

    const summary = document.createElement("summary");
    summary.innerHTML = "<strong>" + standard.code + "</strong> — " + standard.title;
    details.appendChild(summary);

    const list = document.createElement("dl");
    list.className = "rubric-levels";
    standard.levels.forEach(function (level) {
      const dt = document.createElement("dt");
      dt.textContent = level.name + " (" + level.points + " pts)";
      const dd = document.createElement("dd");
      dd.textContent = level.desc;
      list.appendChild(dt);
      list.appendChild(dd);
    });
    details.appendChild(list);

    container.appendChild(details);
  });
};
