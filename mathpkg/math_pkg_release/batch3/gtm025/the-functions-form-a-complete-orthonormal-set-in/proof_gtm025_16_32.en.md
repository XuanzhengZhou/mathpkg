---
role: proof
locale: en
of_concept: "the-functions-form-a-complete-orthonormal-set-in"
source_book: gtm025
source_chapter: "Integration on Locally Compact Spaces"
source_section: "16.32"
---

We have already shown (16.15) that $\{\chi_n\}_{n \in Z}$ is an orthonormal set in $\mathfrak{L}_2$. We now prove that it is complete. Let $T = \{z \in K : |z| = 1\} = \{\exp(it) : -\pi \leq t \leq \pi\}$. For every integer $n$, the function

$$\exp(it) \to \exp(int)$$

is continuous on $T$. Let $\mathfrak{T}$ denote the set of all functions of the form

$$\exp(it) \to \sum_{k=-n}^{n} \alpha_k \exp(ikt)$$

where $\alpha_k \in K$. These functions are called, for an obvious reason, trigonometric polynomials. We have proved in (7.35.b) that $\mathfrak{T}$ is uniformly dense in $\mathfrak{C}(T)$. It is plain that this implies that any function $f \in \mathfrak{C}([-\pi, \pi])$ such that $f(-\pi) = f(\pi)$ can be uniformly approximated [arbitrarily closely] by functions in $\mathfrak{T}$ [regarded as functions of $t \

Thus $\mathfrak{T}$ is dense in $\mathfrak{L}_2([-\pi, \pi])$. By (16.26.v), $\{\chi_n\}_{n \in Z}$ is complete. $\square$
