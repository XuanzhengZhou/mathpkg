---
role: proof
locale: en
of_concept: jordan-composition-series-length
source_book: gtm028
source_chapter: "III"
source_section: "§11"
---

We prove that any normal series without repetitions has length at most $r$. This also proves the second statement, since if the normal series is not already a composition series, we may insert additional submodules without repeating any; this process must lead to a composition series in exactly $r - s$ steps.

We must show that $s \leq r$. The composition series $M = M_0 > M_1 > \cdots > M_r = (0)$ shows that $M_1$ has a composition series of length $r-1$. Let the other series be $M = N_0 > N_1 > \cdots > N_s = (0)$. If $N_1 = M_1$, then we get a normal series for $M_1$ without repetitions and of length $s-1$; by induction hypothesis $s-1 \leq r-1$, $s \leq r$. If $N_1 < M_1$, then we have a normal series for $M_1$ without repetitions and of length $s$; again by induction $s \leq r-1$, and a fortiori $s \leq r$.

We may thus confine ourselves to the case where $N_1$ is not contained in $M_1$ at all. Since there are no submodules between $M_1$ and $M$, it follows that $M_1 + N_1 = M$. Now by Theorem 5, §4,
$$M - M_1 = (M_1 + N_1) - M_1 \cong N_1 - (M_1 \cap N_1).$$
Since $M - M_1$ is simple, so is $N_1 - (M_1 \cap N_1)$, hence there are no submodules between $N_1$ and $M_1 \cap N_1$. Since $M_1$ has a composition series of length $r-1$, and $M_1 \cap N_1 < M_1$, every normal series without repetitions of $M_1 \cap N_1$ has length at most $r-2$, and hence $M_1 \cap N_1$ has a composition series of at most this length. Since there are no submodules between $N_1$ and $M_1 \cap N_1$, $N_1$ has a composition series of length at most $r-1$, so $s \leq r$ by induction.
