---
role: proof
locale: en
of_concept: approximate-eigenvalue-selfadjoint
source_book: gtm015
source_chapter: "57"
source_section: "57.25"
---

# Proof of Approximate eigenvalues and the boundary of spectrum

(57.25) Lemma. Let $H$ be a Hilbert space

for all $x, y$ in $H$. It follows that for every vector $x$,

$$\|(T - mI)x\|^4 = ((T - mI)x|(T - mI)x)^2$$

$$= [\varphi(x, (T - mI)x)]^2$$

$$\leq \varphi(x, x)\varphi((T - mI)x, (T - mI)x)$$

$$\leq \varphi(x, x)\|T - mI\|\|(T - mI)x\|^2,$$

therefore

(*) $$\|(T - mI)x\|^2 \leq \varphi(x, x)\|T - mI\|.$$

By the definition of $m$, there exists a sequence of vectors $x_n$ such that $\|x_n\| = 1$ and $\varphi(x_n, x_n) \to 0$; in view of (*), we have $\|(T - mI)x_n\| \to 0.$
