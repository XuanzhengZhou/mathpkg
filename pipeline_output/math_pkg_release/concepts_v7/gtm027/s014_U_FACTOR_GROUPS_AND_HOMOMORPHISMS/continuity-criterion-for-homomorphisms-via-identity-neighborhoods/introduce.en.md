---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A group homomorphism $f: G \to H$ between topological groups is continuous globally if and only if it is continuous at the identity element $e_G$. Because group operations (translation) are homeomorphisms, continuity at the identity propagates to all points: $f$ is continuous at any $x \in G$ if and only if the map $y \mapsto f(x)^{-1} f(xy)$ is continuous at $e_G$. Thus checking continuity reduces to verifying that $f^{-1}(V)$ is a neighborhood of $e_G$ for every neighborhood $V$ of $e_H$.
