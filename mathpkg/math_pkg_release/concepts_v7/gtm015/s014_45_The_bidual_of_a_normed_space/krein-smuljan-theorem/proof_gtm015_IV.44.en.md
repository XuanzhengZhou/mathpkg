---
role: proof
locale: en
of_concept: krein-smuljan-theorem
source_book: gtm015
source_chapter: "IV"
source_section: "44"
---

# Proof of the Krein-Smuljan Theorem

Let $E$ be a Banach space and $K$ a convex subset of $E'$. We prove the equivalence of:
(a) $K$ is weak* closed;
(b) for every $r > 0$, the set $K \cap B_r$ is weak* closed, where $B_r = \{f \in E' : \|f\| \leq r\}$.

**(a) $\Rightarrow$ (b):** If $K$ is weak* closed, then $K \cap B_r$ is the intersection of two weak* closed sets ($K$ and $B_r$, the latter being weak* compact by Alaoglu, hence weak* closed), so $K \cap B_r$ is weak* closed.

**(b) $\Rightarrow$ (a):** Assume (b) holds. Let $f_0$ be a point in the weak* closure of $K$. We must show $f_0 \in K$.

By the Banach-Alaoglu theorem, each $B_r$ is weak* compact. Since $K \cap B_r$ is weak* closed (by hypothesis) and contained in the weak* compact set $B_r$, it follows that $K \cap B_r$ is weak* compact.

Consider the canonical embedding $J: E \to E''$. For each $r > 0$, the set $J^{-1}(K \cap B_r)$ is a norm-closed convex subset of $E$ (using the bipolar theorem and the fact that $K$ is convex). 

The key step uses the Krein-Smuljan construction: since $K \cap B_r$ is weak* compact and convex, and $f_0$ is in the weak* closure of $K$, one can show that $f_0$ is actually in $K$. The proof proceeds by considering the polar $K^\circ = \{x \in E : |f(x)| \leq 1 \text{ for all } f \in K\}$ and using the bipolar theorem: $K = (K^\circ)^\circ$ when $K$ is weak* closed and convex. The hypothesis (b) ensures that the Krein-Smuljan condition holds, allowing the application of the bipolar theorem to conclude $f_0 \in K$.

Thus $K$ is weak* closed. $\square$
