#!/usr/bin/env python3
"""Extract ALL theorems, definitions, lemmas, propositions, corollaries from GTM099."""
import os, re, yaml, hashlib, json

BOOK_FILE = '/home/a123/文档/mathpkg/pipeline_output/stitched/(GTM099)Finite Reflection Groups/_full.md'
STAGING = '/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/_GTM099_Finite_Reflection_Groups'

with open(BOOK_FILE, 'r') as f:
    content = f.read()

# Remove excessive <|endoftext|> markers
content = re.sub(r'<\|endoftext\|>+', '\n\n', content)

lines = content.split('\n')

# Find all concept headers
concept_pattern = re.compile(
    r'^(\*\*)?(Theorem|Proposition|Lemma|Corollary|Definition)\s+(\d+\.\d+\.\d+)(.*?)(\*\*)?\s*$'
)

concepts = []
for i, line in enumerate(lines):
    line = line.strip()
    m = concept_pattern.match(line)
    if m:
        concept_type = m.group(2)
        number = m.group(3)
        extra = m.group(4).strip()
        concepts.append({
            'line': i,
            'type': concept_type,
            'number': number,
            'extra': extra,
            'full_header': line,
        })

print(f"Found {len(concepts)} concepts")

# Now extract the statement and proof for each concept
# A concept's text runs from its header line until the next concept header or end of section
# We need to be careful about the boundaries

def extract_text(start_line, end_line_exclusive):
    """Extract text between start_line and end_line_exclusive."""
    text_lines = []
    for i in range(start_line, end_line_exclusive):
        text_lines.append(lines[i])
    return '\n'.join(text_lines)

def detect_next_boundary(start_line):
    """Find the next concept header or major section break after start_line."""
    for i in range(start_line + 1, len(lines)):
        ls = lines[i].strip()
        m = concept_pattern.match(ls)
        if m:
            return i
        # Also stop at exercise sections and chapter breaks
        if re.match(r'^(Exercises|CHAPTER\s+\d|chapter\s+\d|REFERENCES|INDEX|APPENDIX|Postlude)', ls, re.IGNORECASE):
            return i
        if re.match(r'^\d+\.\d+\s', ls) and 'Exercise' not in ls:
            # Check if this looks like an exercise header
            if re.match(r'^\d+\.\d+\s+[A-Z]', ls):
                return i
    return len(lines)

def detect_proof_boundary(concept_start, next_concept_start):
    """Find where the proof starts and ends."""
    proof_start = None
    proof_end = next_concept_start
    for i in range(concept_start + 1, next_concept_start):
        ls = lines[i].strip()
        if re.match(r'^\*?\*?Proof\*?\*?\s*$', ls, re.IGNORECASE):
            proof_start = i
            break
    return proof_start, proof_end

# Define concept metadata
concept_meta = {}

# Chapter 1 - Preliminaries
concept_meta['1.2.1'] = {
    'title_en': 'Orbit-Stabilizer Theorem for Permutation Groups',
    'title_zh': '置换群的轨道-稳定子定理',
    'slug': 'orbit_stabilizer_theorem',
    'domain': 'group_theory',
    'subdomain': 'group_actions',
    'chapter': '1',
    'section': '1.2',
}

