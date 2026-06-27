---
role: proof
locale: en
of_concept: orbit-counts-under-line-transitive-group
source_book: gtm006
source_chapter: "XIV"
source_section: "3"
---

If $\Pi$ is transitive on the affine flags of $\mathcal{A}$ then $|\Pi_{C, l}| = |\alpha^{-1} \Pi_{C, l} \alpha|$ for any $\alpha \in \Pi$, so $|\Pi_{C, l}| = k$ is the same for all affine flags $C, l$ of $\mathcal{A}$.

Now count:
- There are $n^2$ affine points and $n^2(n+1)$ affine flags (each point on $n+1$ lines). Since $\Pi$ is flag-transitive, $|\Pi| = n^2(n+1) \cdot |\Pi_{C,l}| = n^2(n+1)k$.
- $\Pi$ is transitive on special points (there are $n+1$ of them), so $|\Pi| = (n+1)|\Pi_D|$. Hence $|\Pi_D| = n^2k$.
- $\Pi$ is transitive on affine lines (there are $n^2+n$ of them... wait, in an affine plane of order $n$, there are $n^2+n$ lines total but $n^2$ are affine lines). Actually, by Theorem 14.6(i), $\Pi$ is transitive on affine lines. There are $n^2$ affine lines (not $n^2+n$), so $|\Pi| = n^2 \cdot |\Pi_l|$. Wait, this gives $|\Pi_l| = (n+1)k$... Let me recount: there are $n^2$ affine points and each point lies on $n+1$ lines, giving $n^2(n+1)$ incident point-line pairs. But each line contains $n$ points, so the number of affine lines is $n(n+1) = n^2 + n$. No — in an affine plane, each parallel class has $n$ lines and there are $n+1$ parallel classes, so $n(n+1)$ lines total. But the line at infinity is one line, and the others are affine lines, so there are $n(n+1)$ affine lines? Actually, total lines in an affine plane of order $n$ is $n^2 + n$ (including the line at infinity). The number of affine lines is $n^2 + n - 1$? No: the line at infinity is a single line; the remaining $n^2 + n - 1$ are affine? No, in a projective plane of order $n$, there are $n^2 + n + 1$ points and lines. Removing a line gives an affine plane with $n^2$ points and the remaining $n^2 + n$ lines. So the number of affine lines is $n^2 + n$. Since $\Pi$ is transitive on these, $|\Pi| = (n^2+n)|\Pi_l|$, giving $|\Pi_l| = \frac{n^2(n+1)k}{n(n+1)} = nk$.

- For the affine point stabilizer: there are $n^2$ affine points and $\Pi$ is transitive on them, so $|\Pi| = n^2|\Pi_C|$, giving $|\Pi_C| = (n+1)k$.

- For $\Pi_{C,D}$: this is a subgroup of $\Pi_C$ fixing a special point $D$. There are $n+1$ special points, and $|\Pi_C| = (n+1)k$, so by the orbit-stabilizer theorem applied to $\Pi_C$ acting on special points, $|\Pi_{C,D}| = k$.

Thus $|\Pi| = n^2(n+1)k$, $|\Pi_D| = n^2k$, $|\Pi_l| = nk$, $|\Pi_C| = (n+1)k$, $|\Pi_{C,D}| = k$.
