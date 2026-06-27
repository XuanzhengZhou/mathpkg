---
role: proof
locale: en
of_concept: von-neumann-inequality-polynomial
source_book: gtm015
source_chapter: "66"
source_section: "Spectral sets"
---

# Proof of von Neumann inequality for contractions

Proof. Let $U$ be the unitary dilation of $T$ on a larger Hilbert space $K \supset H$, so that $T^n = P_H U^n|_H$ for all $n \geq 0$, where $P_H$ is the orthogonal projection of $K$ onto $H$. For any polynomial $p(\lambda) = \sum_{k=0}^n c_k \lambda^k$, we have $p(T) = P_H p(U)|_H$, and therefore

$$\|p(T)\| \leq \|p(U)\|$$

(the two norms are calculated in the Banach algebras $\mathcal{L}(H)$ and $\mathcal{L}(K)$, respectively). On the other hand, since the unit circle is a spectral set for $U$ (66.11), so is $\Delta_1$ (66.7), thus $\|f(U)\| \leq \|f\|_{\Delta_1}$.

The lemma is immediate from these two inequalities.