# Chapter 2 - Finite Groups in Two and Three Dimensions
concept_meta['2.3.1'] = {
    'title_en': "Euler's Rotation Theorem",
    'title_zh': '欧拉旋转定理',
    'slug': 'eulers_rotation_theorem',
    'domain': 'geometry',
    'subdomain': 'orthogonal_transformations',
    'chapter': '2',
    'section': '2.3',
}
concept_meta['2.3.2'] = {
    'title_en': 'Classification of Orthogonal Transformations with Determinant -1',
    'title_zh': '行列式为-1的正交变换分类',
    'slug': 'orthogonal_transformation_det_minus_one',
    'domain': 'geometry',
    'subdomain': 'orthogonal_transformations',
    'chapter': '2',
    'section': '2.3',
}
concept_meta['2.4.1'] = {
    'title_en': 'Pole Permutation by Rotation Groups',
    'title_zh': '旋转群对极点的置换作用',
    'slug': 'pole_permutation_by_rotation_groups',
    'domain': 'group_theory',
    'subdomain': 'finite_rotation_groups',
    'chapter': '2',
    'section': '2.4',
}
concept_meta['2.5.1'] = {
    'title_en': 'Rotation Subgroup Index',
    'title_zh': '旋转子群的指数',
    'slug': 'rotation_subgroup_index',
    'domain': 'group_theory',
    'subdomain': 'orthogonal_groups',
    'chapter': '2',
    'section': '2.5',
}
concept_meta['2.5.2'] = {
    'title_en': 'Classification of Finite Subgroups of O(3)',
    'title_zh': '三维正交群有限子群的分类',
    'slug': 'classification_finite_subgroups_o3',
    'domain': 'group_theory',
    'subdomain': 'orthogonal_groups',
    'chapter': '2',
    'section': '2.5',
}

# Chapter 3 - Fundamental Regions
concept_meta['3.1.1'] = {
    'title_en': 'Vector Space Not a Finite Union of Proper Subspaces',
    'title_zh': '向量空间不是有限个真子空间的并',
    'slug': 'vector_space_not_finite_union_proper_subspaces',
    'domain': 'linear_algebra',
    'subdomain': 'vector_spaces',
    'chapter': '3',
    'section': '3.1',
}
concept_meta['3.1.2'] = {
    'title_en': 'Fricke-Klein Fundamental Region Construction',
    'title_zh': 'Fricke-Klein基本区域构造',
    'slug': 'fricke_klein_fundamental_region',
    'domain': 'geometry',
    'subdomain': 'fundamental_regions',
    'chapter': '3',
    'section': '3.1',
}

