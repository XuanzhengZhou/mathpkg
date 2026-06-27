---
role: proof
locale: en
of_concept: local-maximum-modulus-principle
source_book: gtm035
source_chapter: "Chapter 9"
source_section: "9.3"
---
# Proof of the Local Maximum Modulus Principle

Let $A$ be a Banach algebra and fix $x \in \mathcal{M} \setminus \check{S}(A)$. Let $U$ be a neighborhood of $x$ with $U \subset \mathcal{M} \setminus \check{S}(A)$. We must show that for all $f \in A$,

$$|\hat{f}(x)| \leq \max_{\partial U} |\hat{f}|.$$

Suppose, for contradiction, that the inequality fails. Choose $x_0 \in \overline{U}$ where $|\hat{f}(x_0)| = \max_{\overline{U}} |\hat{f}|$. Then

$$|\hat{f}(x_0)| > \max_{\partial U} |\hat{f}|.$$

Without loss of generality, normalize so that $\hat{f}(x_0) = 1$. Define

$$T = \{y \in \overline{U} : \hat{f}(y) = 1\}.$$

Then $T$ is compact and $T \subset U$ (since $|\hat{f}| < 1$ on $\partial U$).

Set $\varphi = \frac{1}{2}(1 + f) \in A$. Then $\hat{\varphi} = 1$ on $T$, and $|\hat{\varphi}| < 1$ on $\overline{U} \setminus T$ (because $|\hat{f}| < 1$ there, so $|\frac{1}{2}(1 + \hat{f})| < 1$).

Now apply Lemma 9.6 (Extension of Peak Functions) with the closed set $T$ and its open neighborhood $U$. The lemma provides an element $e \in A$ such that

$$\hat{e} = 1 \text{ on } T, \quad |\hat{e}| < 1 \text{ on } \mathcal{M} \setminus T.$$

In particular, since $U \subset \mathcal{M} \setminus \check{S}(A)$, we have $\check{S}(A) \subset \mathcal{M} \setminus T$, so $|\hat{e}| < 1$ on $\check{S}(A)$.

But this contradicts the definition of the Šilov boundary: since $\check{S}(A)$ is a boundary, we must have

$$\max_{\mathcal{M}} |\hat{e}| = \max_{\check{S}(A)} |\hat{e}| < 1,$$

yet $\hat{e}(x_0) = 1$ (since $x_0 \in T$), implying $\max_{\mathcal{M}} |\hat{e}| \geq 1$. This contradiction establishes the theorem. $\square$

The proof relies on Lemma 9.6 (which itself depends on Lemmas 9.4 and 9.5) to extend a local peak function to a global peak function that is strictly less than $1$ on the Šilov boundary.
