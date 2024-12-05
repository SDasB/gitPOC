from configparser import ConfigParser

def read_Config(file_path):
    print(file_path)
    config = ConfigParser()
    config.read(file_path)

    # Check if the file contains the 'DEFAULT' section
    if 'DEFAULT' in config:
        for key, value in config['DEFAULT'].items():
            print(f"DEFAULT_{key}: {value}")

    # Check other sections
    print(config.sections())
    for section in config.sections():
        print(section)
        if section != 'DEFAULT':
            print(f"\n[{section}]")
            for key, value in config[section].items():
                print(f"{key}: {value}")

if __name__ == "__main__":
    properties_file_path = "config.properties"
    read_Config(properties_file_path)