# Chapter 4 - Coxeter Groups
concept_meta['4.1.1'] = {
    'title_en': 'Conjugacy of Roots under Group Action',
    'title_zh': '群作用下根的共轭性',
    'slug': 'conjugacy_of_roots_under_group_action',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '4',
    'section': '4.1',
}
concept_meta['4.1.2'] = {
    'title_en': 'Effectiveness Criterion for Reflection Groups',
    'title_zh': '反射群有效性的判别准则',
    'slug': 'effectiveness_criterion_reflection_groups',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '4',
    'section': '4.1',
}
concept_meta['4.1.3'] = {
    'title_en': 'Finiteness from Finite Root System',
    'title_zh': '有限根系蕴含有限群',
    'slug': 'finiteness_from_finite_root_system',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '4',
    'section': '4.1',
}
concept_meta['4.1.4'] = {
    'title_en': 'Sign Property of Simple Root Differences',
    'title_zh': '单根差的符号性质',
    'slug': 'sign_property_simple_root_differences',
    'domain': 'group_theory',
    'subdomain': 'root_systems',
    'chapter': '4',
    'section': '4.1',
}
concept_meta['4.1.6'] = {
    'title_en': 'Linear Independence of Mutually Obtuse Vectors',
    'title_zh': '相互钝角向量的线性无关性',
    'slug': 'linear_independence_mutually_obtuse_vectors',
    'domain': 'linear_algebra',
    'subdomain': 'inner_product_spaces',
    'chapter': '4',
    'section': '4.1',
}
concept_meta['4.1.9'] = {
    'title_en': 'Fundamental Reflection Preserves Positive Roots Except Its Own',
    'title_zh': '基本反射保持除自身外的正根不变',
    'slug': 'fundamental_reflection_preserves_positive_roots',
    'domain': 'group_theory',
    'subdomain': 'root_systems',
    'chapter': '4',
    'section': '4.1',
}
concept_meta['4.1.10'] = {
    'title_en': 'Existence of Transformation Making Vector Positive',
    'title_zh': '使向量变为正根的变换存在性',
    'slug': 'existence_transformation_making_vector_positive',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '4',
    'section': '4.1',
}
concept_meta['4.1.11'] = {
    'title_en': 'Positive Root Mapped to Simple Root by Group Element',
    'title_zh': '正根可被群元素映为单根',
    'slug': 'positive_root_mapped_to_simple_root',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '4',
    'section': '4.1',
}
concept_meta['4.2.1'] = {
    'title_en': 'Only Identity Fixes Simple Root Basis',
    'title_zh': '仅有恒等变换固定单根基底',
    'slug': 'only_identity_fixes_simple_root_basis',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '4',
    'section': '4.2',
}
concept_meta['4.2.2'] = {
    'title_en': 'Group Action on Positive Roots and Simple Bases',
    'title_zh': '群在正根和单基上的作用',
    'slug': 'group_action_on_positive_roots_and_simple_bases',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '4',
    'section': '4.2',
}
concept_meta['4.2.3'] = {
    'title_en': 'Fundamental Region for Coxeter Groups',
    'title_zh': 'Coxeter群的基本区域',
    'slug': 'fundamental_region_for_coxeter_groups',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '4',
    'section': '4.2',
}
concept_meta['4.2.4'] = {
    'title_en': 'Simplicial Cone is a Fundamental Region',
    'title_zh': '单纯锥是基本区域',
    'slug': 'simplicial_cone_is_fundamental_region',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '4',
    'section': '4.2',
}
concept_meta['4.2.5'] = {
    'title_en': 'Every Reflection is Conjugate to a Fundamental Reflection',
    'title_zh': '每个反射共轭于一个基本反射',
    'slug': 'every_reflection_conjugate_to_fundamental',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '4',
    'section': '4.2',
}
concept_meta['4.2.6'] = {
    'title_en': 'Nonnegativity of Dual Basis Inner Products',
    'title_zh': '对偶基内积的非负性',
    'slug': 'nonnegativity_of_dual_basis_inner_products',
    'domain': 'linear_algebra',
    'subdomain': 'inner_product_spaces',
    'chapter': '4',
    'section': '4.2',
}

# Chapter 5 - Classification
concept_meta['5.1.1'] = {
    'title_en': 'Angle Between Simple Roots Determines Product Order',
    'title_zh': '单根夹角决定乘积阶',
    'slug': 'angle_simple_roots_determines_product_order',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '5',
    'section': '5.1',
}
concept_meta['5.1.2'] = {
    'title_en': 'Coxeter Graph Determines Coxeter Group',
    'title_zh': 'Coxeter图决定Coxeter群',
    'slug': 'coxeter_graph_determines_coxeter_group',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '5',
    'section': '5.1',
}
concept_meta['5.1.3'] = {
    'title_en': 'Coxeter Graph is Positive Definite',
    'title_zh': 'Coxeter图是正定的',
    'slug': 'coxeter_graph_is_positive_definite',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '5',
    'section': '5.1',
}
concept_meta['5.1.4'] = {
    'title_en': 'Connected Coxeter Graph Criterion for Irreducibility',
    'title_zh': '连通Coxeter图与不可约性等价',
    'slug': 'connected_coxeter_graph_irreducibility',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '5',
    'section': '5.1',
}
concept_meta['5.1.7'] = {
    'title_en': 'Classification of Connected Positive Definite Coxeter Graphs',
    'title_zh': '连通正定Coxeter图的分类',
    'slug': 'classification_connected_positive_definite_coxeter_graphs',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '5',
    'section': '5.1',
}
concept_meta['5.2.1'] = {
    'title_en': 'Crystallographic Restriction on Coxeter Graph Marks',
    'title_zh': '晶体学条件限制Coxeter图标号',
    'slug': 'crystallographic_restriction_coxeter_graph_marks',
    'domain': 'group_theory',
    'subdomain': 'crystallographic_groups',
    'chapter': '5',
    'section': '5.2',
}
concept_meta['5.3.1'] = {
    'title_en': 'Classification of Finite Reflection Groups',
    'title_zh': '有限反射群的分类',
    'slug': 'classification_finite_reflection_groups',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '5',
    'section': '5.3',
}
concept_meta['5.4.1'] = {
    'title_en': "Witt's Theorem on Stabilizer of Dual Basis Vector",
    'title_zh': 'Witt关于对偶基向量稳定子的定理',
    'slug': 'witt_theorem_stabilizer_dual_basis_vector',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '5',
    'section': '5.4',
}
concept_meta['5.4.2'] = {
    'title_en': 'Transitivity of Irreducible Coxeter Groups on Root Systems',
    'title_zh': '不可约Coxeter群在根系上的传递性',
    'slug': 'transitivity_irreducible_coxeter_groups_root_systems',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '5',
    'section': '5.4',
}

