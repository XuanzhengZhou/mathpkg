---
role: exercise
locale: en
source_book: gtm095
source_chapter: "2"
source_section: "2"
exercise_number: 1
of_concept: renewal-equation
---

# Exercise 1

Show that the renewal function $m(t)$ defined by $m(t) = \sum_{n=1}^\infty F_n(t)$ satisfies the renewal equation

$$m(t) = F(t) + \int_0^t m(t-x) \, dF(x).$$

Here $F_n$ is the distribution function of $T_n = \sigma_1 + \cdots + \sigma_n$, and $F_1 = F$.
