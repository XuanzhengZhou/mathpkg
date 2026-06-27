---
role: proof
locale: en
of_concept: homomorphism-chain-fstar-autv-autp-autf
source_book: gtm049
source_chapter: "3"
source_section: "3.6"
---

Clearly $\varphi$ and $\psi$ are homomorphisms. Moreover (i) is trivial: $\varphi(z) = z1$ is injective since $z1 = 1$ implies $z = 1$. Statement (ii) follows immediately from Proposition 1: $\psi(f) = \mathcal{P}(f)$ has kernel exactly the non-zero scalar multiples of the identity, which is $F^*\varphi$, and the image of $\psi$ is precisely the projective group $\operatorname{Pr} \mathcal{P}(V)$.

To see that $\theta$ is a homomorphism, choose two projective automorphisms and use Theorem 6 to represent them in the form $\mathcal{P}(f)$, $\mathcal{P}(f')$ where $f, f'$ are semi-linear isomorphisms of $V$ onto $V$ with respect to $\zeta, \zeta'$, respectively. Then $\mathcal{P}(f) \mathcal{P}(f') = \mathcal{P}(ff')$ and the associated field automorphism of $ff'$ is $\zeta\zeta'$. Hence $(\mathcal{P}(f)\mathcal{P}(f'))\theta = \zeta\zeta' = (\mathcal{P}(f)\theta)(\mathcal{P}(f')\theta)$, showing $\theta$ is a homomorphism.

The kernel of $\theta$ consists of those $\pi$ for which the associated field automorphism is the identity, i.e., those $\pi$ that arise from linear isomorphisms, which is exactly $\operatorname{Pr} \mathcal{P}(V)$. The surjectivity onto $\operatorname{Aut} F$ follows from Theorem 6.