# Chapter 6 - Generators and Relations
concept_meta['6.1.2'] = {
    'title_en': 'Alternating Product of Fundamental Reflections on Roots',
    'title_zh': '基本反射交替乘积在根上的作用',
    'slug': 'alternating_product_fundamental_reflections_on_roots',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '6',
    'section': '6.1',
}
concept_meta['6.1.4'] = {
    'title_en': "Coxeter's Presentation Theorem",
    'title_zh': 'Coxeter表示定理',
    'slug': 'coxters_presentation_theorem',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '6',
    'section': '6.1',
}
concept_meta['6.1.5'] = {
    'title_en': 'Homomorphism from Abstract Group to Geometric Group',
    'title_zh': '从抽象群到几何群的同态',
    'slug': 'homomorphism_abstract_group_to_geometric_group',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '6',
    'section': '6.1',
}
concept_meta['6.1.6'] = {
    'title_en': 'Existence of Invariant Inner Product for Finite Linear Groups',
    'title_zh': '有限线性群的不变内积存在性',
    'slug': 'invariant_inner_product_finite_linear_groups',
    'domain': 'linear_algebra',
    'subdomain': 'inner_product_spaces',
    'chapter': '6',
    'section': '6.1',
}
concept_meta['6.1.9'] = {
    'title_en': 'Matrix Commutation Relation for Invariant Forms',
    'title_zh': '不变形式的矩阵交换关系',
    'slug': 'matrix_commutation_relation_invariant_forms',
    'domain': 'linear_algebra',
    'subdomain': 'bilinear_forms',
    'chapter': '6',
    'section': '6.1',
}
concept_meta['6.1.11'] = {
    'title_en': "Coxeter's Theorem: Abstract Reflection Group is Coxeter Group",
    'title_zh': 'Coxeter定理：抽象反射群是Coxeter群',
    'slug': 'coxters_theorem_abstract_reflection_group',
    'domain': 'group_theory',
    'subdomain': 'coxeter_groups',
    'chapter': '6',
    'section': '6.1',
}

