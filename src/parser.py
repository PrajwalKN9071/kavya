from config import get_dynamic_file_paths, extract_variables, search_in_xml, search_in_properties
from utils import compare_and_write_differences
import glob

def print_key_value_pairs():
    application_properties_file, environment_properties_file, xml_files_pattern, _, _, _ ,_= get_dynamic_file_paths()
    variables = extract_variables(application_properties_file)

    # Search for variable values in all XML files
    for file_name in glob.glob(xml_files_pattern):
        variables = search_in_xml(file_name, variables)

    # Search for variable values in environment.properties
    variables = search_in_properties(environment_properties_file, variables)

    for key, values in variables.items():
        print(f'{key}={",".join(values)}')

def write_output_properties():
    application_properties_file, environment_properties_file, xml_files_pattern, output_properties_file, _, _, _ = get_dynamic_file_paths()
    variables = extract_variables(application_properties_file)

    # Search for variable values in all XML files
    for file_name in glob.glob(xml_files_pattern):
        variables = search_in_xml(file_name, variables)

    # Search for variable values in environment.properties
    variables = search_in_properties(environment_properties_file, variables)

    # Write found variables to output_properties.properties
    with open(output_properties_file, 'w') as f:
        for key, values in variables.items():
            for value in values:
                f.write(f'{key}={value}\n')

def write_missing_properties():
    application_properties_file, environment_properties_file, xml_files_pattern, _, missing_properties_file, _, _ = get_dynamic_file_paths()
    variables = extract_variables(application_properties_file)

    # Search for variable values in all XML files
    for file_name in glob.glob(xml_files_pattern):
        variables = search_in_xml(file_name, variables)

    # Search for variable values in environment.properties
    variables = search_in_properties(environment_properties_file, variables)

    # Get all missing variables
    with open(missing_properties_file, 'w') as f:
        for key, values in variables.items():
            if not values:
                f.write(f'{key}=MISSING\n')

# Compare application.properties variables with environment.properties keys and write differences to environment_op.properties
def compare_and_write_differences_main():
    application_properties_file, environment_properties_file,_ , _, _, environment_op_properties_file, _ = get_dynamic_file_paths()
    compare_and_write_differences(application_properties_file, environment_properties_file, environment_op_properties_file)

