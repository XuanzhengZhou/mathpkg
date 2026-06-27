---
role: proof
locale: en
of_concept: schurs-lemma
source_book: gtm020
source_chapter: "4"
source_section: "4.10"
---

**Proof.** The first statement follows from Proposition (4.9): since $f$ is a $G$-morphism from a simple $G$-module $M$, $f$ is either zero or a monomorphism; since $f$ is a $G$-morphism into a simple $G$-module $N$, $f$ is either zero or an epimorphism. If $f$ is nonzero, it is both a monomorphism and an epimorphism, hence an isomorphism.

For the second statement, assume $M = N$ and $F$ is algebraically closed. Since $F$ is algebraically closed, the linear transformation $f: M \to M$ has an eigenvalue $\lambda \in F$. Let $L = \ker(f - \lambda \cdot 1_M)$. Then $L$ is a $G$-submodule of $M$ because $f$ is a $G$-morphism and scalar multiplication commutes with the $G$-action. Since $\lambda$ is an eigenvalue, $L \neq 0$. By simplicity of $M$, we have $L = M$, and therefore $f(x) = \lambda x$ for all $x \in M$. $\square$
