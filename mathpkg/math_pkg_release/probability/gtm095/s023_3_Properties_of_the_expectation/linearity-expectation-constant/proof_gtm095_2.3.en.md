---
role: proof
locale: en
of_concept: linearity-expectation-constant
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Linearity of Expectation with Respect to a Constant

**Property A.** Let $c$ be a constant and let $E\xi$ exist. Then $E(c\xi)$ exists and

$$E(c\xi) = c E\xi.$$

*Proof.* Use the representation $\xi = \xi^+ - \xi^-$ and notice that

- When $c \geq 0$: $(c\xi)^+ = c\xi^+$, $(c\xi)^- = c\xi^-$.
- When $c < 0$: $(c\xi)^+ = -c\xi^-$, $(c\xi)^- = -c\xi^+$.

By definition, $E\xi = E\xi^+ - E\xi^-$ when the difference is well-defined (i.e., not of the form $\infty - \infty$). For $c \geq 0$,

$$E(c\xi) = E((c\xi)^+) - E((c\xi)^-) = E(c\xi^+) - E(c\xi^-) = cE\xi^+ - cE\xi^- = c(E\xi^+ - E\xi^-) = cE\xi.$$

For $c < 0$,

$$E(c\xi) = E((c\xi)^+) - E((c\xi)^-) = E((-c)\xi^-) - E((-c)\xi^+) = (-c)E\xi^- - (-c)E\xi^+ = (-c)(E\xi^- - E\xi^+) = c(E\xi^+ - E\xi^-) = cE\xi.$$

In both cases, $E(c\xi)$ exists and equals $cE\xi$. $\square$
