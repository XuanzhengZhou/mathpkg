---
role: proof
locale: en
of_concept: monic-epic-duality-in-opposite-category
source_book: gtm005
source_chapter: "I"
source_section: "2. Contravariance and Opposites"
---

Recall that an arrow $m$ is monic if $m \circ u = m \circ v$ implies $u = v$, and an arrow $e$ is epi if $u \circ e = v \circ e$ implies $u = v$.

Suppose $f$ is epi in $C$. We must show $f^{\text{op}}$ is monic in $C^{\text{op}}$. Let $u^{\text{op}}, v^{\text{op}}$ be arrows in $C^{\text{op}}$ such that $f^{\text{op}} \circ u^{\text{op}} = f^{\text{op}} \circ v^{\text{op}}$. By the definition of composition in $C^{\text{op}}$, this means $(u \circ f)^{\text{op}} = (v \circ f)^{\text{op}}$, hence $u \circ f = v \circ f$ in $C$. Since $f$ is epi in $C$, we deduce $u = v$, and therefore $u^{\text{op}} = v^{\text{op}}$. Thus $f^{\text{op}}$ is monic in $C^{\text{op}}$.

Conversely, suppose $f^{\text{op}}$ is monic in $C^{\text{op}}$. Let $u, v$ be arrows in $C$ with $u \circ f = v \circ f$. Then $(u \circ f)^{\text{op}} = (v \circ f)^{\text{op}}$, so $f^{\text{op}} \circ u^{\text{op}} = f^{\text{op}} \circ v^{\text{op}}$ in $C^{\text{op}}$. Since $f^{\text{op}}$ is monic, $u^{\text{op}} = v^{\text{op}}$, hence $u = v$. Thus $f$ is epi in $C$.
