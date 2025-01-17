import streamlit as st

# Default local filepaths
DEFAULT_GENERATORS_SPEC_FILE = "mock_generators/named_generators.json"
DEFAULT_GENERATORS_CODE_PATH = "mock_generators/generators"
DEFAULT_ARROWS_SAMPLE_PATH = "mock_generators/samples/arrows.json"
DEFAULT_IMPORTS_PATH = "mock_generators/imports"
DEFAULT_EXPORTS_PATH = "mock_generators/export/files"
DEFAULT_ZIPS_PATH = "mock_generators/export/zips"
DEFAULT_CODE_TEMPLATES_FILE ="mock_generators/template_generators/generic_generator.py"

# Streamlit session keys
GENERATORS = "generators"
SPEC_FILE = "spec_filepath"
CODE_FILE = "code_filepath"
IMPORTED_FILE = "uploaded_file" # Old key for selected import file, this is the raw imported file
IMPORTED_FILENAME = "imported_filename"
IMPORTED_NODES = "imported_nodes"
IMPORTED_RELATIONSHIPS = "imported_relationships"
SAMPLE_ARROWS_FILE= "sample_arrows"
IMPORTS_PATH = "imports_path"
EXPORTS_PATH = "exports_path"
ZIPS_PATH = "zips_path"
CODE_TEMPLATE_FILE = "templates_file"
DEFAULT_DATA_IMPORTER_FILENAME = "neo4j_importer_model"
NEW_GENERATOR_ARGS = "new_generator_args"
MAPPINGS = "mappings"
