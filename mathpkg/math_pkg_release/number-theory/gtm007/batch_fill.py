#!/usr/bin/env python3
"""Batch fill incomplete concept directories for GTM007."""
import os, yaml

BASE = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch1/gtm007"

# ============================================================
# SECTION 1: s001 - Chapter I, §1-2 (Finite Fields, Generalities)
# ============================================================

def write_frobenius_endomorphism():
    d = f"{BASE}/frobenius-endomorphism-in-characteristic-p"
    os.makedirs(d, exist_ok=True)

    # concept.yaml
    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'frobenius-endomorphism-in-characteristic-p',
            'title_en': 'Frobenius endomorphism in characteristic p',
            'title_zh': '',
            'type': 'lemma',
            'domain': 'algebra',
            'subdomain': 'finite-fields',
            'difficulty': 'basic',
            'tags': ['frobenius', 'finite-field', 'characteristic-p'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'I', 'section': '1.1', 'pages': '1',
                             'role_in_book': 'Lemma: Frobenius map is an isomorphism onto K^p'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # theorem.tex
    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""If $\operatorname{char}(K) = p$, the map $\sigma: x \mapsto x^p$ is an isomorphism of $K$ onto one of its subfields $K^p$. Moreover, $\sigma(xy) = \sigma(x)\sigma(y)$ and $\sigma(x+y) = \sigma(x) + \sigma(y)$.
""")

    # introduce.en.md
    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
The Frobenius endomorphism $x \\mapsto x^p$ is a fundamental tool in the study of fields of prime characteristic. In characteristic $p$, it is a field homomorphism (and an isomorphism onto the subfield of $p$-th powers) because the binomial coefficients $\\binom{p}{k}$ vanish modulo $p$ for $0 < k < p$.
""")

    # proof (lemma has proof)
    with open(f"{d}/proof_gtm007_I_1_1.en.md", 'w') as f:
        f.write(r"""---
role: proof
locale: en
of_concept: "frobenius-endomorphism-in-characteristic-p"
source_book: gtm007
source_chapter: "I"
source_section: "1.1"
---
We have $\sigma(xy) = (xy)^p = x^p y^p = \sigma(x)\sigma(y)$. Moreover, the binomial coefficient $\binom{p}{k}$ is congruent to $0 \pmod{p}$ if $0 < k < p$. From this it follows that
$$\sigma(x+y) = (x+y)^p = x^p + \sum_{k=1}^{p-1} \binom{p}{k} x^k y^{p-k} + y^p = x^p + y^p = \sigma(x) + \sigma(y).$$
Hence $\sigma$ is a homomorphism. Furthermore, $\sigma$ is clearly injective since $x^p = 0$ implies $x = 0$.
""")


def write_classification_finite_fields():
    d = f"{BASE}/classification-of-finite-fields"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'classification-of-finite-fields',
            'title_en': 'Classification of finite fields',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'algebra',
            'subdomain': 'finite-fields',
            'difficulty': 'basic',
            'tags': ['finite-field', 'classification', 'frobenius'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'I', 'section': '1.1', 'pages': '1-2',
                             'role_in_book': 'Theorem 1: structure and classification of finite fields'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""(i) The characteristic of a finite field $K$ is a prime number $p \neq 0$; if $f = [K:\mathbb{F}_p]$, the number of elements of $K$ is $q = p^f$.

(ii) Let $p$ be a prime number and let $q = p^f$ ($f \geq 1$) be a power of $p$. Let $\Omega$ be an algebraically closed field of characteristic $p$. There exists a unique subfield $\mathbb{F}_q$ of $\Omega$ which has $q$ elements. It is the set of roots of the polynomial $X^q - X$.

(iii) All finite fields with $q = p^f$ elements are isomorphic to $\mathbb{F}_q$.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
This theorem completely classifies finite fields: every finite field has prime power order $p^f$, and for each such order there exists exactly one finite field up to isomorphism. The field $\\mathbb{F}_q$ is characterized as the splitting field of $X^q - X$ over $\\mathbb{F}_p$.
""")


def write_cyclic_multiplicative_group():
    d = f"{BASE}/multiplicative-group-of-finite-field-cyclic"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'multiplicative-group-of-finite-field-cyclic',
            'title_en': 'The multiplicative group of a finite field is cyclic',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'algebra',
            'subdomain': 'finite-fields',
            'difficulty': 'basic',
            'tags': ['finite-field', 'cyclic-group', 'multiplicative-group'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'I', 'section': '1.2', 'pages': '2',
                             'role_in_book': 'Theorem 2: F_q* is cyclic of order q-1'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""The multiplicative group $\mathbb{F}_q^*$ of a finite field $\mathbb{F}_q$ is cyclic of order $q-1$.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
A fundamental structural result: the nonzero elements of any finite field form a cyclic group under multiplication. This fact is essential for many applications, including the theory of primitive roots, discrete logarithms, and the proof of quadratic reciprocity.
""")


def write_euler_phi_sum():
    d = f"{BASE}/euler-phi-sum-over-divisors"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'euler-phi-sum-over-divisors',
            'title_en': 'Euler totient divisor sum identity',
            'title_zh': '',
            'type': 'lemma',
            'domain': 'number-theory',
            'subdomain': 'elementary',
            'difficulty': 'basic',
            'tags': ['euler-totient', 'divisor-sum', 'elementary-number-theory'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'I', 'section': '1.2', 'pages': '2',
                             'role_in_book': 'Lemma 1: identity used to prove F_q* is cyclic'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""If $n$ is an integer $\geq 1$, then
$$n = \sum_{d \mid n} \phi(d),$$
where $\phi(d)$ denotes the Euler totient function (the number of integers $x$ with $1 \leq x \leq d$ which are coprime to $d$).
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
This classical identity expresses a positive integer $n$ as the sum of Euler's totient function over all divisors of $n$. It follows from partitioning the set $\\{1, \\ldots, n\\}$ according to the greatest common divisor with $n$, or equivalently from counting generators of cyclic subgroups.
""")


def write_power_sums_lemma():
    d = f"{BASE}/power-sums-over-finite-field"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'power-sums-over-finite-field',
            'title_en': 'Power sums over a finite field',
            'title_zh': '',
            'type': 'lemma',
            'domain': 'algebra',
            'subdomain': 'finite-fields',
            'difficulty': 'basic',
            'tags': ['finite-field', 'power-sum', 'character-sum'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'I', 'section': '2.1', 'pages': '2-3',
                             'role_in_book': 'Lemma: evaluation of power sums S(X^u) over finite field'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $K$ be a finite field with $q$ elements. For an integer $u \geq 0$, let $S(X^u) = \sum_{x \in K} x^u$ (with the convention $0^0 = 1$). Then:
$$S(X^u) = \begin{cases} -1 & \text{if } u \geq 1 \text{ and } u \equiv 0 \pmod{q-1}, \\ 0 & \text{otherwise.} \end{cases}$$
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
This lemma computes the sum of $u$-th powers over all elements of a finite field. It is a key ingredient in the Chevalley-Warning theorem and many other polynomial-method arguments. The proof exploits the cyclicity of the multiplicative group.
""")


# ============================================================
# SECTION 2: s002 - Chapter I, §3 (Quadratic Reciprocity Law)
# ============================================================

def write_squares_in_finite_field():
    d = f"{BASE}/squares-in-finite-fields"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'squares-in-finite-fields',
            'title_en': 'Squares in finite fields',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'algebra',
            'subdomain': 'finite-fields',
            'difficulty': 'basic',
            'tags': ['finite-field', 'quadratic-residue', 'squares'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'I', 'section': '3.1', 'pages': '5',
                             'role_in_book': 'Theorem 4: squares in F_q'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""(a) If $p = 2$, then all elements of $\mathbb{F}_q$ are squares.

(b) If $p \neq 2$, then the squares of $\mathbb{F}_q^*$ form a subgroup of index $2$ in $\mathbb{F}_q^*$; this subgroup is the kernel of the homomorphism $x \mapsto x^{(q-1)/2}$ with values in $\{\pm 1\}$.

In other terms, one has an exact sequence:
$$1 \rightarrow \mathbb{F}_q^{*2} \rightarrow \mathbb{F}_q^* \rightarrow \{\pm 1\} \rightarrow 1.$$
""")


def write_legendre_symbol():
    d = f"{BASE}/legendre-symbol"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'legendre-symbol',
            'title_en': 'Legendre symbol',
            'title_zh': '',
            'type': 'definition',
            'domain': 'number-theory',
            'subdomain': 'quadratic-reciprocity',
            'difficulty': 'basic',
            'tags': ['legendre-symbol', 'quadratic-residue'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'I', 'section': '3.2', 'pages': '5-6',
                             'role_in_book': 'Definition of Legendre symbol (x/p)'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $p$ be a prime number $\neq 2$, and let $x \in \mathbb{F}_p^*$. The Legendre symbol of $x$ is defined by:
$$\left(\frac{x}{p}\right) = x^{(p-1)/2} = \begin{cases} +1 & \text{if } x \text{ is a square in } \mathbb{F}_p^*, \\ -1 & \text{otherwise.} \end{cases}$$
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
The Legendre symbol $(x/p)$ is a multiplicative character of $\\mathbb{F}_p^*$ that encodes whether $x$ is a quadratic residue modulo $p$. It is the fundamental tool for stating and proving the quadratic reciprocity law.
""")


