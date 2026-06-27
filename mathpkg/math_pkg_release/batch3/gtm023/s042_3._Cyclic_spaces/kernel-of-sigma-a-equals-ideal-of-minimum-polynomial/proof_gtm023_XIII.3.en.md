---
role: proof
locale: en
of_concept: kernel-of-sigma-a-equals-ideal-of-minimum-polynomial
source_book: gtm023
source_chapter: "XIII"
source_section: "3"
---

Consider first the case that the minimum polynomial has the form $\mu = f^k$ where $f$ is irreducible of degree $p$. Then there is a vector $a \in E$ such that
$$f^{k-1}(\varphi)(a) \neq 0.$$

Suppose now that $h \in K_a$ and let $g$ be the greatest common divisor of $h$ and $\mu$. Since $a \in K(f)$, Corollary I to Proposition I, sec. 13.2 yields
$$a \in K(g).$$

Since $g|\mu$ it follows that $g = f^l$ where $l \leq k$. Hence $f^l(\varphi)a = 0$ and relation $f^{k-1}(\varphi)(a) \neq 0$ implies that $l = k$. Thus $K(g) = K_\mu$. Now it follows from $a \in K(g)$ that $a \in K_\mu$.

In the general case decompose $\mu$ in the form
$$\mu = f_1^{k_1} \ldots f_r^{k_r}, \quad f_i \text{ irreducible}$$
and let
$$E = E_1 \oplus \cdots \oplus E_r$$
be the corresponding decomposition of $E$. Let $\varphi_i: E_i \rightarrow E_i$ ($i = 1 \ldots r$) be the induced transformation. Then the minimum polynomial of $\varphi_i$ is given by
$$\mu_i = f_i^{k_i} \quad (i = 1 \ldots r).$$

Thus, by the first part of the proof, there are vectors $a_i \in E_i$ such that
$$K_{a_i} = I_{\mu_i} \quad (i = 1 \ldots r).$$

Now set
$$a = a_1 + \cdots + a_r.$$

Assume that $f \in K_a$. Then $f(\varphi)a = 0$ whence
$$\sum_{i=1}^r f(\varphi_i)a_i = 0.$$

Since $f(\varphi_i)a_i \in E_i$, it follows that
$$f(\varphi_i)a_i = 0 \quad (i = 1, \ldots, r)$$
whence $f \in I_{\mu_i}$ for each $i$, and therefore $f \in I_{\mu}$. Thus $K_a = I_{\mu}$.
