---
role: proof
locale: en
of_concept: characterization-of-a.e.-convergence-by-measure
source_book: gtm018
source_chapter: "IV"
source_section: "21"
---
**Proof.** The sequence $\{f_n(x)\}$ fails to converge to $f(x)$ iff there exists $\epsilon > 0$ such that $x \in E_n(\epsilon)$ for infinitely many $n$. Thus the divergence set is
$$D = \bigcup_{k=1}^{\infty} \limsup_n E_n(1/k).$$
Hence $\mu(E \cap D) = 0$ (i.e., convergence a.e.) iff $\mu(E \cap \limsup_n E_n(\epsilon)) = 0$ for all $\epsilon > 0$. Since
$$\mu(E \cap \limsup_n E_n(\epsilon)) = \lim_n \mu\left(E \cap \bigcup_{m=n}^{\infty} E_m(\epsilon)\right),$$
the result follows.
