---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The clone of an equational presentation $(\Omega, E)$ is a category $\mathbf{Set}(\Omega, E)$ that encodes all finitary algebraic operations and their composition laws. An object is simply a set $A$ (thought of as a set of variables), and a morphism $\alpha: A \to B$ is a function assigning to each variable in $A$ an $E_A$-equivalence class of $\Omega$-terms over $B$, i.e., a "derived operation" of arity $|A|$ with values in the free algebra on $B$. Composition is defined by substitution: given $\alpha: A \to B$ and $\beta: B \to C$, one first interprets $\alpha$ as landing in $BT$, then extends $\beta$ to the $\Omega$-homomorphism $\beta^{\#}: BT \to CT$ via the universal property, obtaining $\beta^{\#} \circ \alpha: A \to CT$. This categorical encoding of algebraic structure is the central object of study in the book.