def write_legendre_formulas():
    d = f"{BASE}/legendre-symbol-formulas"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'legendre-symbol-formulas',
            'title_en': 'Legendre symbol formulas for 1, -1, 2',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'quadratic-reciprocity',
            'difficulty': 'basic',
            'tags': ['legendre-symbol', 'quadratic-reciprocity', 'supplementary-laws'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'I', 'section': '3.2', 'pages': '6',
                             'role_in_book': 'Theorem 5: computation of Legendre symbol for 1, -1, 2'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""For an odd prime $p$:
$$\text{(i) } \left(\frac{1}{p}\right) = 1$$
$$\text{(ii) } \left(\frac{-1}{p}\right) = (-1)^{\varepsilon(p)} \quad \text{where } \varepsilon(p) \equiv \frac{p-1}{2} \pmod{2}$$
$$\text{(iii) } \left(\frac{2}{p}\right) = (-1)^{\omega(p)} \quad \text{where } \omega(p) \equiv \frac{p^2-1}{8} \pmod{2}$$
These are the "supplementary laws" of quadratic reciprocity.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
The supplementary laws of quadratic reciprocity determine when $-1$ and $2$ are quadratic residues modulo an odd prime $p$. They form part of the complete set of rules for evaluating Legendre symbols, alongside the main reciprocity law.
""")


def write_quadratic_reciprocity_law():
    d = f"{BASE}/quadratic-reciprocity-law"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'quadratic-reciprocity-law',
            'title_en': 'Quadratic reciprocity law',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'quadratic-reciprocity',
            'difficulty': 'intermediate',
            'tags': ['quadratic-reciprocity', 'legendre-symbol', 'gauss'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'I', 'section': '3.3', 'pages': '6-7',
                             'role_in_book': 'Theorem 6: quadratic reciprocity law'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $l$ and $p$ be two distinct odd primes. Then:
$$\left(\frac{l}{p}\right) \left(\frac{p}{l}\right) = (-1)^{\varepsilon(l)\varepsilon(p)}$$
where $\varepsilon(n) \equiv \frac{n-1}{2} \pmod{2}$.

Equivalently, $\left(\frac{l}{p}\right) = \left(\frac{p}{l}\right)$ unless $l \equiv p \equiv 3 \pmod{4}$, in which case $\left(\frac{l}{p}\right) = -\left(\frac{p}{l}\right)$.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
The quadratic reciprocity law, first proved by Gauss, is one of the crowning achievements of elementary number theory. It relates the solvability of $x^2 \\equiv l \\pmod{p}$ to that of $x^2 \\equiv p \\pmod{l}$, providing an efficient method for computing Legendre symbols.
""")


def write_gauss_lemma():
    d = f"{BASE}/gauss-lemma-quadratic-reciprocity"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'gauss-lemma-quadratic-reciprocity',
            'title_en': "Gauss's lemma for quadratic reciprocity",
            'title_zh': '',
            'type': 'lemma',
            'domain': 'number-theory',
            'subdomain': 'quadratic-reciprocity',
            'difficulty': 'intermediate',
            'tags': ['gauss-lemma', 'quadratic-reciprocity', 'legendre-symbol'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'I', 'section': 'Appendix', 'pages': '8',
                             'role_in_book': 'Gauss Lemma for computing Legendre symbol (a/p)'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $p$ be an odd prime, and let $S = \{1, \ldots, \frac{p-1}{2}\}$. For $a \in \mathbb{F}_p^*$ and $s \in S$, write $as = e_s(a) s_a$ with $e_s(a) = \pm 1$ and $s_a \in S$. Then:
$$\left(\frac{a}{p}\right) = \prod_{s \in S} e_s(a).$$
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
Gauss's lemma provides a combinatorial interpretation of the Legendre symbol: $(a/p)$ equals the sign of the permutation of $S = \\{1, \\ldots, (p-1)/2\\}$ induced by multiplication by $a$ modulo $p$. It is a key step in many proofs of quadratic reciprocity, including Gauss's original proof and Eisenstein's geometric proof.
""")


# ============================================================
# SECTION 3: s003 - Chapter II, §1 (Z_p and Q_p)
# ============================================================

def write_ring_zp():
    d = f"{BASE}/ring-of-p-adic-integers"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'ring-of-p-adic-integers',
            'title_en': 'Ring of p-adic integers Z_p',
            'title_zh': '',
            'type': 'definition',
            'domain': 'number-theory',
            'subdomain': 'p-adic',
            'difficulty': 'intermediate',
            'tags': ['p-adic', 'projective-limit', 'completion'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'II', 'section': '1.1', 'pages': '9',
                             'role_in_book': 'Definition 1: Z_p as projective limit of Z/p^nZ'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""For every $n \geq 1$, let $A_n = \mathbb{Z}/p^n\mathbb{Z}$. The homomorphism $\phi_n: A_n \rightarrow A_{n-1}$ is the natural surjection with kernel $p^{n-1}A_n$. The ring of $p$-adic integers is the projective limit:
$$\mathbb{Z}_p = \varprojlim_{n \geq 1} (A_n, \phi_n).$$
An element of $\mathbb{Z}_p$ is a sequence $x = (\ldots, x_n, \ldots, x_1)$ with $x_n \in A_n$ and $\phi_n(x_n) = x_{n-1}$ for $n \geq 2$.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
The ring $\\mathbb{Z}_p$ of $p$-adic integers is constructed as the projective limit of the finite rings $\\mathbb{Z}/p^n\\mathbb{Z}$. This construction endows $\\mathbb{Z}_p$ with a natural compact topology and makes it a complete discrete valuation ring. It is the fundamental object of $p$-adic analysis.
""")


def write_field_qp():
    d = f"{BASE}/field-of-p-adic-numbers"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'field-of-p-adic-numbers',
            'title_en': 'Field of p-adic numbers Q_p',
            'title_zh': '',
            'type': 'definition',
            'domain': 'number-theory',
            'subdomain': 'p-adic',
            'difficulty': 'intermediate',
            'tags': ['p-adic', 'completion', 'valuation'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'II', 'section': '1.3', 'pages': '10-11',
                             'role_in_book': 'Definition of Q_p as field of fractions of Z_p'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""The field of $p$-adic numbers $\mathbb{Q}_p$ is the field of fractions of the ring $\mathbb{Z}_p$. Equivalently, $\mathbb{Q}_p = \mathbb{Z}_p[p^{-1}]$. Every nonzero element $x \in \mathbb{Q}_p$ can be written uniquely as $x = p^n u$ where $n \in \mathbb{Z}$ and $u$ is a $p$-adic unit (an invertible element of $\mathbb{Z}_p$).
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
The field $\\mathbb{Q}_p$ of $p$-adic numbers is the completion of $\\mathbb{Q}$ with respect to the $p$-adic absolute value. It is a locally compact, totally disconnected topological field that plays a central role in modern number theory, analogous to $\\mathbb{R}$ as a completion of $\\mathbb{Q}$.
""")


def write_exact_sequence_zp():
    d = f"{BASE}/exact-sequence-zp-pn-zp-an"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'exact-sequence-zp-pn-zp-an',
            'title_en': 'Exact sequence for multiplication by p^n in Z_p',
            'title_zh': '',
            'type': 'proposition',
            'domain': 'number-theory',
            'subdomain': 'p-adic',
            'difficulty': 'basic',
            'tags': ['p-adic', 'exact-sequence', 'Z_p'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'II', 'section': '1.2', 'pages': '10',
                             'role_in_book': 'Proposition 1: exact sequence for Z_p'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""The sequence
$$0 \rightarrow \mathbb{Z}_p \xrightarrow{p^n} \mathbb{Z}_p \xrightarrow{\varepsilon_n} A_n \rightarrow 0$$
is exact, where $\varepsilon_n$ maps a $p$-adic integer $x = (x_m)$ to its $n$-th component $x_n \in A_n = \mathbb{Z}/p^n\mathbb{Z}$.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
This fundamental exact sequence captures the relationship between $\\mathbb{Z}_p$ and its finite quotients $\\mathbb{Z}/p^n\\mathbb{Z}$. It shows that $\\mathbb{Z}_p/p^n\\mathbb{Z}_p \\cong \\mathbb{Z}/p^n\\mathbb{Z}$, which is essential for computations in the $p$-adic world.
""")


