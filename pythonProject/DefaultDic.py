from collections import defaultdict

url_map_dictionary = {
    "https://alas.aws.amazon.com/": "https://alas.aws.amazon.com/",
    "https://alas.aws.amazon.com/alas2.html": "https://alas.aws.amazon.com/AL2/",
}

def implement_default_dict():
    advisory_ids = defaultdict(list)
    y = 1

    for url in url_map_dictionary:
        print(url)
        z = y
        for x in range(z, z + 10):
            advisory_ids[url].append(x)
            y += 1

    print(advisory_ids)

# Example usage
implement_default_dict()