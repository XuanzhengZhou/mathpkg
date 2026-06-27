---
role: proof
locale: en
of_concept: "let-and-be-measurable-spaces-let-and-be"
source_book: gtm025
source_chapter: "Hilbert Spaces and Spectral Theory"
source_section: "21.29"
---

Suppose that $\mu^\dagger \ll \mu$ and $v^\dagger \ll v$, and let $E \in \mathcal{M} \times \mathcal{N}$ be such that $\mu \times v(E) = 0$. By (21.9), we have

$$0 = \mu \times v(E) = \int_X v(E_x) d\mu(x).$$

By (12.6),

Now combine (1) and (2) and let $f = \xi_A$, where $A \in \mathcal{M} \times \mathcal{N}$ and $\mu^\dagger \times v^\dagger(A) < \infty$. This gives

$$\mu^\dagger \times v^\dagger(A) = \int_{X \times Y} \xi_A(x, y) f_0(x) g_0(y) d\mu \times v(x, y).$$

(3)

Since $\mu^\dagger \times v^\dagger$ is $\sigma$-finite, (3) holds for all $A \in \mathcal{M} \times \mathcal{N}$, and the uniqueness provision in (19.24) proves (i).

Now suppose that $\mu^\dagger \perp \mu$. Let $B$ be a set in $\mathcal{M}$ such that $\mu(B) = 0$ and $\mu^\dagger(B') = 0$. Then, as noted in (21.11), we have

$$\mu \times v(B \times Y) = \mu(B)v(Y) = 0$$

and

$$\mu^\dagger \times v^\dagger((B \times Y)') = \mu^\dagger \times v^\dagger(B' \times Y) = \mu^\dagger(B')v^\dagger(Y) = 0.$$

This implies that $\mu^\dagger \times v^\dagger \perp \mu \times v$. For arbitrary $\mu, \mu^\dagger, v$, and $v^\dagger$, we have

$$\mu^\dagger \times v^\dagger = (\mu_a^\dagger + \mu_s^\dagger) \times (v_a^\dagger + v_s^\dagger)$$

$$= (\mu_a^\dagger \times v_a^\dagger) + (\mu_a^\dagger \times v_s^\dagger) + (\mu_s^\dagger \times v_a^\dagger) + (\mu_s^\dagger \times v_s^\dagger),$$

from which (ii) and (iii) follow easily. $\square$

FUBINI's theorem and Lebesgue's dominated convergence theorem are cornerstones of analysis. The theory

measurable for all $n \in N$ and $s_n \circ \varphi \rightarrow f \circ \varphi$ except on $\varphi^{-1}(F)$. Since $\overline{\lambda \times \lambda}(\varphi^{-1}(F)) = 0$, it follows that $f \circ \varphi$ is $\overline{\mathcal{M}_{\lambda} \times \mathcal{M}_{\lambda}}$-measurable (11.24).
