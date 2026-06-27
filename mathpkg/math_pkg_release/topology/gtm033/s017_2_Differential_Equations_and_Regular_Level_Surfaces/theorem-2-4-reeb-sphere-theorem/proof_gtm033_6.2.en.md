---
role: proof
locale: en
of_concept: theorem-2-4-reeb-sphere-theorem
source_book: gtm033
source_chapter: "6"
source_section: "2"
---

# Proof of Reeb Sphere Theorem

Let the critical points be $P_+$ and $P_-$. We may assume $P_+$ is a maximum and $P_-$ a minimum. Put $f(P_+) = z_+$, $f(P_-) = z_-$.

By Morse's lemma there are coordinates $(x_1, \ldots, x_n)$ in a neighborhood $U_+$ of $P_+$ giving $f|_{U_+}$ the form

$$f(x) = -x_1^2 - \cdots - x_n^2 + z_+.$$

Therefore there exists $b < z_+$ such that the set

$$D_+ = f^{-1}[b, z_+]$$

is a neighborhood of $P_+$ diffeomorphic to the $n$-disk $D^n$. Geometrically, the sublevel set $f^{-1}[b, z_+]$ consists of points whose coordinates satisfy $x_1^2 + \cdots + x_n^2 \leq z_+ - b$, which is an $n$-disk.

Similarly, by applying Morse's lemma at the minimum $P_-$, there exists $a > z_-$ such that the set

$$D_- = f^{-1}[z_-, a]$$

is a neighborhood of $P_-$ diffeomorphic to $D^n$. (At a minimum, the local form is $f(x) = x_1^2 + \cdots + x_n^2 + z_-$, so $f^{-1}[z_-, a]$ is again an $n$-disk.)

We assume $z_- < a < b < z_+$, so the disks are disjoint. Note that

$$\partial D_+ \approx \partial D_- \approx S^{n-1}.$$

Now consider the intermediate region $f^{-1}[a, b]$. On this region, $f$ has no critical points (the only critical points are $P_-$ with value $z_- < a$, and $P_+$ with value $z_+ > b$). Moreover, $f^{-1}(a) = \partial D_- \approx S^{n-1}$ and $f^{-1}(b) = \partial D_+ \approx S^{n-1}$. By the Regular Interval Theorem (Theorem 2.2), the set $f^{-1}[a, b]$ is diffeomorphic to

$$S^{n-1} \times [a, b] \cong S^{n-1} \times I.$$

Therefore $M$ can be decomposed as

$$M = D_- \cup (S^{n-1} \times I) \cup D_+,$$

where the attaching maps on each end are diffeomorphisms of $S^{n-1}$. More precisely:

- $D_-$ attaches to $S^{n-1} \times I$ along $S^{n-1} \times \{a\} \cong \partial D_-$
- $D_+$ attaches to $S^{n-1} \times I$ along $S^{n-1} \times \{b\} \cong \partial D_+$

This is precisely the standard decomposition of the $n$-sphere $S^n$ as the union of two $n$-disks glued along their boundaries with a cylindrical region $S^{n-1} \times I$ between them. Hence $M$ is homeomorphic to $S^n$.

(Note: The conclusion is homeomorphism, not diffeomorphism, because the gluing diffeomorphisms of $S^{n-1}$ may not extend to a diffeomorphism of the entire sphere. However, topologically any two orientation-preserving diffeomorphisms of $S^{n-1}$ are isotopic for $n \neq 4$, but the theorem as stated only claims homeomorphism.)
