---
role: proof
locale: en
of_concept: fraction-inequality
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "14. The space (s)"
---

# Proof of Fraction Inequality

**Lemma (14.3).** If $\alpha, \beta, \gamma$ are nonnegative real numbers such that $\alpha \leq \beta + \gamma$, then

$$\frac{\alpha}{1 + \alpha} \leq \frac{\beta}{1 + \beta} + \frac{\gamma}{1 + \gamma}.$$

*Proof.* The function $t \mapsto \frac{t}{1+t}$ is increasing for $t \geq 0$, since its derivative is $\frac{1}{(1+t)^2} > 0$. From $\alpha \leq \beta + \gamma$ we have

$$\frac{\alpha}{1+\alpha} \leq \frac{\beta+\gamma}{1+\beta+\gamma}.$$

Now

$$\frac{\beta+\gamma}{1+\beta+\gamma} = \frac{\beta}{1+\beta+\gamma} + \frac{\gamma}{1+\beta+\gamma} \leq \frac{\beta}{1+\beta} + \frac{\gamma}{1+\gamma},$$

since the denominators satisfy $1+\beta+\gamma \geq 1+\beta$ and $1+\beta+\gamma \geq 1+\gamma$. Combining the two inequalities yields the desired result. $\square$
