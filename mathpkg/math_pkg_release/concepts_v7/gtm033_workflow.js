export const meta = {
  name: 'v7-extract-gtm033',
  description: 'GTM033: 21 sections → concept extraction',
  phases: [{ title: 'Extract', detail: 'One agent per section' }]
}

var SECTIONS = ["/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s001_1_Differential_topology.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s002_0_Submanifolds_of.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s003_1_The_Grassmann_manifold.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s004_3_Embeddings_and_Immersions\n\nFigure.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s005_2_Approximations\n\nopen_cover.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s006_2_Approximations.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s007_3_Approximations_on.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s008_15_Submanifolds.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s009_3_The_Classification_of_Vector_Bundles\n\nWe_now_prove_a_basic.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s010_4_Oriented_Vector_Bundles\n\nLet.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s011_5_Tubular_Neighborhoods\n\nLet.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s012_6_Collars_and_Tubular_Neighborhoods_of_Neat_Submanifolds\n\nFi.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s013_1_There_is_an_obvious_definition_of.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s014_1_Degrees_of_Maps\n\nIn_this_section_we_exploit_orientations_a.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s015_9_The_Hopf_invariant_of_a_map.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s016_1_Morse_Functions\n\nLet.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s017_2_Differential_Equations_and_Regular_Level_Surfaces.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s018_2_Differential_Equations_and_Regular_Level_Surfaces\n\nLet.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s019_2_A_relative_CW.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s020_1_Isotopy\n\nFigure.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM033)Differential Topology/s021_3_Isotopies_of_Disks\n\nThe_following_useful_result_says_that.md"]
var STAGING = '/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm033'
var BOOK_SLUG = 'gtm033'

phase('Extract')
log(BOOK_SLUG + ': ' + SECTIONS.length + ' sections')

var results = await pipeline(SECTIONS, function(prev, sp) {
  return async function() {
    var sn = sp.split('/').pop().replace('.md','')
    var dd = STAGING + '/' + sn
    
    var prompt = '=== V7 CONCEPT EXTRACTOR (Per-Section) ===\n\n' +
      'READ: ' + sp + '\n\n' +
      'Extract EVERY theorem, definition, lemma, proposition, corollary, axiom.\n' +
      'For EACH concept, write 3 files in: ' + dd + '/{SLUG}/\n\n' +
      '1. concept.yaml: id,title_en,title_zh:"",type,domain,subdomain,difficulty,tags,depends_on,source_books,content_hash:"",extraction_date:"2026-06-25",extraction_agent:"v7-test"\n' +
      '2. theorem.tex: PURE LaTeX STATEMENT only. NO proof.\n' +
      '3. introduce.en.md: YAML frontmatter(role:introduce,locale:en,content_hash:"",written_against:"") + 2-4 English sentences.\n\n' +
      'CRITICAL: slug = semantic-english-lowercase-hyphen (kummers-theorem NOT ' + key.lower() + '-thm-3-2). ' +
      'source_books = array of OBJECTS. theorem.tex = ZERO natural language.\n\n' +
      'Write .done: echo DONE > ' + dd + '/.done\n' +
      'Write .fail if stuck: echo FAIL > ' + dd + '/.fail'
    
    try { await agent(prompt, { label: sn.substring(0,40), phase: 'Extract' }) } catch(e) {}
    
    // Count on disk
    var cnt = 0
    try {
      var cr = await agent(
        'python3 -c "import os; d=\'' + dd + '\'; print(len([x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))]) if os.path.exists(d) else 0)"',
        { label: 'cnt-'+sn.substring(0,25), phase: 'Extract' }
      )
      cnt = cr ? parseInt(cr.trim()) || 0 : 0
    } catch(e) {}
    
    return { section: sn.substring(0,50), concepts: cnt }
  }
})

var valid = results.filter(function(r) { return r !== null })
var total = valid.reduce(function(s, r) { return s + (r.concepts || 0) }, 0)
log(BOOK_SLUG + ': ' + total + ' concepts from ' + valid.length + '/' + SECTIONS.length + ' sections')
return { book: BOOK_SLUG, sections: SECTIONS.length, sections_done: valid.length, concepts: total }
