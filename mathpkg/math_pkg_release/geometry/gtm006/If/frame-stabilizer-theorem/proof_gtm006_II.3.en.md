---
role: proof
locale: en
of_concept: frame-stabilizer-theorem
source_book: gtm006
source_chapter: "II"
source_section: "3"
---

Let $E_1, \dots, E_{n+2}$ be the given frame and choose a basis $e_1, \dots, e_{n+1}$ such that $E_i = \langle e_i \rangle$ and $E_{n+2} = \langle e_1 + \cdots + e_{n+1} \rangle$ (Lemma 2.5). Let $G$ be the subgroup of $P\Gamma L(V)$ fixing each $E_i$ pointwise.

For each $\alpha \in \operatorname{Aut} K$ and $k \in K^*$, define a semi-linear transformation $\theta(\alpha, k)$ on $V$ by sending the basis vector $e_i$ to $k e_i$ (linear map of scaling by $k$) composed with the field automorphism $\alpha$ acting on coordinates: $( \sum x_i e_i )^{\theta(\alpha,k)} = \sum k x_i^\alpha e_i$. Then $\theta(\alpha, k)$ maps each $E_i$ to itself and maps $E_{n+2} = \langle \sum e_i \rangle$ to $\langle \sum k e_i \rangle = \langle \sum e_i \rangle$.

Let $H = \{\theta(\alpha, k) \mid \alpha \in \operatorname{Aut} K, k \in K^*\}$ and let $N = \{\theta(\alpha, k) \mid \omega_k = \alpha^{-1}\}$ where $\omega_k$ is conjugation by $k$. The subgroup $N$ consists of those transformations inducing the identity on $\mathcal{P}(V)$. Thus $G \cong H/N$.

Define $\phi: H \to \operatorname{Aut} K$ by $\phi(\theta(\alpha, k)) = \omega_k \circ \alpha$. A computation shows $\theta(\alpha,k) \circ \theta(\beta,h) = \theta(\alpha \circ \beta, k^\beta h)$ and therefore $\omega_{k^\beta h} \circ \alpha \circ \beta = (\omega_h \circ \beta) \circ (\omega_k \circ \alpha)$, so $\phi$ is a homomorphism onto $\operatorname{Aut} K$. The kernel is $\{\theta(\alpha,k) \mid \omega_k \circ \alpha = 1\} = N$, giving $\operatorname{Aut} K \cong H/N \cong G$.

For $G \cap PGL(V)$, restrict to $\alpha = 1$ (linear transformations). The same argument with $\theta(1,k) \mapsto \omega_k$ gives $G \cap PGL(V) \cong \operatorname{In} K$. $\square$
