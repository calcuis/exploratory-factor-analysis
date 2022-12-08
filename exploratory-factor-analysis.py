import numpy as np
from sklearn.decomposition import FactorAnalysis

def perform_exploratory_factor_analysis(data, num_factors):
    # Create the FactorAnalysis object
    factor_analyzer = FactorAnalysis(n_components=num_factors)

    # Fit the data using the factor analyzer
    factor_analyzer.fit(data)

    # Get the loadings matrix
    loadings_matrix = factor_analyzer.components_

    # Return the loadings matrix
    return loadings_matrix
