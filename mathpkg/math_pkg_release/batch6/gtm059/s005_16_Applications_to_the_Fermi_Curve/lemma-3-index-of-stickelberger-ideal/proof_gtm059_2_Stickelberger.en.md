---
role: proof
locale: en
of_concept: lemma-3-index-of-stickelberger-ideal
source_book: gtm059
source_chapter: "2"
source_section: "Stickelberger Ideals and Bernoulli Distributions"
---

**Note:** The source text is severely degraded by OCR. The following proof sketch reconstructs the main argument.

Define a homomorphism $T: R^- \to \frac{1}{w}\mathbf{Z}/\mathbf{Z}$ by mapping an element $\sum a_\sigma \sigma$ of the group ring to its coefficient at the identity element, reduced modulo $\mathbf{Z}$. That is,
$$T\!\left(\sum_{\sigma \in G} a_\sigma \sigma\right) = a_1 \pmod{\mathbf{Z}}.$$

One verifies that for the Stickelberger element $\theta = \sum_{(b,m)=1} \left\langle \frac{b}{m} \right\rangle \sigma_b^{-1}$, we have
$$T(\theta) = \frac{1}{m}\sum_{\substack{(b,m)=1 \\ 1 \leq b < m}} b - \frac{1}{2} \pmod{\mathbf{Z}},$$
which simplifies using the identity $\sum_{(b,m)=1, 1 \leq b < m} b = \frac{m\varphi(m)}{2}$ (valid for $m > 1$) to show that $T$ is surjective onto $\frac{1}{w}\mathbf{Z}/\mathbf{Z}$.

It remains to prove that $\ker(T) = S$. The inclusion $S \subset \ker(T)$ follows from the computation above. For the reverse inclusion, one shows that any element in $\ker(T)$ can be expressed as a $\mathbf{Z}$-linear combination of Stickelberger elements, using the relations that define $S$.

Hence $[R^- : S] = |\operatorname{im}(T)| = w$, the number of roots of unity in $\mathbf{Q}(\zeta_m)$.
