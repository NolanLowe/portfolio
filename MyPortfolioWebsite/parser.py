class Parser:
    def __init__(self, prepend_link):
        self.data = []
        self.prepend_link = prepend_link

    def append(self, title: str, language: str, desc: list[str], image: str = None) -> None:
        desc = " ".join(desc)
        print(image)
        new_entry = {
            'title': title.split(':')[1].strip(),
            'language': language.split(':')[1].strip(),
            'description': desc.split(':')[1].strip(),
            'link': self.prepend_link + title.split(':')[1].strip(),
            'image': image
        }

        self.data.append(new_entry)