# Chapter 7 - Invariants
concept_meta['7.2.2'] = {
    'title_en': 'Linear Polynomial Divisor Property for Reflections',
    'title_zh': '反射的线性多项式整除性质',
    'slug': 'linear_polynomial_divisor_property_reflections',
    'domain': 'invariant_theory',
    'subdomain': 'polynomial_invariants',
    'chapter': '7',
    'section': '7.2',
}
concept_meta['7.3.1'] = {
    'title_en': 'Averaging Operator Projects onto Invariants',
    'title_zh': '平均算子投影到不变量',
    'slug': 'averaging_operator_projects_onto_invariants',
    'domain': 'invariant_theory',
    'subdomain': 'polynomial_invariants',
    'chapter': '7',
    'section': '7.3',
}
concept_meta['7.3.3'] = {
    'title_en': 'Polynomial Relation Among Invariants',
    'title_zh': '不变量间的多项式关系',
    'slug': 'polynomial_relation_among_invariants',
    'domain': 'invariant_theory',
    'subdomain': 'polynomial_invariants',
    'chapter': '7',
    'section': '7.3',
}
concept_meta['7.3.5'] = {
    'title_en': 'Shephard-Todd-Chevalley Theorem',
    'title_zh': 'Shephard-Todd-Chevalley定理',
    'slug': 'shephard_todd_chevalley_theorem',
    'domain': 'invariant_theory',
    'subdomain': 'polynomial_invariants',
    'chapter': '7',
    'section': '7.3',
}
concept_meta['7.4.1'] = {
    'title_en': 'Trace Generating Function for Polynomial Representations',
    'title_zh': '多项式表示的迹生成函数',
    'slug': 'trace_generating_function_polynomial_representations',
    'domain': 'invariant_theory',
    'subdomain': 'molien_series',
    'chapter': '7',
    'section': '7.4',
}
concept_meta['7.4.2'] = {
    'title_en': 'Dimension of Subspace via Trace of Projection',
    'title_zh': '投影的迹给出子空间维数',
    'slug': 'dimension_subspace_via_trace_of_projection',
    'domain': 'linear_algebra',
    'subdomain': 'projections',
    'chapter': '7',
    'section': '7.4',
}
concept_meta['7.4.3'] = {
    'title_en': 'Dimension of Invariant Subspace via Averaged Trace',
    'title_zh': '不变子空间维数的平均迹公式',
    'slug': 'dimension_invariant_subspace_averaged_trace',
    'domain': 'invariant_theory',
    'subdomain': 'molien_series',
    'chapter': '7',
    'section': '7.4',
}
concept_meta['7.4.5'] = {
    'title_en': "Molien Series as Product of Basic Generator Degrees",
    'title_zh': 'Molien级数表示为基本生成元度数的乘积',
    'slug': 'molien_series_product_basic_generator_degrees',
    'domain': 'invariant_theory',
    'subdomain': 'molien_series',
    'chapter': '7',
    'section': '7.4',
}
concept_meta['7.4.6'] = {
    'title_en': 'Uniqueness of Basic Generator Degrees',
    'title_zh': '基本生成元度数的唯一性',
    'slug': 'uniqueness_basic_generator_degrees',
    'domain': 'invariant_theory',
    'subdomain': 'polynomial_invariants',
    'chapter': '7',
    'section': '7.4',
}
concept_meta['7.4.7'] = {
    'title_en': 'Group Order as Product of Basic Generator Degrees',
    'title_zh': '群阶等于基本生成元度数之积',
    'slug': 'group_order_product_basic_generator_degrees',
    'domain': 'invariant_theory',
    'subdomain': 'polynomial_invariants',
    'chapter': '7',
    'section': '7.4',
}
concept_meta['7.4.8'] = {
    'title_en': 'Number of Reflections in Coxeter Group',
    'title_zh': 'Coxeter群中反射的个数',
    'slug': 'number_of_reflections_in_coxeter_group',
    'domain': 'invariant_theory',
    'subdomain': 'polynomial_invariants',
    'chapter': '7',
    'section': '7.4',
}
concept_meta['7.4.9'] = {
    'title_en': 'Shephard-Todd Characterization of Reflection Groups',
    'title_zh': 'Shephard-Todd反射群刻画定理',
    'slug': 'shephard_todd_characterization_reflection_groups',
    'domain': 'invariant_theory',
    'subdomain': 'polynomial_invariants',
    'chapter': '7',
    'section': '7.4',
}
concept_meta['7.4.11'] = {
    'title_en': 'Coxeter Group Has Quadratic Invariant',
    'title_zh': 'Coxeter群有二次不变量',
    'slug': 'coxeter_group_has_quadratic_invariant',
    'domain': 'invariant_theory',
    'subdomain': 'polynomial_invariants',
    'chapter': '7',
    'section': '7.4',
}

