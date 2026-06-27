---
role: exercise
locale: en
chapter: "1"
section: "1"
exercise_number: 2
---

# Exercise 1.2

Let $\mathfrak{A}$ be a uniform algebra on a compact Hausdorff space $X$ and let $h: \mathfrak{A} \to \mathbb{C}$ be a homomorphism. Show that there exists a probability measure (a positive measure of total mass $1$) $\mu$ on $X$ such that

$$h(f) = \int_X f \, d\mu \quad \text{for all } f \in \mathfrak{A}.$$

**Hint:** Extend $h$ to a bounded linear functional on $C(X)$ using the Hahn-Banach theorem, then apply the Riesz representation theorem. Use the fact that $h(\mathbf{1}) = 1$ (since $h$ maps the unit to $1$) to show that the representing measure has total mass $1$, and verify positivity by considering nonnegative functions.
