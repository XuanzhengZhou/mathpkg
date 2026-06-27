---
role: proof
locale: en
of_concept: sorgenfrey-line-base-clopen
source_book: gtm027
source_chapter: "1"
source_section: "K"
---

# Proof that Base Elements of the Sorgenfrey Line Are Clopen

**Proposition.** Let $X = \mathbb{R}$ and let $\mathfrak{J}$ be the topology with base $\mathfrak{R} = \{[a,b) : a, b \in \mathbb{R}, a < b\}$. Then each member of the base $\mathfrak{R}$ is both open and closed. Consequently, the space $(X, \mathfrak{J})$ is not connected.

*Proof.* By definition, each $[a,b) \in \mathfrak{R}$ is a basic open set, hence open.

To show $[a,b)$ is closed, we prove its complement is open. The complement is:
$$\mathbb{R} \setminus [a,b) = (-\infty, a) \cup [b, \infty).$$

For any $x \in (-\infty, a)$, we have $x \in [x, a) \subseteq (-\infty, a)$, so $(-\infty, a)$ is open (as a union of basic open sets).

For any $x \in [b, \infty)$, we have $x \in [x, x+1) \subseteq [b, \infty)$, so $[b, \infty)$ is open.

Thus the complement is a union of open sets, hence open, so $[a,b)$ is closed.

Since $[a,b)$ is both open and closed and is a proper, nonempty subset of $\mathbb{R}$, the space is not connected. Indeed, $[a,b)$ and its complement form a separation of $X$. $\square$
