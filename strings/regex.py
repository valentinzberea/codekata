class Regex(object):

    QUANTIFIER = 0
    CHARACTER = 1

    def __init__(self, pattern):
        self.pattern = pattern

    def match(self, text):
        result = []
        for i in range(0, len(text)):

            text_index = i
            for j in range(0, len(self.pattern)):
                pattern_char = self.pattern[j]

                if pattern_char[j] == '*':
                    is_match = self.match_char(text[text_index], pattern_char)
                    while 
                text_index += 1

                if i+j >= len(text):
                    break

                is_match = self.match_char(text[i+j], pattern_char)
                if is_match is False:
                    break
                if j == len(self.pattern) - 1:
                    result.append(text[i:i+j+1])


        return result

    def match_char(self, text_char, pattern_char):
        if pattern_char == '.':
            return True
        elif pattern_char == text_char:
            return True
        else:
            return False

    def pattern_char_type():
        if pattern_char in ['*', '?']:
            return QUANTIFIER
        else:
            return CHARACTER
