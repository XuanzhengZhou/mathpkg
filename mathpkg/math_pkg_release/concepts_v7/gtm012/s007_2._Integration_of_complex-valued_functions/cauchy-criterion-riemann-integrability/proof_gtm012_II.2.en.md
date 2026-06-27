---
role: proof
locale: en
of_concept: cauchy-criterion-riemann-integrability
source_book: gtm012
source_chapter: "2"
source_section: "2. Integration of complex-valued functions"
---

# Proof of Cauchy criterion for Riemann integrability

**Proposition 2.3.** A bounded function \(f: [a, b] \to \mathbb{C}\) is integrable if and only if for every \(\varepsilon > 0\) there exists \(\delta > 0\) such that

\[
|S(f; P) - S(f; Q)| < \varepsilon
\]

whenever \(P\) and \(Q\) are partitions of \([a, b]\) with \(|P| < \delta\) and \(|Q| < \delta\).

*Proof.* \((\Leftarrow)\) Suppose the Cauchy condition holds. For each \(n \in \mathbb{N}\), choose \(\delta_n > 0\) such that \(|S(f; P) - S(f; Q)| < 1/n\) whenever \(|P|, |Q| < \delta_n\). Pick a sequence of partitions \(P_n\) with \(|P_n| < \delta_n\). Then \((S(f; P_n))_{n=1}^\infty\) is a Cauchy sequence in \(\mathbb{C}\), hence converges to some \(z \in \mathbb{C}\).

Given \(\varepsilon > 0\), choose \(N\) with \(1/N < \varepsilon/2\) and such that \(|S(f; P_N) - z| < \varepsilon/2\). Take \(\delta = \delta_N\). Then for any partition \(P\) with \(|P| < \delta\),

\[
|S(f; P) - z| \leq |S(f; P) - S(f; P_N)| + |S(f; P_N) - z| < \frac{1}{N} + \frac{\varepsilon}{2} < \varepsilon.
\]

Thus \(\lim_{|P| \to 0} S(f; P) = z\), so \(f\) is integrable with integral \(z\).

\((\Rightarrow)\) Suppose \(f\) is integrable with integral \(z\). Given \(\varepsilon > 0\), choose \(\delta > 0\) such that \(|S(f; P) - z| < \varepsilon/2\) whenever \(|P| < \delta\). Then for any partitions \(P, Q\) with \(|P|, |Q| < \delta\),

\[
|S(f; P) - S(f; Q)| \leq |S(f; P) - z| + |z - S(f; Q)| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
\]

\(\square\)
