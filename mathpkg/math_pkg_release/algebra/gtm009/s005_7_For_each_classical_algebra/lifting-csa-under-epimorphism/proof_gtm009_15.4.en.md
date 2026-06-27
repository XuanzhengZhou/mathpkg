---
role: proof
locale: en
of_concept: lifting-csa-under-epimorphism
source_book: gtm009
source_chapter: "15"
source_section: "15.4"
---

$H$ is nilpotent, by assumption. By the preceding lemma (Lemma A of 15.4), $\phi(H)$ is a CSA of $\phi(K) = H'$. Since CSAs are minimal Engel subalgebras (Theorem 15.3), and $\phi(H) \subset H'$ with both being CSAs of $H'$, minimality forces $\phi(H) = H'$.

If $x \in L$ normalizes $H$, then $\phi(x)$ normalizes $\phi(H) = H'$. Since $H'$ is self-normalizing, $\phi(x) \in \phi(H)$, which means $x \in H + \operatorname{Ker} \phi$.

But $\operatorname{Ker} \phi \subset K$ (by construction, since $H' = \phi(K)$ and $\operatorname{Ker} \phi$ maps to $0 \in H'$), so $x \in H + K \subset K$.

Now $x \in N_K(H) = H$, since $H$ is a CSA of $K$ (hence self-normalizing in $K$). Therefore $H$ is self-normalizing in $L$, and together with nilpotence, $H$ is a CSA of $L$.
