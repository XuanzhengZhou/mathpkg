---
role: proof
locale: en
of_concept: limit-of-nf-superregular-process
source_book: gtm040
source_chapter: "10"
source_section: "9. Fine boundary functions"
---

**Proof of the first statement.** The function $g = Nf$ with $f \geq 0$ is non-negative and superregular. Since $g$ is $\pi$-integrable, $\pi g$ is finite. Hence $\{g(x_n)\}$ is a non-negative supermartingale, and by the supermartingale convergence theorem, $g(x_n) \to z \geq 0$ almost everywhere with respect to $\Pr$.

Now $g \geq P^n g$ for all $n$ (by the superregular property: $g \geq Pg$). Since $f \geq 0$ and $g = Nf$, writing $g = \sum_{k=0}^\infty P^k f$, we have $P^n g = \sum_{k=n}^\infty P^k f \to 0$ as $n \to \infty$. By dominated convergence, $\pi P^n g \to 0$.

Thus
\[
M_\pi[z] \leq \lim_{n \to \infty} M_\pi[g(x_n)] = \lim_{n \to \infty} (\pi P^n g) = 0,
\]
which forces $z = 0$ almost everywhere with respect to $\Pr$.

**Proof of the second statement.** The proof is the same as the proof of Corollary 10-44, with the same reasoning applied to the $h$-process with $h = K(\cdot, x)$ for almost every $x \in B_e$ (with respect to $\mu$) for which $K(\cdot, x)$ is normalized.
