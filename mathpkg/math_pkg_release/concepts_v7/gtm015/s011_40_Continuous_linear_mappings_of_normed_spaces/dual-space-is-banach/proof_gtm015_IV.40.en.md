---
role: proof
locale: en
of_concept: dual-space-is-banach
source_book: gtm015
source_chapter: "IV"
source_section: "40"
---

# Proof of The dual space of a normed space is a Banach space

**Corollary (40.9).** If $E$ is any normed space, then its dual $E' = \mathcal{L}(E, \mathbb{K})$ is a Banach space.

**Proof.**

By definition (40.8), $E' = \mathcal{L}(E, \mathbb{K})$ is the space of continuous linear mappings from $E$ into the scalar field $\mathbb{K}$, equipped with the operator norm

$$\|f\| = \sup\{|f(x)| : x \in E,\ \|x\| \leq 1\}.$$

The scalar field $\mathbb{K}$ (either $\mathbb{R}$ or $\mathbb{C}$) is complete with respect to its usual absolute value. By Theorem (40.7) (completeness of $\mathcal{L}(E, F)$ when $F$ is a Banach space), the space $\mathcal{L}(E, \mathbb{K})$ is complete in the operator norm. Hence $E'$ is a Banach space.
