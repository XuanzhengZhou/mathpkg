---
role: proof
source_book: gtm-0073
chapter: IV
section: "IV.2"
proof_technique: cardinality-comparison
locale: en
content_hash: ""
written_against: ""
---
If $Y$ is another basis, $Y$ must be infinite (otherwise a finite subset of $X$ would generate $F$). Let $K(Y)$ be the set of all finite subsets of $Y$. Define $f: X \to K(Y)$ by mapping $x$ to the finite set of basis elements from $Y$ appearing in its expression. Each finite subset of $Y$ has at most finitely many preimages, so $|X| \le |K(Y)| \cdot \aleph_0 = |Y|$ (since $Y$ is infinite). Interchanging $X$ and $Y$ gives $|Y| \le |X|$. By Schroeder-Bernstein, $|X| = |Y|$.
