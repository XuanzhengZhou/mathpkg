---
role: proof
locale: en
of_concept: distribution-function-continuity-atom
source_book: gtm018
source_chapter: "X"
source_section: "13"
---

The only argument which needs modification is the one used to establish 8.C. We are to prove that if $[a_0, b_0)$ is a semiclosed interval contained in the union of a sequence $\{[a_i, b_i)\}$ of semiclosed intervals, then

$$\nu([a_0, b_0)) \leq \sum_{i=1}^{\infty} \nu([a_i, b_i)).$$

If $a_0 = b_0$, the result is trivial; otherwise let $\epsilon$ be a positive number such that $\epsilon < b_0 - a_0$. Since $f$ is continuous on the left at $a_i$, to every positive number $\delta$ and every positive integer $i$ there corresponds a positive number $\epsilon_i$ such that

$$f(a_i) - f(a_i - \epsilon_i) < \frac{\delta}{2^i}, \quad i = 1, 2, \dots.$$

If $F_0 = [a_0, b_0 - \epsilon]$ and $U_i = (a_i - \epsilon_i, b_i)$, $i = 1, 2, \dots$, then $F_0 \subset \bigcup_{i=1}^{\infty} U_i$, and therefore, by the Heine–Borel theorem, there is a positive integer $n$ such that

$$F_0 \subset \bigcup_{i=1}^{n} U_i.$$

From the analog of 8.B for $\nu$ we obtain

$$f(b_0 - \epsilon) - f(a_0) \leq \sum_{i=1}^{n} (f(b_i) - f(a_i - \epsilon_i)) = \sum_{i=1}^{n} (f(b_i) - f(a_i)) + \sum_{i=1}^{n} (f(a_i) - f(a_i - \epsilon_i)) \leq \sum_{i=1}^{\infty} (f(b_i) - f(a_i)) + \delta.$$

Since $\epsilon$ and $\delta$ are arbitrary, the desired result follows from the fact that $f$ is continuous on the left at $b_0$.

The proof is completed by the observation that $f_\nu$ is continuous at $x$ if and only if the last term of this relation vanishes.
