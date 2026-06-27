---
role: proof
locale: en
of_concept: monotonicity-expectation
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Monotonicity of Expectation

**Property B.** Let $\xi \leq \eta$. Then

$$E\xi \leq E\eta$$

with the understanding that if $-\infty < E\xi$ then $-\infty < E\eta$ and $E\xi \leq E\eta$, or if $E\eta < \infty$ then $E\xi < \infty$ and $E\xi \leq E\eta$.

*Proof.* First, if $0 \leq \xi \leq \eta$, then $E\xi$ and $E\eta$ are defined (by definition of expectation for nonnegative random variables) and the inequality $E\xi \leq E\eta$ follows directly from the definition of the Lebesgue integral for nonnegative functions (formula (6)).

Now let $E\xi > -\infty$; then $E\xi^- < \infty$. If $\xi \leq \eta$, we have $\xi^+ \leq \eta^+$ and $\xi^- \geq \eta^-$. Therefore $E\eta^- \leq E\xi^- < \infty$; consequently $E\eta$ is defined and

$$E\xi = E\xi^+ - E\xi^- \leq E\eta^+ - E\eta^- = E\eta.$$

The case when $E\eta < \infty$ is discussed similarly: then $E\eta^+ < \infty$. Since $\xi \leq \eta$, we have $\xi^+ \leq \eta^+$, so $E\xi^+ \leq E\eta^+ < \infty$ and $E\xi$ is defined, and the inequality follows as above. $\square$
