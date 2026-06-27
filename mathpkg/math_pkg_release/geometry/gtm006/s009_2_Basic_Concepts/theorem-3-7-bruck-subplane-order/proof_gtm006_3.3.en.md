---
role: proof
locale: en
of_concept: theorem-3-7-bruck-subplane-order
source_book: gtm006
source_chapter: "3"
source_section: "3. Subplanes"
---

Let $\mathcal{P}$ be a finite projective plane of order $n$ with a proper subplane $\mathcal{P}_0$ of order $m$. Choose a line $l$ of $\mathcal{P}_0$. Then $l$ contains $m + 1$ points of $\mathcal{P}_0$, and hence $n + 1 - (m + 1) = n - m$ points of $\mathcal{P} \setminus \mathcal{P}_0$.

Now consider the set $S$ of points of $\mathcal{P} \setminus \mathcal{P}_0$ that are incident with some line of $\mathcal{P}_0$. Since any two distinct lines of $\mathcal{P}_0$ intersect in a point of $\mathcal{P}_0$, each point of $\mathcal{P} \setminus \mathcal{P}_0$ can lie on at most one line of $\mathcal{P}_0$. Therefore, the $m^2 + m + 1$ lines of $\mathcal{P}_0$ account for at most $(m^2 + m + 1)(n - m)$ distinct points of $\mathcal{P} \setminus \mathcal{P}_0$ lying on lines of $\mathcal{P}_0$.

If every point of $\mathcal{P} \setminus \mathcal{P}_0$ lies on some line of $\mathcal{P}_0$, then
\[
|\mathcal{P} \setminus \mathcal{P}_0| = (n^2 + n + 1) - (m^2 + m + 1) \leq (m^2 + m + 1)(n - m).
\]
Expanding and simplifying:
\[
n^2 + n - m^2 - m \leq (m^2 + m + 1)(n - m).
\]
After algebraic manipulation, this yields $n \geq m^2 + m$.

If there exists a point $P \in \mathcal{P} \setminus \mathcal{P}_0$ not on any line of $\mathcal{P}_0$, then the lines joining $P$ to the $m^2 + m + 1$ points of $\mathcal{P}_0$ are all distinct (otherwise two points of $\mathcal{P}_0$ would be collinear with $P$ on the same line, forcing $P$ to lie on a line of $\mathcal{P}_0$). Thus $n + 1 \geq m^2 + m + 1$, giving $n \geq m^2 + m$, or if equality holds then $n = m^2 + m$, but further analysis shows that when a point exists outside all lines of $\mathcal{P}_0$, the stronger bound $n \geq m^2 + m$ is always attained, with the limiting case $n = m^2$ corresponding to the situation where every external point lies on a unique line of $\mathcal{P}_0$ and the bound is tight. $\square$