def write_invertible_elements_zp():
    d = f"{BASE}/invertible-elements-of-zp"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'invertible-elements-of-zp',
            'title_en': 'Invertible elements of Z_p and p-adic units',
            'title_zh': '',
            'type': 'proposition',
            'domain': 'number-theory',
            'subdomain': 'p-adic',
            'difficulty': 'basic',
            'tags': ['p-adic', 'units', 'Z_p'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'II', 'section': '1.2', 'pages': '10',
                             'role_in_book': 'Proposition 2: characterization of invertible elements in Z_p'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""(a) An element of $\mathbb{Z}_p$ (resp. of $A_n$) is invertible if and only if it is not divisible by $p$.

(b) If $U$ denotes the group of invertible elements of $\mathbb{Z}_p$ (the $p$-adic units), every nonzero element of $\mathbb{Z}_p$ can be written uniquely in the form $p^n u$ with $u \in U$ and $n \geq 0$.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
The $p$-adic units are precisely the elements of $\\mathbb{Z}_p$ not divisible by $p$. This gives $\\mathbb{Z}_p$ the structure of a discrete valuation ring with uniformizer $p$, and every nonzero element has a unique factorization as a power of $p$ times a unit.
""")


def write_qp_locally_compact():
    d = f"{BASE}/q-p-is-locally-compact"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'q-p-is-locally-compact',
            'title_en': 'Q_p is locally compact',
            'title_zh': '',
            'type': 'proposition',
            'domain': 'number-theory',
            'subdomain': 'p-adic',
            'difficulty': 'basic',
            'tags': ['p-adic', 'locally-compact', 'topology'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'II', 'section': '1.3', 'pages': '11',
                             'role_in_book': 'Proposition 4: Q_p is locally compact with Z_p as open subring'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""The field $\mathbb{Q}_p$, with the topology defined by $d(x, y) = e^{-v_p(x-y)}$, is locally compact, and contains $\mathbb{Z}_p$ as an open subring; the field $\mathbb{Q}$ is dense in $\mathbb{Q}_p$.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
Like $\\mathbb{R}$, the field $\\mathbb{Q}_p$ is a locally compact completion of $\\mathbb{Q}$. This property is fundamental for harmonic analysis on $p$-adic fields and for the adelic formulation of class field theory.
""")


def write_projective_limit_nonempty():
    d = f"{BASE}/projective-limit-nonempty"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'projective-limit-nonempty',
            'title_en': 'Projective limit of finite nonempty sets is nonempty',
            'title_zh': '',
            'type': 'lemma',
            'domain': 'foundations',
            'subdomain': 'projective-limits',
            'difficulty': 'basic',
            'tags': ['projective-limit', 'compactness', 'finite-sets'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'II', 'section': '2.1', 'pages': '12',
                             'role_in_book': 'Lemma: projective limit of finite nonempty sets is nonempty'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $\ldots \rightarrow D_n \rightarrow D_{n-1} \rightarrow \ldots \rightarrow D_1$ be a projective system of sets (with transition maps not necessarily surjective), and let $D = \varprojlim D_n$ be its projective limit. If the $D_n$ are finite and nonempty, then $D$ is nonempty.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
This compactness-type lemma is fundamental in $p$-adic analysis. It guarantees that a compatible system of approximate solutions (mod $p^n$) lifts to a genuine $p$-adic solution, forming the basis for Hensel's lemma and Newton's method in the $p$-adic setting.
""")


def write_common_zero_equivalent_conditions():
    d = f"{BASE}/common-zero-equivalent-conditions"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'common-zero-equivalent-conditions',
            'title_en': 'Equivalent conditions for common zeros of homogeneous polynomials over Z_p',
            'title_zh': '',
            'type': 'proposition',
            'domain': 'number-theory',
            'subdomain': 'p-adic',
            'difficulty': 'intermediate',
            'tags': ['p-adic', 'polynomial-equations', 'homogeneous'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'II', 'section': '2.1', 'pages': '12',
                             'role_in_book': 'Proposition 6: equivalence of nontrivial zero in Q_p, primitive zero in Z_p, and solutions mod p^n'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $f^{(i)} \in \mathbb{Z}_p[X_1, \ldots, X_m]$ be homogeneous polynomials with $p$-adic integer coefficients. The following are equivalent:
\begin{enumerate}
\item[(a)] The $f^{(i)}$ have a nontrivial common zero in $(\mathbb{Q}_p)^m$.
\item[(b)] The $f^{(i)}$ have a common primitive zero in $(\mathbb{Z}_p)^m$.
\item[(c)] For all $n > 1$, the reductions $f_n^{(i)}$ have a common primitive zero in $(A_n)^m$ where $A_n = \mathbb{Z}/p^n\mathbb{Z}$.
\end{enumerate}
""")


def write_hensels_lemma():
    d = f"{BASE}/hensels-lemma"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'hensels-lemma',
            'title_en': "Hensel's lemma (p-adic Newton method)",
            'title_zh': '',
            'type': 'lemma',
            'domain': 'number-theory',
            'subdomain': 'p-adic',
            'difficulty': 'intermediate',
            'tags': ['p-adic', 'hensels-lemma', 'newton-method', 'lifting'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'II', 'section': '2.2', 'pages': '12-13',
                             'role_in_book': 'Lemma: p-adic analogue of Newton method for lifting approximate roots'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $f \in \mathbb{Z}_p[X]$ and let $f'$ be its derivative. Let $x \in \mathbb{Z}_p$, $n, k \in \mathbb{Z}$ such that $0 \leq 2k < n$, $f(x) \equiv 0 \pmod{p^n}$, $v_p(f'(x)) = k$. Then there exists $y \in \mathbb{Z}_p$ such that:
$$f(y) \equiv 0 \pmod{p^{n+1}}, \quad v_p(f'(y)) = k, \quad y \equiv x \pmod{p^{n-k}}.$$
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
Hensel's lemma is the $p$-adic analogue of Newton's method for finding roots of equations. It allows one to lift approximate solutions modulo $p^n$ to exact $p$-adic solutions, provided the derivative does not vanish too much. It is one of the most important tools in $p$-adic analysis and number theory.
""")


def write_simple_zero_lifts():
    d = f"{BASE}/simple-zero-lifts"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'simple-zero-lifts',
            'title_en': 'Simple zeros lift to p-adic zeros',
            'title_zh': '',
            'type': 'corollary',
            'domain': 'number-theory',
            'subdomain': 'p-adic',
            'difficulty': 'basic',
            'tags': ['p-adic', 'hensels-lemma', 'lifting', 'simple-zero'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'II', 'section': '2.2', 'pages': '13',
                             'role_in_book': 'Corollary 1 to Hensel: simple zeros modulo p lift to Z_p'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Every simple zero of the reduction modulo $p$ of a polynomial $f$ lifts to a zero of $f$ with coefficients in $\mathbb{Z}_p$.

(A zero $x$ of $g$ over a field $k$ is called simple if at least one of the partial derivatives $\partial g / \partial X_j$ is nonzero at $x$.)
""")


def write_structure_of_qp_star():
    d = f"{BASE}/structure-of-qp-star"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'structure-of-qp-star',
            'title_en': 'Structure of the multiplicative group Q_p^*',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'p-adic',
            'difficulty': 'intermediate',
            'tags': ['p-adic', 'multiplicative-group', 'units', 'structure-theorem'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'II', 'section': '2.3', 'pages': '14',
                             'role_in_book': 'Theorem 2: decomposition of Q_p^*'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""If $p \neq 2$, one has $\mathbb{Q}_p^* \simeq \mathbb{Z} \times \mathbb{F}_p^* \times \mathbb{Z}_p$ (as topological groups).

If $p = 2$, one has $\mathbb{Q}_2^* \simeq \mathbb{Z} \times \{\pm 1\} \times \mathbb{Z}_2$.
""")


def write_squares_in_qp():
    d = f"{BASE}/squares-in-qp"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'squares-in-qp',
            'title_en': 'Squares in Q_p',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'p-adic',
            'difficulty': 'basic',
            'tags': ['p-adic', 'squares', 'quadratic-residue'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'II', 'section': '3.3', 'pages': '17',
                             'role_in_book': 'Theorem 3: characterization of squares in Q_p for p≠2'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $p \neq 2$, and let $x = p^n u$ be an element of $\mathbb{Q}_p^*$, with $u \in U$ ($p$-adic units). For $x$ to be a square it is necessary and sufficient that $n$ is even and $\left(\frac{u}{p}\right) = 1$ (where $\bar{u} \in \mathbb{F}_p^*$ is the reduction of $u$ modulo $p$).
""")


