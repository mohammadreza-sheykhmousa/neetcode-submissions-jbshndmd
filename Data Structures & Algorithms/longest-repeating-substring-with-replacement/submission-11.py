class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        max_freq = 0  # Track the maximum frequency in current window
        longest_len = 0
        
        for r in range(len(s)):
            # Add current character to frequency map
            freq[s[r]] = freq.get(s[r], 0) + 1
            # Update max frequency in current window
            max_freq = max(max_freq, freq[s[r]])
            
            # Current window size
            window_len = r - l + 1
            
            # If we need more than k replacements, shrink window
            while window_len - max_freq > k:
                freq[s[l]] -= 1
                l += 1
                window_len = r - l + 1  # Update window length
                # Note: We don't need to update max_freq here for correctness
                # (though it could be optimized)
            
            # Update answer
            longest_len = max(longest_len, window_len)
        
        return longest_len