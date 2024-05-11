def print_docs(directory):
    all_file = os.walk(directory)
    for catalog in all_file:
        print(f"Папка {catalog[0]}содержит:")
    print(f'Директория:{", ".join([folder for ])}')