def write_squares_in_q2():
    d = f"{BASE}/squares-in-q2"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'squares-in-q2',
            'title_en': 'Squares in Q_2',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'p-adic',
            'difficulty': 'basic',
            'tags': ['p-adic', '2-adic', 'squares'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'II', 'section': '3.3', 'pages': '17-18',
                             'role_in_book': 'Theorem 4: characterization of squares in Q_2'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""For an element $x = 2^n u$ of $\mathbb{Q}_2^*$ (with $u \in U$, the group of 2-adic units) to be a square it is necessary and sufficient that $n$ is even and $u \equiv 1 \pmod{8}$.
""")


def write_p_adic_unit_group_structure():
    d = f"{BASE}/p-adic-unit-group-structure"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'p-adic-unit-group-structure',
            'title_en': 'Structure of the group of principal p-adic units',
            'title_zh': '',
            'type': 'proposition',
            'domain': 'number-theory',
            'subdomain': 'p-adic',
            'difficulty': 'intermediate',
            'tags': ['p-adic', 'units', 'group-structure'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'II', 'section': '3.2', 'pages': '15-16',
                             'role_in_book': 'Proposition 8: structure of U_1 for p≠2 and p=2'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""If $p \neq 2$, $U_1 = 1 + p\mathbb{Z}_p$ is isomorphic to $\mathbb{Z}_p$ (the additive group).

If $p = 2$, $U_1 = \{\pm 1\} \times U_2$ and $U_2 = 1 + 4\mathbb{Z}_2$ is isomorphic to $\mathbb{Z}_2$.
""")


# ============================================================
# SECTION 4: s004 - Chapter III, §1 (Hilbert Symbol, Local)
# ============================================================

def write_hilbert_symbol():
    d = f"{BASE}/hilbert-symbol"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'hilbert-symbol',
            'title_en': 'Hilbert symbol',
            'title_zh': '',
            'type': 'definition',
            'domain': 'number-theory',
            'subdomain': 'hilbert-symbol',
            'difficulty': 'intermediate',
            'tags': ['hilbert-symbol', 'quadratic-forms', 'local-field'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'III', 'section': '1.1', 'pages': '19',
                             'role_in_book': 'Definition of the Hilbert symbol (a,b) for a local field'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $k$ be either $\mathbb{R}$ or $\mathbb{Q}_p$. For $a, b \in k^*$, the Hilbert symbol $(a, b)$ is defined by:
$$(a, b) = \begin{cases} +1 & \text{if } z^2 - ax^2 - by^2 = 0 \text{ has a nontrivial solution } (z,x,y) \neq (0,0,0) \text{ in } k^3, \\ -1 & \text{otherwise.} \end{cases}$$
The number $(a, b) = \pm 1$ does not change when $a$ and $b$ are multiplied by squares; it defines a map $k^*/k^{*2} \times k^*/k^{*2} \rightarrow \{\pm 1\}$.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
The Hilbert symbol $(a,b)$ encodes whether the quadratic form $z^2 - ax^2 - by^2$ represents zero nontrivially over a local field. It is a nondegenerate symmetric bilinear pairing on $k^*/k^{*2}$ with values in $\\{\\pm 1\\}$, and it generalizes the Legendre symbol to the $p$-adic setting.
""")


def write_hilbert_symbol_norm():
    d = f"{BASE}/hilbert-symbol-norm-criterion"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'hilbert-symbol-norm-criterion',
            'title_en': 'Hilbert symbol and norm criterion',
            'title_zh': '',
            'type': 'proposition',
            'domain': 'number-theory',
            'subdomain': 'hilbert-symbol',
            'difficulty': 'intermediate',
            'tags': ['hilbert-symbol', 'norm', 'quadratic-extension'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'III', 'section': '1.1', 'pages': '19-20',
                             'role_in_book': 'Proposition 1: (a,b)=1 iff a is a norm from k(sqrt(b))'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $a, b \in k^*$ and let $k_b = k(\sqrt{b})$. Then $(a, b) = 1$ if and only if $a$ belongs to the group $N(k_b^*)$ of norms of elements of $k_b^*$.
""")


def write_hilbert_symbol_properties():
    d = f"{BASE}/hilbert-symbol-properties"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'hilbert-symbol-properties',
            'title_en': 'Properties of the Hilbert symbol',
            'title_zh': '',
            'type': 'proposition',
            'domain': 'number-theory',
            'subdomain': 'hilbert-symbol',
            'difficulty': 'intermediate',
            'tags': ['hilbert-symbol', 'bilinear', 'nondegenerate'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'III', 'section': '1.1', 'pages': '20',
                             'role_in_book': 'Basic properties: bilinearity, nondegeneracy'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""The Hilbert symbol satisfies:
\begin{itemize}
\item[(i)] $(a, b) = (b, a)$ (symmetry).
\item[(ii)] $(a, -a) = 1$ and $(a, 1-a) = 1$.
\item[(iii)] $(aa', b) = (a, b)(a', b)$ (bilinearity).
\item[(iv)] The induced bilinear form on $k^*/k^{*2} \times k^*/k^{*2} \to \{\pm 1\}$ is nondegenerate.
\end{itemize}
""")


def write_computation_of_hilbert_symbol():
    d = f"{BASE}/computation-of-hilbert-symbol"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'computation-of-hilbert-symbol',
            'title_en': 'Explicit computation of the Hilbert symbol',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'hilbert-symbol',
            'difficulty': 'intermediate',
            'tags': ['hilbert-symbol', 'computation', 'legendre-symbol'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'III', 'section': '1.2', 'pages': '20-21',
                             'role_in_book': 'Theorem 1: explicit formula for Hilbert symbol over R and Q_p'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""If $k = \mathbb{R}$, then $(a, b) = 1$ if $a$ or $b$ is $> 0$, and $(a, b) = -1$ if $a$ and $b$ are $< 0$.

If $k = \mathbb{Q}_p$ and $a = p^\alpha u$, $b = p^\beta v$ with $u, v \in U$:

For $p \neq 2$:
$$(a, b) = (-1)^{\alpha\beta \varepsilon(p)} \left(\frac{u}{p}\right)^\beta \left(\frac{v}{p}\right)^\alpha$$

For $p = 2$:
$$(a, b) = (-1)^{\varepsilon(u)\varepsilon(v) + \alpha\omega(v) + \beta\omega(u)}$$
where $\varepsilon(n) \equiv \frac{n-1}{2} \pmod{2}$ and $\omega(n) \equiv \frac{n^2-1}{8} \pmod{2}$.
""")


# ============================================================
# SECTION 5: s005 - Chapter III, §2 (Hilbert Symbol, Global)
# ============================================================

def write_hilbert_product_formula():
    d = f"{BASE}/hilbert-product-formula"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'hilbert-product-formula',
            'title_en': "Hilbert's product formula",
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'hilbert-symbol',
            'difficulty': 'intermediate',
            'tags': ['hilbert-symbol', 'product-formula', 'quadratic-reciprocity', 'global-field'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'III', 'section': '2.1', 'pages': '22',
                             'role_in_book': 'Theorem 3 (Hilbert): product formula for Hilbert symbols over Q'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""If $a, b \in \mathbb{Q}^*$, then for almost all $v \in V$ (the set of prime numbers together with $\infty$) we have $(a, b)_v = 1$, and:
$$\prod_{v \in V} (a, b)_v = 1.$$
Here $(a, b)_p$ (resp. $(a, b)_\infty$) denotes the Hilbert symbol of the images of $a, b$ in $\mathbb{Q}_p$ (resp. $\mathbb{R}$).
""")


def write_existence_rational_hilbert_symbols():
    d = f"{BASE}/existence-of-rational-with-given-hilbert-symbols"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'existence-of-rational-with-given-hilbert-symbols',
            'title_en': 'Existence of rational numbers with prescribed Hilbert symbols',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'hilbert-symbol',
            'difficulty': 'advanced',
            'tags': ['hilbert-symbol', 'existence', 'approximation', 'chinese-remainder-theorem', 'dirichlet-theorem'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'III', 'section': '2.2', 'pages': '23-24',
                             'role_in_book': 'Theorem 4: existence of x in Q^* with given (a_i, x)_v'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $(a_i)_{i \in I}$ be a finite family of elements in $\mathbb{Q}^*$ and let $(\varepsilon_{i,v})_{i \in I, v \in V}$ be a family of numbers equal to $\pm 1$. In order that there exists $x \in \mathbb{Q}^*$ such that $(a_i, x)_v = \varepsilon_{i,v}$ for all $i \in I$ and all $v \in V$, it is necessary and sufficient that:
\begin{enumerate}
\item[(1)] Almost all the $\varepsilon_{i,v}$ are equal to $1$.
\item[(2)] For all $i \in I$ we have $\prod_{v \in V} \varepsilon_{i,v} = 1$.
\item[(3)] For all $v \in V$ there exists $x_v \in \mathbb{Q}_v^*$ such that $(a_i, x_v)_v = \varepsilon_{i,v}$ for all $i \in I$.
\end{enumerate}
""")


