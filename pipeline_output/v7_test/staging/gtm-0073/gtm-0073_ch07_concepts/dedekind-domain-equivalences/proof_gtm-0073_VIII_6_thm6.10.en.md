---
role: proof
source_book: gtm-0073
chapter: "VIII"
section: "VIII.6"
proof_technique: cyclic-implications
locale: en
content_hash: ""
written_against: ""
---
The proof establishes a cycle of implications: (i) \(\Rightarrow\) (ii) \(\Rightarrow\) (iii), (iv) \(\Leftrightarrow\) (v) (trivial), (iii) \(\Leftrightarrow\) (vi) and (vii) \(\Leftrightarrow\) (iv) via Theorem 6.8, (vi) \(\Rightarrow\) (vii) via the Remark preceding Theorem 6.3. The critical remaining links are (iv) \(\Rightarrow\) (viii), (viii) \(\Rightarrow\) (ix), and (ix) \(\Rightarrow\) (i).

(iv) \(\Rightarrow\) (viii): Invertibility implies finite generation (Lemma 6.7), so \(R\) is Noetherian. If \(u \in K\) is integral, \(R[u]\) is a finitely generated fractional ideal, hence invertible; since \(R[u]R[u] = R[u]\), multiplying by the inverse gives \(R[u] = R\), so \(u \in R\) and \(R\) is integrally closed. Every nonzero prime is maximal by a contradiction argument using the invertibility of powers.

(viii) \(\Rightarrow\) (ix): For a nonzero prime \(P\), the localization \(R_P\) is a local Noetherian domain whose maximal ideal is principal, hence a discrete valuation ring.

(ix) \(\Rightarrow\) (i): Uses the local-global principle: an ideal is determined by its localizations; since each \(R_P\) is a DVR, proper ideals factor as products of prime ideals.
