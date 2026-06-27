---
role: exercise
locale: en
chapter: "5"
section: "Q: Example on Compactification"
exercise_number: 1
---

# Exercise Q: Stone-Čech Compactification of $\Omega_0$

Let $\Omega'$ be the set of all ordinal numbers less than or equal to the first uncountable ordinal $\Omega$, and let $\Omega_0 = \Omega' \setminus \{\Omega\}$, each endowed with the order topology.

Prove that the Stone-Čech compactification $\beta(\Omega_0)$ is homeomorphic to $\Omega'$.

*Hint:* Use Problem 5.P (characterization of the Stone-Čech compactification via bounded continuous functions). Show that every bounded real-valued continuous function $f$ on $\Omega_0$ is *eventually constant*: there exists $x \in \Omega_0$ such that $f(y) = f(x)$ for all $y > x$. The interlacing lemma (Lemma 4.E) shows that for $r > s$, one of the sets $\{x : f(x) \geq r\}$ and $\{x : f(x) \leq s\}$ is countable. Use this fact to prove that $f$ is eventually constant. (The boundedness hypothesis is actually not essential.)

*Reference:* Tong [1].