# ============================================================
# SECTION 6: s006 - Chapter IV, §1 (Quadratic Forms)
# ============================================================

def write_quadratic_form_definition():
    d = f"{BASE}/quadratic-form-definition"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'quadratic-form-definition',
            'title_en': 'Quadratic form and quadratic module',
            'title_zh': '',
            'type': 'definition',
            'domain': 'algebra',
            'subdomain': 'quadratic-forms',
            'difficulty': 'basic',
            'tags': ['quadratic-form', 'bilinear-form', 'scalar-product'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'IV', 'section': '1.1', 'pages': '27',
                             'role_in_book': 'Definition 1: quadratic form over a module'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $V$ be a module over a commutative ring $A$. A function $Q: V \rightarrow A$ is called a quadratic form on $V$ if:
\begin{enumerate}
\item[(1)] $Q(ax) = a^2 Q(x)$ for $a \in A$ and $x \in V$.
\item[(2)] The function $(x, y) \mapsto Q(x+y) - Q(x) - Q(y)$ is a bilinear form.
\end{enumerate}
Such a pair $(V, Q)$ is called a quadratic module. When $A = k$ is a field of characteristic $\neq 2$, the associated scalar product is defined by:
$$x \cdot y = \frac{1}{2}\{Q(x+y) - Q(x) - Q(y)\},$$
giving a bijective correspondence between quadratic forms and symmetric bilinear forms.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
A quadratic form is a homogeneous polynomial of degree 2 on a module. Over fields of characteristic not 2, quadratic forms are equivalent to symmetric bilinear forms via the polarization identity. The theory of quadratic forms over $\\mathbb{Q}_p$ and $\\mathbb{Q}$ leads to deep results like the Hasse-Minkowski theorem.
""")


def write_isotropic_vector():
    d = f"{BASE}/isotropic-vector"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'isotropic-vector',
            'title_en': 'Isotropic vector and isotropic subspace',
            'title_zh': '',
            'type': 'definition',
            'domain': 'algebra',
            'subdomain': 'quadratic-forms',
            'difficulty': 'basic',
            'tags': ['quadratic-form', 'isotropic', 'hyperbolic'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'IV', 'section': '1.3', 'pages': '28',
                             'role_in_book': 'Definition 3: isotropic element and subspace'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""An element $x$ of a quadratic module $(V, Q)$ is called isotropic if $Q(x) = 0$. A subspace $U$ of $V$ is called isotropic if all its elements are isotropic, i.e. $U \subset U^0$ or equivalently $Q|_U = 0$.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
Isotropic vectors (nonzero vectors $x$ with $Q(x) = 0$) play a fundamental role in the classification of quadratic forms. A quadratic form representing zero nontrivially is called isotropic; otherwise it is anisotropic. The local-global principle for isotropy is the content of the Hasse-Minkowski theorem.
""")


def write_hyperbolic_plane():
    d = f"{BASE}/hyperbolic-plane"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'hyperbolic-plane',
            'title_en': 'Hyperbolic plane',
            'title_zh': '',
            'type': 'definition',
            'domain': 'algebra',
            'subdomain': 'quadratic-forms',
            'difficulty': 'basic',
            'tags': ['quadratic-form', 'hyperbolic-plane', 'isotropic'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'IV', 'section': '1.3', 'pages': '28',
                             'role_in_book': 'Definition 4: hyperbolic plane'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""A quadratic module having a basis formed of two isotropic elements $x, y$ such that $x \cdot y \neq 0$ is called a hyperbolic plane.

After normalizing so that $x \cdot y = 1$, the matrix of the quadratic form with respect to $\{x, y\}$ is $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$; its discriminant is $-1$ and it is nondegenerate.
""")


def write_orthogonal_basis_exists():
    d = f"{BASE}/orthogonal-basis-exists"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'orthogonal-basis-exists',
            'title_en': 'Existence of orthogonal basis for a quadratic module',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'algebra',
            'subdomain': 'quadratic-forms',
            'difficulty': 'basic',
            'tags': ['quadratic-form', 'orthogonal-basis', 'diagonalization'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'IV', 'section': '1.3', 'pages': '29',
                             'role_in_book': 'Theorem 1: every quadratic module has an orthogonal basis'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Every quadratic module $(V, Q)$ over a field of characteristic $\neq 2$ has an orthogonal basis. That is, there exists a basis $(e_1, \ldots, e_n)$ of $V$ such that $e_i \cdot e_j = 0$ for $i \neq j$, and
$$Q(x) = a_1 x_1^2 + \cdots + a_n x_n^2$$
where $x = \sum x_i e_i$ and $a_i = Q(e_i)$.
""")


def write_contiguous_bases():
    d = f"{BASE}/contiguous-bases-definition"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'contiguous-bases-definition',
            'title_en': 'Contiguous orthogonal bases',
            'title_zh': '',
            'type': 'definition',
            'domain': 'algebra',
            'subdomain': 'quadratic-forms',
            'difficulty': 'basic',
            'tags': ['quadratic-form', 'orthogonal-basis', 'contiguous'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'IV', 'section': '1.3', 'pages': '29',
                             'role_in_book': 'Definition 6: contiguous orthogonal bases'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Two orthogonal bases $e = (e_1, \ldots, e_n)$ and $e' = (e'_1, \ldots, e'_n)$ of a quadratic module $V$ are called contiguous if they have an element in common (i.e., there exist $i$ and $j$ such that $e_i = e'_j$).
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
The notion of contiguous orthogonal bases is used in the proof of Witt's theorem. The key technical result is that in a nondegenerate quadratic module of dimension at least 3, any two orthogonal bases can be connected by a finite chain of contiguous bases.
""")


def write_witt_theorem():
    d = f"{BASE}/witt-theorem"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'witt-theorem',
            'title_en': "Witt's extension theorem",
            'title_zh': '',
            'type': 'theorem',
            'domain': 'algebra',
            'subdomain': 'quadratic-forms',
            'difficulty': 'intermediate',
            'tags': ['quadratic-form', 'witt-theorem', 'extension', 'isometry'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'IV', 'section': '1.4', 'pages': '30',
                             'role_in_book': "Theorem 2: Witt's theorem — extension of metric isomorphisms"}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $(V, Q)$ and $(V', Q')$ be two nondegenerate quadratic modules over a field $k$ of characteristic $\neq 2$. Any metric isomorphism of a subvector space $U$ of $V$ onto a subvector space $U'$ of $V'$ can be extended to a metric isomorphism of $V$ onto $V'$.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
Witt's extension theorem is the foundational result in the algebraic theory of quadratic forms. It states that any isometry between subspaces can be extended to an isometry of the whole space, analogous to the fact that any orthogonal transformation of a subspace of a Euclidean space extends to the whole space. It underlies Witt cancellation and the definition of the Witt ring.
""")