# Corollary 2 (under 7.4.1)
concept_meta['7.4.1.cor2'] = {
    'title_en': 'Dimension of Homogeneous Polynomial Space',
    'title_zh': '齐次多项式空间的维数',
    'slug': 'dimension_homogeneous_polynomial_space',
    'domain': 'invariant_theory',
    'subdomain': 'polynomial_spaces',
    'type_override': 'corollary',
    'chapter': '7',
    'section': '7.4',
}

# Also add Proposition 4.1.5 and 4.1.8 and 5.1.5 and 5.1.6
# These are stated inline but have significant content
concept_meta['4.1.5'] = {
    'title_en': 'Simple Reflection Maps Neighboring Root to Positive Root',
    'title_zh': '单反射将相邻根映为正根',
    'slug': 'simple_reflection_maps_neighboring_root_positive',
    'domain': 'group_theory',
    'subdomain': 'root_systems',
    'chapter': '4',
    'section': '4.1',
}
concept_meta['4.1.8'] = {
    'title_en': 'Uniqueness of Simple Root Basis',
    'title_zh': '单根基底的唯一性',
    'slug': 'uniqueness_of_simple_root_basis',
    'domain': 'group_theory',
    'subdomain': 'root_systems',
    'chapter': '4',
    'section': '4.1',
}
concept_meta['5.1.5'] = {
    'title_en': 'Determinant Formula for Marked Graphs',
    'title_zh': '标号图的行列式公式',
    'slug': 'determinant_formula_for_marked_graphs',
    'domain': 'linear_algebra',
    'subdomain': 'coxeter_graphs',
    'chapter': '5',
    'section': '5.1',
}
concept_meta['5.1.6'] = {
    'title_en': 'Subgraph Determinant Positivity Lemma',
    'title_zh': '子图行列式正性引理',
    'slug': 'subgraph_determinant_positivity_lemma',
    'domain': 'linear_algebra',
    'subdomain': 'coxeter_graphs',
    'chapter': '5',
    'section': '5.1',
}
concept_meta['7.4.10'] = {
    'title_en': 'Linear Invariant Implies Trivial Group',
    'title_zh': '线性不变量蕴含平凡群',
    'slug': 'linear_invariant_implies_trivial_group',
    'domain': 'invariant_theory',
    'subdomain': 'polynomial_invariants',
    'chapter': '7',
    'section': '7.4',
}

# Map concept numbers to their lines
concept_lines = {}
for c in concepts:
    concept_lines[c['number']] = c['line']

# Build a comprehensive concept list with all metadata
all_concepts = {}
for c in concepts:
    num = c['number']
    if num in concept_meta:
        all_concepts[num] = {**c, **concept_meta[num]}
    else:
        all_concepts[num] = {**c, 'title_en': c['type'] + ' ' + num, 'title_zh': '', 'slug': f"concept_{num.replace('.','_')}", 'domain': 'mathematics', 'subdomain': 'general', 'chapter': num.split('.')[0], 'section': num.rsplit('.',1)[0]}

# Also add the special concepts not caught by the primary regex
# Check for 4.1.5, 4.1.8, 5.1.5, 5.1.6, 7.4.10
for extra_num in ['4.1.5', '4.1.8', '5.1.5', '5.1.6', '7.4.10', '7.4.1.cor2']:
    if extra_num not in all_concepts:
        meta = concept_meta[extra_num]
        all_concepts[extra_num] = {
            'line': -1,
            'type': meta.get('type_override', 'proposition'),
            'number': extra_num,
            'extra': '',
            'full_header': f"{meta.get('type_override', 'Proposition')} {extra_num}",
            **meta,
        }

print("All concept numbers:", sorted(all_concepts.keys()))

# Helper to create safe slugs
def make_slug(s):
    s = s.lower().replace(' ', '_').replace("'", '').replace('-', '_')
    s = re.sub(r'[^a-z0-9_]', '', s)
    return s

# Now generate files for each concept
os.makedirs(STAGING, exist_ok=True)

