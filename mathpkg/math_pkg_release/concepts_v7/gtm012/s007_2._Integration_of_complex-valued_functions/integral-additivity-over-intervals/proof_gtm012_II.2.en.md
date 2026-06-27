---
role: proof
locale: en
of_concept: integral-additivity-over-intervals
source_book: gtm012
source_chapter: "2"
source_section: "2. Integration of complex-valued functions"
---

# Proof of Additivity of the integral over subintervals

**Proposition 2.5.** Suppose \(a < b < c\) and \(f: [a, c] \to \mathbb{C}\) is bounded. Then \(f\) is integrable on \([a, c]\) if and only if it is integrable on \([a, b]\) and on \([b, c]\). If so, then

\[
\int_a^c f = \int_a^b f + \int_b^c f.
\]

*Proof.* Suppose first that \(f\) is integrable on \([a, b]\) and on \([b, c]\). Given \(\varepsilon > 0\), choose \(\delta > 0\) so that

\[
\tag{2.5}
\left| S(f; P) - \int_a^b f \right| < \tfrac{1}{2}\varepsilon, \qquad
\left| S(f; Q) - \int_b^c f \right| < \tfrac{1}{2}\varepsilon
\]

whenever \(P\) is a partition of \([a, b]\) with \(|P| < \delta\) and \(Q\) is a partition of \([b, c]\) with \(|Q| < \delta\).

Now let \(P'\) be any partition of \([a, c]\) with \(|P'| < \delta\). Add the point \(b\) to \(P'\) if it is not already present; let the resulting partition be \(P''\). Then \(|P''| \leq |P'| < \delta\). The points of \(P''\) in \([a, b]\) form a partition \(P_1\) of \([a, b]\) and the points of \(P''\) in \([b, c]\) form a partition \(P_2\) of \([b, c]\). Both have mesh \(< \delta\). Moreover,

\[
S(f; P'') = S(f; P_1) + S(f; P_2).
\]

The Riemann sum \(S(f; P')\) differs from \(S(f; P'')\) only in the subinterval that contains the added point \(b\); since \(f\) is bounded, this difference tends to zero with the mesh. More precisely, refining a partition by one point changes the Riemann sum by at most \(2M|P'|\) where \(M = \sup |f|\). Therefore, for sufficiently small \(\delta\), we have

\[
\left| S(f; P') - \left( \int_a^b f + \int_b^c f \right) \right| < \varepsilon.
\]

It follows that \(f\) is integrable on \([a, c]\) with integral \(\int_a^b f + \int_b^c f\).

Conversely, suppose \(f\) is not integrable on \([a, b]\) (the argument for \([b, c]\) is symmetric). Then there exists \(\varepsilon > 0\) such that for every \(\delta > 0\) there are partitions \(P_1, P_2\) of \([a, b]\) with \(|P_1| < \delta, |P_2| < \delta\) but

\[
|S(f; P_1) - S(f; P_2)| > \varepsilon.
\]

Choose a partition \(Q\) of \([b, c]\) with \(|Q| < \delta\) (possible by taking a sufficiently fine uniform partition). Let \(P_1', P_2'\) be the partitions of \([a, c]\) obtained by taking all points of \(Q\) together with the points of \(P_1, P_2\) respectively. Then \(|P_1'| < \delta, |P_2'| < \delta\), and

\[
S(f; P_1') = S(f; P_1) + S(f; Q), \qquad
S(f; P_2') = S(f; P_2) + S(f; Q),
\]

so

\[
|S(f; P_1') - S(f; P_2')| = |S(f; P_1) - S(f; P_2)| > \varepsilon.
\]

By Proposition 2.3 (the Cauchy criterion), \(f\) is not integrable on \([a, c]\). \(\square\)