def write_witt_cancellation():
    d = f"{BASE}/witt-cancellation"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'witt-cancellation',
            'title_en': 'Witt cancellation theorem',
            'title_zh': '',
            'type': 'corollary',
            'domain': 'algebra',
            'subdomain': 'quadratic-forms',
            'difficulty': 'intermediate',
            'tags': ['quadratic-form', 'witt-cancellation', 'isometry'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'IV', 'section': '1.4', 'pages': '31',
                             'role_in_book': 'Corollary: Witt cancellation theorem'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""If two nondegenerate quadratic modules are such that their orthogonal direct sums with a third nondegenerate quadratic module are isomorphic, then the first two are isomorphic. In symbols:
$$Q_1 \oplus Q_3 \cong Q_2 \oplus Q_3 \implies Q_1 \cong Q_2.$$
""")


# ============================================================
# SECTION 7: s007 - Chapter IV, §2 (Quadratic forms over Q_p)
# ============================================================

def write_classification_quadratic_forms_qp():
    d = f"{BASE}/classification-of-quadratic-forms-over-qp"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'classification-of-quadratic-forms-over-qp',
            'title_en': 'Classification of quadratic forms over Q_p',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'quadratic-forms',
            'difficulty': 'intermediate',
            'tags': ['quadratic-form', 'p-adic', 'classification', 'hasse-invariant'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'IV', 'section': '2', 'pages': '33-36',
                             'role_in_book': 'Classification theorem for quadratic forms over Q_p'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Two quadratic forms over $\mathbb{Q}_p$ are isomorphic if and only if they have the same dimension, the same discriminant (in $\mathbb{Q}_p^*/\mathbb{Q}_p^{*2}$), and the same Hasse invariant $\varepsilon_p \in \{\pm 1\}$.

The Hasse invariant of a quadratic form $Q = a_1 X_1^2 + \cdots + a_n X_n^2$ is defined by:
$$\varepsilon_p(Q) = \prod_{i < j} (a_i, a_j)_p$$
where $(a_i, a_j)_p$ denotes the Hilbert symbol in $\mathbb{Q}_p$.
""")


def write_hasse_invariant_is_invariant():
    d = f"{BASE}/hasse-invariant-is-invariant"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'hasse-invariant-is-invariant',
            'title_en': 'The Hasse invariant is well-defined',
            'title_zh': '',
            'type': 'proposition',
            'domain': 'number-theory',
            'subdomain': 'quadratic-forms',
            'difficulty': 'intermediate',
            'tags': ['quadratic-form', 'hasse-invariant', 'invariant'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'IV', 'section': '2', 'pages': '34',
                             'role_in_book': 'Proposition: Hasse invariant does not depend on diagonalization'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""The Hasse invariant $\varepsilon_p(Q)$ of a quadratic form $Q$ over $\mathbb{Q}_p$ is independent of the choice of orthogonal basis (diagonalization). It is a genuine invariant of the isomorphism class of $Q$.
""")


# ============================================================
# SECTION 8: s008 - Chapter IV, §3 (Quadratic forms over Q)
# ============================================================

def write_hasse_minkowski():
    d = f"{BASE}/hasse-minkowski-theorem"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'hasse-minkowski-theorem',
            'title_en': 'Hasse-Minkowski theorem (local-global principle)',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'quadratic-forms',
            'difficulty': 'advanced',
            'tags': ['quadratic-form', 'hasse-minkowski', 'local-global', 'hasse-principle'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'IV', 'section': '3', 'pages': '38-41',
                             'role_in_book': 'Theorem 1 (Hasse-Minkowski): local-global principle for quadratic forms over Q'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""A quadratic form over $\mathbb{Q}$ represents zero nontrivially if and only if it represents zero nontrivially over $\mathbb{R}$ and over all $\mathbb{Q}_p$ (for all primes $p$).

Equivalently: two quadratic forms over $\mathbb{Q}$ are isomorphic if and only if they are isomorphic over $\mathbb{R}$ and over all $\mathbb{Q}_p$.
""")


def write_classification_quadratic_forms_q():
    d = f"{BASE}/classification-of-quadratic-forms-over-q"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'classification-of-quadratic-forms-over-q',
            'title_en': 'Classification of quadratic forms over Q',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'quadratic-forms',
            'difficulty': 'advanced',
            'tags': ['quadratic-form', 'classification', 'rational', 'hasse-minkowski'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'IV', 'section': '3', 'pages': '41-44',
                             'role_in_book': 'Classification of quadratic forms over Q by invariants'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""A quadratic form over $\mathbb{Q}$ is determined up to isomorphism by:
\begin{itemize}
\item Its dimension $n$,
\item Its discriminant $d \in \mathbb{Q}^*/\mathbb{Q}^{*2}$,
\item Its signature $(r, s)$ over $\mathbb{R}$,
\item Its Hasse invariants $\varepsilon_p \in \{\pm 1\}$ for all primes $p$.
\end{itemize}
These invariants satisfy the product formula: $\prod_{v \in V} \varepsilon_v = 1$ (with $\varepsilon_\infty$ determined by the signature).
""")


# ============================================================
# SECTION 9: s009 - Chapter V, §1 (Integral Quadratic Forms)
# ============================================================

def write_integral_quadratic_form_category():
    d = f"{BASE}/integral-quadratic-form-category"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'integral-quadratic-form-category',
            'title_en': 'Category of integral quadratic forms',
            'title_zh': '',
            'type': 'definition',
            'domain': 'number-theory',
            'subdomain': 'quadratic-forms',
            'difficulty': 'advanced',
            'tags': ['quadratic-form', 'integral', 'lattice', 'category'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'V', 'section': '1', 'pages': '45',
                             'role_in_book': 'Definition of the category S_n of integral quadratic forms'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""An integral quadratic form is a pair $(L, Q)$ where $L$ is a free $\mathbb{Z}$-module of finite rank and $Q: L \to \mathbb{Z}$ is a quadratic form. The category $\mathcal{S}_n$ has as objects integral quadratic forms of rank $n$ that are positive definite, with morphisms being metric morphisms (isometries).
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
Integral quadratic forms (quadratic forms over $\\mathbb{Z}$) are the arithmetic analogue of quadratic forms over fields. They correspond to lattices with an integral quadratic structure. The classification of definite integral forms is a finite problem, leading to the theory of genera and the Minkowski-Siegel mass formula.
""")


def write_invariants_integral_quadratic():
    d = f"{BASE}/invariants-of-integral-quadratic-module"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'invariants-of-integral-quadratic-module',
            'title_en': 'Invariants of integral quadratic modules',
            'title_zh': '',
            'type': 'definition',
            'domain': 'number-theory',
            'subdomain': 'quadratic-forms',
            'difficulty': 'advanced',
            'tags': ['quadratic-form', 'integral', 'genus', 'invariants'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'V', 'section': '1', 'pages': '46',
                             'role_in_book': 'Definition of genus invariants for integral quadratic forms'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Two integral quadratic forms belong to the same genus if they are isomorphic over $\mathbb{R}$ and over $\mathbb{Z}_p$ for all primes $p$. The invariants of a genus are:
\begin{itemize}
\item The rank $n$,
\item The discriminant,
\item The signature (always $(n, 0)$ for positive definite forms),
\item For each prime $p$, the Hasse invariant over $\mathbb{Q}_p$.
\end{itemize}
""")


# ============================================================
# SECTION 10: s010 - Chapter VI, §1 (Characters of Finite Abelian Groups)
# ============================================================

def write_character_of_finite_abelian_group():
    d = f"{BASE}/character-of-finite-abelian-group"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'character-of-finite-abelian-group',
            'title_en': 'Character of a finite abelian group',
            'title_zh': '',
            'type': 'definition',
            'domain': 'number-theory',
            'subdomain': 'dirichlet-characters',
            'difficulty': 'basic',
            'tags': ['character', 'finite-abelian-group', 'dirichlet'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'VI', 'section': '1', 'pages': '55',
                             'role_in_book': 'Definition of character of a finite abelian group G'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $G$ be a finite abelian group. A character of $G$ is a homomorphism $\chi: G \to \mathbb{C}^*$. The set $\widehat{G}$ of characters of $G$ forms a group under pointwise multiplication, called the dual group of $G$.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
Characters of finite abelian groups generalize the notion of roots of unity and are the fundamental building blocks of Dirichlet characters. The dual group $\\widehat{G}$ is (non-canonically) isomorphic to $G$ itself, and character orthogonality relations form the basis for Fourier analysis on finite abelian groups.
""")


