from lxml import etree


def validate_and_fix(xml_file_path, dtd_file_path):
    try:
        dtd = etree.DTD(dtd_file_path)
        tree = etree.parse(xml_file_path)

        if dtd.validate(tree):
            print("XML is valid against DTD.")
        else:
            print("XML is not valid against DTD. Errors:")
            for error in dtd.error_log.filter_from_errors():
                print(error)

            # Attempt to fix the XML
            for error in dtd.error_log:
                if error.type_name == 'DTD_UNKNOWN_ELEMENT':
                    # Replace unknown element with a generic one
                    error_message = error.message.replace("unknown element", "genericElement")
                    print(f"Attempting to fix: {error_message}")
                    xml_string = etree.tostring(tree, encoding='utf-8').decode('utf-8')
                    xml_string = xml_string.replace(error.message, "<genericElement/>")
                    with open(xml_file_path, 'w') as xml_file:
                        xml_file.write(xml_string)
                    print("XML fixed. Please re-run validation.")
                    break
    except etree.XMLSyntaxError as e:
        print(f"XML syntax error: {e}")


# Example usage:
xml_file_path = 'C:\\Users\\achaud12\\Downloads\\XMLUSA.xml'
dtd_file_path = 'C:\\Users\\achaud12\\Downloads\\go(1).dtd'
validate_and_fix(xml_file_path, dtd_file_path)