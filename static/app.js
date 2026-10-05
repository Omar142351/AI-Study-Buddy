// AI Study Buddy frontend: collect input -> fetch() the API -> render the JSON.
//
// The HTML you build in W2-1 must contain every id used below.
// If you see "Cannot read properties of null" in the browser console, an id is missing or misspelled.

const form = document.getElementById("study-form");
const topicInput = document.getElementById("topic");
const topicCount = document.getElementById("topic-count");
const modeHint = document.getElementById("mode-hint");
const submitBtn = document.getElementById("submit-btn");
const errorBox = document.getElementById("error");
const resultBox = document.getElementById("result");
const modeEl = document.getElementById("result-mode");
const titleEl = document.getElementById("result-title");
const answerEl = document.getElementById("result-answer");
const pointsBlock = document.getElementById("points-block");
const pointsEl = document.getElementById("result-points");

const BUTTON_TEXT = "Ask Study Buddy";

const MODE_HINTS = {
  explain: "I will explain it in simple words, with an example and a question to test yourself.",
  example: "I will give you 2 analogies from everyday life, sports, gaming or school.",
  quiz: "I will write 3 multiple-choice questions. The answers are at the bottom.",
  summarize: "I will write short study notes with a main idea and 3 takeaways.",
};

const MODE_LABELS = {
  explain: "Explanation",
  example: "Examples",
  quiz: "Quiz",
  summarize: "Study notes",
};

// ---------- helpers (provided) ----------
function currentMode() {
  return form.querySelector('input[name="mode"]:checked').value;
}

function showError(message) {
  errorBox.textContent = message;
  errorBox.hidden = false;
}

function clearError() {
  errorBox.hidden = true;
  errorBox.textContent = "";
}

// ---------- WEEK 2 ----------

// TODO(W2-2): setLoading(isLoading)
//   disable the submit button while waiting and change its text to "Thinking...";
//   restore BUTTON_TEXT and enable it again when done.
function setLoading(isLoading) {
  // your code
}

// TODO(W2-3): updateHint()
//   Show the help text for the selected mode: modeHint.textContent = MODE_HINTS[currentMode()]
//   Call it when a mode radio changes AND once when the page loads (last line of this file).
//   Hint: form.querySelectorAll('input[name="mode"]').forEach(radio => radio.addEventListener("change", ...))
function updateHint() {
  // your code
}

// TODO(W2-4): live character counter
//   When the user types in topicInput, set topicCount.textContent to e.g. "12 / 200".
//   Hint: topicInput.addEventListener("input", ...) and topicInput.maxLength

// TODO(W2-5): renderResult(data)
//   data looks like {topic, mode, title, answer, key_points: [...]}
//   - modeEl.textContent = MODE_LABELS[data.mode] + " · " + data.topic
//   - fill titleEl and answerEl using .textContent   (NEVER innerHTML: AI text must not become HTML)
//   - key points: create one <li> per point inside pointsEl (document.createElement + replaceChildren)
//   - hide pointsBlock when there are no key points (quiz mode has none)
//   - finally show resultBox (resultBox.hidden = false)
function renderResult(data) {
  // your code
}

// TODO(W2-6): the submit handler
//   form.addEventListener("submit", async (event) => { ... })
//   1. event.preventDefault() and clearError()
//   2. build the payload {topic, mode} (trim the topic)
//   3. quick check: empty topic -> showError("Please type a topic first.") and stop
//   4. setLoading(true)
//   5. const response = await fetch("/api/study", { method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(payload) })
//   6. const data = await response.json()
//   7. if (!response.ok) -> throw new Error(data.error || "Something went wrong. Please try again.")
//   8. renderResult(data)
//   9. catch: a network failure throws a TypeError -> show "Can't reach the server..."; otherwise show err.message
//   10. finally: setLoading(false)   <- the button must ALWAYS come back, success or failure
//
// Checkpoint: with the backend from Week 1 running, clicking the button shows the fake study result.

updateHint();