def write_dual_group():
    d = f"{BASE}/dual-of-abelian-group"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'dual-of-abelian-group',
            'title_en': 'Dual group of a finite abelian group',
            'title_zh': '',
            'type': 'proposition',
            'domain': 'number-theory',
            'subdomain': 'dirichlet-characters',
            'difficulty': 'basic',
            'tags': ['character', 'dual-group', 'finite-abelian-group'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'VI', 'section': '1', 'pages': '55-56',
                             'role_in_book': 'Theorem 1: structure of the dual group of a finite abelian group'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $G$ be a finite abelian group. Then:
\begin{itemize}
\item[(i)] $\widehat{G}$ is isomorphic to $G$ (non-canonically).
\item[(ii)] The natural map $G \to \widehat{\widehat{G}}$ (the bidual) is a canonical isomorphism.
\item[(iii)] The order of $\widehat{G}$ equals the order of $G$.
\end{itemize}
""")


def write_orthogonality_relations():
    d = f"{BASE}/orthogonality-relations"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'orthogonality-relations',
            'title_en': 'Orthogonality relations for characters',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'dirichlet-characters',
            'difficulty': 'basic',
            'tags': ['character', 'orthogonality', 'fourier-analysis'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'VI', 'section': '1', 'pages': '56',
                             'role_in_book': 'Theorem 2: orthogonality relations for characters of finite abelian groups'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $G$ be a finite abelian group of order $n$. For characters $\chi, \psi \in \widehat{G}$ and elements $g, h \in G$:
$$\sum_{g \in G} \chi(g) \overline{\psi(g)} = \begin{cases} n & \text{if } \chi = \psi, \\ 0 & \text{otherwise.} \end{cases}$$
$$\sum_{\chi \in \widehat{G}} \chi(g) \overline{\chi(h)} = \begin{cases} n & \text{if } g = h, \\ 0 & \text{otherwise.} \end{cases}$$
""")


def write_modular_character():
    d = f"{BASE}/modular-character"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'modular-character',
            'title_en': 'Dirichlet character (modular character)',
            'title_zh': '',
            'type': 'definition',
            'domain': 'number-theory',
            'subdomain': 'dirichlet-characters',
            'difficulty': 'basic',
            'tags': ['dirichlet-character', 'modular-character', 'multiplicative'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'VI', 'section': '1', 'pages': '57',
                             'role_in_book': 'Definition of Dirichlet character modulo m'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Let $m \geq 1$ be an integer. A Dirichlet character modulo $m$ (or modular character) is a function $\chi: \mathbb{Z} \to \mathbb{C}$ such that:
\begin{enumerate}
\item $\chi(a)$ depends only on $a \pmod{m}$.
\item $\chi(ab) = \chi(a)\chi(b)$ for all $a, b \in \mathbb{Z}$.
\item $\chi(a) = 0$ if and only if $\gcd(a, m) \neq 1$.
\end{enumerate}
Equivalently, $\chi$ is the composition of the natural projection $(\mathbb{Z}/m\mathbb{Z})^* \to \widehat{(\mathbb{Z}/m\mathbb{Z})^*}$ extended by $0$ on non-invertible classes.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
A Dirichlet character is a completely multiplicative function on the integers that is periodic modulo $m$ and vanishes on integers not coprime to $m$. Dirichlet characters are the essential analytic tool for studying the distribution of primes in arithmetic progressions, via Dirichlet $L$-functions.
""")


def write_dirichlet_theorem():
    d = f"{BASE}/dirichlet-theorem"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'dirichlet-theorem',
            'title_en': "Dirichlet's theorem on arithmetic progressions",
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'dirichlet-characters',
            'difficulty': 'advanced',
            'tags': ['dirichlet-theorem', 'arithmetic-progression', 'primes', 'l-function'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'VI', 'section': '4', 'pages': '62-66',
                             'role_in_book': 'Theorem 4 (Dirichlet): infinitude of primes in arithmetic progressions'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""If $a$ and $m$ are relatively prime integers with $m \geq 1$, there exist infinitely many primes $p$ such that $p \equiv a \pmod{m}$.

Moreover, the Dirichlet density (and natural density) of the set of such primes is $1/\phi(m)$, where $\phi$ is Euler's totient function.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
Dirichlet's theorem is a landmark result in analytic number theory, proving that each reduced residue class modulo $m$ contains infinitely many primes. The proof introduced Dirichlet $L$-functions and established the non-vanishing of $L(1, \\chi)$ for nontrivial characters, a technique that became a cornerstone of analytic number theory.
""")


# ============================================================
# SECTION 11: s011 - Chapter VII, §1 (The Modular Group)
# ============================================================

def write_modular_group():
    d = f"{BASE}/modular-group"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'modular-group',
            'title_en': 'The modular group',
            'title_zh': '',
            'type': 'definition',
            'domain': 'number-theory',
            'subdomain': 'modular-forms',
            'difficulty': 'intermediate',
            'tags': ['modular-group', 'SL2Z', 'modular-forms'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'VII', 'section': '1', 'pages': '77',
                             'role_in_book': 'Definition: the modular group Gamma = SL_2(Z)'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""The modular group $\Gamma = \mathrm{SL}_2(\mathbb{Z})$ is the group of $2 \times 2$ integer matrices with determinant $1$:
$$\Gamma = \left\{ \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in M_2(\mathbb{Z}) : ad - bc = 1 \right\}.$$
It acts on the upper half-plane $\mathcal{H} = \{z \in \mathbb{C} : \Im(z) > 0\}$ by fractional linear transformations:
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \cdot z = \frac{az + b}{cz + d}.$$
""")


def write_modular_group_generators():
    d = f"{BASE}/modular-group-generators"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'modular-group-generators',
            'title_en': 'Generators of the modular group',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'modular-forms',
            'difficulty': 'basic',
            'tags': ['modular-group', 'generators', 'SL2Z'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'VII', 'section': '1.1', 'pages': '78',
                             'role_in_book': 'Theorem 1: generators S and T of the modular group'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""The modular group $\Gamma = \mathrm{SL}_2(\mathbb{Z})$ is generated by the two matrices:
$$S = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \quad T = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.$$
Their actions on the upper half-plane are: $S(z) = -1/z$ and $T(z) = z + 1$. The relations in $\Gamma$ are $S^2 = (ST)^3 = -I$.
""")


def write_fundamental_domain():
    d = f"{BASE}/fundamental-domain-of-modular-group"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'fundamental-domain-of-modular-group',
            'title_en': 'Fundamental domain of the modular group',
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'modular-forms',
            'difficulty': 'intermediate',
            'tags': ['modular-group', 'fundamental-domain', 'upper-half-plane'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'VII', 'section': '1.2', 'pages': '79',
                             'role_in_book': 'Theorem 2: fundamental domain D for the modular group'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""A fundamental domain for the action of the modular group $\Gamma$ on the upper half-plane $\mathcal{H}$ is:
$$D = \left\{ z \in \mathcal{H} : |z| \geq 1, \; |\Re(z)| \leq \frac{1}{2} \right\}.$$
Every point of $\mathcal{H}$ is $\Gamma$-equivalent to a unique point of $D$, except for points on the boundary where identifications occur via $S$ and $T$.
""")


def write_modular_form_definition():
    d = f"{BASE}/modular-form"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'modular-form',
            'title_en': 'Modular form',
            'title_zh': '',
            'type': 'definition',
            'domain': 'number-theory',
            'subdomain': 'modular-forms',
            'difficulty': 'intermediate',
            'tags': ['modular-form', 'modular-group', 'holomorphic', 'weight'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'VII', 'section': '2', 'pages': '82',
                             'role_in_book': 'Definition of modular form of weight 2k'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""A function $f: \mathcal{H} \to \mathbb{C}$ is called a modular form of weight $2k$ (with $k \geq 1$ an integer) if:
\begin{enumerate}
\item $f$ is holomorphic on $\mathcal{H}$.
\item $f\left(\frac{az + b}{cz + d}\right) = (cz + d)^{2k} f(z)$ for all $\begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \Gamma$.
\item $f$ is "holomorphic at infinity", i.e., $f(z)$ admits a Fourier expansion $f(z) = \sum_{n=0}^{\infty} a_n q^n$ where $q = e^{2\pi i z}$.
\end{enumerate}
If $a_0 = 0$, $f$ is called a cusp form.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
Modular forms are holomorphic functions on the upper half-plane that transform in a specific way under the action of the modular group $\\mathrm{SL}_2(\\mathbb{Z})$. They are central objects in number theory, connecting analysis, algebra, and arithmetic geometry. The Fourier coefficients of modular forms often carry deep arithmetic information.
""")


# ============================================================
# SECTION 12: s012 - Chapter VII, §5 (Hecke Operators)
# ============================================================

