---
role: proof
locale: en
of_concept: simple-sets-exist
source_book: gtm037
source_chapter: "6"
source_section: "Recursive Function Theory"
---

Let $g$ be a recursive function universal for unary primitive recursive functions. For any $e \in \omega$ let

$$f(e) \simeq (\mu y\,[g(e, (y)_0) = (y)_1 \text{ and } (y)_1 > 2e])_1.$$

Thus $f$ is partial recursive. For each $e \in \omega$ let $\psi_e(x) = g(e, x)$ for all $x \in \omega$. Clearly for any $e \in \omega$,

(1) if $e \in \operatorname{Dmn} f$, then $f(e) \in \operatorname{Rng} \psi_e$ and $f(e) > 2e$;

(2) if $\operatorname{Rng} \psi_e$ is infinite then $e \in \operatorname{Dmn} f$.

Now $\operatorname{Rng} f$ is simple. For, it is obviously r.e. Suppose $B$ is any infinite r.e. set. By choice of $g$, choose $e \in \omega$ so that $\operatorname{Rng} \psi_e = B$. By (2) and (1), $f(e) \in \operatorname{Rng} \psi_e$. Thus $B \cap \operatorname{Rng} f \neq \varnothing$. Finally, to show that $\omega \setminus \operatorname{Rng} f$ is infinite, note

(3) if $n \in \omega$, then $2n \cap \operatorname{Rng} f \subseteq f[\,n\,]$.

For, let $i \in 2n \cap \operatorname{Rng} f$. Say $i = f(j)$. By (1), $2j < f(j)$, so $2j < i < 2n$. Thus $j < n$, so $i \in f[\,n\,]$.

Since (3) holds, $|2n \cap \operatorname{Rng} f| \leq n$, hence $|2n \setminus \operatorname{Rng} f| \geq n$, for any $n \in \omega$. Thus $\omega \setminus \operatorname{Rng} f$ is infinite. $\square$
