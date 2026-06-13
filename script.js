// Shared logic for essay question pages.
// Each question page sets `window.QUESTION_ID` and `window.QUESTION_PROMPT`
// before loading this script.

(function () {
  const id = window.QUESTION_ID;
  if (!id) return;

  const textarea = document.getElementById("essay");
  const wordCountEl = document.getElementById("word-count");
  const saveStatusEl = document.getElementById("save-status");
  const copyBtn = document.getElementById("copy-feedback-btn");
  const clearBtn = document.getElementById("clear-btn");
  const toast = document.getElementById("toast");

  const storageKey = "essay-practice:" + id;
  let saveTimeout = null;

  function countWords(text) {
    const trimmed = text.trim();
    if (!trimmed) return 0;
    return trimmed.split(/\s+/).length;
  }

  function updateWordCount() {
    const words = countWords(textarea.value);
    wordCountEl.textContent = words + (words === 1 ? " word" : " words");
  }

  function showToast(message) {
    toast.textContent = message;
    toast.classList.add("show");
    setTimeout(() => toast.classList.remove("show"), 2500);
  }

  // Load saved draft
  const saved = localStorage.getItem(storageKey);
  if (saved) {
    textarea.value = saved;
  }
  updateWordCount();

  textarea.addEventListener("input", function () {
    updateWordCount();
    saveStatusEl.textContent = "";
    clearTimeout(saveTimeout);
    saveTimeout = setTimeout(function () {
      localStorage.setItem(storageKey, textarea.value);
      saveStatusEl.textContent = "Draft saved.";
    }, 600);
  });

  if (clearBtn) {
    clearBtn.addEventListener("click", function () {
      if (!confirm("Clear your draft for this question? This cannot be undone.")) return;
      textarea.value = "";
      localStorage.removeItem(storageKey);
      updateWordCount();
      saveStatusEl.textContent = "Draft cleared.";
    });
  }

  if (copyBtn) {
    copyBtn.addEventListener("click", async function () {
      const essay = textarea.value.trim();
      if (!essay) {
        showToast("Write your essay first, then copy it for feedback.");
        return;
      }

      const rubricText =
        typeof window.buildRubricText === "function" ? window.buildRubricText() : "";

      const rubric = [
        "Please act as my English teacher and grade the essay below using the rubric provided.",
        "",
        "ESSAY PROMPT:",
        window.QUESTION_PROMPT,
        "",
        "RUBRIC (for each standard below, assign one performance level and its point value):",
        rubricText,
        "For each standard (RL1, RL3, W4), tell me which performance level my essay earned (Exhibiting Depth = 4, Achieving = 3, Approaching = 2, Beginning = 1, Did Not Demonstrate = 0), the points earned, and a short justification that quotes my essay. Then give an overall score out of 12 and specific, constructive feedback on how to improve.",
        "",
        "MY ESSAY:",
        essay,
      ].join("\n");

      try {
        await navigator.clipboard.writeText(rubric);
        showToast("Copied! Paste this into Claude (opening now) to get your feedback and score.");
        window.open("https://claude.ai/new", "_blank");
      } catch (err) {
        showToast("Couldn't copy automatically. Select the essay text and copy it manually.");
      }
    });
  }
})();
