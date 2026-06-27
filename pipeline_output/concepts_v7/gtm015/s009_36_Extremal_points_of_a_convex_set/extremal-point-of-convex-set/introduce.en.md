---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Let $E$ be a vector space over $\mathbb{K}$ and let $A$ be a convex subset of $E$. A point $a \in A$ is called an **extremal point** of $A$ if there exists no nondegenerate open segment $\langle u, v \rangle$ such that $a \in \langle u, v \rangle \subset A$.

Equivalently, $a \in A$ is extremal if the relations $a \in \langle u, v \rangle \subset A$ imply $u = v$. In other words, an extremal point cannot be expressed as a strict convex combination of two distinct points that, together with the segment joining them, lie entirely within $A$.

A useful technical remark: in the definition, it is no restriction to suppose $u, v \in A$. Indeed, if $a = \alpha u + (1-\alpha)v$ with $0 < \alpha < 1$ and $\langle u, v \rangle \subset A$, then the midpoints $u' = \frac{1}{2}u + \frac{1}{2}a$ and $v' = \frac{1}{2}a + \frac{1}{2}v$ belong to $A$, and $a \in \langle u', v' \rangle \subset \langle u, v \rangle \subset A$; moreover $u' \neq v'$ unless $u = v$.

The geometric intuition is clear: for a convex polygon in the plane, the extremal points are precisely its vertices — no vertex can lie in the interior of a line segment whose endpoints are also in the polygon. The remarkable fact, explored throughout this section, is that in sufficiently rich topological-algebraic contexts (compact convex sets in locally convex spaces), extremal points exist in abundance and determine the structure of the whole set.
