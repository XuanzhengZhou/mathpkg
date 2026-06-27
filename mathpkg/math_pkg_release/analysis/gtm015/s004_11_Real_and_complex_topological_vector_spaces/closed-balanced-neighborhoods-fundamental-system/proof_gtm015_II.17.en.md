---
role: proof
locale: en
of_concept: closed-balanced-neighborhoods-fundamental-system
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "17. Balanced sets, absorbent sets"
---

# Proof that Closed Balanced Neighborhoods Form a Fundamental System

**Theorem (17.9).** Let $E$ be any TVS over $\mathbb{K}$ and let $\mathcal{B}$ be the class of all neighborhoods of $\theta$ that are closed and balanced. Then (i) $\mathcal{B}$ is a fundamental system of neighborhoods of $\theta$, and (ii) $\lambda V \in \mathcal{B}$ for all $V \in \mathcal{B}$, $\lambda \in \mathbb{K}$, $\lambda \neq 0$.

*Proof.* (i) $\mathcal{B}$ is a neighborhood base at $\theta$ by (17.8), which states that every neighborhood of $\theta$ contains a closed balanced neighborhood of $\theta$. Indeed, given any neighborhood $U$ of $\theta$, there exists a closed balanced neighborhood $V$ of $\theta$ with $V \subset U$. Thus the family of closed balanced neighborhoods is a base at $\theta$.

(ii) If $\lambda \in \mathbb{K}$, $\lambda \neq 0$, the mapping $x \mapsto \lambda x$ is a homeomorphism (by (11.5)), hence it preserves closed sets (as a homeomorphism) and balanced sets (if $V$ is balanced and $|\mu| \leq 1$, then $\mu(\lambda V) = (\mu \lambda)V \subset \lambda V$ when $|\mu| \leq 1$ implies $|\mu \lambda|/|\lambda| = |\mu| \leq 1$, but more directly: $\lambda V$ is the image of a balanced set under a linear homeomorphism, hence balanced). It also preserves neighborhoods of $\theta$ (since it maps $\theta$ to $\theta$ and is a homeomorphism). In particular, $V \in \mathcal{B}$ implies $\lambda V \in \mathcal{B}$. $\square$
