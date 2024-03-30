class FileHandler:
    def __init__(self):
        """
        hello
        """
        with open(file='chaff.txt', mode='r') as file:
            contents = [line.strip() for line in file.readlines() if line != "\n"]
            self.sentences = " ".join(contents).split('.')
            self.sentences = [line + "." for line in self.sentences]

        self.sentences.insert(0, "Ready to go?")
        self.sentences.insert(0, "Remember these <>?")
        self.sentences.insert(0, "It resumes when you enter your first letter.")
        self.sentences.insert(0, "The time stops after each line.")
        self.sentences.insert(0, "Start typing!!")
        # The timer starts when you start.

        self.index = 0
        self.last = len(self.sentences)

    def has_next(self):
        if self.index + 1 < self.last:
            return True
        else:
            return False

    def get_next(self):
        """
        return next line in sequence
        :return:
        """
        if self.has_next():
            self.index += 1
            return self.sentences[self.index]
        else:
            return "List has run out!"

    def get(self):
        """
        return currently loaded line
        :return:
        """
        return self.sentences[self.index]
