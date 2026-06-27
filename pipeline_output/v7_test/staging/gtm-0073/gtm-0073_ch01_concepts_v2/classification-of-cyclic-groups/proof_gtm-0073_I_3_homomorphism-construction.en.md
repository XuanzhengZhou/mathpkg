```yaml
---
role: proof
source_book: gtm-0073
chapter: I
section: "I.3"
proof_technique: homomorphism-construction
locale: en
content_hash: ""
written_against: ""
---
Let $G = \langle a \rangle$ be a cyclic group. Define $\alpha \colon \mathbb{Z} \to G$ by $k \mapsto a^k$. By Theorems 1.9 and 2.8, $\alpha$ is an epimorphism. If $\operatorname{Ker} \alpha = 0$, then $\mathbb{Z} \cong G$ by Theorem 2.3(i). Otherwise $\operatorname{Ker} \alpha$ is a nontrivial subgroup of $\mathbb{Z}$, hence $\operatorname{Ker} \alpha = \langle m \rangle$ where $m$ is the least positive integer such that $a^m = e$ (Theorem 3.1). For all $r,s \in \mathbb{Z}$, $a^r = a^s$ if and only if $a^{r-s} = e$, which holds if and only if $r - s \in \langle m \rangle$. Thus $\alpha(r) = \alpha(s)$ exactly when $r \equiv s \pmod{m}$, and $\alpha$ induces an isomorphism $\mathbb{Z}/\langle m \rangle = \mathbb{Z}_m \cong G$.
