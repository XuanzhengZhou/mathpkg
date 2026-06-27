---
role: exercise
locale: en
chapter: "1"
section: "3"
exercise_number: 4
---

Let $\mathcal{C}$ be a category and let $f: A \to B$ be a morphism in $\mathcal{C}$. Then $f$ is a **monomorphism** (resp. **epimorphism**) in case it is cancellable on the left (resp. right) in $\mathcal{C}$; i.e., in case for each pair of morphisms $g, h: C \to A$ (resp. $g, h: B \to C$) in $\mathcal{C}$, if $fg = fh$ (resp. if $gf = hf$), then $g = h$. The morphism $f$ is an **isomorphism** in case it is invertible in $\mathcal{C}$; i.e., in case there is a morphism $g: B \to A$ with $gf = 1_A$ and $fg = 1_B$.

1. Prove that if $f: A \to B$ and $f': B \to C$ are both monomorphisms, epimorphisms, or isomorphisms, respectively, then $f'f$ is a monomorphism, epimorphism, or isomorphism.

2. Prove that in the concrete category $\mathcal{R}$ of all rings and ring homomorphisms, the inclusion map $f: \mathbb{Z} \to \mathbb{Q}$ is both a monomorphism and an epimorphism but not an isomorphism. (Also, see Exercise (4.2).)
