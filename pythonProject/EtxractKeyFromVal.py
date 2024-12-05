from typing import Dict, List

def get_keys_by_value(d: Dict[str, List[str]], target_value: str) -> List[str]:
    return [key for key, values in d.items() if target_value in values]

# Example usage:
my_dict = {'a': ['ALAS2', 'ALAS3', 'ALAS69'], 'b': ['ALAS12', 'ALAS33', 'ALAS34'], 'c': ['ALAS14', 'ALAS55', 'ALAS66']}

target_value = 'ALAS2'
keys_for_target_value = get_keys_by_value(my_dict, target_value)

print(f"Keys for value {target_value}: {keys_for_target_value}")