# For each concept, figure out what text to extract
concept_texts = {}

for num, cdata in sorted(all_concepts.items()):
    if cdata['line'] < 0:
        continue  # skip special entries without lines

    start = cdata['line']
    # Find next concept or section break
    end = detect_next_boundary(start)

    text = extract_text(start, end)
    concept_texts[num] = text

    # Detect proof boundary
    proof_start, proof_end = detect_proof_boundary(start, end)

    # Extract statement (everything from header to proof marker)
    statement_lines = []
    if proof_start:
        for i in range(start, proof_start):
            statement_lines.append(lines[i])
    else:
        for i in range(start, min(start + 30, end)):
            statement_lines.append(lines[i])
    statement = '\n'.join(statement_lines)

    # Extract proof
    proof_text = ''
    if proof_start and proof_start < end:
        proof_lines = []
        for i in range(proof_start, end):
            proof_lines.append(lines[i])
        proof_text = '\n'.join(proof_lines)

    # Create slug
    slug = cdata.get('slug', make_slug(cdata.get('title_en', f"concept_{num.replace('.','_')}")))

    # Create directory
    concept_dir = os.path.join(STAGING, slug)
    os.makedirs(concept_dir, exist_ok=True)

    # concept_type
    ctype = cdata['type'].lower()

    # Write concept.yaml
    yaml_data = {
        'id': slug,
        'title_en': cdata.get('title_en', f'{cdata["type"]} {num}'),
        'title_zh': cdata.get('title_zh', ''),
        'type': ctype,
        'domain': cdata.get('domain', 'mathematics'),
        'subdomain': cdata.get('subdomain', 'general'),
        'difficulty': 'basic',
        'tags': [],
        'depends_on': {'required': [], 'recommended': [], 'suggested': []},
        'proof_deps': {},
        'source_books': [{
            'book_id': 'GTM099',
            'author': 'L.C. Grove, C.T. Benson',
            'title': 'Finite Reflection Groups',
            'chapter': cdata.get('chapter', ''),
            'section': cdata.get('section', ''),
            'pages': '',
            'role_in_book': f'{cdata["type"]} in Chapter {cdata.get("chapter", "?")}'
        }],
        'content_hash': hashlib.sha256(text.encode()).hexdigest()[:16],
        'extraction_date': '2026-06-24',
        'extraction_agent': 'v7-10books',
    }

    with open(os.path.join(concept_dir, 'concept.yaml'), 'w') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # Write theorem.tex (pure LaTeX statement)
    # Convert markdown to LaTeX-like format
    tex_content = statement
    # Remove the header line itself
    header_line = cdata['full_header']
    tex_content = tex_content.replace(header_line, '', 1).strip()
    # Remove ** markers
    tex_content = re.sub(r'\*\*', '', tex_content)
    # Clean up
    tex_content = tex_content.strip()

    with open(os.path.join(concept_dir, 'theorem.tex'), 'w') as f:
        f.write(tex_content + '\n')

    # Write introduce.en.md
    title = cdata.get('title_en', f'{cdata["type"]} {num}')
    ctype_cap = cdata['type'].capitalize()
    chapter = cdata.get('chapter', '?')

    desc = f"""---
id: {slug}
title: "{title}"
type: {ctype}
---

{ctype_cap} {num} from Chapter {chapter} of Grove and Benson's "Finite Reflection Groups" (GTM 99). This result is part of the systematic development of finite reflection groups and Coxeter groups.
"""

    with open(os.path.join(concept_dir, 'introduce.en.md'), 'w') as f:
        f.write(desc)

    print(f"  Created {slug}")

# Write .done marker
with open(os.path.join(STAGING, '.done'), 'w') as f:
    f.write(f'DONE - {len(all_concepts)} concepts extracted\n')

print(f"\nTotal concepts extracted: {len(all_concepts)}")
print(f"Done marker written to {os.path.join(STAGING, '.done')}")
