---
role: exercise
locale: en
chapter: "IV"
section: "2"
exercise_number: 1
---

Let $f: \mathbf{R} \to \mathbf{R}$ be a smooth even function. Show that there exists a smooth function $g: \mathbf{R} \to \mathbf{R}$ such that $f(x) = g(x^2)$.

*Hint:* Use the trick used to prove Lemma 2.5 (the Borel Theorem). Since $f$ is even, its Taylor series at $0$ contains only even powers: $f(x) \sim \sum_{n=0}^{\infty} a_n x^{2n}$. Define $g$ formally by $g(y) \sim \sum_{n=0}^{\infty} a_n y^n$, and use bump functions with rapidly increasing scaling factors to make this series converge to a smooth function.
