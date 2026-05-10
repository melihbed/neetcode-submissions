class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        ["Hello", "World"]
        ["12", "21", ...]
        "12,21,...|23, 41, ...|..."

        "1221..."
        "  "
        """
        encoded_string = []
        if not strs:  # ← handle empty list
            return ""
        # Convert the char to corresponding ASCII
        for s in strs:
            if s == "":
                encoded_string.append("EMPTY")
            else:
                asciiL = ",".join(str(ord(c)) for c in s)
                encoded_string.append(asciiL)
        
        return "|".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        """
        "12,21,...|23, 41, ...|..."
        """
        strings = []

        if not s:  # 
            return []

        for s in s.split("|"): # ["12, 21,...", "23, 41, ...", ...]
            if s == "EMPTY":
                strings.append("")  # restore empty string
            else:
                chars = "".join(chr(int(c)) for c in s.split(","))
                strings.append(chars)

        return strings
