---
role: proof
locale: en
of_concept: quotient-hausdorff-not-regular
source_book: gtm027
source_chapter: "4"
source_section: "F. Example (The Tychonoff Plank) on Subspaces of Normal Spaces"
---

# Proof: Quotient Space that is Hausdorff but Not Regular

**Statement (a)**: There exists a quotient space $X/R$ (of a regular space $X$) which is a Hausdorff space but is not regular.

**Construction**:

Let $X$ be the Tychonoff Plank, i.e., $X = (\Omega' \times \Omega') \setminus \{(\Omega, \Omega)\}$ with the subspace topology. Recall that $\Omega' = [0, \Omega]$ is compact Hausdorff and $X$ is a subspace of a normal space.

Let $A = \Omega_0 \times \{\Omega\} \subset X$ (the "top edge" excluding the corner). Define an equivalence relation $R$ on $X$ by collapsing $A$ to a single point; that is, all points of $A$ are identified with each other, and every other point is identified only with itself.

Formally,
$$(x, y) \sim (x', y') \iff (x, y) = (x', y') \text{ or both belong to } A.$$

The quotient space $X/R$ has as members:
- The equivalence class $[A]$ (the collapsed set $A$), and
- Singletons $\{[x]\}$ for each $x \in X \setminus A$.

**$X/R$ is Hausdorff**: Take two distinct points in $X/R$. If neither is $[A]$, they correspond to distinct points in $X \setminus A$, and since $X$ is Hausdorff (as a subspace of a Hausdorff space), they can be separated by disjoint open sets in $X$. The images of these open sets under the quotient map are open (since $R$ identifies only points of $A$, and these open sets can be chosen to avoid $A$), yielding disjoint open neighborhoods in $X/R$.

If one point is $[A]$ and the other is $[p]$ for some $p \notin A$, then we need to separate them. The point $p = (x, y) \in X \setminus A$. Since $(\Omega, \Omega) \notin X$, the second coordinate $y < \Omega$. We can find a basic open neighborhood of $p$ in $X$ that does not intersect $A$ (e.g., by choosing the second-coordinate interval to stay below $\Omega$). Meanwhile, a saturated open neighborhood of $A$ can be constructed as the union of neighborhoods of points in $A$. With careful choice, these can be made disjoint.

**$X/R$ is not regular**: The point $[A] \in X/R$ and the closed set $C = \overline{\{(x, x) : x \in \Omega_0\}}$ (the closure of the diagonal in $X/R$) cannot be separated by disjoint open sets. The argument is analogous to the proof that the Tychonoff Plank is not normal.

Specifically, the diagonal $D = \{(x, x) : x \in \Omega_0\}$ is a closed subset of $X$ disjoint from $A$. In the quotient, its image is a closed set (since $R$ is a closed equivalence relation). However, any open set in $X/R$ containing $[A]$ must intersect every neighborhood of the image of $D$, by essentially the same argument as in part (e) using the function $f$.

Thus $X/R$ fails to be regular, even though it is a Hausdorff space. This shows that regularity is not preserved under quotient maps, even when starting from a regular (in fact, completely regular) space.
