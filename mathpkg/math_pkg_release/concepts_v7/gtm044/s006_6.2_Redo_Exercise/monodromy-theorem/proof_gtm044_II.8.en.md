---
role: proof
locale: en
of_concept: monodromy-theorem
source_book: gtm044
source_chapter: "II"
source_section: "8"
---

# Proof of the Monodromy Theorem (Theorem 8.14)

**Theorem 8.14 (Monodromy Theorem).** Let $\Omega$ be a simply connected open set in $\mathbb{C}$, and suppose an analytic function element $\mathcal{Q}$ is a lifting of a connected open set $\mathcal{O} \subset \Omega$. If $\mathcal{Q}$ can be analytically continued along any polygonal path in $\Omega$, then $\mathcal{Q}$ has a unique extension to a single-valued analytic function on all of $\Omega$.

*Proof.* Let $\mathcal{Q}$ be an analytic function element defined on $\mathcal{O} \subset \Omega$. By hypothesis, for any polygonal path $\gamma$ in $\Omega$ starting at a point $P_0 \in \mathcal{O}$, there exists an analytic continuation of $\mathcal{Q}$ along $\gamma$.

**Uniqueness.** Suppose $f$ and $g$ are two analytic functions on $\Omega$ that both extend $\mathcal{Q}$. Then $f = g$ on $\mathcal{O}$. Since $\mathcal{O}$ is a nonempty open set and $\Omega$ is connected, the Identity Theorem for analytic functions implies $f = g$ on all of $\Omega$. So the extension, if it exists, is unique.

**Existence.** Fix a base point $z_0 \in \mathcal{O}$. For any $z \in \Omega$, since $\Omega$ is open and connected (being simply connected), it is path-connected. Choose a polygonal path $\gamma$ from $z_0$ to $z$ in $\Omega$. By the analytic continuation hypothesis, there exists an analytic function element $\mathcal{Q}_z$ obtained by continuing $\mathcal{Q}$ along $\gamma$. Define $F(z)$ to be the value of this continuation at $z$.

We must show that $F(z)$ is well-defined (independent of the choice of polygonal path). Let $\gamma_1$ and $\gamma_2$ be two polygonal paths from $z_0$ to $z$ in $\Omega$. Their concatenation $\gamma = \gamma_1 \circ \gamma_2^{-1}$ is a closed polygonal path based at $z_0$ in $\Omega$.

Since $\Omega$ is simply connected, $\gamma$ is homotopic to the constant path at $z_0$ within $\Omega$. Using the homotopy, we can subdivide the deformation into a finite sequence of elementary modifications. At each stage, the analytic continuation is preserved because:

1. Any sufficiently small polygonal deformation of a path within an open set where the function element is defined does not change the continuation (by the local existence and uniqueness of analytic continuation).
2. The homotopy can be approximated by a sequence of polygonal paths, each differing from the previous by a small deformation within a disk contained in $\Omega$.

More concretely, let $H: [0, 1] \times [0, 1] \to \Omega$ be a homotopy from $\gamma$ to the constant path. By compactness of $[0,1] \times [0,1]$, its image is compact, so it can be covered by finitely many open disks $D_1, \ldots, D_k \subset \Omega$ on which analytic continuations exist and are unique. Subdivide the homotopy parameter $[0,1]$ finely enough so that for each subinterval $[t_j, t_{j+1}]$, the path $H(\cdot, t_j)$ and $H(\cdot, t_{j+1})$ differ only within a single disk $D_i$. Within $D_i$, analytic continuation along both subpaths yields the same result (by the uniqueness of analytic continuation on a disk). Hence the analytic continuation along $\gamma$ brings $\mathcal{Q}$ back to itself. Therefore the continuations along $\gamma_1$ and $\gamma_2$ yield the same value at $z$.

Thus $F(z)$ is well-defined on $\Omega$.

**Analyticity.** For any $z \in \Omega$, choose a small disk $D \subset \Omega$ centered at $z$. The value $F(w)$ for $w \in D$ can be obtained by continuing $\mathcal{Q}$ along a fixed path to $z$, then along the straight line segment from $z$ to $w$ within $D$. The resulting function on $D$ is precisely the analytic function element obtained by continuation to $D$, so $F$ is analytic in a neighborhood of each point of $\Omega$. Hence $F$ is analytic on $\Omega$, and $F|_{\mathcal{O}} = \mathcal{Q}$. $\square$
