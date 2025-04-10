import os

# Define the base path for the math section
base_math_path = "02 Math"

# Define the structure: {directory_path: [list_of_filenames]}
# We use os.path.join to make it OS-independent
structure = {
    # --- 01 Probability ---
    os.path.join(base_math_path, "01 Probability"): [], # Main directory
    os.path.join(base_math_path, "01 Probability", "01 Basic Probability Theory"): [
        "01_Definition_and_Terminology.md",
        "02_Types_of_Probability.md",
        "03_Combinatorics.md",
        "04_Conditional_Probability.md",
        "05_Independence.md",
        "06_Bayes_Theorem.md",
    ],
    os.path.join(base_math_path, "01 Probability", "02 Random Variables"): [
        "01_Definition.md",
        "02_Probability_Mass_Function_PMF.md",
        "03_Probability_Density_Function_PDF.md",
        "04_Cumulative_Distribution_Function_CDF.md",
    ],
    os.path.join(base_math_path, "01 Probability", "03 Common Probability Distributions"): [
        "01_Bernoulli_Distribution.md",
        "02_Binomial_Distribution.md",
        "03_Poisson_Distribution.md",
        "04_Uniform_Distribution.md",
        "05_Normal_Gaussian_Distribution.md", # Already have a Gaussian file elsewhere, maybe link later? Let's create for completeness here.
        "06_Exponential_Distribution.md",
        "07_Overview.md", # Optional: A file linking/summarizing distributions
    ],
    os.path.join(base_math_path, "01 Probability", "04 Expectation Variance Covariance"): [
        "01_Expected_Value.md",
        "02_Variance_and_Standard_Deviation.md",
        "03_Covariance_and_Correlation.md",
    ],
    os.path.join(base_math_path, "01 Probability", "05 Important Theorems"): [
        "01_Law_of_Large_Numbers_LLN.md",
        "02_Central_Limit_Theorem_CLT.md", # Already have a CLT file elsewhere, link later. Create for now.
    ],

    # --- 02 Inferential Statistics ---
    # Assuming this structure largely exists, but add if needed.
    # Example: Add a specific placeholder if missing
    # os.path.join(base_math_path, "02 Inferential statistics", "Some_New_Topic"): [
    #     "Placeholder.md",
    # ],


    # --- 03 Linear Algebra ---
    os.path.join(base_math_path, "03 Linear Algebra"): [], # Main directory
    os.path.join(base_math_path, "03 Linear Algebra", "01 Core Objects"): [
        "01_Scalars.md",
        "02_Vectors.md",
        "03_Matrices.md",
        "04_Tensors.md",
    ],
    os.path.join(base_math_path, "03 Linear Algebra", "02 Basic Operations"): [
        "01_Vector_Operations.md",
        "02_Matrix_Operations.md",
    ],
    os.path.join(base_math_path, "03 Linear Algebra", "03 Matrix Properties and Concepts"): [
        "01_Identity_Matrix.md",
        "02_Inverse_Matrix.md",
        "03_Determinant.md",
        "04_Trace.md",
    ],
    os.path.join(base_math_path, "03 Linear Algebra", "04 Vector Spaces and Concepts"): [
        "01_Linear_Independence.md",
        "02_Span_and_Basis.md",
        "03_Rank.md",
    ],
    os.path.join(base_math_path, "03 Linear Algebra", "05 Norms"): [
        "01_Definition.md",
        "02_L1_Norm_Manhattan.md",
        "03_L2_Norm_Euclidean.md",
        "04_Frobenius_Norm.md",
    ],
    os.path.join(base_math_path, "03 Linear Algebra", "06 Decompositions and Factorizations"): [
        "01_Eigenvalues_and_Eigenvectors.md",
        "02_Singular_Value_Decomposition_SVD.md",
        "03_Overview.md", # Optional summary file
    ],

    # --- 04 Calculus ---
    os.path.join(base_math_path, "04 Calculus"): [], # Main directory
    os.path.join(base_math_path, "04 Calculus", "01 Foundations"): [
        "01_Functions_Limits_Continuity.md",
        "02_Derivatives.md",
        "03_Rules_of_Differentiation.md",
        "04_Chain_Rule.md", # Explicitly call out Chain Rule importance
    ],
    os.path.join(base_math_path, "04 Calculus", "02 Multivariable Calculus"): [
        "01_Functions_of_Multiple_Variables.md",
        "02_Partial_Derivatives.md",
        "03_Gradient.md",
        "04_Directional_Derivatives.md",
    ],
    os.path.join(base_math_path, "04 Calculus", "03 Optimization"): [
        "01_Maxima_and_Minima.md",
        "02_Gradient_Descent.md",
        "03_Gradient_Descent_Variants.md", # SGD, Mini-batch, Adam etc.
        "04_Convexity.md",
    ],
    os.path.join(base_math_path, "04 Calculus", "04 Advanced Topics"): [
        "01_Hessian_Matrix.md",
        "02_Jacobian_Matrix.md",
        "03_Lagrange_Multipliers.md",
    ],
     os.path.join(base_math_path, "04 Calculus", "05 Integrals"): [
        "01_Definite_and_Indefinite_Integrals.md",
        "02_Applications_in_Probability.md",
    ],
}

# Create the directories and files
for dir_path, filenames in structure.items():
    try:
        os.makedirs(dir_path, exist_ok=True)
        print(f"Ensured directory exists: {dir_path}")
        for filename in filenames:
            file_path = os.path.join(dir_path, filename)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    # Optional: Write a placeholder title
                    title = filename.replace('.md', '').replace('_', ' ')[2:] if filename.startswith('0') else filename.replace('.md', '').replace('_', ' ')
                    f.write(f"# {title} (Placeholder)\n\n")
                print(f"  Created file: {filename}")
            else:
                print(f"  File already exists: {filename}")
    except OSError as e:
        print(f"Error creating directory {dir_path} or file: {e}")

print("\nMath structure creation process finished.")