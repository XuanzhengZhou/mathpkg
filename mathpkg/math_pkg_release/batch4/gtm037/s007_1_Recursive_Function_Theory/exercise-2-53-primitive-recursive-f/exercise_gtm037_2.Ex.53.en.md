---
role: exercise
locale: en
chapter: "2"
section: "Exercises"
exercise_number: 53
---

Suppose that $g$ is $1$-ary primitive recursive, $h$ is $4$-ary primitive recursive and $f$ is defined as follows:

$$f(0, n) = f(1, n) = gn$$
$$f(m + 1, n) = h(f(m - 1, n), f(m, n), m, n) \quad \text{for } m > 0.$$

Show that $f$ is primitive recursive.
