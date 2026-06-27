---
role: proof
locale: en
of_concept: graded-nakayama-lemma
source_book: gtm004
source_chapter: "VII"
source_section: "7"
---

# Proof of the Graded Nakayama Lemma

**Proposition 7.3.** Let $M$ be a graded $P$-module, where $P = K[x_1, \ldots, x_m]$ is the polynomial ring. If $M \otimes_P K = 0$, then $M = 0$.

Here $K$ is regarded as a $P$-module via the augmentation $\varepsilon : P \to K$.

**Proof.** Suppose $M \neq 0$. Let $m \in M$ be a non-zero homogeneous element of minimal degree. (Such an element exists since $M$ is graded and non-zero.)

Consider the multiplication map

$$\mu : M \otimes_K P_+ \to M, \quad \mu(m \otimes f) = m f,$$

where $P_+ = \bigoplus_{d \geq 1} P_d$ is the augmentation ideal. The cokernel of $\mu$ is precisely $M \otimes_P K$:

$$M \otimes_P K \cong M / (M \cdot P_+).$$

If $M \otimes_P K = 0$, then $M = M \cdot P_+$, meaning every element of $M$ can be written as a sum $\sum m_i f_i$ with $f_i \in P_+$.

Write $m = \sum_{i=1}^{s} m_i f_i$ with $m_i \in M$ and $f_i \in P_+$ homogeneous, non-zero. Then $\deg f_i \geq 1$ for all $i$, so

$$\deg m = \deg(m_i f_i) = \deg m_i + \deg f_i \geq \deg m_i + 1 > \deg m_i$$

for each $i$. This contradicts the minimality of the degree of $m$ (since each $m_i$ has strictly smaller degree than $m$).

Therefore our assumption $M \neq 0$ is false, and $M = 0$. $\square$
