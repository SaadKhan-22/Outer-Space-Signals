# write your code here
from collections import Counter
from difflib import SequenceMatcher

def main():
    """Main function to run the program."""
    #print("🛸 NASA Signal Decoder - Deciphering Messages from Planet Dyslexia 🛸")
    
    # Your code logic goes here -- feel free to add functions or classes as needed
    #print("Analyzing 64KB of alien signals...")
    #print("Searching for 721-character encrypted message...")

    #equal to the no. of characters in the message
    sliding_window_size = 721
    highest_decoded_freq = list("EATOIRSNHU")  



    # ************** Loading Data **************
    #read the text and create a list of all the words - assuming the words are separated by spaces
    with open("signal.txt", encoding='utf-8') as file:
        signal_text = file.read()

    def get_score(substring):

        #returns dict where key = letter and value = no. of instances
        #spaces not needed when counting
        counts = Counter(substring.replace(" ", ""))
        most_freq_letters = [each[0] for each in counts.most_common(10)]


        return SequenceMatcher(None, most_freq_letters, highest_decoded_freq).ratio()

   

    candidates = []
    #create a list of all possible candidates given the window size
    for i in range(0, len(signal_text) - sliding_window_size + 1):

        window = signal_text[i:i + sliding_window_size]
        score = get_score(window)
        candidates.append((score, i, window))



    candidates.sort(reverse=True)
    #the top 10 candidates score-wise
    best_match_windows = candidates[:10]


    def build_mapping(text):

        #removing spaces - again
        counts = Counter(text.replace(" ", ""))
        top_encrypted = [item[0] for item in counts.most_common(10)]
        return dict(zip(top_encrypted, highest_decoded_freq))



    def decrypt(candidate, mapping):
        return ''.join(mapping.get(c, c) if c != ' ' else ' ' for c in candidate)



    #gets the best sequence based on score
    for idx, (score, start, window) in enumerate(best_match_windows):
        mapping = build_mapping(window)
        decrypted = decrypt(window, mapping)
        print(f"\n--- Candidate Sequence #{idx+1} (Score: {score:.2f}, Start Index: {start}) ---")
        print(decrypted[:721] + "...\n")

        #testing possible mappings
        print(decrypted[:300]\
                                .replace('V', 'A')\
                                .replace('D', 'M')\
                                .replace('S', 'G')\
                                .replace('O', 'D')\
                                .replace('R', 'I') + "...")






if __name__ == "__main__":
    main() 




