---
role: exercise
locale: en
chapter: "5"
section: "Exercises"
exercise_number: 52
---

Show that the function $f$ defined as follows is recursive.

$$f(0, y) = y + 1,$$
$$f(1, y) = y + 2,$$
$$f(x + 2, 0) = f(x + 1, 1),$$
$$f(x + 2, y + 1) = f(x, f(x + 1, f(x + 2, y))).$$