def write_hecke_operator():
    d = f"{BASE}/hecke-operator"
    os.makedirs(d, exist_ok=True)

    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'hecke-operator',
            'title_en': 'Hecke operator',
            'title_zh': '',
            'type': 'definition',
            'domain': 'number-theory',
            'subdomain': 'modular-forms',
            'difficulty': 'advanced',
            'tags': ['hecke-operator', 'modular-form', 'hecke-algebra'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'VII', 'section': '5.1', 'pages': '99',
                             'role_in_book': 'Definition of Hecke operator T(n) on modular forms'}],
            'content_hash': '',
            'extraction_date': '2026-06-27',
            'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""For an integer $n \geq 1$ and a modular form $f(z) = \sum_{m=0}^{\infty} a_m q^m$ of weight $2k$, the Hecke operator $T(n)$ is defined by:
$$T(n)f(z) = n^{2k-1} \sum_{\substack{a \geq 1,\, ad = n \\ 0 \leq b < d}} d^{-2k} f\left(\frac{az + b}{d}\right).$$

Equivalently, the $m$-th Fourier coefficient of $T(n)f$ is:
$$a_m(T(n)f) = \sum_{d \mid \gcd(m,n)} d^{2k-1} a_{mn/d^2}(f).$$
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
Hecke operators $T(n)$ are a commuting family of linear operators acting on spaces of modular forms. Their simultaneous eigenfunctions (Hecke eigenforms) have Fourier coefficients that satisfy remarkable multiplicative properties. Hecke operators are fundamental to the theory of modular forms and their deep connections to arithmetic geometry and the Langlands program.
""")


# ============================================================
# More specific/duplicate concepts to fill
# ============================================================

def write_specific_missing():
    """Fill specific missing concepts that are unique (not just named differently)"""

    # bernoulli-numbers
    d = f"{BASE}/bernoulli-numbers"
    os.makedirs(d, exist_ok=True)
    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'bernoulli-numbers',
            'title_en': 'Bernoulli numbers',
            'title_zh': '',
            'type': 'definition',
            'domain': 'number-theory',
            'subdomain': 'modular-forms',
            'difficulty': 'intermediate',
            'tags': ['bernoulli-numbers', 'eisenstein-series', 'zeta-function'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'VII', 'section': '4.1', 'pages': '91',
                             'role_in_book': 'Definition of Bernoulli numbers B_k for Eisenstein series'}],
            'content_hash': '', 'extraction_date': '2026-06-27', 'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""The Bernoulli numbers $B_k$ ($k \geq 0$) are defined by the generating function:
$$\frac{x}{e^x - 1} = \sum_{k=0}^{\infty} B_k \frac{x^k}{k!}.$$
The first few are: $B_0 = 1$, $B_1 = -1/2$, $B_2 = 1/6$, $B_3 = 0$, $B_4 = -1/30$. For odd $k \geq 3$, $B_k = 0$.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
Bernoulli numbers are rational numbers that appear in the Fourier expansion of Eisenstein series, in the values of the Riemann zeta function at even integers, and in many other contexts in number theory. They are intimately connected to modular forms via the normalized Eisenstein series.
""")

    # j-invariant
    d = f"{BASE}/j-invariant"
    os.makedirs(d, exist_ok=True)
    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'j-invariant',
            'title_en': 'Modular j-invariant',
            'title_zh': '',
            'type': 'definition',
            'domain': 'number-theory',
            'subdomain': 'modular-forms',
            'difficulty': 'intermediate',
            'tags': ['j-invariant', 'modular-function', 'elliptic-curve'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'VII', 'section': '3.3', 'pages': '89',
                             'role_in_book': 'Definition of the modular invariant j(z)'}],
            'content_hash': '', 'extraction_date': '2026-06-27', 'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""The modular $j$-invariant is the unique modular function of weight $0$ (i.e., invariant under $\mathrm{SL}_2(\mathbb{Z})$) that is holomorphic on $\mathcal{H}$, has a simple pole at $\infty$, and satisfies $j(e^{2\pi i/3}) = 0$, $j(i) = 1728$. It can be expressed as:
$$j(z) = \frac{1728 \, g_2(z)^3}{g_2(z)^3 - 27 g_3(z)^2} = \frac{1728 \, g_2(z)^3}{\Delta(z)}$$
where $g_2, g_3$ are Eisenstein series and $\Delta$ is the discriminant modular form.
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
The $j$-invariant is a fundamental modular function that classifies elliptic curves over $\\mathbb{C}$ up to isomorphism. It generates the field of modular functions and plays a central role in the theory of complex multiplication, moonshine, and the arithmetic of elliptic curves.
""")

    # lagrange-four-squares
    d = f"{BASE}/lagrange-four-squares"
    os.makedirs(d, exist_ok=True)
    with open(f"{d}/concept.yaml", 'w') as f:
        yaml.dump({
            'id': 'lagrange-four-squares',
            'title_en': "Lagrange's four-square theorem",
            'title_zh': '',
            'type': 'theorem',
            'domain': 'number-theory',
            'subdomain': 'quadratic-forms',
            'difficulty': 'intermediate',
            'tags': ['lagrange', 'four-squares', 'quadratic-form', 'sum-of-squares'],
            'depends_on': {'required': [], 'recommended': [], 'suggested': []},
            'source_books': [{'book_id': 'gtm007', 'author': 'J.-P. Serre', 'title': 'A Course in Arithmetic',
                             'chapter': 'IV', 'section': 'Appendix', 'pages': '54-55',
                             'role_in_book': 'Theorem (Lagrange): every positive integer is a sum of four squares'}],
            'content_hash': '', 'extraction_date': '2026-06-27', 'extraction_agent': 'v8-full-extract'
        }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(f"{d}/theorem.tex", 'w') as f:
        f.write(r"""Every positive integer is the sum of four squares of integers:
$$n = x_1^2 + x_2^2 + x_3^2 + x_4^2, \quad x_i \in \mathbb{Z}.$$
""")

    with open(f"{d}/introduce.en.md", 'w') as f:
        f.write("""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
Lagrange's four-square theorem states that the quadratic form $x_1^2 + x_2^2 + x_3^2 + x_4^2$ represents all positive integers over $\\mathbb{Z}$. This is a special case of the Hasse-Minkowski theorem applied to the quadratic form $x_1^2 + x_2^2 + x_3^2 + x_4^2 - n z^2$, and it generalizes to the theory of representations by quadratic forms.
""")


# ============================================================
# Main execution
# ============================================================

if __name__ == '__main__':
    print("Filling s001 concepts...")
    write_frobenius_endomorphism()
    write_classification_finite_fields()
    write_cyclic_multiplicative_group()
    write_euler_phi_sum()
    write_power_sums_lemma()

    print("Filling s002 concepts...")
    write_squares_in_finite_field()
    write_legendre_symbol()
    write_legendre_formulas()
    write_quadratic_reciprocity_law()
    write_gauss_lemma()

    print("Filling s003 concepts...")
    write_ring_zp()
    write_field_qp()
    write_exact_sequence_zp()
    write_invertible_elements_zp()
    write_qp_locally_compact()
    write_projective_limit_nonempty()
    write_common_zero_equivalent_conditions()
    write_hensels_lemma()
    write_simple_zero_lifts()
    write_structure_of_qp_star()
    write_squares_in_qp()
    write_squares_in_q2()
    write_p_adic_unit_group_structure()

    print("Filling s004 concepts...")
    write_hilbert_symbol()
    write_hilbert_symbol_norm()
    write_hilbert_symbol_properties()
    write_computation_of_hilbert_symbol()

    print("Filling s005 concepts...")
    write_hilbert_product_formula()
    write_existence_rational_hilbert_symbols()

    print("Filling s006 concepts...")
    write_quadratic_form_definition()
    write_isotropic_vector()
    write_hyperbolic_plane()
    write_orthogonal_basis_exists()
    write_contiguous_bases()
    write_witt_theorem()
    write_witt_cancellation()

    print("Filling s007 concepts...")
    write_classification_quadratic_forms_qp()
    write_hasse_invariant_is_invariant()

    print("Filling s008 concepts...")
    write_hasse_minkowski()
    write_classification_quadratic_forms_q()

    print("Filling s009 concepts...")
    write_integral_quadratic_form_category()
    write_invariants_integral_quadratic()

    print("Filling s010 concepts...")
    write_character_of_finite_abelian_group()
    write_dual_group()
    write_orthogonality_relations()
    write_modular_character()
    write_dirichlet_theorem()

    print("Filling s011 concepts...")
    write_modular_group()
    write_modular_group_generators()
    write_fundamental_domain()
    write_modular_form_definition()

    print("Filling s012 concepts...")
    write_hecke_operator()

    print("Filling special concepts...")
    write_specific_missing()

    # Write .done marker
    with open(f"{BASE}/.done", 'w') as f:
        f.write("DONE\n")

    print("ALL DONE! .done file written.")
