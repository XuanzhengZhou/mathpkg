---
role: proof
locale: en
of_concept: baer-subplane-characterization
source_book: gtm006
source_chapter: "3"
source_section: "3"
---

**Proof.** This follows from the proof of Theorem 3.5. Let $\mathcal{P}$ be a finite projective plane of order $n$ and let $\mathcal{P}_0$ be a subplane of order $m$.

By definition, $\mathcal{P}_0$ is a Baer subplane if every line of $\mathcal{P}$ meets $\mathcal{P}_0$ in at least one point. Equivalently, $\mathcal{P}_0$ is a Baer subplane precisely when the number of points of $\mathcal{P}_0$ satisfies $|\mathcal{P}_0| = m^2 + m + 1 = \sqrt{|\mathcal{P}|}$ type relations, which forces $n = m^2$.

($\Rightarrow$) If $\mathcal{P}_0$ is a Baer subplane, then every point of $\mathcal{P}$ lies on at least one line that meets $\mathcal{P}_0$ in $m+1$ points (a line of $\mathcal{P}_0$). Counting incidences between points of $\mathcal{P}$ and lines of $\mathcal{P}_0$ yields $n^2 + n + 1 = (m^2 + m + 1) + (n - m)(m + 1 + \cdots)$, which forces $n = m^2$.

($\Leftarrow$) Conversely, if $n = m^2$, then by Theorem 3.5 we have that every line of $\mathcal{P}$ meets $\mathcal{P}_0$ in either $1$ or $m+1$ points, and every point of $\mathcal{P}$ lies on either $1$ or $m+1$ lines of $\mathcal{P}_0$. Since any line intersecting $\mathcal{P}_0$ in $m+1$ points is actually a line of $\mathcal{P}_0$, and any line intersecting $\mathcal{P}_0$ in $1$ point is not, the condition $n = m^2$ guarantees that $\mathcal{P}_0$ is a Baer subplane. $\square$
