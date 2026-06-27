---
role: proof
locale: en
of_concept: affine-coordinate-ring-properties
source_book: gtm052
source_chapter: "I"
source_section: "3"
---

We proceed in several steps. First we define a map $\alpha: A(Y) \to \mathcal{O}(Y)$. Every polynomial $f \in A = k[x_1, \ldots, x_n]$ defines a regular function on $\mathbf{A}^n$ and hence on $Y$. Thus we have a homomorphism $A \to \mathcal{O}(Y)$. Its kernel is just $I(Y)$, so we obtain an injective homomorphism $\alpha: A(Y) \to \mathcal{O}(Y)$.

From (1.4) we know there is a 1-1 correspondence between points of $Y$ (which are the minimal algebraic subsets of $Y$) and maximal ideals of $A$ containing $I(Y)$. Passing to the quotient by $I(Y)$, these correspond to maximal ideals of $A(Y)$.

To show $\alpha$ is surjective (hence an isomorphism, proving (a)), let $f \in \mathcal{O}(Y)$ be a regular function. Then by definition, $Y$ can be covered by open sets $U_i$ on which $f = g_i/h_i$ with $h_i \neq 0$ on $U_i$. Using the fact that $A(Y)$ is Noetherian and standard algebraic arguments, one shows $f \in A(Y)$.

For (b), the correspondence $P \mapsto \mathfrak{m}_P$ is the standard one from the Nullstellensatz (see I.1.4).

For (c), since $\alpha$ identifies $A(Y)$ with $\mathcal{O}(Y)$, the localization $A(Y)_{\mathfrak{m}_P}$ corresponds to germs of regular functions near $P$, yielding $\mathcal{O}_P \cong A(Y)_{\mathfrak{m}_P}$. The equality $\dim \mathcal{O}_P = \dim Y$ follows from the fact that dimension is preserved under localization at a maximal ideal.

For (d), $K(Y)$ is by definition the quotient field of $\mathcal{O}(Y)$ (or equivalently of any $\mathcal{O}_P$). Since $\mathcal{O}(Y) \cong A(Y)$, $K(Y)$ is the quotient field of $A(Y)$, a finitely generated $k$-algebra which is an integral domain, so $K(Y)$ is a finitely generated extension field of $k$. The transcendence degree equals $\dim Y$ by the dimension theory of finitely generated $k$-algebras.
