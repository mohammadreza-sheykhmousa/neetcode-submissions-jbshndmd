class Solution:
    def isValid(self, s: str) -> bool:
        # while "()" in s or "{}" in s or "[]" in s:
        #     s = s.replace("()", "")
        #     s = s.replace("{}", "")
        #     s = s.replace("[]", "")
        # return s == ""
        # stack = []
        # matches = {")": "(", "]": "[", "}": "{"}

        # for c in s: #let's write the false part first we are checking if the 
        #             #stack empty and and closing has lates open and if open save it
        #     #logic [()], [])
        #     if c in matches: #if it is closing braket
        #         if stack and stack[-1] == c2o[c]:
        #             stack.pop
        #         else:
        #             return False
        #     else:
        #         stack.append(c)

        # return len(stack) == 0
        matches = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack or stack[-1] != matches[c]:
                    return False
                stack.pop() # heeey its a match we can delete it now
        return len(stack) == 0
        # if opening bracket → push onto stack
# if closing bracket → check if it matches stack top
#                    → if yes → pop
#                    → if no → return False
# if closing but stack empty → return False
# -----------------
# "close with nothing open"    → not stack → return False
# "wrong type open"            → stack[-1] != matches[c] → return False
# "unclosed at end"            → len(stack) != 0 → return False




        