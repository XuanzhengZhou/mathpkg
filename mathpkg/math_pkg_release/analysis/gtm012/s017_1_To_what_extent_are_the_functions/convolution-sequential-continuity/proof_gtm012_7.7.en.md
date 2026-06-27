---
role: proof
locale: en
of_concept: convolution-sequential-continuity
source_book: gtm012
source_chapter: "7"
source_section: "7. Convolution of distributions"
---

# Proof of Sequential Continuity of Convolution with a Distribution

**Lemma 7.5.** If $F \in \mathcal{P}'$, $(u_n)_{1}^{\infty} \subset \mathcal{P}$, and $u_n \to u$ in the sense of $\mathcal{P}$, then $F * u_n \to F * u$ in the sense of $\mathcal{P}$.

*Proof.* This lemma is proved in the course of showing that the convolution of two distributions $F * G$ is continuous on $\mathcal{P}$. Recall that the definition

$$(F * G)(u) = F(G^\sim * u), \quad u \in \mathcal{P},$$

together with the fact that $G^\sim * u \in \mathcal{P}$ and the map $u \mapsto G^\sim * u$ is continuous from $\mathcal{P}$ to $\mathcal{P}$, yields that $F * G \in \mathcal{P}'$. The key step is verifying that if $u_n \to u$ in $\mathcal{P}$, then $G^\sim * u_n \to G^\sim * u$ in $\mathcal{P}$. Applying this to $F$ in place of $G$, we obtain:

$$(F * u_n)(x) = F(T_x \tilde{u}_n) = F(T_x (u_n)^\sim),$$

and as $u_n \to u$ in $\mathcal{P}$, the smoothness argument from Proposition 7.1 gives $F * u_n \to F * u$ in $\mathcal{P}$.

More explicitly, since $F$ is a continuous linear functional on $\mathcal{P}$, and the map $u \mapsto T_x \tilde{u}$ is continuous in the $\mathcal{P}$-topology for each fixed $x$, the pointwise convergence follows. The uniformity for all derivatives is obtained from the identity $D^k(F * u) = F * (D^k u)$, so that $D^k(F * u_n) = F * (D^k u_n) \to F * (D^k u)$ uniformly. $\square$
