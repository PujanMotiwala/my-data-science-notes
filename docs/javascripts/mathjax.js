window.MathJax = {
  tex: {
    // Define the inline math delimiters MathJax should recognize
    // arithmatex typically converts $...$ to \(...\)
    inlineMath: [ ["\\(","\\)"] ],
    // Define the display math delimiters MathJax should recognize
    // arithmatex typically converts $$...$$ to \[...\]
    displayMath: [ ["\\[","\\]"] ],
    // Allow processing of environments like align, gather, etc.
    processEnvironments: true,
    // Allow processing of escaped dollar signs \$
    processEscapes: true
  },
  // Options for how MathJax interacts with the HTML page
  options: {
    // Skip processing math in elements with these classes (e.g., code blocks)
    ignoreHtmlClass: ".*|",
    // Process math only in elements with this class (set by arithmatex)
    processHtmlClass: "arithmatex"
  },
  // Specific output processor options (optional, but good defaults)
  chtml: {
    matchFontHeight: true // Adjust font size to match surrounding text
  },
  // Loader options (usually defaults are fine)
  loader: {
    load: ['input/tex', 'output/chtml'] // Load TeX input and CommonHTML output processor
  }
};

// Optional: Log to console to confirm the config is loaded
// console.log("MathJax Configuration Loaded:", window.MathJax);