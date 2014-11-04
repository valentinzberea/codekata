class Regex(object):

    def match(self, regex, text):

        assert type(regex) is str
        assert type(text) is str

        result = []

        if len(text) == 0 or len(regex) == 0:
            return result

        i = 0
        while i < len(text):
            idx = self.match_here(regex, text[i:])
            if idx > -1:
                result.append(text[i:i+idx])
                i += idx
            else:
                i += 1

        return result

    def match_here(self, regex, text):
        if len(regex) == 0:
            return 0

        if len(regex) > 1 and regex[1] == '*':
            return self.match_star(regex[0], regex[2:], text)

        if text[0] == regex[0] or regex[0] == '.':
            return 1 + self.match_here(regex[1:], text[1:])

        return -1

    def match_star(self, char, regex, text):
        if len(text) == 0:
            return self.match_here(regex, text)

        for i in range(0, len(text)):
            idx = self.match_here(regex, text[i:])
            if idx == 0:
                return len(text)
            elif idx > 0:
                return i+idx
            if text[i] != char and char != '.':
                return i

        return -1
